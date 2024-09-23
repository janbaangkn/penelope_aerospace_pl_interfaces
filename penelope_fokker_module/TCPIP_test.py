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
            "uid<tfst_1_1>"\
            "max_obstacle_height<40.0>"\
            "diam<5.0>"\
            "stack_thickness_tag<10.0>"\
            "pose<"\
                "pose_p_x<68.5>"\
                "pose_p_y<493>"\
                "pose_p_z<38>"\
                "pose_o_x<71>"\
                "pose_o_y<180>"\
                "pose_o_z<0>"\
            ">"\
        ">"\
        "hole_location<"\
            "uid<tfst_1_2>"\
            "max_obstacle_height<40.0>"\
            "diam<5.0>"\
            "stack_thickness_tag<10.0>"\
            "pose<"\
                "pose_p_x<104.5>"\
                "pose_p_y<493>"\
                "pose_p_z<38>"\
                "pose_o_x<71>"\
                "pose_o_y<180>"\
                "pose_o_z<0>"\
            ">"\
        ">"\
        "hole_location<"\
            "uid<tfst_1_3>"\
            "max_obstacle_height<40.0>"\
            "diam<5.0>"\
            "stack_thickness_tag<10.0>"\
            "pose<"\
                "pose_p_x<140.5>"\
                "pose_p_y<493>"\
                "pose_p_z<38>"\
                "pose_o_x<71>"\
                "pose_o_y<180>"\
                "pose_o_z<0>"\
            ">"\
        ">"\
        "hole_location<"\
            "uid<tfst_1_4>"\
            "max_obstacle_height<40.0>"\
            "diam<5.0>"\
            "stack_thickness_tag<10.0>"\
            "pose<"\
                "pose_p_x<177>"\
                "pose_p_y<493>"\
                "pose_p_z<38>"\
                "pose_o_x<71>"\
                "pose_o_y<180>"\
                "pose_o_z<0>"\
            ">"\
        ">"\
        "hole_location<"\
            "uid<tfst_2_1>"\
            "max_obstacle_height<40.0>"\
            "diam<5.0>"\
            "stack_thickness_tag<10.0>"\
            "pose<"\
                "pose_p_x<68.5>"\
                "pose_p_y<457>"\
                "pose_p_z<38>"\
                "pose_o_x<71>"\
                "pose_o_y<180>"\
                "pose_o_z<0>"\
            ">"\
        ">"\
        "hole_location<"\
            "uid<tfst_2_2>"\
            "max_obstacle_height<40.0>"\
            "diam<5.0>"\
            "stack_thickness_tag<10.0>"\
            "pose<"\
                "pose_p_x<104.5>"\
                "pose_p_y<457>"\
                "pose_p_z<38>"\
                "pose_o_x<71>"\
                "pose_o_y<180>"\
                "pose_o_z<0>"\
            ">"\
        ">"\
        "hole_location<"\
            "uid<tfst_2_3>"\
            "max_obstacle_height<40.0>"\
            "diam<5.0>"\
            "stack_thickness_tag<10.0>"\
            "pose<"\
                "pose_p_x<140.5>"\
                "pose_p_y<457>"\
                "pose_p_z<38>"\
                "pose_o_x<71>"\
                "pose_o_y<180>"\
                "pose_o_z<0>"\
            ">"\
        ">"\
        "hole_location<"\
            "uid<tfst_2_4>"\
            "max_obstacle_height<40.0>"\
            "diam<5.0>"\
            "stack_thickness_tag<10.0>"\
            "pose<"\
                "pose_p_x<177>"\
                "pose_p_y<457>"\
                "pose_p_z<38>"\
                "pose_o_x<71>"\
                "pose_o_y<180>"\
                "pose_o_z<0>"\
            ">"\
        ">"\
        "hole_location<"\
            "uid<tfst_3_1>"\
            "max_obstacle_height<40.0>"\
            "diam<5.0>"\
            "stack_thickness_tag<10.0>"\
            "pose<"\
                "pose_p_x<68.5>"\
                "pose_p_y<421>"\
                "pose_p_z<38>"\
                "pose_o_x<71>"\
                "pose_o_y<180>"\
                "pose_o_z<0>"\
            ">"\
        ">"\
        "hole_location<"\
            "uid<tfst_3_2>"\
            "max_obstacle_height<40.0>"\
            "diam<5.0>"\
            "stack_thickness_tag<10.0>"\
            "pose<"\
                "pose_p_x<104.5>"\
                "pose_p_y<421>"\
                "pose_p_z<38>"\
                "pose_o_x<71>"\
                "pose_o_y<180>"\
                "pose_o_z<0>"\
            ">"\
        ">"\
        "hole_location<"\
            "uid<tfst_3_3>"\
            "max_obstacle_height<40.0>"\
            "diam<5.0>"\
            "stack_thickness_tag<10.0>"\
            "pose<"\
                "pose_p_x<140.5>"\
                "pose_p_y<421>"\
                "pose_p_z<38>"\
                "pose_o_x<71>"\
                "pose_o_y<180>"\
                "pose_o_z<0>"\
            ">"\
        ">"\
        "hole_location<"\
            "uid<tfst_3_4>"\
            "max_obstacle_height<40.0>"\
            "diam<5.0>"\
            "stack_thickness_tag<10.0>"\
            "pose<"\
                "pose_p_x<177>"\
                "pose_p_y<421>"\
                "pose_p_z<38>"\
                "pose_o_x<71>"\
                "pose_o_y<180>"\
                "pose_o_z<0>"\
            ">"\
        ">"\
    ">"\
">"

feedback = send_message(uid=robot_uid, message=msg, feedback=True)
if feedback:
    print(f"Feedback: {feedback}")

# add temporary fastener in storage
msg = "populate_agent<"\
"tempfs<"\
    "tempf<"\
        "uid<tempf_01>"\
        "loc_uid<tfst_1_1>"\
        "fastener_state<1>"\
        "diam<5.0>"\
        "shaft_height<60.0>"\
        "min_stack_thickness<3.0>"\
        "max_stack_thickness<17.0>"\
        "tcp_tip_dist<25.0>"\
        "tcp_top_dist<21.0>"\
    ">"\
    "tempf<"\
        "uid<tempf_02>"\
        "loc_uid<tfst_1_2>"\
        "fastener_state<1>"\
        "diam<5.0>"\
        "shaft_height<60.0>"\
        "min_stack_thickness<3.0>"\
        "max_stack_thickness<17.0>"\
        "tcp_tip_dist<25.0>"\
        "tcp_top_dist<21.0>"\
    ">"\
    "tempf<"\
        "uid<tempf_03>"\
        "loc_uid<tfst_1_3>"\
        "fastener_state<1>"\
        "diam<5.0>"\
        "shaft_height<60.0>"\
        "min_stack_thickness<3.0>"\
        "max_stack_thickness<17.0>"\
        "tcp_tip_dist<25.0>"\
        "tcp_top_dist<21.0>"\
    ">"\
    "tempf<"\
        "uid<tempf_04>"\
        "loc_uid<tfst_1_4>"\
        "fastener_state<1>"\
        "diam<5.0>"\
        "shaft_height<60.0>"\
        "min_stack_thickness<3.0>"\
        "max_stack_thickness<17.0>"\
        "tcp_tip_dist<25.0>"\
        "tcp_top_dist<21.0>"\
    ">"\
    "tempf<"\
        "uid<tempf_05>"\
        "loc_uid<tfst_2_1>"\
        "fastener_state<1>"\
        "diam<5.0>"\
        "shaft_height<60.0>"\
        "min_stack_thickness<3.0>"\
        "max_stack_thickness<17.0>"\
        "tcp_tip_dist<25.0>"\
        "tcp_top_dist<21.0>"\
    ">"\
    "tempf<"\
        "uid<tempf_06>"\
        "loc_uid<tfst_2_2>"\
        "fastener_state<1>"\
        "diam<5.0>"\
        "shaft_height<60.0>"\
        "min_stack_thickness<3.0>"\
        "max_stack_thickness<17.0>"\
        "tcp_tip_dist<25.0>"\
        "tcp_top_dist<21.0>"\
    ">"\
    "tempf<"\
        "uid<tempf_07>"\
        "loc_uid<tfst_2_3>"\
        "fastener_state<1>"\
        "diam<5.0>"\
        "shaft_height<60.0>"\
        "min_stack_thickness<3.0>"\
        "max_stack_thickness<17.0>"\
        "tcp_tip_dist<25.0>"\
        "tcp_top_dist<21.0>"\
    ">"\
    "tempf<"\
        "uid<tempf_08>"\
        "loc_uid<tfst_2_4>"\
        "fastener_state<1>"\
        "diam<5.0>"\
        "shaft_height<60.0>"\
        "min_stack_thickness<3.0>"\
        "max_stack_thickness<17.0>"\
        "tcp_tip_dist<25.0>"\
        "tcp_top_dist<21.0>"\
    ">"\
    "tempf<"\
        "uid<tempf_09>"\
        "loc_uid<tfst_3_1>"\
        "fastener_state<1>"\
        "diam<5.0>"\
        "shaft_height<60.0>"\
        "min_stack_thickness<3.0>"\
        "max_stack_thickness<17.0>"\
        "tcp_tip_dist<25.0>"\
        "tcp_top_dist<21.0>"\
    ">"\
    "tempf<"\
        "uid<tempf_10>"\
        "loc_uid<tfst_3_2>"\
        "fastener_state<1>"\
        "diam<5.0>"\
        "shaft_height<60.0>"\
        "min_stack_thickness<3.0>"\
        "max_stack_thickness<17.0>"\
        "tcp_tip_dist<25.0>"\
        "tcp_top_dist<21.0>"\
    ">"\
    "tempf<"\
        "uid<tempf_11>"\
        "loc_uid<tfst_3_3>"\
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
        "hole_location<"\
            "uid<pr_01_02>"\
            "max_obstacle_height<40.0>"\
            "diam<5.0>"\
            "stack_thickness_tag<9.0>"\
            "pose<"\
                "pose_p_x<-126.5>"\
                "pose_p_y<796.0>"\
                "pose_p_z<1155.0>"\
                "pose_o_x<89.16>"\
                "pose_o_y<75.8>"\
                "pose_o_z<-158.73>"\
            ">"\
        ">"\
        "hole_location<"\
            "uid<pr_01_03>"\
            "max_obstacle_height<40.0>"\
            "diam<5.0>"\
            "stack_thickness_tag<9.0>"\
            "pose<"\
                "pose_p_x<-92.0>"\
                "pose_p_y<796.0>"\
                "pose_p_z<1155.0>"\
                "pose_o_x<89.16>"\
                "pose_o_y<75.8>"\
                "pose_o_z<-158.73>"\
            ">"\
        ">"\
        "hole_location<"\
            "uid<pr_01_04>"\
            "max_obstacle_height<40.0>"\
            "diam<5.0>"\
            "stack_thickness_tag<9.0>"\
            "pose<"\
                "pose_p_x<-56.0>"\
                "pose_p_y<796.0>"\
                "pose_p_z<1154.0>"\
                "pose_o_x<89.16>"\
                "pose_o_y<75.8>"\
                "pose_o_z<-158.73>"\
            ">"\
        ">"\
        "hole_location<"\
            "uid<pr_01_05>"\
            "max_obstacle_height<40.0>"\
            "diam<5.0>"\
            "stack_thickness_tag<9.0>"\
            "pose<"\
                "pose_p_x<-10.0>"\
                "pose_p_y<796.0>"\
                "pose_p_z<1154.0>"\
                "pose_o_x<89.16>"\
                "pose_o_y<75.8>"\
                "pose_o_z<-158.73>"\
            ">"\
        ">"\
        "hole_location<"\
            "uid<pr_01_06>"\
            "max_obstacle_height<40.0>"\
            "diam<5.0>"\
            "stack_thickness_tag<9.0>"\
            "pose<"\
                "pose_p_x<25.5>"\
                "pose_p_y<796.0>"\
                "pose_p_z<1154.0>"\
                "pose_o_x<89.16>"\
                "pose_o_y<75.8>"\
                "pose_o_z<-158.73>"\
            ">"\
        ">"\
        "hole_location<"\
            "uid<pr_01_07>"\
            "max_obstacle_height<40.0>"\
            "diam<5.0>"\
            "stack_thickness_tag<9.0>"\
            "pose<"\
                "pose_p_x<60.0>"\
                "pose_p_y<796.0>"\
                "pose_p_z<1154.0>"\
                "pose_o_x<89.16>"\
                "pose_o_y<75.8>"\
                "pose_o_z<-158.73>"\
            ">"\
        ">"\
        "hole_location<"\
            "uid<pr_01_08>"\
            "max_obstacle_height<40.0>"\
            "diam<5.0>"\
            "stack_thickness_tag<9.0>"\
            "pose<"\
                "pose_p_x<96.0>"\
                "pose_p_y<796.0>"\
                "pose_p_z<1154.0>"\
                "pose_o_x<89.16>"\
                "pose_o_y<75.8>"\
                "pose_o_z<-158.73>"\
            ">"\
        ">"\
    ">"\
">"

feedback = send_message(uid=robot_uid, message=msg, feedback=True)
if feedback:
    print(f"Feedback: {feedback}")

# add two actions
msg = "populate_agent<"\
"actions<"\
    "action<"\
        "uid<A01>"\
        "action_type<install_tempf>"\
        "loc_uid<pr_01_01>"\
        "action_state<1>"\
        "speed<100>"\
    ">"\
    "action<"\
        "uid<A02>"\
        "action_type<remove_fastener>"\
        "loc_uid<pr_01_01>"\
        "action_state<1>"\
        "speed<100>"\
    ">"\
">"

feedback = send_message(uid=robot_uid, message=msg, feedback=True)
if feedback:
    print(f"Feedback: {feedback}")

# execute operation with uid
feedback = send_message(uid=robot_uid, message="execute_single_operation<A01>", feedback=True)
if feedback:
    print(f"Feedback: {feedback}")

while True:
    if MessageService().inboxes.get(robot_uid) and len(MessageService().inboxes.get(robot_uid).messages) > 0:
        print(f"Message in inbox: {MessageService().get_inbox_message(robot_uid)}")
    time.sleep(0.01)

