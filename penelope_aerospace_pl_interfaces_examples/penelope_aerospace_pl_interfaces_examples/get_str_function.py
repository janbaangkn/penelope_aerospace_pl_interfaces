OPEN_TAG = "<"
CLOSE_TAG = ">"
PROVIDE_STATUS_MSG = OPEN_TAG + "PROVIDE_STATUS" + CLOSE_TAG
UID_TAG = "uid" + OPEN_TAG
STORAGE_TAG = "storage" + OPEN_TAG
PRODUCTS_TAG = "products" + OPEN_TAG
PRODUCT_TAG = "product" + OPEN_TAG
LOCATIONS_TAG = "locations" + OPEN_TAG
LOC_UID_TAG = "loc_uid" + OPEN_TAG
MAX_OBST_HEIGHT_TAG = "max_obstacle_height" + OPEN_TAG
APPR_POS_UID_TAG = "approach_pos_uid" + OPEN_TAG
HOLE_LOCATION_CONT_TAG = "hole_location_container" + OPEN_TAG
HOLE_LOCATION_TAG = "hole_location" + OPEN_TAG
POSE_TAG = "pose" + OPEN_TAG
POSE_PX_TAG = "pose_p_x" + OPEN_TAG
POSE_PY_TAG = "pose_p_y" + OPEN_TAG
POSE_PZ_TAG = "pose_p_z" + OPEN_TAG
POSE_OX_TAG = "pose_o_x" + OPEN_TAG
POSE_OY_TAG = "pose_o_y" + OPEN_TAG
POSE_OZ_TAG = "pose_o_z" + OPEN_TAG
POSE_OW_TAG = "pose_o_w" + OPEN_TAG
DIAM_TAG = "diam" + OPEN_TAG
STACK_T_TAG = "stack_thickness_tag" + OPEN_TAG
DRILL_JIG_DIST_TAG = "drill_jig_dist" + OPEN_TAG
DRILLED_TAG = "drilled" + OPEN_TAG
LAYERS_TAG = "layers" + OPEN_TAG
MAT_LAYER_TAG = "material_layer" + OPEN_TAG
LAYER_THICKNESS_TAG = "layer_thickness" + OPEN_TAG  
SHAFT_HEIGHT_TAG = "shaft_height" + OPEN_TAG
MIN_STACK_TAG = "min_stack_thickness" + OPEN_TAG
MAX_STACK_TAG = "max_stack_thickness" + OPEN_TAG
TCP_TIP_DIST_TAG = "tcp_tip_dist" + OPEN_TAG
TCP_TOP_DIST_TAG = "tcp_top_dist" + OPEN_TAG                        
DRILL_SPEED_TAG = "drill_speed" + OPEN_TAG                           
DRILL_FEED_TAG = "drill_feed" + OPEN_TAG                            
LOWER_TORQUE_LIMIT_TAG = "lower_torque_limit" + OPEN_TAG             
UPPER_TORQUE_LIMIT_TAG = "upper_torque_limit" + OPEN_TAG            
TORQUE_THRESHOLD_TAG = "torque_threshold" + OPEN_TAG                      
MAX_TEMPF_CLAMP_FORCE_TAG = "max_tempf_clamp_force" + OPEN_TAG
WAYPOINT_TAG = "waypoint" + OPEN_TAG
WAYPOINTS_TAG = "waypoints" + OPEN_TAG
ORIENTATION_TAG = "orientation" + OPEN_TAG
BLEND_RADIUS_TAG = "blend_radius" + OPEN_TAG
ACTIONS_TAG = "actions" + OPEN_TAG
ACTION_TAG = "action" + OPEN_TAG
OBJ_UID_TAG = "obj_uid" + OPEN_TAG
ACTION_STATE_TAG = "action_state" + OPEN_TAG
PASSING_UIDS_TAG = "passing_uids" + OPEN_TAG
PASSING_UID_TAG = "passing_uid" + OPEN_TAG
SPEED_TAG = "speed" + OPEN_TAG
DRILL_TASKS_TAG = "drill_tasks" + OPEN_TAG
DRILL_TASK_TAG = "drill_task" + OPEN_TAG
FASTENERS_TAG = "fasteners" + OPEN_TAG
FASTENER_TAG = "fastener" + OPEN_TAG
FASTENER_STATE_TAG = "fastener_state" + OPEN_TAG
TEMPFS_TAG = "tempfs" + OPEN_TAG
TEMPF_TAG = "tempf" + OPEN_TAG
DOCKING_POSS_TAG = "docking_positions" + OPEN_TAG
DOCKING_POS_TAG = "docking_position" + OPEN_TAG
END_EFFECTORS_TAG = "end_effectors" + OPEN_TAG
END_EFFECTOR_TAG = "end_effector" + OPEN_TAG
END_EFFECTOR_STATE_TAG = "end_effector_state" + OPEN_TAG
END_EFFECTOR_UID_TAG = "end_effector_uid" + OPEN_TAG
EXECUTE_TAG = "execute" + OPEN_TAG

   
# Function to send list of storage location containers to the cobot controller
# AssemblyHoleLocationContainer
def storage_str_to_cobot(storage_in):
    str = STORAGE_TAG + _get_hole_location_container_to_cobot_str(storage_in) + CLOSE_TAG
    return str

# Function to send list of product containers with holes to the cobot controller
def products_str_to_cobot(products_in):
    str = PRODUCTS_TAG

    for product in products_in:
        str = PRODUCT_TAG + _get_hole_location_container_to_cobot_str(product) + CLOSE_TAG

    str = str + CLOSE_TAG

    return str

# Function to send list of defined waypoints to the cobot controller
def waypoints_str_to_cobot(waypoints_in):
    str = WAYPOINTS_TAG

    for waypoint in waypoints_in:
        str = str + _get_waypoint_to_cobot_str(waypoint)

    str = str + CLOSE_TAG

    return str


# Function to send list of defined actions to the cobot controller
def actions_str_to_cobot(actions_in): 
    str = ACTIONS_TAG

    for action in actions_in:
        str = str + _get_action_to_cobot_str(action)

    str = str + CLOSE_TAG

    return str

# Function to send list of holes to be drilled to the cobot controller
def drill_tasks_str_to_cobot(drill_tasks_in): 
    str = DRILL_TASKS_TAG

    for drill_task in drill_tasks_in:
        str = str + _get_drill_task_to_cobot_str(drill_task)

    str = str + CLOSE_TAG

    return str 

# Function to send list of available fasteners to the cobot controller
def fasteners_str_to_cobot(fasteners_in):  
    str = FASTENERS_TAG

    for fastener in fasteners_in:
        str = str + _get_fastener_to_cobot_str(fastener)

    str = str + CLOSE_TAG

    return str 

# Function to send list of available temporary fasteners to the cobot controller
def tempfs_str_to_cobot(tempfs_in): 
    str = TEMPFS_TAG

    for tempf in tempfs_in:
        str = str + _get_tempf_to_cobot_str(tempf)

    str = str + CLOSE_TAG

    return str 

# Function to send list of available docking positions for End Effectors to the cobot controller
def docking_pos_str_to_cobot(docking_pos_in): 
    str = DOCKING_POSS_TAG

    for docking_pos in docking_pos_in:
        str = str + _get_docking_pos_to_cobot_str(docking_pos)

    str = str + CLOSE_TAG

    return str 
    
# Function to send list of available End Effectors to the cobot controller
def ee_str_to_cobot(ee_in):  
    str = END_EFFECTORS_TAG

    for ee in ee_in:
        str = str + _get_end_effector_to_cobot_str(ee)

    str = str + CLOSE_TAG

    return str 

# get message string for AssemblyHoleLocationContainer
def _get_hole_location_container_to_cobot_str(cont_in):
    str = HOLE_LOCATION_CONT_TAG 
    
    # uid of the container
    str = str + UID_TAG + cont_in.uid + CLOSE_TAG

    # list of hole locations
    str = str + LOCATIONS_TAG
    for ahl in cont_in.locations:
        str = str + _get_hole_location_to_cobot_str(ahl)
    str = str + CLOSE_TAG

    # max_obstacle_height
    str = str + MAX_OBST_HEIGHT_TAG + str(cont_in.max_obstacle_height) + CLOSE_TAG

    # approach_pos_uid
    str = str + APPR_POS_UID_TAG + cont_in.approach_pos_uid + CLOSE_TAG 

    return str + CLOSE_TAG

# get message string for AssemblyHoleLocation
def _get_hole_location_to_cobot_str(loc_in):
    str = HOLE_LOCATION_TAG 
    # uid of the hole position: string uid
    str = str + UID_TAG + loc_in.uid + CLOSE_TAG                         

    # Nominal location of the hole: geometry_msgs/Pose nom_pos
    str = str + _get_pose_str(loc_in.nom_pos)             

    # Diameter of the hole: float32 diam
    str = str + DIAM_TAG + str(loc_in.diam) + CLOSE_TAG                

    # Total thickness at the hole
    # Must be equal to the sum of layer thicknesses: float32 stack_t
    str = str + STACK_T_TAG + str(loc_in.stack_t) + CLOSE_TAG        

    # distance of the drill jig hole entry above the surface: float32 drill_jig_dist                  
    str = str + DRILL_JIG_DIST_TAG + str(loc_in.drill_jig_dist) + CLOSE_TAG

    # Whether or not the hole has been drilled: bool drilled
    str = str + DRILLED_TAG + str(loc_in.drilled) + CLOSE_TAG             

    # Material definition for each layer: AssemblyMaterialLayer[] layers
    str = str + LAYERS_TAG
    for layer in loc_in.layers:
        str = str + _get_material_layer_to_cobot_str(layer)
    str = str + CLOSE_TAG

    return str + CLOSE_TAG

# get message string for geometry_msgs/Pose
def _get_pose_str(pose_in):
    str = POSE_TAG 

    # Get position
    str = str + POSE_PX_TAG + str(pose_in.position.x) + CLOSE_TAG
    str = str + POSE_PY_TAG + str(pose_in.position.y) + CLOSE_TAG
    str = str + POSE_PZ_TAG + str(pose_in.position.z) + CLOSE_TAG

    # Get orientation
    str = str + POSE_OX_TAG + str(pose_in.orientation.x) + CLOSE_TAG
    str = str + POSE_OY_TAG + str(pose_in.orientation.y) + CLOSE_TAG
    str = str + POSE_OZ_TAG + str(pose_in.orientation.z) + CLOSE_TAG
    str = str + POSE_OW_TAG + str(pose_in.orientation.w) + CLOSE_TAG

    return str + CLOSE_TAG

# get message string for AssemblyMaterialLayer
def _get_material_layer_to_cobot_str(layer_in):
    str = MAT_LAYER_TAG 

    # uid of the layer: string uid   
    str = str + UID_TAG + layer_in.uid + CLOSE_TAG

    # Thickness of the layer:float32 thickness 
    str = str + LAYER_THICKNESS_TAG + str(layer_in.thickness) + CLOSE_TAG

    # Drill specifications during the drilling in this layer
    # Speed of the drill:float32 speed     
    str = str + DRILL_SPEED_TAG + str(layer_in.speed) + CLOSE_TAG  

    # Feed rate of the drill:float32 feed  
    str = str + DRILL_FEED_TAG + str(layer_in.feed) + CLOSE_TAG 

    # Lower limit(s) of the torque bandwidth(s):float32 lower_torque_limits  
    str = str + LOWER_TORQUE_LIMIT_TAG + str(layer_in.lower_torque_limits) + CLOSE_TAG

    # Upper limit(s) of the torque bandwidth(s):float32 upper_torque_limits  
    str = str + UPPER_TORQUE_LIMIT_TAG + str(layer_in.upper_torque_limits) + CLOSE_TAG  

    # Torque level/threshold to switch to the next layer in the stack: float32 threshold 
    str = str + TORQUE_THRESHOLD_TAG + str(layer_in.threshold) + CLOSE_TAG 

    # Temporary fastening specifications for this layer
    # Maximum temporary fastener clamp force:float32 max_clamp_force                 
    str = str + MAX_TEMPF_CLAMP_FORCE_TAG + str(layer_in.max_clamp_force) + CLOSE_TAG

    return str + CLOSE_TAG

# get message string for AssemblyWaypoint
def _get_waypoint_to_cobot_str(waypoint_in):
    str = WAYPOINT_TAG

    # uid: uid of the hole Waypoint
    str = str + UID_TAG + waypoint_in.uid + CLOSE_TAG

    # pos: location of the waypoint
    str = str + _get_pose_str(waypoint_in.pos)

    # bool: orient: whether or not the orientation is mandatory
    str = str + ORIENTATION_TAG + str(waypoint_in.orient) + CLOSE_TAG

    # float: blend_radius: Whether the cobot movement can cut a corner when
    # passing this waypoint.
    str = str + BLEND_RADIUS_TAG + str(waypoint_in.blend_radius) + CLOSE_TAG

    return str + CLOSE_TAG
    
# get message string for AssemblyAction
def _get_action_to_cobot_str(action_in):
    str = ACTIONS_TAG

    # string uid: uid of the hole Action
    str = str + UID_TAG + action_in.uid + CLOSE_TAG

    # string obj_uid: uid of the action object to execute
    str = str + OBJ_UID_TAG + action_in.obj_uid + CLOSE_TAG

    # string loc_uid: uid of the target location of the object
    str = str + LOC_UID_TAG + action_in.loc_uid + CLOSE_TAG
                                    
    # AssemblyActionState state: Status of the action (uint8)
    str = str + ACTION_STATE_TAG + str(action_in.state) + CLOSE_TAG

    # string[] passing: list of waypoints uids to pass
    # e.g. to pass between pick up and place of a temporary fastener
    # string loc_uid: uid of the target location of the object
    str = str + PASSING_UIDS_TAG 
    for passing in action_in.passing:
        str = str + PASSING_UID_TAG + action_in.passing + CLOSE_TAG
    str = str + CLOSE_TAG

    # uint8 speed: the speed as percentage of the maximum speed
    str = str + SPEED_TAG + str(action_in.speed) + CLOSE_TAG

    return str + CLOSE_TAG

# get message string for AssemblyDrillTask
def _get_drill_task_to_cobot_str(drill_task_in):
    str = DRILL_TASK_TAG

    #string ee_uid                           # uid of the end effector needed drill this hole
    str = str + UID_TAG + drill_task_in.uid + CLOSE_TAG

    #float32 diam                            # diameter of the drill
                                                # for reference only because real diameter defined by ee_uid
    str = str + DIAM_TAG + str(drill_task_in.diam) + CLOSE_TAG

    #geometry_msgs/Pose jig_pos              # Location of the drill jig drill guiding hole
                                                # Only available after drilling
    str = str + _get_pose_str(drill_task_in.jig_pos)

    #AssemblyMaterialLayer[] layers          # Material layers as encountered during drilling
                                                # Data filled during and_or after drilling
    str = str + LAYERS_TAG
    for layer in drill_task_in.layers:
        str = str + _get_material_layer_to_cobot_str(layer)
    str = str + CLOSE_TAG

    return str + CLOSE_TAG 

# get message string for AssemblyFastener
def _get_fastener_to_cobot_str(fastener_in):
    str = FASTENER_TAG

    #string uid                              # uid of the fastener
    str = str + UID_TAG + fastener_in.uid + CLOSE_TAG

    #string loc_uid                          # uid of the location of the fastener in one of the containers
    str = str + LOC_UID_TAG + fastener_in.loc_uid + CLOSE_TAG

    #string ee_uid                           # uid of the end effector needed to install this fastener
    str = str + END_EFFECTOR_UID_TAG + fastener_in.ee_uid + CLOSE_TAG

    #AssemblyFastState state                 # The state of the fastener
    str = str + FASTENER_STATE_TAG + str(fastener_in.state) + CLOSE_TAG

    #geometry_msgs/Pose inst_pos             # Installed location of the fastener
                                                # Only available after installation
    str = str + _get_pose_str(fastener_in.inst_pos)

    #float32 diam                            # diameter of the fastener
    str = str + DIAM_TAG + str(fastener_in.diam) + CLOSE_TAG

    #float32 shaft_height                    # the height of the shaft that is sticking out when in storage location
    str = str + SHAFT_HEIGHT_TAG + str(fastener_in.shaft_height) + CLOSE_TAG

    #float32 min_stack                       # the minimum stack
    str = str + MIN_STACK_TAG + str(fastener_in.min_stack) + CLOSE_TAG

    #float32 max_stack                       # the maximum stack
    str = str + MAX_STACK_TAG + str(fastener_in.max_stack) + CLOSE_TAG

    #float32 tcp_tip_distace                 # distance between hole entry point and tip if inserted in a hole
    str = str + TCP_TIP_DIST_TAG + str(fastener_in.tcp_tip_distace) + CLOSE_TAG

    #float32 tcp_top_distace                 # distance between hole entry point and top if inserted in a hole
                                                # the top is where the tcp is when engaging the tempf
    str = str + TCP_TOP_DIST_TAG + str(fastener_in.tcp_tip_distace) + CLOSE_TAG

    return str + CLOSE_TAG 

# get message string for AssemblyTempf
def _get_tempf_to_cobot_str(tempf_in):
    str = TEMPF_TAG

    #string uid                              # uid of the temporary fastener
    str = str + UID_TAG + tempf_in.uid + CLOSE_TAG

    #string loc_uid                          # uid of the location of the temporary fastener
    str = str + LOC_UID_TAG + tempf_in.loc_uid + CLOSE_TAG

    #string ee_uid                           # uid of the end effector needed to manipulate this temporary fastener
    str = str + END_EFFECTOR_UID_TAG + tempf_in.ee_uid + CLOSE_TAG

    #AssemblyFastState state                 # The state of the temporary fastener
    str = str + FASTENER_STATE_TAG + str(tempf_in.state) + CLOSE_TAG

    #geometry_msgs/Pose inst_pos             # Installed location of the temporary fastener
                                                # Only available after installation
    str = str + _get_pose_str(tempf_in.inst_pos)

    #float32 diam                            # diameter of the temporary fastener
    str = str + DIAM_TAG + str(tempf_in.diam) + CLOSE_TAG

    #float32 shaft_height                    # the height of the shaft that is sticking out when installed
    str = str + SHAFT_HEIGHT_TAG + str(tempf_in.shaft_height) + CLOSE_TAG

    #float32 min_stack                       # the minimum stack
    str = str + MIN_STACK_TAG + str(tempf_in.min_stack) + CLOSE_TAG

    #float32 max_stack                       # the maximum stack
    str = str + MAX_STACK_TAG + str(tempf_in.max_stack) + CLOSE_TAG

    #float32 tcp_tip_distace                 # distance between hole entry point and tip if inserted in a hole 
    str = str + TCP_TIP_DIST_TAG + str(tempf_in.tcp_tip_distace) + CLOSE_TAG

    #float32 tcp_top_distace                 # distance between hole entry point and top if inserted in a hole
                                                # the top is where the tcp is when engaging the tempf 
    str = str + TCP_TOP_DIST_TAG + str(tempf_in.tcp_tip_distace) + CLOSE_TAG        

    return str + CLOSE_TAG 

# get message string for AssemblyEeDockingPos
def _get_docking_pos_to_cobot_str(docking_pos_in):
    str = DOCKING_POS_TAG

    #string uid                  # uid of the Docking Position
    str = str + UID_TAG + docking_pos_in.uid + CLOSE_TAG

    #geometry_msgs/Pose pos      # location of the Docking Position
    str = str + _get_pose_str(docking_pos_in.pos)

    return str + CLOSE_TAG 
    
# get message string for End Effector
def _get_end_effector_to_cobot_str(ee_in):
    str = END_EFFECTOR_TAG

    #string uid                      # uid of the End Effector
    str = str + UID_TAG + ee_in.uid + CLOSE_TAG

    #string loc_uid                  # uid of the location of the End Effector in one of
                                        # possible docking positions
    str = str + LOC_UID_TAG + ee_in.loc_uid + CLOSE_TAG

    str = str + DOCKING_POSS_TAG
    #string[] poss_dock_pos_uids     # list of possible docking position uid's
    for poss_docking_pos_uid in ee_in.poss_dock_pos_uids:
        str = str + DOCKING_POS_TAG + poss_docking_pos_uid + CLOSE_TAG
    str = str + CLOSE_TAG

    #AssemblyEeState state           # The state of the End Effector
    #uint8 STORED = 1, uint8 ON_COBOT = 2, uint8 STORED_NEED_SERVICE = 3
    str = str + END_EFFECTOR_STATE_TAG + str(ee_in.state) + CLOSE_TAG

    return str + CLOSE_TAG  