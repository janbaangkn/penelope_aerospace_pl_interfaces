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
    # 1-4 oude storage
    msg = "populate_agent<"\
        "permf_storage_loc<"\
            "uid<permf_storage>"\
            "locations<"\
                "hole_location<"\
                    "uid<pf_st_01_01>"\
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
                    "uid<pf_st_01_02>"\
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
                    "uid<pf_st_01_03>"\
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
                    "uid<pf_st_01_04>"\
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
            ">"\
        ">"\
    ">"    
    
    safe_send_message(pf_cobot_uid, msg, "add_permf_storage_locations")
    #5-8 oude storage            
    msg = "populate_agent<"\
        "permf_storage_loc<"\
            "uid<permf_storage>"\
            "locations<"\
                "hole_location<"\
                    "uid<pf_st_01_05>"\
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
                    "uid<pf_st_01_06>"\
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
                    "uid<pf_st_01_07>"\
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
                    "uid<pf_st_01_08>"\
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
            ">"\
        ">"\
    ">"

    safe_send_message(pf_cobot_uid, msg, "add_permf_storage_locations")
    #9-12 oude storage
    msg = "populate_agent<"\
        "permf_storage_loc<"\
            "uid<permf_storage>"\
            "locations<"\
                "hole_location<"\
                    "uid<pf_st_01_09>"\
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
                    "uid<pf_st_01_10>"\
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
                    "uid<pf_st_01_11>"\
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
                    "uid<pf_st_01_12>"\
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
            ">"\
        ">"\
    ">"
    
    safe_send_message(pf_cobot_uid, msg, "add_permf_storage_locations")
    #13-14 oude storage
    msg = "populate_agent<"\
        "permf_storage_loc<"\
            "uid<permf_storage>"\
            "locations<"\
                "hole_location<"\
                    "uid<pf_st_01_13>"\
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
                    "uid<pf_st_01_14>"\
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
    #1-4 nieuwe storage
    msg = "populate_agent<"\
        "permf_storage_loc<"\
            "uid<permf_storage>"\
            "locations<"\
                "hole_location<"\
                    "uid<pf_st_02_01>"\
                    "max_obstacle_height<40.0>"\
                    "diam<5.055>"\
                    "stack_thickness_tag<5.0>"\
                    "pose<"\
                        "pose_p_x<-284.04>"\
                        "pose_p_y<250.81>"\
                        "pose_p_z<41.050>"\
                        "pose_o_x<28.12>"\
                        "pose_o_y<179.09>"\
                        "pose_o_z<-19.82>"\
                    ">"\
                ">"\
                "hole_location<"\
                    "uid<pf_st_02_02>"\
                    "max_obstacle_height<40.0>"\
                    "diam<5.055>"\
                    "stack_thickness_tag<5.0>"\
                    "pose<"\
                        "pose_p_x<-308.41>"\
                        "pose_p_y<248.96>"\
                        "pose_p_z<40.740>"\
                        "pose_o_x<179.71>"\
                        "pose_o_y<-178.71>"\
                        "pose_o_z<140.43>"\
                    ">"\
                ">"\
                "hole_location<"\
                    "uid<pf_st_02_03>"\
                    "max_obstacle_height<40.0>"\
                    "diam<5.055>"\
                    "stack_thickness_tag<5.0>"\
                    "pose<"\
                        "pose_p_x<-333.45>"\
                        "pose_p_y<246.81>"\
                        "pose_p_z<40.850>"\
                        "pose_o_x<133.42>"\
                        "pose_o_y<-179.08>"\
                        "pose_o_z<105.48>"\
                    ">"\
                ">"\
                "hole_location<"\
                    "uid<pf_st_02_04>"\
                    "max_obstacle_height<40.0>"\
                    "diam<5.055>"\
                    "stack_thickness_tag<5.0>"\
                    "pose<"\
                        "pose_p_x<-383.25>"\
                        "pose_p_y<244.10>"\
                        "pose_p_z<41.510>"\
                        "pose_o_x<12.36>"\
                        "pose_o_y<179.27>"\
                        "pose_o_z<-28.54>"\
                    ">"\
                ">"\
            ">"\
        ">"\
    ">"
    
    safe_send_message(pf_cobot_uid, msg, "add_permf_storage_locations")

# add hole locations, stack thickness and diameter in the permf product list
def add_permf_product_locations():
    #L-profiel R3 1-4
    msg = "populate_agent<"\
        "product<"\
            "uid<product>"\
            "locations<"\
                "hole_location<"\
                    "uid<pf_pr_r3_01>"\
                    "max_obstacle_height<40.0>"\
                    "diam<5.055>"\
                    "stack_thickness_tag<5.0>"\
                    "pose<"\
                        "pose_p_x<-144.21>"\
                        "pose_p_y<633.460>"\
                        "pose_p_z<1101.92>"\
                        "pose_o_x<92.33>"\
                        "pose_o_y<74.92>"\
                        "pose_o_z<94.72>"\
                    ">"\
                ">"\
                    "hole_location<"\
                    "uid<pf_pr_r3_02>"\
                    "max_obstacle_height<40.0>"\
                    "diam<5.055>"\
                    "stack_thickness_tag<5.0>"\
                    "pose<"\
                        "pose_p_x<-111.51>"\
                        "pose_p_y<632.79>"\
                        "pose_p_z<1102.18>"\
                        "pose_o_x<90.57>"\
                        "pose_o_y<75.3>"\
                        "pose_o_z<89.2>"\
                    ">"\
                ">"\
                "hole_location<"\
                    "uid<pf_pr_r3_03>"\
                    "max_obstacle_height<40.0>"\
                    "diam<5.055>"\
                    "stack_thickness_tag<5.0>"\
                    "pose<"\
                        "pose_p_x<-81.15>"\
                        "pose_p_y<633.44>"\
                        "pose_p_z<1101.91>"\
                        "pose_o_x<92.29>"\
                        "pose_o_y<74.55>"\
                        "pose_o_z<92.8>"\
                    ">"\
                ">"\
                "hole_location<"\
                    "uid<pf_pr_r3_04>"\
                    "max_obstacle_height<40.0>"\
                    "diam<5.055>"\
                    "stack_thickness_tag<5.0>"\
                    "pose<"\
                        "pose_p_x<-49.76>"\
                        "pose_p_y<634.36>"\
                        "pose_p_z<1102.71>"\
                        "pose_o_x<91.51>"\
                        "pose_o_y<74.17>"\
                        "pose_o_z<93.91>"\
                    ">"\
                ">"\
            ">"\
        ">"\
    ">"

    safe_send_message(pf_cobot_uid, msg, "add_permf_product_locations")
    
    #L-profiel R3 5-8
    msg = "populate_agent<"\
        "product<"\
            "uid<product>"\
            "locations<"\
                "hole_location<"\
                    "uid<pf_pr_r3_05>"\
                    "max_obstacle_height<40.0>"\
                    "diam<5.055>"\
                    "stack_thickness_tag<5.0>"\
                    "pose<"\
                        "pose_p_x<-16.62>"\
                        "pose_p_y<629.93>"\
                        "pose_p_z<1102.57>"\
                        "pose_o_x<90.26>"\
                        "pose_o_y<71.49>"\
                        "pose_o_z<90.54>"\
                    ">"\
                ">"\
                "hole_location<"\
                    "uid<pf_pr_r3_06>"\
                    "max_obstacle_height<40.0>"\
                    "diam<5.055>"\
                    "stack_thickness_tag<5.0>"\
                    "pose<"\
                        "pose_p_x<14.57>"\
                        "pose_p_y<632.59>"\
                        "pose_p_z<1103.37>"\
                        "pose_o_x<90.26>"\
                        "pose_o_y<71.49>"\
                        "pose_o_z<90.54>"\
                    ">"\
                ">"\
                "hole_location<"\
                    "uid<pf_pr_r3_07>"\
                    "max_obstacle_height<40.0>"\
                    "diam<5.055>"\
                    "stack_thickness_tag<5.0>"\
                    "pose<"\
                        "pose_p_x<46.24>"\
                        "pose_p_y<632.17>"\
                        "pose_p_z<1103.7>"\
                        "pose_o_x<90.66>"\
                        "pose_o_y<71.3>"\
                        "pose_o_z<90.74>"\
                    ">"\
                ">"\
                "hole_location<"\
                    "uid<pf_pr_r3_08>"\
                    "max_obstacle_height<40.0>"\
                    "diam<5.055>"\
                    "stack_thickness_tag<5.0>"\
                    "pose<"\
                        "pose_p_x<77.2>"\
                        "pose_p_y<633.17>"\
                        "pose_p_z<1104.55>"\
                        "pose_o_x<93.1>"\
                        "pose_o_y<71.16>"\
                        "pose_o_z<88.81>"\
                    ">"\
                ">"\
            ">"\
        ">"\
    ">"

    safe_send_message(pf_cobot_uid, msg, "add_permf_product_locations")

    #L-profiel R3 9 R1 1
    msg = "populate_agent<"\
        "product<"\
            "uid<product>"\
            "locations<"\
                "hole_location<"\
                    "uid<pf_pr_r3_09>"\
                    "max_obstacle_height<40.0>"\
                    "diam<5.055>"\
                    "stack_thickness_tag<5.0>"\
                    "pose<"\
                        "pose_p_x<16.1>"\
                        "pose_p_y<634.20>"\
                        "pose_p_z<1102.36>"\
                        "pose_o_x<92.18>"\
                        "pose_o_y<75.8>"\
                        "pose_o_z<97.94>"\
                    ">"\
                ">"\
                "hole_location<"\
                 "uid<pf_pr_r01_01>"\
                 "max_obstacle_height<40.0>"\
                 "diam<5.055>"\
                 "stack_thickness_tag<5.0>"\
                    "pose<"\
                        "pose_p_x<-113.310>"\
                        "pose_p_y<1039.84>"\
                        "pose_p_z<299.63>"\
                        "pose_o_x<90.62>"\
                        "pose_o_y<47.52>"\
                        "pose_o_z<-85.64>"\
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
                        "pose_p_x<16.0>"\
                        "pose_p_y<991.0>"\
                        "pose_p_z<706.0>"\
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
                "loc_uid<pf_st_02_01>"\
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
                "loc_uid<pf_st_02_02>"\
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
                "loc_uid<pf_st_02_03>"\
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
                "loc_uid<pf_st_02_04>"\
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


    msg = "populate_agent<"\
        "fasteners<"\
            "fastener<"\
                "uid<permf_05>"\
                "loc_uid<pf_st_01_05>"\
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
                "loc_uid<pf_st_01_06>"\
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
                "loc_uid<pf_st_01_07>"\
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
                "loc_uid<pf_st_01_08>"\
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

    msg = "populate_agent<"\
        "fasteners<"\
                "fastener<"\
                "uid<permf_09>"\
                "loc_uid<pf_st_01_09>"\
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
                "loc_uid<pf_st_01_10>"\
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
                "loc_uid<pf_st_01_11>"\
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
                "loc_uid<pf_st_01_12>"\
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

    msg = "populate_agent<"\
        "fasteners<"\
                "fastener<"\
                "uid<permf_13>"\
                "loc_uid<pf_st_01_13>"\
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
                "loc_uid<pf_st_01_14>"\
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
                "loc_uid<pf_pr_r01_01>"\
                "action_state<1>"\
                "speed<100>"\
            ">"\
            "action<"\
                "uid<pf_A01>"\
                "action_type<install_permf>"\
                "loc_uid<pf_pr_r3_02>"\
                "action_state<1>"\
                "speed<100>"\
            ">"\
            "action<"\
                "uid<pf_A03>"\
                "action_type<install_permf>"\
                "loc_uid<pf_pr_r3_03>"\
                "action_state<1>"\
                "speed<100>"\
            ">"\
            "action<"\
                "uid<pf_A04>"\
                "action_type<install_permf>"\
                "loc_uid<pf_pr_r3_04>"\
                "action_state<1>"\
                "speed<100>"\
            ">"\
            "action<"\
                "uid<pf_A05>"\
                "action_type<install_permf>"\
                "loc_uid<pf_pr_r3_05>"\
                "action_state<1>"\
                "speed<100>"\
            ">"\
            "action<"\
                "uid<pf_A06>"\
                "action_type<install_permf>"\
                "loc_uid<pf_pr_r3_06>"\
                "action_state<1>"\
                "speed<100>"\
            ">"\
            "action<"\
                "uid<pf_A06>"\
                "action_type<install_permf>"\
                "loc_uid<pf_pr_r3_07>"\
                "action_state<1>"\
                "speed<100>"\
            ">"\
            "action<"\
                "uid<pf_A06>"\
                "action_type<install_permf>"\
                "loc_uid<pf_pr_r3_08>"\
                "action_state<1>"\
                "speed<100>"\
            ">"\
                "action<"\
                "uid<pf_A06>"\
                "action_type<install_permf>"\
                "loc_uid<pf_pr_r3_09>"\
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

