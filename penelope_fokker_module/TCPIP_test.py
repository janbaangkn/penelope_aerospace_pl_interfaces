from tcp_communication.tcp_client import run_tcp_client
from tcp_communication.communication_functions import send_message
from tcp_communication.message_service_class import MessageService
import threading
import time

ip_address = "10.237.20.101"
port = 20002
robot_uid = f"{ip_address}/{port}"

tcp_client_thread = threading.Thread(target=run_tcp_client, args=(ip_address, port))
tcp_client_thread.start()
message = "get_status"

feedback = send_message(uid=robot_uid, message=message, feedback=True)
if feedback:
    print(f"Feedback: {feedback}")

# add hole locations, stack thickness and diameter in the permanent fastener storage list 
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

# # add permanent fastener in storage
msg = "populate_agent<"\
"tempfs<"\
    "tempf<"\
        "uid<tempf_01>"\
        "loc_uid<tfst_01>"\
        "fastener_state<1>"\
        "diam<5.0>"\
        "shaft_height<60.0>"\
        "min_stack_thickness<3.0>"\
        "max_stack_thickness<17.0>"\
        "tcp_tip_dist<25.0>"\
        "tcp_top_dist<21.0>"\
    ">"\
">"

feedback = send_message(uid=robot_uid, message=msg, feedback=True)
if feedback:
    print(f"Feedback: {feedback}")

# # add hole locations, stack thickness and diameter in the product list
msg = "populate_agent<"\
"product<"\
    "uid<product>"\
    "locations<"\
        "hole_location<"\
            "uid<pr_01_01>"\
            "max_obstacle_height<40.0>"\
            "diam<5.0>"\
            "stack_thickness_tag<9.0>"\
            "pose<"\
                "pose_p_x<-162.0>"\
                "pose_p_y<796.0>"\
                "pose_p_z<1155.0>"\
                "pose_o_x<89.16>"\
                "pose_o_y<75.8>"\
                "pose_o_z<-158.73>"\
            ">"\
        ">"\
    ">"\
">"

# agent.product.add_loc_to_holes_and_fast_lst("pr_01_02", 5, 9, posx(-126.5,796,1155,89.16,75.8,-158.73))
# agent.product.add_loc_to_holes_and_fast_lst("pr_01_03", 5, 9, posx(-92,796,1155,89.16,75.8,-158.73))
# agent.product.add_loc_to_holes_and_fast_lst("pr_01_04", 5, 9, posx(-56,796,1154.5,89.16,75.8,-158.73))
# agent.product.add_loc_to_holes_and_fast_lst("pr_01_05", 5, 9, posx(-10,796,1154.5,89.16,75.8,-158.73))
# agent.product.add_loc_to_holes_and_fast_lst("pr_01_06", 5, 9, posx(25.5,796,1154,89.16,75.8,-158.73))
# agent.product.add_loc_to_holes_and_fast_lst("pr_01_07", 5, 9, posx(60,796,1154,89.16,75.8,-158.73))
# agent.product.add_loc_to_holes_and_fast_lst("pr_01_08", 5, 9, posx(96,796,1154,89.16,75.8,-158.73))

feedback = send_message(uid=robot_uid, message=msg, feedback=True)
if feedback:
    print(f"Feedback: {feedback}")


# insert and install a permf from storage to product
# agent._add_install_tempf_action("A01", "pr_01_01")
# agent._add_remove_tempf_action("A02", "pr_01_01")

# agent.execute_all(check_inventory = False)

while True:
    if MessageService().inboxes.get(robot_uid) and len(MessageService().inboxes.get(robot_uid).messages) > 0:
        print(f"Message in inbox: {MessageService().get_inbox_message(robot_uid)}")
    time.sleep(0.01)

