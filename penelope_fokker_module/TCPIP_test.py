from tcp_communication.tcp_client import run_tcp_client
from tcp_communication.communication_functions import send_message
from tcp_communication.message_service_class import MessageService
import threading
import time

tf_ip_address = "10.237.20.101"
tf_port = 20002
tf_cobot_uid = f"{tf_ip_address}/{tf_port}"
tf_tcp_client_thread = threading.Thread(target=run_tcp_client, args=(tf_ip_address, tf_port))
tf_tcp_client_thread.start()

# pf_ip_address = "10.237.20.103"
# pf_port = 20002
# pf_cobot_uid = f"{pf_ip_address}/{pf_port}"
# pf_tcp_client_thread = threading.Thread(target=run_tcp_client, args=(pf_ip_address, pf_port))
# pf_tcp_client_thread.start()

message = "get_status"

feedback = send_message(uid=tf_cobot_uid, message=message, feedback=True)
print(f"Feedback: {feedback}")

# feedback = send_message(uid=pf_cobot_uid, message=message, feedback=True)
# print(f"Feedback: {feedback}")

# go to home
feedback = send_message(uid=tf_cobot_uid, message="goto_home", feedback=True)
if feedback:
    print(f"Feedback: {feedback}")

# # go to home
# feedback = send_message(uid=pf_cobot_uid, message="goto_home", feedback=True)
# if feedback:
#     print(f"Feedback: {feedback}")

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
                "pose_p_y<493.0>"\
                "pose_p_z<38.0>"\
                "pose_o_x<71.0>"\
                "pose_o_y<180.0>"\
                "pose_o_z<0.0>"\
            ">"\
        ">"\
        "hole_location<"\
            "uid<tfst_1_2>"\
            "max_obstacle_height<40.0>"\
            "diam<5.0>"\
            "stack_thickness_tag<10.0>"\
            "pose<"\
                "pose_p_x<104.5>"\
                "pose_p_y<493.0>"\
                "pose_p_z<38.0>"\
                "pose_o_x<71.0>"\
                "pose_o_y<180.0>"\
                "pose_o_z<0.0>"\
            ">"\
        ">"\
        "hole_location<"\
            "uid<tfst_1_3>"\
            "max_obstacle_height<40.0>"\
            "diam<5.0>"\
            "stack_thickness_tag<10.0>"\
            "pose<"\
                "pose_p_x<140.5>"\
                "pose_p_y<493.0>"\
                "pose_p_z<38.0>"\
                "pose_o_x<71.0>"\
                "pose_o_y<180.0>"\
                "pose_o_z<0.0>"\
            ">"\
        ">"\
        "hole_location<"\
            "uid<tfst_1_4>"\
            "max_obstacle_height<40.0>"\
            "diam<5.0>"\
            "stack_thickness_tag<10.0>"\
            "pose<"\
                "pose_p_x<177.0>"\
                "pose_p_y<493.0>"\
                "pose_p_z<38.0>"\
                "pose_o_x<71.0>"\
                "pose_o_y<180.0>"\
                "pose_o_z<0.0>"\
            ">"\
        ">"\
        "hole_location<"\
            "uid<tfst_2_1>"\
            "max_obstacle_height<40.0>"\
            "diam<5.0>"\
            "stack_thickness_tag<10.0>"\
            "pose<"\
                "pose_p_x<68.5>"\
                "pose_p_y<457.0>"\
                "pose_p_z<38.0>"\
                "pose_o_x<71.0>"\
                "pose_o_y<180.0>"\
                "pose_o_z<0.0>"\
            ">"\
        ">"\
        "hole_location<"\
            "uid<tfst_2_2>"\
            "max_obstacle_height<40.0>"\
            "diam<5.0>"\
            "stack_thickness_tag<10.0>"\
            "pose<"\
                "pose_p_x<104.5>"\
                "pose_p_y<457.0>"\
                "pose_p_z<38.0>"\
                "pose_o_x<71.0>"\
                "pose_o_y<180.0>"\
                "pose_o_z<0.0>"\
            ">"\
        ">"\
        "hole_location<"\
            "uid<tfst_2_3>"\
            "max_obstacle_height<40.0>"\
            "diam<5.0>"\
            "stack_thickness_tag<10.0>"\
            "pose<"\
                "pose_p_x<140.5>"\
                "pose_p_y<457.0>"\
                "pose_p_z<38.0>"\
                "pose_o_x<71.0>"\
                "pose_o_y<180.0>"\
                "pose_o_z<0.0>"\
            ">"\
        ">"\
        "hole_location<"\
            "uid<tfst_2_4>"\
            "max_obstacle_height<40.0>"\
            "diam<5.0>"\
            "stack_thickness_tag<10.0>"\
            "pose<"\
                "pose_p_x<177.0>"\
                "pose_p_y<457.0>"\
                "pose_p_z<38.0>"\
                "pose_o_x<71.0>"\
                "pose_o_y<180.0>"\
                "pose_o_z<0.0>"\
            ">"\
        ">"\
        "hole_location<"\
            "uid<tfst_3_1>"\
            "max_obstacle_height<40.0>"\
            "diam<5.0>"\
            "stack_thickness_tag<10.0>"\
            "pose<"\
                "pose_p_x<68.5>"\
                "pose_p_y<421.0>"\
                "pose_p_z<38.0>"\
                "pose_o_x<71.0>"\
                "pose_o_y<180.0>"\
                "pose_o_z<0.0>"\
            ">"\
        ">"\
        "hole_location<"\
            "uid<tfst_3_2>"\
            "max_obstacle_height<40.0>"\
            "diam<5.0>"\
            "stack_thickness_tag<10.0>"\
            "pose<"\
                "pose_p_x<104.5>"\
                "pose_p_y<421.0>"\
                "pose_p_z<38.0>"\
                "pose_o_x<71.0>"\
                "pose_o_y<180.0>"\
                "pose_o_z<0.0>"\
            ">"\
        ">"\
        "hole_location<"\
            "uid<tfst_3_3>"\
            "max_obstacle_height<40.0>"\
            "diam<5.0>"\
            "stack_thickness_tag<10.0>"\
            "pose<"\
                "pose_p_x<140.5>"\
                "pose_p_y<421.0>"\
                "pose_p_z<38.0>"\
                "pose_o_x<71.0>"\
                "pose_o_y<180.0>"\
                "pose_o_z<0.0>"\
            ">"\
        ">"\
        "hole_location<"\
            "uid<tfst_3_4>"\
            "max_obstacle_height<40.0>"\
            "diam<5.0>"\
            "stack_thickness_tag<10.0>"\
            "pose<"\
                "pose_p_x<177.0>"\
                "pose_p_y<421.0>"\
                "pose_p_z<38.0>"\
                "pose_o_x<71.0>"\
                "pose_o_y<180.0>"\
                "pose_o_z<0.0>"\
            ">"\
        ">"\
    ">"\
">"

feedback = send_message(uid=tf_cobot_uid, message=msg, feedback=True)
if feedback:
    print(f"Feedback: {feedback}")


# add hole locations, stack thickness and diameter in the product list
msg = "populate_agent<"\
"product<"\
    "uid<product>"\
    "locations<"\
        "hole_location<"\
            "uid<left_drill_jig_01>"\
            "max_obstacle_height<40.0>"\
            "diam<5.0>"\
            "stack_thickness_tag<9.0>"\
            "pose<"\
                "pose_p_x<11.0>"\
                "pose_p_y<838.0>"\
                "pose_p_z<1117.5>"\
                "pose_o_x<90.0>"\
                "pose_o_y<75.0>"\
                "pose_o_z<0.0>"\
            ">"\
        ">"\
        "hole_location<"\
            "uid<left_drill_jig_08>"\
            "max_obstacle_height<40.0>"\
            "diam<5.0>"\
            "stack_thickness_tag<9.0>"\
            "pose<"\
                "pose_p_x<13.5>"\
                "pose_p_y<902.0>"\
                "pose_p_z<908.5>"\
                "pose_o_x<90.0>"\
                "pose_o_y<69.0>"\
                "pose_o_z<0.0>"\
            ">"\
        ">"\
        "hole_location<"\
            "uid<left_drill_jig_15>"\
            "max_obstacle_height<40.0>"\
            "diam<5.0>"\
            "stack_thickness_tag<9.0>"\
            "pose<"\
                "pose_p_x<16.5>"\
                "pose_p_y<991.0>"\
                "pose_p_z<708.0>"\
                "pose_o_x<90.0>"\
                "pose_o_y<63.0>"\
                "pose_o_z<0.0>"\
            ">"\
        ">"\
        "hole_location<"\
            "uid<inner_vert_jig_01_01>"\
            "max_obstacle_height<40.0>"\
            "diam<5.0>"\
            "stack_thickness_tag<9.0>"\
            "pose<"\
                "pose_p_x<222.0>"\
                "pose_p_y<865.0>"\
                "pose_p_z<1021.5>"\
                "pose_o_x<90.0>"\
                "pose_o_y<72.0>"\
                "pose_o_z<10.0>"\
            ">"\
        ">"\
        "hole_location<"\
            "uid<inner_vert_jig_01_08>"\
            "max_obstacle_height<40.0>"\
            "diam<5.0>"\
            "stack_thickness_tag<9.0>"\
            "pose<"\
                "pose_p_x<226.0>"\
                "pose_p_y<938.0>"\
                "pose_p_z<815.0>"\
                "pose_o_x<90.0>"\
                "pose_o_y<66.0>"\
                "pose_o_z<10.0>"\
            ">"\
        ">"\
        "hole_location<"\
            "uid<inner_vert_jig_02_01>"\
            "max_obstacle_height<40.0>"\
            "diam<5.0>"\
            "stack_thickness_tag<9.0>"\
            "pose<"\
                "pose_p_x<450.8>"\
                "pose_p_y<865.0>"\
                "pose_p_z<1020.0>"\
                "pose_o_x<90.0>"\
                "pose_o_y<72.0>"\
                "pose_o_z<25.0>"\
            ">"\
        ">"\
        "hole_location<"\
            "uid<inner_vert_jig_02_08>"\
            "max_obstacle_height<40.0>"\
            "diam<5.0>"\
            "stack_thickness_tag<9.0>"\
            "pose<"\
                "pose_p_x<452.0>"\
                "pose_p_y<938.0>"\
                "pose_p_z<814.0>"\
                "pose_o_x<90.0>"\
                "pose_o_y<66.0>"\
                "pose_o_z<25.0>"\
            ">"\
        ">"\
        "hole_location<"\
            "uid<inner_vert_jig_03_01>"\
            "max_obstacle_height<40.0>"\
            "diam<5.0>"\
            "stack_thickness_tag<9.0>"\
            "pose<"\
                "pose_p_x<621.0>"\
                "pose_p_y<862.0>"\
                "pose_p_z<1021.5>"\
                "pose_o_x<90.0>"\
                "pose_o_y<72.0>"\
                "pose_o_z<30.0>"\
            ">"\
        ">"\
        "hole_location<"\
            "uid<inner_vert_jig_03_08>"\
            "max_obstacle_height<40.0>"\
            "diam<5.0>"\
            "stack_thickness_tag<9.0>"\
            "pose<"\
                "pose_p_x<623.0>"\
                "pose_p_y<938.0>"\
                "pose_p_z<817.0>"\
                "pose_o_x<90.0>"\
                "pose_o_y<66.0>"\
                "pose_o_z<30.0>"\
            ">"\
        ">"\
    ">"\
">"

feedback = send_message(uid=tf_cobot_uid, message=msg, feedback=True)
if feedback:
    print(f"Feedback: {feedback}")

# add 3 temporary fasteners in storage
# add 8 temporary fasteners in the product
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
        "loc_uid<left_drill_jig_08>"\
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
        "loc_uid<left_drill_jig_15>"\
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
        "loc_uid<inner_vert_jig_01_01>"\
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
        "loc_uid<inner_vert_jig_01_08>"\
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
        "loc_uid<inner_vert_jig_02_01>"\
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
        "loc_uid<inner_vert_jig_02_08>"\
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
        "loc_uid<inner_vert_jig_03_01>"\
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
        "loc_uid<inner_vert_jig_03_08>"\
        "fastener_state<1>"\
        "diam<5.0>"\
        "shaft_height<60.0>"\
        "min_stack_thickness<3.0>"\
        "max_stack_thickness<17.0>"\
        "tcp_tip_dist<25.0>"\
        "tcp_top_dist<21.0>"\
    ">"\
">"

feedback = send_message(uid=tf_cobot_uid, message=msg, feedback=True)
if feedback:
    print(f"Feedback: {feedback}")

# add ten actions
# 01: install a tempf in left_drill_jig_01
# 02: remove tempf from left_drill_jig_01
# 03: remove tempf from left_drill_jig_08
# 04: remove tempf from left_drill_jig_15
# 05: remove tempf from inner_vert_jig_01_01
# 06: remove tempf from inner_vert_jig_01_08
# 07: remove tempf from inner_vert_jig_02_01
# 08: remove tempf from inner_vert_jig_02_08
# 09: remove tempf from inner_vert_jig_03_01
# 10: remove tempf from inner_vert_jig_03_08
msg = "populate_agent<"\
"actions<"\
    "action<"\
        "uid<A01>"\
        "action_type<install_tempf>"\
        "loc_uid<left_drill_jig_01>"\
        "action_state<1>"\
        "speed<100>"\
    ">"\
    "action<"\
        "uid<A02>"\
        "action_type<remove_fastener>"\
        "loc_uid<left_drill_jig_01>"\
        "action_state<1>"\
        "speed<100>"\
    ">"\
    "action<"\
        "uid<A03>"\
        "action_type<remove_fastener>"\
        "loc_uid<left_drill_jig_08>"\
        "action_state<1>"\
        "speed<100>"\
    ">"\
    "action<"\
        "uid<A04>"\
        "action_type<remove_fastener>"\
        "loc_uid<left_drill_jig_15>"\
        "action_state<1>"\
        "speed<100>"\
    ">"\
    "action<"\
        "uid<A05>"\
        "action_type<remove_fastener>"\
        "loc_uid<inner_vert_jig_01_01>"\
        "action_state<1>"\
        "speed<100>"\
    ">"\
    "action<"\
        "uid<A06>"\
        "action_type<remove_fastener>"\
        "loc_uid<inner_vert_jig_01_02>"\
        "action_state<1>"\
        "speed<100>"\
    ">"\
    "action<"\
        "uid<A07>"\
        "action_type<remove_fastener>"\
        "loc_uid<inner_vert_jig_02_01>"\
        "action_state<1>"\
        "speed<100>"\
    ">"\
    "action<"\
        "uid<A08>"\
        "action_type<remove_fastener>"\
        "loc_uid<inner_vert_jig_02_02>"\
        "action_state<1>"\
        "speed<100>"\
    ">"\
    "action<"\
        "uid<A09>"\
        "action_type<remove_fastener>"\
        "loc_uid<inner_vert_jig_03_01>"\
        "action_state<1>"\
        "speed<100>"\
    ">"\
    "action<"\
        "uid<A10>"\
        "action_type<remove_fastener>"\
        "loc_uid<inner_vert_jig_03_02>"\
        "action_state<1>"\
        "speed<100>"\
    ">"\
">"

feedback = send_message(uid=tf_cobot_uid, message=msg, feedback=True)
if feedback:
    print(f"Feedback: {feedback}")

# execute operation with uid
feedback = send_message(uid=tf_cobot_uid, message="execute_single_operation<A01>", feedback=True)
if feedback:
    print(f"Feedback: {feedback}")

# go to home
feedback = send_message(uid=tf_cobot_uid, message="goto_home", feedback=True)
if feedback:
    print(f"Feedback: {feedback}")

while True:
    if MessageService().inboxes.get(tf_cobot_uid) and len(MessageService().inboxes.get(tf_cobot_uid).messages) > 0:
        print(f"Message in inbox: {MessageService().get_inbox_message(tf_cobot_uid)}")
    time.sleep(0.01)

