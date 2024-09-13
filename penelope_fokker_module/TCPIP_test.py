from tcp_communication.tcp_client import run_tcp_client
from tcp_communication.communication_functions import send_message
from tcp_communication.message_service_class import MessageService
import threading

ip_address = "10.237.20.101"
port = 20002
robot_uid = f"{ip_address}/{port}"

tcp_client_thread = threading.Thread(target=run_tcp_client, args=(ip_address, port))
tcp_client_thread.start()
message = "get_status"

feedback = send_message(uid=robot_uid, message=message, feedback=True)
if feedback:
    print(f"Feedback: {feedback}")

msg = "populate_agent<"\
"tempf_storage_loc<"\
    "uid<tempf_storage>"\
    "locations<"\
        "hole_location<"\
            "uid<tfst_01>"\
            "max_obstacle_height<40.0>"\
            "diam<5.0>"\
            "stack_thickness_tag<10.0>"\
            "pose<"\
                "pose_p_x<122.4>"\
                "pose_p_y<476.77>"\
                "pose_p_z<38>"\
                "pose_o_x<35>"\
                "pose_o_y<180>"\
                "pose_o_z<-35>"\
            ">"\
        ">"\
    ">"\
">"

feedback = send_message(uid=robot_uid, message=msg, feedback=True)
if feedback:
    print(f"Feedback: {feedback}")

# while True:
#     if MessageService().inboxes.get(robot_uid) and len(MessageService().inboxes.get(robot_uid).messages) > 0:
#         print(f"Message in inbox: {MessageService().get_inbox_message(robot_uid)}")
#     time.sleep(0.01)

