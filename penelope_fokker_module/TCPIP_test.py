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

#1 go to home for cobot with uid_in
def cobot_goto_home(uid_in):
    safe_send_message(uid_in, "goto_home", "cobot_goto_home")

#3->4 add hole locations, stack thickness and diameter in the temp fastener storage list 
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

#5->10 add hole locations, stack thickness and diameter in the permanent fastener storage list
def add_permf_storage_locations():

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
                        "pose_p_x<-289.29>"\
                        "pose_p_y<323.09>"\
                        "pose_p_z<38.17>"\
                        "pose_o_x<38.29>"\
                        "pose_o_y<-179.13>"\
                        "pose_o_z<82.44>"\
                    ">"\
                ">"\
                "hole_location<"\
                    "uid<pf_st_02_02>"\
                    "max_obstacle_height<40.0>"\
                    "diam<5.055>"\
                    "stack_thickness_tag<5.0>"\
                    "pose<"\
                        "pose_p_x<-313.48>"\
                        "pose_p_y<322.56>"\
                        "pose_p_z<38.66>"\
                        "pose_o_x<160.73>"\
                        "pose_o_y<179.46>"\
                        "pose_o_z<-162.19>"\
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
    
    #Nieuwe storage 5-8
    msg = "populate_agent<"\
        "permf_storage_loc<"\
            "uid<permf_storage>"\
            "locations<"\
                 "hole_location<"\
                     "uid<pf_st_02_05>"\
                     "max_obstacle_height<40.0>"\
                     "diam<5.055>"\
                     "stack_thickness_tag<5.0>"\
                     "pose<"\
                         "pose_p_x<-408.68>"\
                         "pose_p_y<242.47>"\
                         "pose_p_z<40.7>"\
                         "pose_o_x<138.31>"\
                         "pose_o_y<-179.38>"\
                         "pose_o_z<100.95>"\
                     ">"\
                 ">"\
                 "hole_location<"\
                     "uid<pf_st_02_06>"\
                     "max_obstacle_height<40.0>"\
                     "diam<5.055>"\
                     "stack_thickness_tag<5.0>"\
                     "pose<"\
                         "pose_p_x<-431.03>"\
                         "pose_p_y<239.71>"\
                         "pose_p_z<40.860>"\
                         "pose_o_x<134.53>"\
                         "pose_o_y<-178.91>"\
                         "pose_o_z<100.75>"\
                     ">"\
                 ">"\
                 "hole_location<"\
                     "uid<pf_st_02_07>"\
                     "max_obstacle_height<40.0>"\
                     "diam<5.055>"\
                     "stack_thickness_tag<5.0>"\
                     "pose<"\
                         "pose_p_x<-434.47>"\
                         "pose_p_y<265.57>"\
                         "pose_p_z<40.70>"\
                         "pose_o_x<156.38>"\
                         "pose_o_y<-178.73>"\
                         "pose_o_z<130.34>"\
                     ">"\
                 ">"\
                 "hole_location<"\
                     "uid<pf_st_02_08>"\
                     "max_obstacle_height<40.0>"\
                     "diam<5.055>"\
                     "stack_thickness_tag<5.0>"\
                     "pose<"\
                         "pose_p_x<-409.52>"\
                         "pose_p_y<267.11>"\
                         "pose_p_z<41.650>"\
                         "pose_o_x<125.46>"\
                         "pose_o_y<-179.15>"\
                         "pose_o_z<102.13>"\
                     ">"\
                ">"\
            ">"\
        ">"\
    ">"
    
    safe_send_message(pf_cobot_uid, msg, "add_permf_storage_locations")

    #Nieuwe storage 9-12
    msg = "populate_agent<"\
        "permf_storage_loc<"\
            "uid<permf_storage>"\
            "locations<"\
                "hole_location<"\
                     "uid<pf_st_02_09>"\
                     "max_obstacle_height<40.0>"\
                     "diam<5.055>"\
                     "stack_thickness_tag<5.0>"\
                     "pose<"\
                         "pose_p_x<-384.91>"\
                         "pose_p_y<268.93>"\
                         "pose_p_z<41.22>"\
                         "pose_o_x<161.66>"\
                         "pose_o_y<-179.03>"\
                         "pose_o_z<135.08>"\
                     ">"\
                 ">"\
                 "hole_location<"\
                     "uid<pf_st_02_10>"\
                     "max_obstacle_height<40.0>"\
                     "diam<5.055>"\
                     "stack_thickness_tag<5.0>"\
                     "pose<"\
                         "pose_p_x<-360.31>"\
                         "pose_p_y<270.34>"\
                         "pose_p_z<41.73>"\
                         "pose_o_x<93.22>"\
                         "pose_o_y<-179.58>"\
                         "pose_o_z<68.4>"\
                     ">"\
                 ">"\
                 "hole_location<"\
                     "uid<pf_st_02_11>"\
                     "max_obstacle_height<40.0>"\
                     "diam<5.055>"\
                     "stack_thickness_tag<5.0>"\
                     "pose<"\
                         "pose_p_x<-334.89>"\
                         "pose_p_y<271.85>"\
                         "pose_p_z<41.32>"\
                         "pose_o_x<138.47>"\
                         "pose_o_y<-178.93>"\
                         "pose_o_z<111.65>"\
                     ">"\
                 ">"\
                 "hole_location<"\
                     "uid<pf_st_02_12>"\
                     "max_obstacle_height<40.0>"\
                     "diam<5.055>"\
                     "stack_thickness_tag<5.0>"\
                     "pose<"\
                         "pose_p_x<-309.72>"\
                         "pose_p_y<273.26>"\
                         "pose_p_z<41.65>"\
                         "pose_o_x<155.49>"\
                         "pose_o_y<-178.9>"\
                         "pose_o_z<126.36>"\
                     ">"\
                 ">"\
            ">"\
        ">"\
    ">"
    
    safe_send_message(pf_cobot_uid, msg, "add_permf_storage_locations")

    #Nieuwe storage 13-16
    msg = "populate_agent<"\
        "permf_storage_loc<"\
            "uid<permf_storage>"\
            "locations<"\
                "hole_location<"\
                     "uid<pf_st_02_13>"\
                     "max_obstacle_height<40.0>"\
                     "diam<5.055>"\
                     "stack_thickness_tag<5.0>"\
                     "pose<"\
                         "pose_p_x<-284.91>"\
                         "pose_p_y<274.72>"\
                         "pose_p_z<41.060>"\
                         "pose_o_x<97.96>"\
                         "pose_o_y<-179.43>"\
                         "pose_o_z<76.22>"\
                     ">"\
                 ">"\
                 "hole_location<"\
                     "uid<pf_st_02_14>"\
                     "max_obstacle_height<40.0>"\
                     "diam<5.055>"\
                     "stack_thickness_tag<5.0>"\
                     "pose<"\
                         "pose_p_x<-286.78>"\
                         "pose_p_y<302.28>"\
                         "pose_p_z<41.07>"\
                         "pose_o_x<65.76>"\
                         "pose_o_y<-179.76>"\
                         "pose_o_z<39.85>"\
                     ">"\
                 ">"\
                 "hole_location<"\
                     "uid<pf_st_02_15>"\
                     "max_obstacle_height<40.0>"\
                     "diam<5.055>"\
                     "stack_thickness_tag<5.0>"\
                     "pose<"\
                         "pose_p_x<-311.91>"\
                         "pose_p_y<300.83>"\
                         "pose_p_z<41.0>"\
                         "pose_o_x<102.81>"\
                         "pose_o_y<-178.64>"\
                         "pose_o_z<76.38>"\
                     ">"\
                 ">"\
                 "hole_location<"\
                     "uid<pf_st_02_16>"\
                     "max_obstacle_height<40.0>"\
                     "diam<5.055>"\
                     "stack_thickness_tag<5.0>"\
                     "pose<"\
                         "pose_p_x<-336.6>"\
                         "pose_p_y<299.41>"\
                         "pose_p_z<41.720>"\
                         "pose_o_x<117.21>"\
                         "pose_o_y<-179.27>"\
                         "pose_o_z<92.73>"\
                     ">"\
                 ">"\
            ">"\
        ">"\
    ">"
    
    safe_send_message(pf_cobot_uid, msg, "add_permf_storage_locations")

    #Nieuwe storage 17-19
    msg = "populate_agent<"\
        "permf_storage_loc<"\
            "uid<permf_storage>"\
            "locations<"\
                "hole_location<"\
                     "uid<pf_st_02_17>"\
                     "max_obstacle_height<40.0>"\
                     "diam<5.055>"\
                     "stack_thickness_tag<5.0>"\
                     "pose<"\
                         "pose_p_x<-361.11>"\
                         "pose_p_y<297.63>"\
                         "pose_p_z<40.510>"\
                         "pose_o_x<130.06>"\
                         "pose_o_y<-178.58>"\
                         "pose_o_z<107.11>"\
                     ">"\
                 ">"\
                 "hole_location<"\
                     "uid<pf_st_02_18>"\
                     "max_obstacle_height<40.0>"\
                     "diam<5.055>"\
                     "stack_thickness_tag<5.0>"\
                     "pose<"\
                         "pose_p_x<-386.34>"\
                         "pose_p_y<296.12>"\
                         "pose_p_z<40.73>"\
                         "pose_o_x<130.06>"\
                         "pose_o_y<-178.58>"\
                         "pose_o_z<107.11>"\
                     ">"\
                 ">"\
                 "hole_location<"\
                     "uid<pf_st_02_19>"\
                     "max_obstacle_height<40.0>"\
                     "diam<5.055>"\
                     "stack_thickness_tag<5.0>"\
                     "pose<"\
                         "pose_p_x<-411.27>"\
                         "pose_p_y<294.7>"\
                         "pose_p_z<40.57>"\
                         "pose_o_x<165.45>"\
                         "pose_o_y<-178.98>"\
                         "pose_o_z<143.62>"\
                     ">"\
                 ">"\
            ">"\
        ">"\
    ">"
    
    safe_send_message(pf_cobot_uid, msg, "add_permf_storage_locations")
    
#6->16 add hole locations, stack thickness and diameter in the permf product list
def add_permf_product_locations():

    #pr 02 1-4
    msg = "populate_agent<"\
        "product<"\
            "uid<product>"\
            "locations<"\
                "hole_location<"\
                    "uid<pf_pr_r2_01>"\
                    "max_obstacle_height<40.0>"\
                    "diam<5.055>"\
                    "stack_thickness_tag<5.0>"\
                    "pose<"\
                        "pose_p_x<-143.37>"\
                        "pose_p_y<790.92>"\
                        "pose_p_z<679.73>"\
                        "pose_o_x<91.50>"\
                        "pose_o_y<60.63>"\
                        "pose_o_z<-88.52>"\
                    ">"\
                ">"\
                "hole_location<"\
                    "uid<pf_pr_r2_02>"\
                    "max_obstacle_height<40.0>"\
                    "diam<5.055>"\
                    "stack_thickness_tag<5.0>"\
                    "pose<"\
                        "pose_p_x<-115.64>"\
                        "pose_p_y<791.490>"\
                        "pose_p_z<679.91>"\
                        "pose_o_x<91.76>"\
                        "pose_o_y<60.59>"\
                        "pose_o_z<-87.27>"\
                    ">"\
                ">"\
                "hole_location<"\
                    "uid<pf_pr_r2_03>"\
                    "max_obstacle_height<40.0>"\
                    "diam<5.055>"\
                    "stack_thickness_tag<5.0>"\
                    "pose<"\
                        "pose_p_x<-84.42>"\
                        "pose_p_y<790.580>"\
                        "pose_p_z<679.96>"\
                        "pose_o_x<92.29>"\
                        "pose_o_y<60.73>"\
                        "pose_o_z<-87.56>"\
                    ">"\
                ">"\
                "hole_location<"\
                    "uid<pf_pr_r2_04>"\
                    "max_obstacle_height<40.0>"\
                    "diam<5.055>"\
                    "stack_thickness_tag<5.0>"\
                    "pose<"\
                        "pose_p_x<-21.23>"\
                        "pose_p_y<791.710>"\
                        "pose_p_z<679.71>"\
                        "pose_o_x<90.81>"\
                        "pose_o_y<62.47>"\
                        "pose_o_z<-90.61>"\
                    ">"\
                ">"\
            ">"\
        ">"\
    ">"

    safe_send_message(pf_cobot_uid, msg, "add_permf_product_locations")
    
    #pr 02 5-8
    msg = "populate_agent<"\
        "product<"\
            "uid<product>"\
            "locations<"\
                "hole_location<"\
                    "uid<pf_pr_r2_05>"\
                    "max_obstacle_height<40.0>"\
                    "diam<5.055>"\
                    "stack_thickness_tag<5.0>"\
                    "pose<"\
                        "pose_p_x<41.76>"\
                        "pose_p_y<791.78>"\
                        "pose_p_z<679.91>"\
                        "pose_o_x<93.01>"\
                        "pose_o_y<62.4>"\
                        "pose_o_z<-90.03>"\
                    ">"\
                ">"\
                "hole_location<"\
                    "uid<pf_pr_r2_06>"\
                    "max_obstacle_height<40.0>"\
                    "diam<5.055>"\
                    "stack_thickness_tag<5.0>"\
                    "pose<"\
                        "pose_p_x<73.13>"\
                        "pose_p_y<789.04>"\
                        "pose_p_z<679.57>"\
                        "pose_o_x<93.1>"\
                        "pose_o_y<60.26>"\
                        "pose_o_z<-90.71>"\
                    ">"\
                ">"\
                "hole_location<"\
                    "uid<pf_pr_r2_07>"\
                    "max_obstacle_height<40.0>"\
                    "diam<5.055>"\
                    "stack_thickness_tag<5.0>"\
                    "pose<"\
                        "pose_p_x<105.03>"\
                        "pose_p_y<788.64>"\
                        "pose_p_z<679.8>"\
                        "pose_o_x<91.65>"\
                        "pose_o_y<59.39>"\
                        "pose_o_z<-91.05>"\
                    ">"\
                ">"\
                "hole_location<"\
                    "uid<pf_pr_r2_08>"\
                    "max_obstacle_height<40.0>"\
                    "diam<5.055>"\
                    "stack_thickness_tag<5.0>"\
                    "pose<"\
                        "pose_p_x<168.63>"\
                        "pose_p_y<790.48>"\
                        "pose_p_z<679.73>"\
                        "pose_o_x<92.09>"\
                        "pose_o_y<61.33>"\
                        "pose_o_z<-91.86>"\
                    ">"\
                ">"\
            ">"\
        ">"\
    ">"
    
    safe_send_message(pf_cobot_uid, msg, "add_permf_product_locations")
    
    #pr 02 9-10
    msg = "populate_agent<"\
        "product<"\
            "uid<product>"\
            "locations<"\
                "hole_location<"\
                    "uid<pf_pr_r2_09>"\
                    "max_obstacle_height<40.0>"\
                    "diam<5.055>"\
                    "stack_thickness_tag<5.0>"\
                    "pose<"\
                        "pose_p_x<199.69>"\
                        "pose_p_y<789.95>"\
                        "pose_p_z<679.75>"\
                        "pose_o_x<93.5>"\
                        "pose_o_y<61.01>"\
                        "pose_o_z<-91.61>"\
                    ">"\
                ">"\
                "hole_location<"\
                    "uid<pf_pr_r2_10>"\
                    "max_obstacle_height<40.0>"\
                    "diam<5.055>"\
                    "stack_thickness_tag<5.0>"\
                    "pose<"\
                        "pose_p_x<231.28>"\
                        "pose_p_y<790.7>"\
                        "pose_p_z<680.03>"\
                        "pose_o_x<92.86>"\
                        "pose_o_y<60.61>"\
                        "pose_o_z<-93.3>"\
                    ">"\
                ">"\
            ">"\
        ">"\
    ">"

    safe_send_message(pf_cobot_uid, msg, "add_permf_product_locations")

    #pr 01 1-4
    msg = "populate_agent<"\
        "product<"\
            "uid<product>"\
            "locations<"\
                "hole_location<"\
                    "uid<pf_pr_r1_01>"\
                    "max_obstacle_height<40.0>"\
                    "diam<5.055>"\
                    "stack_thickness_tag<5.0>"\
                    "pose<"\
                        "pose_p_x<230.72>"\
                        "pose_p_y<624.9>"\
                        "pose_p_z<1104.2>"\
                        "pose_o_x<92.35>"\
                        "pose_o_y<72.28>"\
                        "pose_o_z<-91.88>"\
                    ">"\
                ">"\
                "hole_location<"\
                    "uid<pf_pr_r1_02>"\
                    "max_obstacle_height<40.0>"\
                    "diam<5.055>"\
                    "stack_thickness_tag<5.0>"\
                    "pose<"\
                        "pose_p_x<199.25>"\
                        "pose_p_y<631.19>"\
                        "pose_p_z<1105.08>"\
                        "pose_o_x<91.09>"\
                        "pose_o_y<75.20>"\
                        "pose_o_z<-89.31>"\
                    ">"\
                ">"\
                "hole_location<"\
                    "uid<pf_pr_r1_03>"\
                    "max_obstacle_height<40.0>"\
                    "diam<5.055>"\
                    "stack_thickness_tag<5.0>"\
                    "pose<"\
                        "pose_p_x<167.01>"\
                        "pose_p_y<627.9>"\
                        "pose_p_z<1104.53>"\
                        "pose_o_x<92.39>"\
                        "pose_o_y<72.39>"\
                        "pose_o_z<-86.71>"\
                    ">"\
                ">"\
                "hole_location<"\
                    "uid<pf_pr_r1_04>"\
                    "max_obstacle_height<40.0>"\
                    "diam<5.055>"\
                    "stack_thickness_tag<5.0>"\
                    "pose<"\
                        "pose_p_x<135.37>"\
                        "pose_p_y<628.27>"\
                        "pose_p_z<1102.88>"\
                        "pose_o_x<90.57>"\
                        "pose_o_y<76.53>"\
                        "pose_o_z<-93.36>"\
                    ">"\
                ">"\
            ">"\
        ">"\
    ">"
    
    safe_send_message(pf_cobot_uid, msg, "add_permf_product_locations")

    #pr 01 5-8
    msg = "populate_agent<"\
        "product<"\
            "uid<product>"\
            "locations<"\
                "hole_location<"\
                    "uid<pf_pr_r1_05>"\
                    "max_obstacle_height<40.0>"\
                    "diam<5.055>"\
                    "stack_thickness_tag<5.0>"\
                    "pose<"\
                        "pose_p_x<104.27>"\
                        "pose_p_y<629.0>"\
                        "pose_p_z<1103.41>"\
                        "pose_o_x<90.68>"\
                        "pose_o_y<77.4>"\
                        "pose_o_z<-92.03>"\
                    ">"\
                ">"\
                "hole_location<"\
                    "uid<pf_pr_r1_06>"\
                    "max_obstacle_height<40.0>"\
                    "diam<5.055>"\
                    "stack_thickness_tag<5.0>"\
                    "pose<"\
                        "pose_p_x<72.71>"\
                        "pose_p_y<624.07>"\
                        "pose_p_z<1103.55>"\
                        "pose_o_x<88.88>"\
                        "pose_o_y<71.69>"\
                        "pose_o_z<-88.94>"\
                    ">"\
                ">"\
                "hole_location<"\
                    "uid<pf_pr_r1_07>"\
                    "max_obstacle_height<40.0>"\
                    "diam<5.055>"\
                    "stack_thickness_tag<5.0>"\
                    "pose<"\
                        "pose_p_x<41.46>"\
                        "pose_p_y<628.94>"\
                        "pose_p_z<1104.27>"\
                        "pose_o_x<89.24>"\
                        "pose_o_y<73.46>"\
                        "pose_o_z<-89.00>"\
                    ">"\
                ">"\
                "hole_location<"\
                    "uid<pf_pr_r1_08>"\
                    "max_obstacle_height<40.0>"\
                    "diam<5.055>"\
                    "stack_thickness_tag<5.0>"\
                    "pose<"\
                        "pose_p_x<9.27>"\
                        "pose_p_y<629.7>"\
                        "pose_p_z<1104.46>"\
                        "pose_o_x<90.54>"\
                        "pose_o_y<73.64>"\
                        "pose_o_z<-89.09>"\
                    ">"\
                ">"\
            ">"\
        ">"\
    ">"
    
    safe_send_message(pf_cobot_uid, msg, "add_permf_product_locations")
    
    #pr 01 9
    msg = "populate_agent<"\
        "product<"\
            "uid<product>"\
            "locations<"\
                "hole_location<"\
                    "uid<pf_pr_r1_09>"\
                    "max_obstacle_height<40.0>"\
                    "diam<5.055>"\
                    "stack_thickness_tag<5.0>"\
                    "pose<"\
                        "pose_p_x<-20.89>"\
                        "pose_p_y<631.25>"\
                        "pose_p_z<1104.42>"\
                        "pose_o_x<89.84>"\
                        "pose_o_y<73.64>"\
                        "pose_o_z<-87.88>"\
                    ">"\
                ">"\
            ">"\
        ">"\
    ">"
    
    safe_send_message(pf_cobot_uid, msg, "add_permf_product_locations")
    
#3->19 add hole locations, stack thickness and diameter in the tempf product list
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
                        "pose_p_z<704.0>"\
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
                        "pose_p_x<226.5>"\
                        "pose_p_y<938.0>"\
                        "pose_p_z<811.0>"\
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
                        "pose_p_x<625>"\
                        "pose_p_y<938.0>"\
                        "pose_p_z<812.5>"\
                        "pose_o_x<90.0>"\
                        "pose_o_y<66.0>"\
                        "pose_o_z<30.0>"\
                    ">"\
                ">"\
            ">"\
        ">"\
    ">"
    
    safe_send_message(tf_cobot_uid, msg, "add_tempf_product_locations")

#5->24 add permanent fasteners in storage
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
                "loc_uid<pf_st_02_05>"\
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
                "loc_uid<pf_st_02_06>"\
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
                "loc_uid<pf_st_02_07>"\
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
                "loc_uid<pf_st_02_08>"\
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
                "loc_uid<pf_st_02_09>"\
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
                "loc_uid<pf_st_02_10>"\
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
                "loc_uid<pf_st_02_11>"\
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
                "loc_uid<pf_st_02_12>"\
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
                "loc_uid<pf_st_02_13>"\
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
                "loc_uid<pf_st_02_14>"\
                "fastener_state<1>"\
                "diam<5.055>"\
                "shaft_height<23.37>"\
                "min_stack_thickness<3.96>"\
                "max_stack_thickness<5.59>"\
                "tcp_tip_dist<14.81>"\
                "tcp_top_dist<4.45>"\
            ">"\
            "fastener<"\
                "uid<permf_15>"\
                "loc_uid<pf_st_02_15>"\
                "fastener_state<1>"\
                "diam<5.055>"\
                "shaft_height<23.37>"\
                "min_stack_thickness<3.96>"\
                "max_stack_thickness<5.59>"\
                "tcp_tip_dist<14.81>"\
                "tcp_top_dist<4.45>"\
            ">"\
            "fastener<"\
                "uid<permf_16>"\
                "loc_uid<pf_st_02_16>"\
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
                "uid<permf_17>"\
                "loc_uid<pf_st_02_17>"\
                "fastener_state<1>"\
                "diam<5.055>"\
                "shaft_height<23.37>"\
                "min_stack_thickness<3.96>"\
                "max_stack_thickness<5.59>"\
                "tcp_tip_dist<14.81>"\
                "tcp_top_dist<4.45>"\
            ">"\
            "fastener<"\
                "uid<permf_18>"\
                "loc_uid<pf_st_02_18>"\
                "fastener_state<1>"\
                "diam<5.055>"\
                "shaft_height<23.37>"\
                "min_stack_thickness<3.96>"\
                "max_stack_thickness<5.59>"\
                "tcp_tip_dist<14.81>"\
                "tcp_top_dist<4.45>"\
            ">"\
            "fastener<"\
                "uid<permf_19>"\
                "loc_uid<pf_st_02_19>"\
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
    
#3->27 add 9 temporary fasteners in storage  
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

#3->30 Add the permanent fastener actions to the agent
# Defined actions will be executed later
def add_permf_actions():
    msg = "populate_agent<"\
        "actions<"\
            "action<"\
                "uid<pf_A02>"\
                "action_type<install_permf>"\
                "loc_uid<pf_pr_r2_02>"\
                "action_state<1>"\
                "speed<100>"\
            ">"\
            "action<"\
                "uid<pf_A03>"\
                "action_type<install_permf>"\
                "loc_uid<pf_pr_r2_03>"\
                "action_state<1>"\
                "speed<100>"\
            ">"\
            "action<"\
                "uid<pf_A04>"\
                "action_type<install_permf>"\
                "loc_uid<pf_pr_r2_04>"\
                "action_state<1>"\
                "speed<100>"\
            ">"\
            "action<"\
                "uid<pf_A05>"\
                "action_type<install_permf>"\
                "loc_uid<pf_pr_r2_05>"\
                "action_state<1>"\
                "speed<100>"\
            ">"\
            "action<"\
                "uid<pf_A08>"\
                "action_type<install_permf>"\
                "loc_uid<pf_pr_r2_08>"\
                "action_state<1>"\
                "speed<100>"\
            ">"\
        ">"\
    ">"

    safe_send_message(pf_cobot_uid, msg, "add_permf_actions")

    msg = "populate_agent<"\
        "actions<"\
            "action<"\
                "uid<pf_A09>"\
                "action_type<install_permf>"\
                "loc_uid<pf_pr_r2_10>"\
                "action_state<1>"\
                "speed<100>"\
            ">"\
            "action<"\
                "uid<pf_A11>"\
                "action_type<install_permf>"\
                "loc_uid<pf_pr_r1_02>"\
                "action_state<1>"\
                "speed<100>"\
            ">"\
            "action<"\
                "uid<pf_A12>"\
                "action_type<install_permf>"\
                "loc_uid<pf_pr_r1_03>"\
                "action_state<1>"\
                "speed<100>"\
            ">"\
            "action<"\
                "uid<pf_A13>"\
                "action_type<install_permf>"\
                "loc_uid<pf_pr_r1_04>"\
                "action_state<1>"\
                "speed<100>"\
            ">"\
            "action<"\
                "uid<pf_A14>"\
                "action_type<install_permf>"\
                "loc_uid<pf_pr_r1_05>"\
                "action_state<1>"\
                "speed<100>"\
            ">"\
            "action<"\
                "uid<pf_A16>"\
                "action_type<install_permf>"\
                "loc_uid<pf_pr_r1_07>"\
                "action_state<1>"\
                "speed<100>"\
            ">"\
        ">"\
    ">"

    safe_send_message(pf_cobot_uid, msg, "add_permf_actions")
    msg = "populate_agent<"\
        "actions<"\
            "action<"\
                "uid<pf_A17>"\
                "action_type<install_permf>"\
                "loc_uid<pf_pr_r1_08>"\
                "action_state<1>"\
                "speed<100>"\
            ">"\
            "action<"\
                "uid<pf_A18>"\
                "action_type<install_permf>"\
                "loc_uid<pf_pr_r1_09>"\
                "action_state<1>"\
                "speed<100>"\
        ">"\
    ">"

    safe_send_message(pf_cobot_uid, msg, "add_permf_actions")
    
#2->32 add nine actions....not yet execute them
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

#2->34 add nine actions....not yet execute them
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

#1->35 execute action with uid on cobot with uid
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

pf_ip_address = "10.237.20.103"
pf_port = 20002
pf_cobot_uid = f"{pf_ip_address}/{pf_port}"
pf_tcp_client_thread = threading.Thread(target=run_tcp_client, args=(pf_ip_address, pf_port))
pf_tcp_client_thread.start()

cobot_goto_home(tf_cobot_uid)
cobot_goto_home(pf_cobot_uid)

add_tempf_storage_locations()
add_tempf_product_locations()
add_tempf_in_storage()
add_tempf_install_actions()
add_tempf_uninstall_actions()

add_permf_storage_locations()
add_permf_product_locations()
add_permf_in_storage()
add_permf_actions()

# install the temporary fasteners
execute_action(tf_cobot_uid, "tf_i_A01")
execute_action(tf_cobot_uid, "tf_i_A02")
execute_action(tf_cobot_uid, "tf_i_A03")
# execute_action(tf_cobot_uid, "tf_i_A04")
# execute_action(tf_cobot_uid, "tf_i_A05")
# execute_action(tf_cobot_uid, "tf_i_A06")
# execute_action(tf_cobot_uid, "tf_i_A07")
# execute_action(tf_cobot_uid, "tf_i_A08")
# execute_action(tf_cobot_uid, "tf_i_A09")
cobot_goto_home(tf_cobot_uid)

# install the permanent fasteners
execute_action(pf_cobot_uid, "pf_A02")
cobot_goto_home(pf_cobot_uid)
execute_action(pf_cobot_uid, "pf_A03")
cobot_goto_home(pf_cobot_uid)
execute_action(pf_cobot_uid, "pf_A04")
cobot_goto_home(pf_cobot_uid)
execute_action(pf_cobot_uid, "pf_A05")
cobot_goto_home(pf_cobot_uid)
execute_action(pf_cobot_uid, "pf_A09")
cobot_goto_home(pf_cobot_uid)
execute_action(pf_cobot_uid, "pf_A11")
cobot_goto_home(pf_cobot_uid)
execute_action(pf_cobot_uid, "pf_A12")
cobot_goto_home(pf_cobot_uid)
execute_action(pf_cobot_uid, "pf_A13")
cobot_goto_home(pf_cobot_uid)
execute_action(pf_cobot_uid, "pf_A14")
cobot_goto_home(pf_cobot_uid)
execute_action(pf_cobot_uid, "pf_A16")
cobot_goto_home(pf_cobot_uid)
execute_action(pf_cobot_uid, "pf_A17")
cobot_goto_home(pf_cobot_uid)
execute_action(pf_cobot_uid, "pf_A18")
cobot_goto_home(pf_cobot_uid)

# uninstall the temporary fasteners
execute_action(tf_cobot_uid, "tf_u_A01")
execute_action(tf_cobot_uid, "tf_u_A02")
execute_action(tf_cobot_uid, "tf_u_A03")
# execute_action(tf_cobot_uid, "tf_u_A04")
# execute_action(tf_cobot_uid, "tf_u_A05")
# execute_action(tf_cobot_uid, "tf_u_A06")
# execute_action(tf_cobot_uid, "tf_u_A07")
# execute_action(tf_cobot_uid, "tf_u_A08")
# execute_action(tf_cobot_uid, "tf_u_A09")
cobot_goto_home(tf_cobot_uid)

##################################################################################################
##################################################################################################
##################################################################################################

