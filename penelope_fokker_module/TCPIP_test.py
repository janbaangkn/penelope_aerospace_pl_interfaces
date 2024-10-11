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

# go to home
feedback = send_message(uid=tf_cobot_uid, message="goto_home", feedback=True)
if feedback:
    print(f"Feedback: {feedback}")

# go to home
# feedback = send_message(uid=pf_cobot_uid, message="goto_home", feedback=True)
# if feedback:
#     print(f"Feedback: {feedback}")

# add hole locations, stack thickness and diameter in the permanent fastener storage list 
# msg = "populate_agent<"\
# "permf_storage_loc<"\
#     "uid<permf_storage>"\
#     "locations<"\
#         "hole_location<"\
#             "uid<pf_st_01>"\
#             "max_obstacle_height<40.0>"\
#             "diam<5.055>"\
#             "stack_thickness_tag<5.0>"\
#             "pose<"\
#                 "pose_p_x<-91.82>"\
#                 "pose_p_y<307.27>"\
#                 "pose_p_z<35.46>"\
#                 "pose_o_x<50.11>"\
#                 "pose_o_y<178.79>"\
#                 "pose_o_z<30.39>"\
#             ">"\
#         ">"\
#         "hole_location<"\
#             "uid<pf_st_02>"\
#             "max_obstacle_height<40.0>"\
#             "diam<5.055>"\
#             "stack_thickness_tag<5.0>"\
#             "pose<"\
#                 "pose_p_x<-92.95>"\
#                 "pose_p_y<330.78>"\
#                 "pose_p_z<35.310>"\
#                 "pose_o_x<100.1>"\
#                 "pose_o_y<-179.1>"\
#                 "pose_o_z<89.0>"\
#             ">"\
#         ">"\
#         "hole_location<"\
#             "uid<pf_st_03>"\
#             "max_obstacle_height<40.0>"\
#             "diam<5.055>"\
#             "stack_thickness_tag<5.0>"\
#             "pose<"\
#                 "pose_p_x<-117.08>"\
#                 "pose_p_y<306.12>"\
#                 "pose_p_z<35.13>"\
#                 "pose_o_x<153.13>"\
#                 "pose_o_y<-179.72>"\
#                 "pose_o_z<128.87>"\
#             ">"\
#         ">"\
#         "hole_location<"\
#             "uid<pf_st_04>"\
#             "max_obstacle_height<40.0>"\
#             "diam<5.055>"\
#             "stack_thickness_tag<5.0>"\
#             "pose<"\
#                 "pose_p_x<-117.4>"\
#                 "pose_p_y<331.62>"\
#                 "pose_p_z<35.23>"\
#                 "pose_o_x<44.76>"\
#                 "pose_o_y<179.76>"\
#                 "pose_o_z<23.75>"\
#             ">"\
#         ">"\
#         "hole_location<"\
#             "uid<pf_st_05>"\
#             "max_obstacle_height<40.0>"\
#             "diam<5.055>"\
#             "stack_thickness_tag<5.0>"\
#             "pose<"\
#                 "pose_p_x<-142.3>"\
#                 "pose_p_y<306.01>"\
#                 "pose_p_z<35.14>"\
#                 "pose_o_x<94.83>"\
#                 "pose_o_y<179.42>"\
#                 "pose_o_z<74.38>"\
#             ">"\
#         ">"\
#         "hole_location<"\
#             "uid<pf_st_06>"\
#             "max_obstacle_height<40.0>"\
#             "diam<5.055>"\
#             "stack_thickness_tag<5.0>"\
#             "pose<"\
#                 "pose_p_x<-142.85>"\
#                 "pose_p_y<330.23>"\
#                 "pose_p_z<35.35>"\
#                 "pose_o_x<76.47>"\
#                 "pose_o_y<-179.05>"\
#                 "pose_o_z<55.94>"\
#             ">"\
#         ">"\
#         "hole_location<"\
#             "uid<pf_st_07>"\
#             "max_obstacle_height<40.0>"\
#             "diam<5.055>"\
#             "stack_thickness_tag<5.0>"\
#             "pose<"\
#                 "pose_p_x<-167.04>"\
#                 "pose_p_y<306.16>"\
#                 "pose_p_z<35.19>"\
#                 "pose_o_x<36.58>"\
#                 "pose_o_y<179.2>"\
#                 "pose_o_z<3.74>"\
#             ">"\
#         ">"\
#         "hole_location<"\
#             "uid<pf_st_08>"\
#             "max_obstacle_height<40.0>"\
#             "diam<5.055>"\
#             "stack_thickness_tag<5.0>"\
#             "pose<"\
#                 "pose_p_x<-167.67>"\
#                 "pose_p_y<330.93>"\
#                 "pose_p_z<35.31>"\
#                 "pose_o_x<9.27>"\
#                 "pose_o_y<179.52>"\
#                 "pose_o_z<-16.26>"\
#             ">"\
#         ">"\
#         "hole_location<"\
#             "uid<pf_st_09>"\
#             "max_obstacle_height<40.0>"\
#             "diam<5.055>"\
#             "stack_thickness_tag<5.0>"\
#             "pose<"\
#                 "pose_p_x<-192.09>"\
#                 "pose_p_y<304.93>"\
#                 "pose_p_z<35.37>"\
#                 "pose_o_x<136.23>"\
#                 "pose_o_y<-178.74>"\
#                 "pose_o_z<106.02>"\
#             ">"\
#         ">"\
#         "hole_location<"\
#             "uid<pf_st_10>"\
#             "max_obstacle_height<40.0>"\
#             "diam<5.055>"\
#             "stack_thickness_tag<5.0>"\
#             "pose<"\
#                 "pose_p_x<-192.36>"\
#                 "pose_p_y<329.79>"\
#                 "pose_p_z<35.48>"\
#                 "pose_o_x<163.76>"\
#                 "pose_o_y<-178.77>"\
#                 "pose_o_z<136.94>"\
#             ">"\
#         ">"\
#         "hole_location<"\
#             "uid<pf_st_11>"\
#             "max_obstacle_height<40.0>"\
#             "diam<5.055>"\
#             "stack_thickness_tag<5.0>"\
#             "pose<"\
#                 "pose_p_x<-216.47>"\
#                 "pose_p_y<304.11>"\
#                 "pose_p_z<35.9>"\
#                 "pose_o_x<121.83>"\
#                 "pose_o_y<-178.14>"\
#                 "pose_o_z<101.79>"\
#             ">"\
#         ">"\
#         "hole_location<"\
#             "uid<pf_st_12>"\
#             "max_obstacle_height<40.0>"\
#             "diam<5.055>"\
#             "stack_thickness_tag<5.0>"\
#             "pose<"\
#                 "pose_p_x<-217.87>"\
#                 "pose_p_y<329.26>"\
#                 "pose_p_z<39.53>"\
#                 "pose_o_x<86.5>"\
#                 "pose_o_y<-178.7>"\
#                 "pose_o_z<61.99>"\
#             ">"\
#         ">"\
#         "hole_location<"\
#             "uid<pf_st_13>"\
#             "max_obstacle_height<40.0>"\
#             "diam<5.055>"\
#             "stack_thickness_tag<5.0>"\
#             "pose<"\
#                 "pose_p_x<-241.51>"\
#                 "pose_p_y<303.99>"\
#                 "pose_p_z<35.51>"\
#                 "pose_o_x<163.82>"\
#                 "pose_o_y<-178.42>"\
#                 "pose_o_z<135.21>"\
#             ">"\
#         ">"\
#         "hole_location<"\
#             "uid<pf_st_14>"\
#             "max_obstacle_height<40.0>"\
#             "diam<5.055>"\
#             "stack_thickness_tag<5.0>"\
#             "pose<"\
#                 "pose_p_x<-242.91>"\
#                 "pose_p_y<329.1>"\
#                 "pose_p_z<35.48>"\
#                 "pose_o_x<78.96>"\
#                 "pose_o_y<-179.05>"\
#                 "pose_o_z<57.88>"\
#             ">"\
#         ">"\
#     ">"\
# ">"

# feedback = send_message(uid=pf_cobot_uid, message=msg, feedback=True)
# if feedback:
#     print(f"Feedback: {feedback}")
# 
# # add hole locations, stack thickness and diameter in the temp fastener storage list 
msg = "populate_agent<"\
    "tempf_storage_loc<"\
        "uid<tempf_storage>"\
        "locations<"\
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
    ">"\
">"

feedback = send_message(uid=tf_cobot_uid, message=msg, feedback=True)
if feedback:
    print(f"Feedback: {feedback}")

# add hole locations, stack thickness and diameter in the permf product list
# msg = "populate_agent<"\
# "product<"\
#     "uid<product>"\
#     "locations<"\
#         "hole_location<"\
#             "uid<pf_pr_01>"\
#             "max_obstacle_height<40.0>"\
#             "diam<5.055>"\
#             "stack_thickness_tag<5.0>"\
#             "pose<"\
#                 "pose_p_x<-329.83>"\
#                 "pose_p_y<729.110>"\
#                 "pose_p_z<813.0>"\
#                 "pose_o_x<91.57>"\
#                 "pose_o_y<64.97>"\
#                 "pose_o_z<85.09>"\
#             ">"\
#         ">"\
#             "hole_location<"\
#             "uid<pf_pr_02>"\
#             "max_obstacle_height<40.0>"\
#             "diam<5.055>"\
#             "stack_thickness_tag<5.0>"\
#             "pose<"\
#                 "pose_p_x<-330.54>"\
#                 "pose_p_y<655.720>"\
#                 "pose_p_z<1017.77>"\
#                 "pose_o_x<92.02>"\
#                 "pose_o_y<72.47>"\
#                 "pose_o_z<86.73>"\
#             ">"\
#         ">"\
#         "hole_location<"\
#             "uid<pf_pr_03>"\
#             "max_obstacle_height<40.0>"\
#             "diam<5.055>"\
#             "stack_thickness_tag<5.0>"\
#             "pose<"\
#                 "pose_p_x<-499.6>"\
#                 "pose_p_y<729.81>"\
#                 "pose_p_z<810.5>"\
#                 "pose_o_x<90.34>"\
#                 "pose_o_y<66.72>"\
#                 "pose_o_z<88.64>"\
#             ">"\
#         ">"\
#         "hole_location<"\
#             "uid<pf_pr_04>"\
#             "max_obstacle_height<40.0>"\
#             "diam<5.055>"\
#             "stack_thickness_tag<5.0>"\
#             "pose<"\
#                 "pose_p_x<-500.57>"\
#                 "pose_p_y<654.29>"\
#                 "pose_p_z<1016.11>"\
#                 "pose_o_x<92.08>"\
#                 "pose_o_y<70.39>"\
#                 "pose_o_z<89.6>"\
#             ">"\
#         ">"\
#         "hole_location<"\
#             "uid<pf_pr_05>"\
#             "max_obstacle_height<40.0>"\
#             "diam<5.055>"\
#             "stack_thickness_tag<5.0>"\
#             "pose<"\
#                 "pose_p_x<-725.72>"\
#                 "pose_p_y<727.750>"\
#                 "pose_p_z<812.340>"\
#                 "pose_o_x<88.94>"\
#                 "pose_o_y<67.13>"\
#                 "pose_o_z<93.49>"\
#             ">"\
#         ">"\
#         "hole_location<"\
#             "uid<pf_pr_06>"\
#             "max_obstacle_height<40.0>"\
#             "diam<5.055>"\
#             "stack_thickness_tag<5.0>"\
#             "pose<"\
#                 "pose_p_x<-727.53>"\
#                 "pose_p_y<652.19>"\
#                 "pose_p_z<1018.0>"\
#                 "pose_o_x<91.6>"\
#                 "pose_o_y<72.39>"\
#                 "pose_o_z<87.84>"\
#             ">"\
#         ">"\
#         "hole_location<"\
#             "uid<pf_pr_11>"\
#             "max_obstacle_height<40.0>"\
#             "diam<5.055>"\
#             "stack_thickness_tag<5.0>"\
#             "pose<"\
#                 "pose_p_x<-329.47>"\
#                 "pose_p_y<717.91>"\
#                 "pose_p_z<841.81>"\
#                 "pose_o_x<89.64>"\
#                 "pose_o_y<65.69>"\
#                 "pose_o_z<89.42>"\
#             ">"\
#         ">"\
#         "hole_location<"\
#             "uid<pf_pr_12>"\
#             "max_obstacle_height<40.0>"\
#             "diam<5.055>"\
#             "stack_thickness_tag<5.0>"\
#             "pose<"\
#                 "pose_p_x<-329.71>"\
#                 "pose_p_y<706.63>"\
#                 "pose_p_z<869.79>"\
#                 "pose_o_x<91.56>"\
#                 "pose_o_y<67.41>"\
#                 "pose_o_z<90.22>"\
#             ">"\
#         ">"\
#         "hole_location<"\
#             "uid<pf_pr_13>"\
#             "max_obstacle_height<40.0>"\
#             "diam<5.055>"\
#             "stack_thickness_tag<5.0>"\
#             "pose<"\
#                 "pose_p_x<-330.01>"\
#                 "pose_p_y<695.28>"\
#                 "pose_p_z<900.14>"\
#                 "pose_o_x<92.7>"\
#                 "pose_o_y<65.84>"\
#                 "pose_o_z<87.58>"\
#             ">"\
#         ">"\
#         "hole_location<"\
#             "uid<pf_pr_14>"\
#             "max_obstacle_height<40.0>"\
#             "diam<5.055>"\
#             "stack_thickness_tag<5.0>"\
#             "pose<"\
#                 "pose_p_x<-329.56>"\
#                 "pose_p_y<684.27>"\
#                 "pose_p_z<929.38>"\
#                 "pose_o_x<91.51>"\
#                 "pose_o_y<68.44>"\
#                 "pose_o_z<88.93>"\
#             ">"\
#         ">"\
#         "hole_location<"\
#             "uid<pf_pr_15>"\
#             "max_obstacle_height<40.0>"\
#             "diam<5.055>"\
#             "stack_thickness_tag<5.0>"\
#             "pose<"\
#                 "pose_p_x<-330.18>"\
#                 "pose_p_y<673.5>"\
#                 "pose_p_z<958.83>"\
#                 "pose_o_x<91.71>"\
#                 "pose_o_y<70.89>"\
#                 "pose_o_z<90.12>"\
#             ">"\
#         ">"\
#         "hole_location<"\
#             "uid<pf_pr_16>"\
#             "max_obstacle_height<40.0>"\
#             "diam<5.055>"\
#             "stack_thickness_tag<5.0>"\
#             "pose<"\
#                 "pose_p_x<-329.3>"\
#                 "pose_p_y<663.78>"\
#                 "pose_p_z<988.91>"\
#                 "pose_o_x<91.67>"\
#                 "pose_o_y<69.43>"\
#                 "pose_o_z<89.35>"\
#             ">"\
#         ">"\
#         "hole_location<"\
#             "uid<pf_pr_17>"\
#             "max_obstacle_height<40.0>"\
#             "diam<5.055>"\
#             "stack_thickness_tag<5.0>"\
#             "pose<"\
#                 "pose_p_x<-499.9>"\
#                 "pose_p_y<717.33>"\
#                 "pose_p_z<840.44>"\
#                 "pose_o_x<90.91>"\
#                 "pose_o_y<66.33>"\
#                 "pose_o_z<87.68>"\
#             ">"\
#         ">"\
#         "hole_location<"\
#             "uid<pf_pr_18>"\
#             "max_obstacle_height<40.0>"\
#             "diam<5.055>"\
#             "stack_thickness_tag<5.0>"\
#             "pose<"\
#                 "pose_p_x<-499.9>"\
#                 "pose_p_y<705.34>"\
#                 "pose_p_z<869.08>"\
#                 "pose_o_x<90.37>"\
#                 "pose_o_y<67.4>"\
#                 "pose_o_z<89.8>"\
#             ">"\
#         ">"\
#         "hole_location<"\
#             "uid<pf_pr_19>"\
#             "max_obstacle_height<40.0>"\
#             "diam<5.055>"\
#             "stack_thickness_tag<5.0>"\
#             "pose<"\
#                 "pose_p_x<-499.34>"\
#                 "pose_p_y<694.19>"\
#                 "pose_p_z<897.67>"\
#                 "pose_o_x<89.7>"\
#                 "pose_o_y<69.98>"\
#                 "pose_o_z<88.57>"\
#             ">"\
#         ">"\
#         "hole_location<"\
#             "uid<pf_pr_20>"\
#             "max_obstacle_height<40.0>"\
#             "diam<5.055>"\
#             "stack_thickness_tag<5.0>"\
#             "pose<"\
#                 "pose_p_x<-498.99>"\
#                 "pose_p_y<682.8>"\
#                 "pose_p_z<927.57>"\
#                 "pose_o_x<89.89>"\
#                 "pose_o_y<68.2>"\
#                 "pose_o_z<89.85>"\
#             ">"\
#         ">"\
#         "hole_location<"\
#             "uid<pf_pr_21>"\
#             "max_obstacle_height<40.0>"\
#             "diam<5.055>"\
#             "stack_thickness_tag<5.0>"\
#             "pose<"\
#                 "pose_p_x<-500.06>"\
#                 "pose_p_y<673.07>"\
#                 "pose_p_z<957.22>"\
#                 "pose_o_x<92.09>"\
#                 "pose_o_y<69.97>"\
#                 "pose_o_z<89.56>"\
#             ">"\
#         ">"\
#         "hole_location<"\
#             "uid<pf_pr_22>"\
#             "max_obstacle_height<40.0>"\
#             "diam<5.055>"\
#             "stack_thickness_tag<5.0>"\
#             "pose<"\
#                 "pose_p_x<-499.8>"\
#                 "pose_p_y<664.19>"\
#                 "pose_p_z<986.93>"\
#                 "pose_o_x<93.46>"\
#                 "pose_o_y<71.1>"\
#                 "pose_o_z<86.57>"\
#             ">"\
#         ">"\
#     ">"\
# ">"\

# feedback = send_message(uid=pf_cobot_uid, message=msg, feedback=True)
# if feedback:
#     print(f"Feedback: {feedback}")

# # add hole locations, stack thickness and diameter in the tempf product list
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
                "pose_p_z<1113.5>"\
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
                "pose_p_x<13.0>"\
                "pose_p_y<902.0>"\
                "pose_p_z<905.0>"\
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
                "pose_p_z<705.5>"\
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
                "pose_p_z<1018.2>"\
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
                "pose_p_z<812.0>"\
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
                "pose_p_x<451.5>"\
                "pose_p_y<863.0>"\
                "pose_p_z<1015.5>"\
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
                "pose_p_x<453.5>"\
                "pose_p_y<939.0>"\
                "pose_p_z<810.0>"\
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
                "pose_p_x<622.0>"\
                "pose_p_y<864.0>"\
                "pose_p_z<1020.0>"\
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
                "pose_p_z<814.5>"\
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

# add permanent fasteners in storage
# msg = "populate_agent<"\
# "fasteners<"\
#     "fastener<"\
#         "uid<permf_01>"\
#         "loc_uid<pf_st_01>"\
#         "fastener_state<1>"\
#         "diam<5.055>"\
#         "shaft_height<23.37>"\
#         "min_stack_thickness<3.96>"\
#         "max_stack_thickness<5.59>"\
#         "tcp_tip_dist<14.81>"\
#         "tcp_top_dist<4.45>"\
#     ">"\
#     "fastener<"\
#         "uid<permf_02>"\
#         "loc_uid<pf_st_02>"\
#         "fastener_state<1>"\
#         "diam<5.055>"\
#         "shaft_height<23.37>"\
#         "min_stack_thickness<3.96>"\
#         "max_stack_thickness<5.59>"\
#         "tcp_tip_dist<14.81>"\
#         "tcp_top_dist<4.45>"\
#     ">"\
#     "fastener<"\
#         "uid<permf_03>"\
#         "loc_uid<pf_st_03>"\
#         "fastener_state<1>"\
#         "diam<5.055>"\
#         "shaft_height<23.37>"\
#         "min_stack_thickness<3.96>"\
#         "max_stack_thickness<5.59>"\
#         "tcp_tip_dist<14.81>"\
#         "tcp_top_dist<4.45>"\
#     ">"\
#     "fastener<"\
#         "uid<permf_04>"\
#         "loc_uid<pf_st_04>"\
#         "fastener_state<1>"\
#         "diam<5.055>"\
#         "shaft_height<23.37>"\
#         "min_stack_thickness<3.96>"\
#         "max_stack_thickness<5.59>"\
#         "tcp_tip_dist<14.81>"\
#         "tcp_top_dist<4.45>"\
#     ">"\
#     "fastener<"\
#         "uid<permf_05>"\
#         "loc_uid<pf_st_05>"\
#         "fastener_state<1>"\
#         "diam<5.055>"\
#         "shaft_height<23.37>"\
#         "min_stack_thickness<3.96>"\
#         "max_stack_thickness<5.59>"\
#         "tcp_tip_dist<14.81>"\
#         "tcp_top_dist<4.45>"\
#     ">"\
#     "fastener<"\
#         "uid<permf_06>"\
#         "loc_uid<pf_st_06>"\
#         "fastener_state<1>"\
#         "diam<5.055>"\
#         "shaft_height<23.37>"\
#         "min_stack_thickness<3.96>"\
#         "max_stack_thickness<5.59>"\
#         "tcp_tip_dist<14.81>"\
#         "tcp_top_dist<4.45>"\
#     ">"\
#     "fastener<"\
#         "uid<permf_07>"\
#         "loc_uid<pf_st_07>"\
#         "fastener_state<1>"\
#         "diam<5.055>"\
#         "shaft_height<23.37>"\
#         "min_stack_thickness<3.96>"\
#         "max_stack_thickness<5.59>"\
#         "tcp_tip_dist<14.81>"\
#         "tcp_top_dist<4.45>"\
#     ">"\
#         "fastener<"\
#         "uid<permf_08>"\
#         "loc_uid<pf_st_08>"\
#         "fastener_state<1>"\
#         "diam<5.055>"\
#         "shaft_height<23.37>"\
#         "min_stack_thickness<3.96>"\
#         "max_stack_thickness<5.59>"\
#         "tcp_tip_dist<14.81>"\
#         "tcp_top_dist<4.45>"\
#     ">"\
#         "fastener<"\
#         "uid<permf_09>"\
#         "loc_uid<pf_st_09>"\
#         "fastener_state<1>"\
#         "diam<5.055>"\
#         "shaft_height<23.37>"\
#         "min_stack_thickness<3.96>"\
#         "max_stack_thickness<5.59>"\
#         "tcp_tip_dist<14.81>"\
#         "tcp_top_dist<4.45>"\
#     ">"\
#         "fastener<"\
#         "uid<permf_10>"\
#         "loc_uid<pf_st_10>"\
#         "fastener_state<1>"\
#         "diam<5.055>"\
#         "shaft_height<23.37>"\
#         "min_stack_thickness<3.96>"\
#         "max_stack_thickness<5.59>"\
#         "tcp_tip_dist<14.81>"\
#         "tcp_top_dist<4.45>"\
#     ">"\
#     "fastener<"\
#         "uid<permf_11>"\
#         "loc_uid<pf_st_11>"\
#         "fastener_state<1>"\
#         "diam<5.055>"\
#         "shaft_height<23.37>"\
#         "min_stack_thickness<3.96>"\
#         "max_stack_thickness<5.59>"\
#         "tcp_tip_dist<14.81>"\
#         "tcp_top_dist<4.45>"\
#     ">"\
#         "fastener<"\
#         "uid<permf_12>"\
#         "loc_uid<pf_st_12>"\
#         "fastener_state<1>"\
#         "diam<5.055>"\
#         "shaft_height<23.37>"\
#         "min_stack_thickness<3.96>"\
#         "max_stack_thickness<5.59>"\
#         "tcp_tip_dist<14.81>"\
#         "tcp_top_dist<4.45>"\
#     ">"\
#         "fastener<"\
#         "uid<permf_13>"\
#         "loc_uid<pf_st_13>"\
#         "fastener_state<1>"\
#         "diam<5.055>"\
#         "shaft_height<23.37>"\
#         "min_stack_thickness<3.96>"\
#         "max_stack_thickness<5.59>"\
#         "tcp_tip_dist<14.81>"\
#         "tcp_top_dist<4.45>"\
#     ">"\
#         "fastener<"\
#         "uid<permf_14>"\
#         "loc_uid<pf_st_14>"\
#         "fastener_state<1>"\
#         "diam<5.055>"\
#         "shaft_height<23.37>"\
#         "min_stack_thickness<3.96>"\
#         "max_stack_thickness<5.59>"\
#         "tcp_tip_dist<14.81>"\
#         "tcp_top_dist<4.45>"\
#     ">"\
# ">"\

# feedback = send_message(uid=pf_cobot_uid, message=msg, feedback=True)
# if feedback:
#     print(f"Feedback: {feedback}")

# # add 3 temporary fasteners in storage  (fastener state 1)
# # add 8 temporary fasteners in the product (fastener state 3)
msg = "populate_agent<"\
"tempfs<"\
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
        "fastener_state<3>"\
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
        "fastener_state<3>"\
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
        "fastener_state<3>"\
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
        "fastener_state<3>"\
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
        "fastener_state<3>"\
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
        "fastener_state<3>"\
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
        "fastener_state<3>"\
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
        "fastener_state<3>"\
        "diam<5.0>"\
        "shaft_height<60.0>"\
        "min_stack_thickness<3.0>"\
        "max_stack_thickness<17.0>"\
        "tcp_tip_dist<25.0>"\
        "tcp_top_dist<21.0>"\
    ">"\
">"\
">"

feedback = send_message(uid=tf_cobot_uid, message=msg, feedback=True)
if feedback:
    print(f"Feedback: {feedback}")


# msg = "populate_agent<"\
# "actions<"\
#     "action<"\
#         "uid<A01>"\
#         "action_type<install_permf>"\
#         "loc_uid<pf_pr_14>"\
#         "action_state<1>"\
#         "speed<100>"\
#     ">"\
#     "action<"\
#         "uid<A02>"\
#         "action_type<install_permf>"\
#         "loc_uid<pf_pr_13>"\
#         "action_state<1>"\
#         "speed<100>"\
#     ">"\
#     "action<"\
#         "uid<A03>"\
#         "action_type<install_permf>"\
#         "loc_uid<pf_pr_12>"\
#         "action_state<1>"\
#         "speed<100>"\
#     ">"\
#     "action<"\
#         "uid<A04>"\
#         "action_type<install_permf>"\
#         "loc_uid<pf_pr_11>"\
#         "action_state<1>"\
#         "speed<100>"\
#     ">"\
#     "action<"\
#         "uid<A05>"\
#         "action_type<install_permf>"\
#         "loc_uid<pf_pr_10>"\
#         "action_state<1>"\
#         "speed<100>"\
#     ">"\
#     "action<"\
#         "uid<A06>"\
#         "action_type<install_permf>"\
#         "loc_uid<pf_pr_09>"\
#         "action_state<1>"\
#         "speed<100>"\
#     ">"\
# ">"\

# feedback = send_message(uid=pf_cobot_uid, message=msg, feedback=True)
# if feedback:
#     print(f"Feedback: {feedback}")


# add ten actions....not yet execute them
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
">"\
">"

feedback = send_message(uid=tf_cobot_uid, message=msg, feedback=True)
if feedback:
    print(f"Feedback: {feedback}")



#######################################################################################################################

# # execute operation with uid
# feedback = send_message(uid=pf_cobot_uid, message="execute_single_operation<A01>", feedback=True)
# if feedback:
#     print(f"Feedback: {feedback}")

# # execute operation with uid
# feedback = send_message(uid=pf_cobot_uid, message="execute_single_operation<A02>", feedback=True)
# if feedback:
#     print(f"Feedback: {feedback}")

# # execute operation with uid
# feedback = send_message(uid=pf_cobot_uid, message="execute_single_operation<A03>", feedback=True)
# if feedback:
#     print(f"Feedback: {feedback}")

# # execute operation with uid
# feedback = send_message(uid=pf_cobot_uid, message="execute_single_operation<A04>", feedback=True)
# if feedback:
#     print(f"Feedback: {feedback}")

# # execute operation with uid
# feedback = send_message(uid=pf_cobot_uid, message="execute_single_operation<A05>", feedback=True)
# if feedback:
#     print(f"Feedback: {feedback}")

# # execute operation with uid
# feedback = send_message(uid=pf_cobot_uid, message="execute_single_operation<A03>", feedback=True)
# if feedback:
#     print(f"Feedback: {feedback}")

# execute operation with uid
feedback = send_message(uid=tf_cobot_uid, message="execute_single_operation<A01>", feedback=True)
if feedback:
    print(f"Feedback: {feedback}")

# execute operation with uid
feedback = send_message(uid=tf_cobot_uid, message="execute_single_operation<A02>", feedback=True)
if feedback:
    print(f"Feedback: {feedback}")

# execute operation with uid
feedback = send_message(uid=tf_cobot_uid, message="execute_single_operation<A03>", feedback=True)
if feedback:
    print(f"Feedback: {feedback}")

# execute operation with uid
feedback = send_message(uid=tf_cobot_uid, message="execute_single_operation<A04>", feedback=True)
if feedback:
    print(f"Feedback: {feedback}")

# execute operation with uid
feedback = send_message(uid=tf_cobot_uid, message="execute_single_operation<A05>", feedback=True)
if feedback:
    print(f"Feedback: {feedback}")

# execute operation with uid
feedback = send_message(uid=tf_cobot_uid, message="execute_single_operation<A06>", feedback=True)
if feedback:
    print(f"Feedback: {feedback}")

# execute operation with uid
feedback = send_message(uid=tf_cobot_uid, message="execute_single_operation<A07>", feedback=True)
if feedback:
    print(f"Feedback: {feedback}")

# execute operation with uid
feedback = send_message(uid=tf_cobot_uid, message="execute_single_operation<A08>", feedback=True)
if feedback:
    print(f"Feedback: {feedback}")

# execute operation with uid
feedback = send_message(uid=tf_cobot_uid, message="execute_single_operation<A09>", feedback=True)
if feedback:
    print(f"Feedback: {feedback}")

# execute operation with uid
feedback = send_message(uid=tf_cobot_uid, message="execute_single_operation<A10>", feedback=True)
if feedback:
    print(f"Feedback: {feedback}")

# go to home
feedback = send_message(uid=tf_cobot_uid, message="goto_home", feedback=True)
if feedback:
    print(f"Feedback: {feedback}")


