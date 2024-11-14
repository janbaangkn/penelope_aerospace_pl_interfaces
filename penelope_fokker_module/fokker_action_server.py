from time import sleep

import rclpy
from rclpy.action import ActionServer
from rclpy.node import Node

import threading
from .tcp_communication.tcp_client import run_tcp_client
from .tcp_communication.communication_functions import send_message
from .tcp_communication.message_service_class import TCPInbox

from .get_str_function import *
from .create_action_obj import _find_substring
from .create_action_obj import _create_actions_from_cobot_output
from .create_action_obj import _create_drill_tasks_from_cobot_output
from .create_action_obj import _create_tempfs_from_cobot_output
from .create_action_obj import _create_fasteners_from_cobot_output
from .create_action_obj import _create_ee_from_cobot_output

from penelope_aerospace_pl_msgs.action import CobotOp
from penelope_aerospace_pl_msgs.msg import AssemblyActionState
from penelope_aerospace_pl_msgs.msg import ModuleState
from penelope_aerospace_pl_msgs.msg import ResultCodes


class FokkerActionServer(Node):

    action_name: str = "cobot_station/assemble"

    def __init__(self):
        super().__init__("fokker_action_server")
        self._action_server = ActionServer(self, CobotOp, self.action_name, self.execute_callback)

        self.continue_threads = True

        self.tf_ip_address = "10.237.20.101"
        self.tf_port = 20002
        self.tf_cobot_uid = f"{self.tf_ip_address}/{self.tf_port}"
        self.tf_tcp_client_thread = threading.Thread(target=run_tcp_client, args=(self.tf_ip_address, self.tf_port, self))
        self.tf_tcp_client_thread.start()

        self.send_goto_home(self.tf_cobot_uid)

        self.pf_ip_address = "10.237.20.103"
        self.pf_port = 20002
        self.pf_cobot_uid = f"{self.pf_ip_address}/{self.pf_port}"
        self.pf_tcp_client_thread = threading.Thread(target=run_tcp_client, args=(self.pf_ip_address, self.pf_port, self))
        self.pf_tcp_client_thread.start()

        self.send_goto_home(self.pf_cobot_uid)

        self.inbox_thread = threading.Thread(target=self.process_inbox_messages)
        self.inbox_thread.start()

    def __del__(self):
        """
        Destructor of the FokkerActionServer.
        Will terminate the threads before destructing itself.
        """
        self.terminate_threads()
        sleep(0.5)  # give it time to kill the threads

        # call the base class destructor
        super(FokkerActionServer, self).__del__()

    def terminate_threads(self):
        """
        Set the continue_threads attribute to False to trigger thread termination
        """
        self.continue_threads = False
        
    def execute_callback(self, goal_handle):
        """
        Handle the ros message
        """
        self.get_logger().info("Processing goal handle")

        # Accessing the request data and send to cobot
        # This instantiates and populates the classes in the Cobot controller
        self.send_goal_handle_to_cobot(goal_handle)

        # start sending the uid of the actions to the cobot 
        # to execute these actions
        if goal_handle.request:
            if goal_handle.request.execute:
                if len(goal_handle.request.execute) > 0:
                    for uid in goal_handle.request.execute:
                        cobot_uid = self.get_uid(uid)
                        
                        self.get_logger().info(f"Sending action number with uid: " + uid + " to Cobot " + cobot_uid + ".")
                        self.send_execution_action_uid_to_cobot(uid, cobot_uid)
                        self.get_logger().info(f"Finished passing execution requests to cobot.")

        # Indicate the action succeeded (this does not indicate succes!)
        goal_handle.succeed()

        return self.result_msg

    def get_uid(self, str_in):
        if str_in[:3] == "tf_":
            return self.tf_cobot_uid
        elif str_in[:3] == "pf_":
            return self.pf_cobot_uid
        else:
            if "tf_" in str_in[:20] and "pf_" not in str_in[:20]:
                return self.tf_cobot_uid
            elif "pf_" in str_in[:20] and "tf_" not in str_in[:20]:
                return self.pf_cobot_uid
            if "tf_" in str_in[:40] and "pf_" not in str_in[:40]:
                return self.tf_cobot_uid
            elif "pf_" in str_in[:40] and "tf_" not in str_in[:40]:
                return self.pf_cobot_uid
            else:
                return "cannot determine which cobot"

    def send_execution_action_uid_to_cobot(self, cobot_uid, uid_in):  
        """
        Function to send execution commands to the cobot controller
        Excution commands are given by sending the uid of the action
        to be executed.
        """
        msg_str = EXECUTE_TAG + uid_in + CLOSE_TAG

        feedback = send_message(uid=cobot_uid, message=msg_str, feedback=True)

        if feedback:
            self.result_msg = self._create_feedback_message_from_cobot_output(feedback)

            # Send as feedback in all cases
            self._action_server._goal_handles[-1].publish_feedback(self.result_msg)

    def send_goto_home(self, cobot_uid):
        """
        Function to start moving towards the home position.
        Home position must be known in each cobot in DR_HOME_TARGET_USER
        """
        send_message(uid=cobot_uid, message="goto_home", feedback=False)

    def process_inbox_messages(self) -> None:
        """
        """
        while self.continue_threads:
            # collect message from inbox
            message = TCPInbox().get_message()

            # send message to ROS
            if message:
                self.result_msg = self._create_feedback_message_from_cobot_output(message.input_data)

                # Send to ROS
                self._action_server._goal_handles[-1].publish_feedback(self.result_msg)

    def send_goal_handle_to_cobot(self, goal_handle_in):
        """
        Function to send goal_handle contents to the cobot controller
        Sends everything to the Cobot except for the uids to execute
        """
        # storage location container
        msg_out = permf_storage_str_to_cobot(goal_handle_in.request.permf_storage)
        if msg_out:
            feedback = send_message(uid=self.pf_cobot_uid, message=msg_out, feedback=True)
            if feedback:
                self.result_msg = self._create_feedback_message_from_cobot_output(feedback.input_data)

                # Send as feedback in all cases
                self._action_server._goal_handles[-1].publish_feedback(self.result_msg)
        
        # storage location container
        msg_out = tempf_storage_str_to_cobot(goal_handle_in.request.tempf_storage)
        if msg_out:
            feedback = send_message(uid=self.tf_cobot_uid, message=msg_out, feedback=True)          
            if feedback:
                self.result_msg = self._create_feedback_message_from_cobot_output(feedback.input_data)

                # Send as feedback in all cases
                self._action_server._goal_handles[-1].publish_feedback(self.result_msg)

        # product container with holes
        msg_out = product_str_to_cobot(goal_handle_in.request.product)
        if msg_out:
            uid_out = self.get_uid(msg_out)
            feedback = send_message(uid=uid_out, message=msg_out, feedback=True)        
            if feedback:
                self.result_msg = self._create_feedback_message_from_cobot_output(feedback.input_data)

                # Send as feedback in all cases
                self._action_server._goal_handles[-1].publish_feedback(self.result_msg)

        # list of defined waypoints
        msg_out = waypoints_str_to_cobot(goal_handle_in.request.waypoints)
        if msg_out:
            uid_out = self.get_uid(msg_out)
            feedback = send_message(uid=uid_out, message=msg_out, feedback=True)     
            if feedback:
                self.result_msg = self._create_feedback_message_from_cobot_output(feedback.input_data)

                # Send as feedback in all cases
                self._action_server._goal_handles[-1].publish_feedback(self.result_msg)
        
        # list of holes to be drilled
        # feedback = send_message(uid=self.cobot_uid, message=drill_tasks_str_to_cobot(goal_handle_in.request.drill_tasks), feedback=True) 
        # if feedback:
        #     self.result_msg = self._create_feedback_message_from_cobot_output(feedback.input_data)

        #     # Send as feedback in all cases
        #     self._action_server._goal_handles[-1].publish_feedback(self.result_msg)

        # list of available fasteners
        msg_out = fasteners_str_to_cobot(goal_handle_in.request.fasteners)
        if msg_out:
            feedback = send_message(uid=self.pf_cobot_uid, message=msg_out, feedback=True)    
            if feedback:
                self.result_msg = self._create_feedback_message_from_cobot_output(feedback.input_data)

                # Send as feedback in all cases
                self._action_server._goal_handles[-1].publish_feedback(self.result_msg)

        # list of available temporary fasteners
        msg_out = tempfs_str_to_cobot(goal_handle_in.request.tempfs)
        if msg_out:
            feedback = send_message(uid=self.tf_cobot_uid, message=msg_out, feedback=True)          
            if feedback:
                self.result_msg = self._create_feedback_message_from_cobot_output(feedback.input_data)

                # Send as feedback in all cases
                self._action_server._goal_handles[-1].publish_feedback(self.result_msg)

        # list of available docking positions for End Effectors
        # feedback = send_message(uid=self.cobot_uid, message=docking_pos_str_to_cobot(goal_handle_in.request.docking_pos), feedback=True)
        # if feedback:
        #     feedback_msg = self._create_feedback_message_from_cobot_output(feedback.input_data)

        #     # Send as feedback in all cases
        #     self._action_server._goal_handles[-1].publish_feedback(feedback_msg)

        # list of available End Effectors
        # feedback = send_message(uid=self.cobot_uid, message=ee_str_to_cobot(goal_handle_in.request.ee), feedback=True)              
        # if feedback:
        #     feedback_msg = self._create_feedback_message_from_cobot_output(feedback.input_data)

        #     # Send as feedback in all cases
        #     self._action_server._goal_handles[-1].publish_feedback(feedback_msg)

        # list of defined actions
        # actions must be last because they require all other stuff to be there
        #(always to both cobots)
        msg_out = actions_str_to_cobot(goal_handle_in.request.actions)
        if msg_out:
            uid_out = self.get_uid(msg_out)
            feedback = send_message(uid=uid_out, message=msg_out, feedback=True)         
            if feedback:
                self.result_msg = self._create_feedback_message_from_cobot_output(feedback.input_data)

                # Send as feedback in all cases
                self._action_server._goal_handles[-1].publish_feedback(self.result_msg)

        return 1     

    def _create_feedback_message_from_cobot_output(self, c_str):
        """
        Function to populate feedback message based on information from the cobot controller
        """
        
        # Create a feedback message
        feedback_msg = CobotOp.Feedback()

        a_str = _find_substring(c_str, ACTIONS_TAG)
        if a_str is not None:
            feedback_msg.actions = _create_actions_from_cobot_output(a_str)  

        d_str = _find_substring(c_str, DRILL_TASKS_TAG)
        if d_str is not None:
            feedback_msg.drill_tasks = _create_drill_tasks_from_cobot_output(d_str)

        t_str = _find_substring(c_str, TEMPFS_TAG)
        if t_str is not None:
            feedback_msg.tempfs = _create_tempfs_from_cobot_output(t_str)

        f_str = _find_substring(c_str, FASTENERS_TAG)
        if f_str is not None:
            feedback_msg.fasteners = _create_fasteners_from_cobot_output(f_str)

        ee_str = _find_substring(c_str, END_EFFECTORS_TAG)
        if ee_str is not None:
            feedback_msg.ee = _create_ee_from_cobot_output(ee_str)
        
        # calculate the percentage complete
        complete = 0
        total_actions = 0

        for action in feedback_msg.actions:
            total_actions += 1
            if action.state == AssemblyActionState.SUCCESS:
                complete += 1

        if total_actions > 0:
            feedback_msg.percent_complete = complete / total_actions
        else:
            feedback_msg.percent_complete = 0.0

        if total_actions > 0 and complete == 0:
            feedback_msg.module_state = ModuleState.ACCEPTED
        if complete > 0 and complete < total_actions:
            feedback_msg.module_state = ModuleState.EXECUTING
        
        #TODO implement logic for states below
        #feedback_msg.module_state = ModuleState.PAUSED
        #feedback_msg.module_state = ModuleState.CANCELING
        
        #TODO get any relevant messages from the cobot
        feedback_msg.message = "Not implemented yet"   

        return feedback_msg
    
    def _create_result_message_from_cobot_output(self, c_str):
        """
        Function to populate feedback message based on information from the cobot controller
        """
    
        # Create a feedback message
        result_msg = CobotOp.Result()

        a_str = _find_substring(c_str, ACTIONS_TAG)
        if a_str is not None:
            result_msg.actions_out = _create_actions_from_cobot_output(a_str)  

        d_str = _find_substring(c_str, DRILL_TASKS_TAG)
        if d_str is not None:
            result_msg.drill_tasks_out = _create_drill_tasks_from_cobot_output(d_str)

        t_str = _find_substring(c_str, TEMPFS_TAG)
        if t_str is not None:
            result_msg.tempfs_out = _create_tempfs_from_cobot_output(t_str)

        f_str = _find_substring(c_str, FASTENERS_TAG)
        if f_str is not None:
            result_msg.drill_tasks_out = _create_fasteners_from_cobot_output(f_str)

        ee_str = _find_substring(c_str, END_EFFECTORS_TAG)
        if ee_str is not None:
            result_msg.ee_out = _create_ee_from_cobot_output(ee_str)
        
        # see how many actions are complete
        complete = 0
        total_actions = 0

        for action in result_msg.actions:
            total_actions += 1
            if action.state == AssemblyActionState.SUCCESS:
                complete += 1

        if total_actions == complete:
            result_msg.result_code = ResultCodes.RC_SUCCES 
        else:
            result_msg.result_code = ResultCodes.RC_FAILED

        result_msg.message = "Not implemented yet"  # TODO get any relevant messages from the cobot
        
        return result_msg


def main(args=None):
    # Initialize the ROS2 action server node
    rclpy.init(args=args)
    action_server = FokkerActionServer()
    
    # Spin so the server does not shutdown untill requested (e.g. Ctrl-C or another shutdown event)
    rclpy.spin(action_server)


if __name__ == "__main__":
    main()
