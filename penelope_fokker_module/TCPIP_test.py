from tcp_communication.tcp_client import run_tcp_client
from tcp_communication.communication_functions import send_message
import threading


# NOTICE: uid of product, waypoints and actions must have pf.... or tf.... 
#         to indicate for which cobot it is....

# send the message to the cobot
# catch messages that are too long (>1000)
def safe_send_message(cobot_uid, msg, parent_function):
    if (len(msg) > 1000):
        print(f"add_{parent_function} message to long. len = {len(msg)}")
        return

    feedback = send_message(uid=cobot_uid, message=msg, feedback=True)

    if feedback:
        print(f"Feedback: {feedback}")
    else:
        print(f"No feedback in {parent_function}")
        return

# go to home for cobot with uid_in
def cobot_goto_home(uid_in):
    safe_send_message(uid_in, "goto_home", "cobot_goto_home")

# add hole locations, stack thickness and diameter in the temp fastener storage list 
def add_tempf_storage_locations():

    # storage location 1-1 not used because it is broken and

    msg = "populate_agent<"\
        "tempf_storage_loc<"\
            "uid<tempf_storage>"\
            "locations<"\
                "hole_location<"\
                    "uid<tf_st_1_2>"\
                    "max_obstacle_height<40.0>"\
                    "diam<5.0>"\
                    "stack_thickness_tag<10.0>"\
                    "pose<"\
                        "pose_p_x<104.0>"\
                        "pose_p_y<491.5>"\
                        "pose_p_z<38.0>"\
                        "pose_o_x<71.0>"\
                        "pose_o_y<180.0>"\
                        "pose_o_z<0.0>"\
                    ">"\
                ">"\
                "hole_location<"\
                    "uid<tf_st_1_3>"\
                    "max_obstacle_height<40.0>"\
                    "diam<5.0>"\
                    "stack_thickness_tag<10.0>"\
                    "pose<"\
                        "pose_p_x<140.0>"\
                        "pose_p_y<492.0>"\
                        "pose_p_z<38.0>"\
                        "pose_o_x<71.0>"\
                        "pose_o_y<180.0>"\
                        "pose_o_z<0.0>"\
                    ">"\
                ">"\
                "hole_location<"\
                    "uid<tf_st_1_4>"\
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
                    "uid<tf_st_2_1>"\
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
            ">"\
        ">"\
    ">"

    safe_send_message(tf_cobot_uid, msg, "add_tempf_storage_locations")

    msg = "populate_agent<"\
        "tempf_storage_loc<"\
            "uid<tempf_storage>"\
            "locations<"\
                "hole_location<"\
                    "uid<tf_st_2_2>"\
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
                    "uid<tf_st_2_3>"\
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
                    "uid<tf_st_2_4>"\
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
                    "uid<tf_st_3_1>"\
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
            ">"\
        ">"\
    ">"

    safe_send_message(tf_cobot_uid, msg, "add_tempf_storage_locations")

    msg = "populate_agent<"\
        "tempf_storage_loc<"\
            "uid<tempf_storage>"\
            "locations<"\
                "hole_location<"\
                    "uid<tf_st_3_2>"\
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
                    "uid<tf_st_3_3>"\
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
                    "uid<tf_st_3_4>"\
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

    safe_send_message(tf_cobot_uid, msg, "add_tempf_storage_locations")

# add hole locations, stack thickness and diameter in the permanent fastener storage list
def add_permf_storage_locations():

    # storage location 1-1 not used because it is broken and contains a broken temp as well

    msg = "populate_agent<"\
        "permf_storage_loc<"\
            "uid<permf_storage>"\
            "locations<"\
                "hole_location<"\
                    "uid<pf_st_01>"\
                    "max_obstacle_height<40.0>"\
                    "diam<5.055>"\
                    "stack_thickness_tag<5.0>"\
                    "pose<"\
                        "pose_p_x<-91.82>"\
                        "pose_p_y<307.27>"\
                        "pose_p_z<35.46>"\
                        "pose_o_x<50.11>"\
                        "pose_o_y<178.79>"\
                        "pose_o_z<30.39>"\
                    ">"\
                ">"\
                "hole_location<"\
                    "uid<pf_st_02>"\
                    "max_obstacle_height<40.0>"\
                    "diam<5.055>"\
                    "stack_thickness_tag<5.0>"\
                    "pose<"\
                        "pose_p_x<-92.95>"\
                        "pose_p_y<330.78>"\
                        "pose_p_z<35.310>"\
                        "pose_o_x<100.1>"\
                        "pose_o_y<-179.1>"\
                        "pose_o_z<89.0>"\
                    ">"\
                ">"\
                "hole_location<"\
                    "uid<pf_st_03>"\
                    "max_obstacle_height<40.0>"\
                    "diam<5.055>"\
                    "stack_thickness_tag<5.0>"\
                    "pose<"\
                        "pose_p_x<-117.08>"\
                        "pose_p_y<306.12>"\
                        "pose_p_z<35.13>"\
                        "pose_o_x<153.13>"\
                        "pose_o_y<-179.72>"\
                        "pose_o_z<128.87>"\
                    ">"\
                ">"\
                "hole_location<"\
                    "uid<pf_st_04>"\
                    "max_obstacle_height<40.0>"\
                    "diam<5.055>"\
                    "stack_thickness_tag<5.0>"\
                    "pose<"\
                        "pose_p_x<-117.4>"\
                        "pose_p_y<331.62>"\
                        "pose_p_z<35.23>"\
                        "pose_o_x<44.76>"\
                        "pose_o_y<179.76>"\
                        "pose_o_z<23.75>"\
                    ">"\
                ">"\
                "hole_location<"\
                    "uid<pf_st_05>"\
                    "max_obstacle_height<40.0>"\
                    "diam<5.055>"\
                    "stack_thickness_tag<5.0>"\
                    "pose<"\
                        "pose_p_x<-142.3>"\
                        "pose_p_y<306.01>"\
                        "pose_p_z<35.14>"\
                        "pose_o_x<94.83>"\
                        "pose_o_y<179.42>"\
                        "pose_o_z<74.38>"\
                    ">"\
                ">"\
                "hole_location<"\
                    "uid<pf_st_06>"\
                    "max_obstacle_height<40.0>"\
                    "diam<5.055>"\
                    "stack_thickness_tag<5.0>"\
                    "pose<"\
                        "pose_p_x<-142.85>"\
                        "pose_p_y<330.23>"\
                        "pose_p_z<35.35>"\
                        "pose_o_x<76.47>"\
                        "pose_o_y<-179.05>"\
                        "pose_o_z<55.94>"\
                    ">"\
                ">"\
                "hole_location<"\
                    "uid<pf_st_07>"\
                    "max_obstacle_height<40.0>"\
                    "diam<5.055>"\
                    "stack_thickness_tag<5.0>"\
                    "pose<"\
                        "pose_p_x<-167.04>"\
                        "pose_p_y<306.16>"\
                        "pose_p_z<35.19>"\
                        "pose_o_x<36.58>"\
                        "pose_o_y<179.2>"\
                        "pose_o_z<3.74>"\
                    ">"\
                ">"\
                "hole_location<"\
                    "uid<pf_st_08>"\
                    "max_obstacle_height<40.0>"\
                    "diam<5.055>"\
                    "stack_thickness_tag<5.0>"\
                    "pose<"\
                        "pose_p_x<-167.67>"\
                        "pose_p_y<330.93>"\
                        "pose_p_z<35.31>"\
                        "pose_o_x<9.27>"\
                        "pose_o_y<179.52>"\
                        "pose_o_z<-16.26>"\
                    ">"\
                ">"\
                "hole_location<"\
                    "uid<pf_st_09>"\
                    "max_obstacle_height<40.0>"\
                    "diam<5.055>"\
                    "stack_thickness_tag<5.0>"\
                    "pose<"\
                        "pose_p_x<-192.09>"\
                        "pose_p_y<304.93>"\
                        "pose_p_z<35.37>"\
                        "pose_o_x<136.23>"\
                        "pose_o_y<-178.74>"\
                        "pose_o_z<106.02>"\
                    ">"\
                ">"\
                "hole_location<"\
                    "uid<pf_st_10>"\
                    "max_obstacle_height<40.0>"\
                    "diam<5.055>"\
                    "stack_thickness_tag<5.0>"\
                    "pose<"\
                        "pose_p_x<-192.36>"\
                        "pose_p_y<329.79>"\
                        "pose_p_z<35.48>"\
                        "pose_o_x<163.76>"\
                        "pose_o_y<-178.77>"\
                        "pose_o_z<136.94>"\
                    ">"\
                ">"\
                "hole_location<"\
                    "uid<pf_st_11>"\
                    "max_obstacle_height<40.0>"\
                    "diam<5.055>"\
                    "stack_thickness_tag<5.0>"\
                    "pose<"\
                        "pose_p_x<-216.47>"\
                        "pose_p_y<304.11>"\
                        "pose_p_z<35.9>"\
                        "pose_o_x<121.83>"\
                        "pose_o_y<-178.14>"\
                        "pose_o_z<101.79>"\
                    ">"\
                ">"\
                "hole_location<"\
                    "uid<pf_st_12>"\
                    "max_obstacle_height<40.0>"\
                    "diam<5.055>"\
                    "stack_thickness_tag<5.0>"\
                    "pose<"\
                        "pose_p_x<-217.87>"\
                        "pose_p_y<329.26>"\
                        "pose_p_z<39.53>"\
                        "pose_o_x<86.5>"\
                        "pose_o_y<-178.7>"\
                        "pose_o_z<61.99>"\
                    ">"\
                ">"\
                "hole_location<"\
                    "uid<pf_st_13>"\
                    "max_obstacle_height<40.0>"\
                    "diam<5.055>"\
                    "stack_thickness_tag<5.0>"\
                    "pose<"\
                        "pose_p_x<-241.51>"\
                        "pose_p_y<303.99>"\
                        "pose_p_z<35.51>"\
                        "pose_o_x<163.82>"\
                        "pose_o_y<-178.42>"\
                        "pose_o_z<135.21>"\
                    ">"\
                ">"\
                "hole_location<"\
                    "uid<pf_st_14>"\
                    "max_obstacle_height<40.0>"\
                    "diam<5.055>"\
                    "stack_thickness_tag<5.0>"\
                    "pose<"\
                        "pose_p_x<-242.91>"\
                        "pose_p_y<329.1>"\
                        "pose_p_z<35.48>"\
                        "pose_o_x<78.96>"\
                        "pose_o_y<-179.05>"\
                        "pose_o_z<57.88>"\
                    ">"\
                ">"\
            ">"\
        ">"\
    ">"

    safe_send_message(pf_cobot_uid, msg, "add_permf_storage_locations")

# add hole locations, stack thickness and diameter in the permf product list
def add_permf_product_locations():
    msg = "populate_agent<"\
        "product<"\
            "uid<product>"\
            "locations<"\
                "hole_location<"\
                    "uid<pf_pr_01>"\
                    "max_obstacle_height<40.0>"\
                    "diam<5.055>"\
                    "stack_thickness_tag<5.0>"\
                    "pose<"\
                        "pose_p_x<-329.83>"\
                        "pose_p_y<729.110>"\
                        "pose_p_z<813.0>"\
                        "pose_o_x<91.57>"\
                        "pose_o_y<64.97>"\
                        "pose_o_z<85.09>"\
                    ">"\
                ">"\
                    "hole_location<"\
                    "uid<pf_pr_02>"\
                    "max_obstacle_height<40.0>"\
                    "diam<5.055>"\
                    "stack_thickness_tag<5.0>"\
                    "pose<"\
                        "pose_p_x<-330.54>"\
                        "pose_p_y<655.720>"\
                        "pose_p_z<1017.77>"\
                        "pose_o_x<92.02>"\
                        "pose_o_y<72.47>"\
                        "pose_o_z<86.73>"\
                    ">"\
                ">"\
                "hole_location<"\
                    "uid<pf_pr_03>"\
                    "max_obstacle_height<40.0>"\
                    "diam<5.055>"\
                    "stack_thickness_tag<5.0>"\
                    "pose<"\
                        "pose_p_x<-499.6>"\
                        "pose_p_y<729.81>"\
                        "pose_p_z<810.5>"\
                        "pose_o_x<90.34>"\
                        "pose_o_y<66.72>"\
                        "pose_o_z<88.64>"\
                    ">"\
                ">"\
                "hole_location<"\
                    "uid<pf_pr_04>"\
                    "max_obstacle_height<40.0>"\
                    "diam<5.055>"\
                    "stack_thickness_tag<5.0>"\
                    "pose<"\
                        "pose_p_x<-500.57>"\
                        "pose_p_y<654.29>"\
                        "pose_p_z<1016.11>"\
                        "pose_o_x<92.08>"\
                        "pose_o_y<70.39>"\
                        "pose_o_z<89.6>"\
                    ">"\
                ">"\
                "hole_location<"\
                    "uid<pf_pr_05>"\
                    "max_obstacle_height<40.0>"\
                    "diam<5.055>"\
                    "stack_thickness_tag<5.0>"\
                    "pose<"\
                        "pose_p_x<-725.72>"\
                        "pose_p_y<727.750>"\
                        "pose_p_z<812.340>"\
                        "pose_o_x<88.94>"\
                        "pose_o_y<67.13>"\
                        "pose_o_z<93.49>"\
                    ">"\
                ">"\
                "hole_location<"\
                    "uid<pf_pr_06>"\
                    "max_obstacle_height<40.0>"\
                    "diam<5.055>"\
                    "stack_thickness_tag<5.0>"\
                    "pose<"\
                        "pose_p_x<-727.53>"\
                        "pose_p_y<652.19>"\
                        "pose_p_z<1018.0>"\
                        "pose_o_x<91.6>"\
                        "pose_o_y<72.39>"\
                        "pose_o_z<87.84>"\
                    ">"\
                ">"\
                "hole_location<"\
                    "uid<pf_pr_11>"\
                    "max_obstacle_height<40.0>"\
                    "diam<5.055>"\
                    "stack_thickness_tag<5.0>"\
                    "pose<"\
                        "pose_p_x<-329.47>"\
                        "pose_p_y<717.91>"\
                        "pose_p_z<841.81>"\
                        "pose_o_x<89.64>"\
                        "pose_o_y<65.69>"\
                        "pose_o_z<89.42>"\
                    ">"\
                ">"\
                "hole_location<"\
                    "uid<pf_pr_12>"\
                    "max_obstacle_height<40.0>"\
                    "diam<5.055>"\
                    "stack_thickness_tag<5.0>"\
                    "pose<"\
                        "pose_p_x<-329.71>"\
                        "pose_p_y<706.63>"\
                        "pose_p_z<869.79>"\
                        "pose_o_x<91.56>"\
                        "pose_o_y<67.41>"\
                        "pose_o_z<90.22>"\
                    ">"\
                ">"\
                "hole_location<"\
                    "uid<pf_pr_13>"\
                    "max_obstacle_height<40.0>"\
                    "diam<5.055>"\
                    "stack_thickness_tag<5.0>"\
                    "pose<"\
                        "pose_p_x<-330.01>"\
                        "pose_p_y<695.28>"\
                        "pose_p_z<900.14>"\
                        "pose_o_x<92.7>"\
                        "pose_o_y<65.84>"\
                        "pose_o_z<87.58>"\
                    ">"\
                ">"\
                "hole_location<"\
                    "uid<pf_pr_14>"\
                    "max_obstacle_height<40.0>"\
                    "diam<5.055>"\
                    "stack_thickness_tag<5.0>"\
                    "pose<"\
                        "pose_p_x<-329.56>"\
                        "pose_p_y<684.27>"\
                        "pose_p_z<929.38>"\
                        "pose_o_x<91.51>"\
                        "pose_o_y<68.44>"\
                        "pose_o_z<88.93>"\
                    ">"\
                ">"\
                "hole_location<"\
                    "uid<pf_pr_15>"\
                    "max_obstacle_height<40.0>"\
                    "diam<5.055>"\
                    "stack_thickness_tag<5.0>"\
                    "pose<"\
                        "pose_p_x<-330.18>"\
                        "pose_p_y<673.5>"\
                        "pose_p_z<958.83>"\
                        "pose_o_x<91.71>"\
                        "pose_o_y<70.89>"\
                        "pose_o_z<90.12>"\
                    ">"\
                ">"\
                "hole_location<"\
                    "uid<pf_pr_16>"\
                    "max_obstacle_height<40.0>"\
                    "diam<5.055>"\
                    "stack_thickness_tag<5.0>"\
                    "pose<"\
                        "pose_p_x<-329.3>"\
                        "pose_p_y<663.78>"\
                        "pose_p_z<988.91>"\
                        "pose_o_x<91.67>"\
                        "pose_o_y<69.43>"\
                        "pose_o_z<89.35>"\
                    ">"\
                ">"\
                "hole_location<"\
                    "uid<pf_pr_17>"\
                    "max_obstacle_height<40.0>"\
                    "diam<5.055>"\
                    "stack_thickness_tag<5.0>"\
                    "pose<"\
                        "pose_p_x<-499.9>"\
                        "pose_p_y<717.33>"\
                        "pose_p_z<840.44>"\
                        "pose_o_x<90.91>"\
                        "pose_o_y<66.33>"\
                        "pose_o_z<87.68>"\
                    ">"\
                ">"\
                "hole_location<"\
                    "uid<pf_pr_18>"\
                    "max_obstacle_height<40.0>"\
                    "diam<5.055>"\
                    "stack_thickness_tag<5.0>"\
                    "pose<"\
                        "pose_p_x<-499.9>"\
                        "pose_p_y<705.34>"\
                        "pose_p_z<869.08>"\
                        "pose_o_x<90.37>"\
                        "pose_o_y<67.4>"\
                        "pose_o_z<89.8>"\
                    ">"\
                ">"\
                "hole_location<"\
                    "uid<pf_pr_19>"\
                    "max_obstacle_height<40.0>"\
                    "diam<5.055>"\
                    "stack_thickness_tag<5.0>"\
                    "pose<"\
                        "pose_p_x<-499.34>"\
                        "pose_p_y<694.19>"\
                        "pose_p_z<897.67>"\
                        "pose_o_x<89.7>"\
                        "pose_o_y<69.98>"\
                        "pose_o_z<88.57>"\
                    ">"\
                ">"\
                "hole_location<"\
                    "uid<pf_pr_20>"\
                    "max_obstacle_height<40.0>"\
                    "diam<5.055>"\
                    "stack_thickness_tag<5.0>"\
                    "pose<"\
                        "pose_p_x<-498.99>"\
                        "pose_p_y<682.8>"\
                        "pose_p_z<927.57>"\
                        "pose_o_x<89.89>"\
                        "pose_o_y<68.2>"\
                        "pose_o_z<89.85>"\
                    ">"\
                ">"\
                "hole_location<"\
                    "uid<pf_pr_21>"\
                    "max_obstacle_height<40.0>"\
                    "diam<5.055>"\
                    "stack_thickness_tag<5.0>"\
                    "pose<"\
                        "pose_p_x<-500.06>"\
                        "pose_p_y<673.07>"\
                        "pose_p_z<957.22>"\
                        "pose_o_x<92.09>"\
                        "pose_o_y<69.97>"\
                        "pose_o_z<89.56>"\
                    ">"\
                ">"\
                "hole_location<"\
                    "uid<pf_pr_22>"\
                    "max_obstacle_height<40.0>"\
                    "diam<5.055>"\
                    "stack_thickness_tag<5.0>"\
                    "pose<"\
                        "pose_p_x<-499.8>"\
                        "pose_p_y<664.19>"\
                        "pose_p_z<986.93>"\
                        "pose_o_x<93.46>"\
                        "pose_o_y<71.1>"\
                        "pose_o_z<86.57>"\
                    ">"\
                ">"\
            ">"\
        ">"\
    ">"

    safe_send_message(pf_cobot_uid, msg, "add_permf_product_locations")

# add hole locations, stack thickness and diameter in the tempf product list
def add_tempf_product_locations():
    msg = "populate_agent<"\
        "product<"\
            "uid<product>"\
            "locations<"\
                "hole_location<"\
                    "uid<tf_left_drill_jig_01>"\
                    "max_obstacle_height<40.0>"\
                    "diam<5.0>"\
                    "stack_thickness_tag<9.0>"\
                    "pose<"\
                        "pose_p_x<11.0>"\
                        "pose_p_y<838.0>"\
                        "pose_p_z<1114.5>"\
                        "pose_o_x<90.0>"\
                        "pose_o_y<75.0>"\
                        "pose_o_z<0.0>"\
                    ">"\
                ">"\
                "hole_location<"\
                    "uid<tf_left_drill_jig_08>"\
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
                    "uid<tf_left_drill_jig_15>"\
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
            ">"\
        ">"\
    ">"
    
    safe_send_message(tf_cobot_uid, msg, "add_tempf_product_locations")

    msg = "populate_agent<"\
        "product<"\
            "uid<product>"\
            "locations<"\
                "hole_location<"\
                    "uid<tf_inner_vert_jig_01_01>"\
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
                    "uid<tf_inner_vert_jig_01_08>"\
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
                    "uid<tf_inner_vert_jig_02_01>"\
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
            ">"\
        ">"\
    ">"
    
    safe_send_message(tf_cobot_uid, msg, "add_tempf_product_locations")

    msg = "populate_agent<"\
        "product<"\
            "uid<product>"\
            "locations<"\
                "hole_location<"\
                    "uid<tf_inner_vert_jig_02_08>"\
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
                    "uid<tf_inner_vert_jig_03_01>"\
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
                    "uid<tf_inner_vert_jig_03_08>"\
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
        ">"\
    ">"
    
    safe_send_message(tf_cobot_uid, msg, "add_tempf_product_locations")

# add permanent fasteners in storage
def add_permf_in_storage():
    msg = "populate_agent<"\
        "fasteners<"\
            "fastener<"\
                "uid<permf_01>"\
                "loc_uid<pf_st_01>"\
                "fastener_state<1>"\
                "diam<5.055>"\
                "shaft_height<23.37>"\
                "min_stack_thickness<3.96>"\
                "max_stack_thickness<5.59>"\
                "tcp_tip_dist<14.81>"\
                "tcp_top_dist<4.45>"\
            ">"\
            "fastener<"\
                "uid<permf_02>"\
                "loc_uid<pf_st_02>"\
                "fastener_state<1>"\
                "diam<5.055>"\
                "shaft_height<23.37>"\
                "min_stack_thickness<3.96>"\
                "max_stack_thickness<5.59>"\
                "tcp_tip_dist<14.81>"\
                "tcp_top_dist<4.45>"\
            ">"\
            "fastener<"\
                "uid<permf_03>"\
                "loc_uid<pf_st_03>"\
                "fastener_state<1>"\
                "diam<5.055>"\
                "shaft_height<23.37>"\
                "min_stack_thickness<3.96>"\
                "max_stack_thickness<5.59>"\
                "tcp_tip_dist<14.81>"\
                "tcp_top_dist<4.45>"\
            ">"\
            "fastener<"\
                "uid<permf_04>"\
                "loc_uid<pf_st_04>"\
                "fastener_state<1>"\
                "diam<5.055>"\
                "shaft_height<23.37>"\
                "min_stack_thickness<3.96>"\
                "max_stack_thickness<5.59>"\
                "tcp_tip_dist<14.81>"\
                "tcp_top_dist<4.45>"\
            ">"\
            "fastener<"\
                "uid<permf_05>"\
                "loc_uid<pf_st_05>"\
                "fastener_state<1>"\
                "diam<5.055>"\
                "shaft_height<23.37>"\
                "min_stack_thickness<3.96>"\
                "max_stack_thickness<5.59>"\
                "tcp_tip_dist<14.81>"\
                "tcp_top_dist<4.45>"\
            ">"\
            "fastener<"\
                "uid<permf_06>"\
                "loc_uid<pf_st_06>"\
                "fastener_state<1>"\
                "diam<5.055>"\
                "shaft_height<23.37>"\
                "min_stack_thickness<3.96>"\
                "max_stack_thickness<5.59>"\
                "tcp_tip_dist<14.81>"\
                "tcp_top_dist<4.45>"\
            ">"\
            "fastener<"\
                "uid<permf_07>"\
                "loc_uid<pf_st_07>"\
                "fastener_state<1>"\
                "diam<5.055>"\
                "shaft_height<23.37>"\
                "min_stack_thickness<3.96>"\
                "max_stack_thickness<5.59>"\
                "tcp_tip_dist<14.81>"\
                "tcp_top_dist<4.45>"\
            ">"\
                "fastener<"\
                "uid<permf_08>"\
                "loc_uid<pf_st_08>"\
                "fastener_state<1>"\
                "diam<5.055>"\
                "shaft_height<23.37>"\
                "min_stack_thickness<3.96>"\
                "max_stack_thickness<5.59>"\
                "tcp_tip_dist<14.81>"\
                "tcp_top_dist<4.45>"\
            ">"\
                "fastener<"\
                "uid<permf_09>"\
                "loc_uid<pf_st_09>"\
                "fastener_state<1>"\
                "diam<5.055>"\
                "shaft_height<23.37>"\
                "min_stack_thickness<3.96>"\
                "max_stack_thickness<5.59>"\
                "tcp_tip_dist<14.81>"\
                "tcp_top_dist<4.45>"\
            ">"\
                "fastener<"\
                "uid<permf_10>"\
                "loc_uid<pf_st_10>"\
                "fastener_state<1>"\
                "diam<5.055>"\
                "shaft_height<23.37>"\
                "min_stack_thickness<3.96>"\
                "max_stack_thickness<5.59>"\
                "tcp_tip_dist<14.81>"\
                "tcp_top_dist<4.45>"\
            ">"\
            "fastener<"\
                "uid<permf_11>"\
                "loc_uid<pf_st_11>"\
                "fastener_state<1>"\
                "diam<5.055>"\
                "shaft_height<23.37>"\
                "min_stack_thickness<3.96>"\
                "max_stack_thickness<5.59>"\
                "tcp_tip_dist<14.81>"\
                "tcp_top_dist<4.45>"\
            ">"\
                "fastener<"\
                "uid<permf_12>"\
                "loc_uid<pf_st_12>"\
                "fastener_state<1>"\
                "diam<5.055>"\
                "shaft_height<23.37>"\
                "min_stack_thickness<3.96>"\
                "max_stack_thickness<5.59>"\
                "tcp_tip_dist<14.81>"\
                "tcp_top_dist<4.45>"\
            ">"\
                "fastener<"\
                "uid<permf_13>"\
                "loc_uid<pf_st_13>"\
                "fastener_state<1>"\
                "diam<5.055>"\
                "shaft_height<23.37>"\
                "min_stack_thickness<3.96>"\
                "max_stack_thickness<5.59>"\
                "tcp_tip_dist<14.81>"\
                "tcp_top_dist<4.45>"\
            ">"\
                "fastener<"\
                "uid<permf_14>"\
                "loc_uid<pf_st_14>"\
                "fastener_state<1>"\
                "diam<5.055>"\
                "shaft_height<23.37>"\
                "min_stack_thickness<3.96>"\
                "max_stack_thickness<5.59>"\
                "tcp_tip_dist<14.81>"\
                "tcp_top_dist<4.45>"\
            ">"\
        ">"\
    ">"

    safe_send_message(pf_cobot_uid, msg, "add_permf_in_storage")

# add 9 temporary fasteners in storage  
# fastener in stroage: state 1
# fastener in product: state 3
def add_tempf_in_storage():
    msg = "populate_agent<"\
        "tempfs<"\
            "tempf<"\
                "uid<tempf_02>"\
                "loc_uid<tf_st_1_2>"\
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
                "loc_uid<tf_st_1_3>"\
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
                "loc_uid<tf_st_1_4>"\
                "fastener_state<1>"\
                "diam<5.0>"\
                "shaft_height<60.0>"\
                "min_stack_thickness<3.0>"\
                "max_stack_thickness<17.0>"\
                "tcp_tip_dist<25.0>"\
                "tcp_top_dist<21.0>"\
            ">"\
        ">"\
    ">"

    safe_send_message(tf_cobot_uid, msg, "add_tempf_in_storage")

    msg = "populate_agent<"\
        "tempfs<"\
            "tempf<"\
                "uid<tempf_05>"\
                "loc_uid<tf_st_2_1>"\
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
                "loc_uid<tf_st_2_2>"\
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
                "loc_uid<tf_st_2_3>"\
                "fastener_state<1>"\
                "diam<5.0>"\
                "shaft_height<60.0>"\
                "min_stack_thickness<3.0>"\
                "max_stack_thickness<17.0>"\
                "tcp_tip_dist<25.0>"\
                "tcp_top_dist<21.0>"\
            ">"\
        ">"\
    ">"

    safe_send_message(tf_cobot_uid, msg, "add_tempf_in_storage")

    msg = "populate_agent<"\
        "tempfs<"\
            "tempf<"\
                "uid<tempf_08>"\
                "loc_uid<tf_st_2_4>"\
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
                "loc_uid<tf_st_3_1>"\
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
                "loc_uid<tf_st_3_2>"\
                "fastener_state<1>"\
                "diam<5.0>"\
                "shaft_height<60.0>"\
                "min_stack_thickness<3.0>"\
                "max_stack_thickness<17.0>"\
                "tcp_tip_dist<25.0>"\
                "tcp_top_dist<21.0>"\
            ">"\
        ">"\
    ">"

    safe_send_message(tf_cobot_uid, msg, "add_tempf_in_storage")

# Add the permanent fastener actions to the agent
# Defined actions will be executed later
def add_permf_actions():
    msg = "populate_agent<"\
        "actions<"\
            "action<"\
                "uid<pf_A01>"\
                "action_type<install_permf>"\
                "loc_uid<pf_pr_14>"\
                "action_state<1>"\
                "speed<100>"\
            ">"\
            "action<"\
                "uid<pf_A01>"\
                "action_type<install_permf>"\
                "loc_uid<pf_pr_13>"\
                "action_state<1>"\
                "speed<100>"\
            ">"\
            "action<"\
                "uid<pf_A03>"\
                "action_type<install_permf>"\
                "loc_uid<pf_pr_12>"\
                "action_state<1>"\
                "speed<100>"\
            ">"\
            "action<"\
                "uid<pf_A04>"\
                "action_type<install_permf>"\
                "loc_uid<pf_pr_11>"\
                "action_state<1>"\
                "speed<100>"\
            ">"\
            "action<"\
                "uid<pf_A05>"\
                "action_type<install_permf>"\
                "loc_uid<pf_pr_10>"\
                "action_state<1>"\
                "speed<100>"\
            ">"\
            "action<"\
                "uid<pf_A06>"\
                "action_type<install_permf>"\
                "loc_uid<pf_pr_09>"\
                "action_state<1>"\
                "speed<100>"\
            ">"\
        ">"\
    ">"

    safe_send_message(pf_cobot_uid, msg, "add_permf_actions")

# add nine actions....not yet execute them
# tf_i_A01: install tempf from tf_left_drill_jig_01
# tf_i_A02: install tempf from tf_left_drill_jig_08
# tf_i_A03: install tempf from tf_left_drill_jig_15
# tf_i_A04: install tempf from tf_inner_vert_jig_01_01
# tf_i_A05: install tempf from tf_inner_vert_jig_01_08
# tf_i_A06: install tempf from tf_inner_vert_jig_02_01
# tf_i_A07: install tempf from tf_inner_vert_jig_02_08
# tf_i_A08: install tempf from tf_inner_vert_jig_03_01
# tf_i_A09: install tempf from tf_inner_vert_jig_03_08
def add_tempf_install_actions():

    # "action_type<remove_fastener>" is for remove
    # "action_type<install_tempf>" is for install

    msg = "populate_agent<"\
        "actions<"\
            "action<"\
                "uid<tf_i_A01>"\
                "action_type<install_tempf>"\
                "loc_uid<tf_left_drill_jig_01>"\
                "action_state<1>"\
                "speed<100>"\
            ">"\
            "action<"\
                "uid<tf_i_A02>"\
                "action_type<install_tempf>"\
                "loc_uid<tf_left_drill_jig_08>"\
                "action_state<1>"\
                "speed<100>"\
            ">"\
            "action<"\
                "uid<tf_i_A03>"\
                "action_type<install_tempf>"\
                "loc_uid<tf_left_drill_jig_15>"\
                "action_state<1>"\
                "speed<100>"\
            ">"\
            "action<"\
                "uid<tf_i_A04>"\
                "action_type<install_tempf>"\
                "loc_uid<tf_inner_vert_jig_01_01>"\
                "action_state<1>"\
                "speed<100>"\
            ">"\
            "action<"\
                "uid<tf_i_A05>"\
                "action_type<install_tempf>"\
                "loc_uid<tf_inner_vert_jig_01_08>"\
                "action_state<1>"\
                "speed<100>"\
            ">"\
        ">"\
    ">"

    safe_send_message(tf_cobot_uid, msg, "add_tempf_install_actions")

    
    msg = "populate_agent<"\
        "actions<"\
            "action<"\
                "uid<tf_i_A06>"\
                "action_type<install_tempf>"\
                "loc_uid<tf_inner_vert_jig_02_01>"\
                "action_state<1>"\
                "speed<100>"\
            ">"\
            "action<"\
                "uid<tf_i_A07>"\
                "action_type<install_tempf>"\
                "loc_uid<tf_inner_vert_jig_02_08>"\
                "action_state<1>"\
                "speed<100>"\
            ">"\
            "action<"\
                "uid<tf_i_A08>"\
                "action_type<install_tempf>"\
                "loc_uid<tf_inner_vert_jig_03_01>"\
                "action_state<1>"\
                "speed<100>"\
            ">"\
            "action<"\
                "uid<tf_i_A09>"\
                "action_type<install_tempf>"\
                "loc_uid<tf_inner_vert_jig_03_08>"\
                "action_state<1>"\
                "speed<100>"\
            ">"\
        ">"\
    ">"

    safe_send_message(tf_cobot_uid, msg, "add_tempf_install_actions")

# add nine actions....not yet execute them
# tf_u_A01: uninstall tempf from tf_left_drill_jig_01
# tf_u_A02: uninstall tempf from tf_left_drill_jig_08
# tf_u_A03: uninstall tempf from tf_left_drill_jig_15
# tf_u_A04: uninstall tempf from tf_inner_vert_jig_01_01
# tf_u_A05: uninstall tempf from tf_inner_vert_jig_01_08
# tf_u_A06: uninstall tempf from tf_inner_vert_jig_02_01
# tf_u_A07: uninstall tempf from tf_inner_vert_jig_02_08
# tf_u_A08: uninstall tempf from tf_inner_vert_jig_03_01
# tf_u_A09: uninstall tempf from tf_inner_vert_jig_03_08
def add_tempf_uninstall_actions():

    # "action_type<remove_fastener>" is for remove
    # "action_type<install_tempf>" is for install

    msg = "populate_agent<"\
        "actions<"\
            "action<"\
                "uid<tf_u_A01>"\
                "action_type<remove_fastener>"\
                "loc_uid<tf_left_drill_jig_01>"\
                "action_state<1>"\
                "speed<100>"\
            ">"\
            "action<"\
                "uid<tf_u_A02>"\
                "action_type<remove_fastener>"\
                "loc_uid<tf_left_drill_jig_08>"\
                "action_state<1>"\
                "speed<100>"\
            ">"\
            "action<"\
                "uid<tf_u_A03>"\
                "action_type<remove_fastener>"\
                "loc_uid<tf_left_drill_jig_15>"\
                "action_state<1>"\
                "speed<100>"\
            ">"\
            "action<"\
                "uid<tf_u_A04>"\
                "action_type<remove_fastener>"\
                "loc_uid<tf_inner_vert_jig_01_01>"\
                "action_state<1>"\
                "speed<100>"\
            ">"\
            "action<"\
                "uid<tf_u_A05>"\
                "action_type<remove_fastener>"\
                "loc_uid<tf_inner_vert_jig_01_08>"\
                "action_state<1>"\
                "speed<100>"\
            ">"\
        ">"\
    ">"

    safe_send_message(tf_cobot_uid, msg, "add_tempf_install_actions")

    msg = "populate_agent<"\
        "actions<"\
            "action<"\
                "uid<tf_u_A06>"\
                "action_type<remove_fastener>"\
                "loc_uid<tf_inner_vert_jig_02_01>"\
                "action_state<1>"\
                "speed<100>"\
            ">"\
            "action<"\
                "uid<tf_u_A07>"\
                "action_type<remove_fastener>"\
                "loc_uid<tf_inner_vert_jig_02_08>"\
                "action_state<1>"\
                "speed<100>"\
            ">"\
            "action<"\
                "uid<tf_u_A08>"\
                "action_type<remove_fastener>"\
                "loc_uid<tf_inner_vert_jig_03_01>"\
                "action_state<1>"\
                "speed<100>"\
            ">"\
            "action<"\
                "uid<tf_u_A09>"\
                "action_type<remove_fastener>"\
                "loc_uid<tf_inner_vert_jig_03_08>"\
                "action_state<1>"\
                "speed<100>"\
            ">"\
        ">"\
    ">"

    safe_send_message(tf_cobot_uid, msg, "add_tempf_install_actions")

# execute action with uid on cobot with uid
def execute_action(cobot_uid_in, action_uid_in):
    msg = "execute_single_operation<" + action_uid_in + ">"

    safe_send_message(cobot_uid_in, msg, "execute_action")


##################################################################################################
##################################################################################################
##################################################################################################

# Set up a TCPIP client of each cobot
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

cobot_goto_home(tf_cobot_uid)
# cobot_goto_home(pf_cobot_uid)

add_tempf_storage_locations()
add_tempf_product_locations()
add_tempf_in_storage()
add_tempf_install_actions()
add_tempf_uninstall_actions()

# add_permf_storage_locations()
# add_permf_product_locations()
# add_permf_in_storage()
# add_permf_actions()

# install the temporary fasteners
execute_action(tf_cobot_uid, "tf_i_A01")
execute_action(tf_cobot_uid, "tf_i_A02")
execute_action(tf_cobot_uid, "tf_i_A03")
execute_action(tf_cobot_uid, "tf_i_A04")
execute_action(tf_cobot_uid, "tf_i_A05")
execute_action(tf_cobot_uid, "tf_i_A06")
execute_action(tf_cobot_uid, "tf_i_A07")
execute_action(tf_cobot_uid, "tf_i_A08")
execute_action(tf_cobot_uid, "tf_i_A09")
cobot_goto_home(tf_cobot_uid)

# install the permanent fasteners
# execute_action(pf_cobot_uid, "pf_A01")
# etcetera
# etcetera
# cobot_goto_home(pf_cobot_uid)

# uninstall the temporary fasteners
execute_action(tf_cobot_uid, "tf_u_A01")
execute_action(tf_cobot_uid, "tf_u_A02")
execute_action(tf_cobot_uid, "tf_u_A03")
execute_action(tf_cobot_uid, "tf_u_A04")
execute_action(tf_cobot_uid, "tf_u_A05")
execute_action(tf_cobot_uid, "tf_u_A06")
execute_action(tf_cobot_uid, "tf_u_A07")
execute_action(tf_cobot_uid, "tf_u_A08")
execute_action(tf_cobot_uid, "tf_u_A09")
cobot_goto_home(tf_cobot_uid)

##################################################################################################
##################################################################################################
##################################################################################################

