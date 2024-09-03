# -*- coding: utf-8 -*-
"""
Created on Thu Feb 29 11:49:37 2024
@author: Bram and Jan Baan
Last update: ....2023
As a reminder:
a = rotation about z-axis
b = rotation about rotated y-axis
c = rotation about rotated z-axis
"""
 
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# """STANDIN FUNCTIONS: DO NOT USE"""
 
# DR_BASE = ""
# DR_USER_NOM = ""
# DR_USER_PROBE = ""
# DR_TOOL = ""
# DR_USER_NOM_OPP = ""
# DR_AXIS_Z = ""
# DR_SSTOP = ""
# DR_MV_MOD_ABS = ""
 
# DR_PM_WARNING = 1
# DR_PM_MESSAGE =1

# s1 = ""
# str1 = ""
 
# def set_velx(): pass
# def set_accx(): pass
# def get_current_posx(): pass
# def get_tool_force(): pass
# def get_distance(): pass
# def transpose(): pass
# def eul2rotm(): pass
# def coord_transform(): pass
# def posx(): pass
# def change_operation_speed(): pass
# def movel(): pass
# def amovel(): pass
# def amove_spiral(): pass
# def amove_periodic(): pass
# def wait(): pass
# def set_ref_coord(): pass
# def task_compliance_ctrl(): pass
# def set_desired_force(): pass
# def release_force(): pass
# def release_compliance_ctrl(): pass
# def get_digital_input(): pass
# def set_digital_output(): pass
# def tp_popup(): pass
# def tp_log(): pass
# def set_tcp(): pass
# def overwrite_user_cart_coord(): pass
# def check_motion(): pass
# def stop(): pass
# def rotm2eul(): pass
# def set_user_cart_coord(): pass
# def set_digital_outputs(): pass
# def set_tool_digital_output(): pass
# def set_tool_digital_outputs() : pass
# def server_socket_open() : pass
# def server_socket_close() : pass
# def server_socket_read(): pass
# def thread_run(): pass
# def get_current_posj(): pass
 
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
 
# Some global variables
from math import acos
from math import sqrt
from datetime import datetime
import time
import math
import os
import queue
import re
import socket
 
Pi = math.pi
start_time = time.time()
 
BYTES_MSG_LENGTH  = 4

DEFAULT_ENCODER = "UTF-8"

TCP_SPEED_LIMIT = 250
TCP_ROT_LIMIT = 120
JOINT_SPEED_LIMIT = [90, 90, 135, 150, 150, 150]
 
# Standard gaps used to prevent collision during movements
SAFE_Z_GAP = 5
GLOBAL_CLEARANCE_DURING_MOVEMENTS = 65 #Max TCP TOP DIST or any other object + delta 60 + 20
 
 
# The default accuracy with which the fastener location is initially known
# This also defines the radius of the spiral move
TEMPF_DEFAULT_POSITIONAL_DEVIATION = 5.0
# The default accuracy with which the fastener direction is initially known in degrees
TEMPF_DEFAULT_ORIENTATION_DEVIATION = 5.0
# The threshold a fastener is considered well defined, so no additional hole searchin needs to be done
XY_POS_THRESHOLD = 0.2
Z_POS_THRESHOLD = 0.2
Z_ANGLE_THRESHOLD = 0.2
# angle in radians at which two fasteners must minimally be with respect to the fastener to be corrected
# fasteners must be somewhat on opposite sides to the fastener to be corrected
GET_WEIGHTED_AVERAGES_MIN_ANGLE = 2.0
 
 
# Maximum stiffness for the best accuracy during probing tempf in probe()
PROBE_COMPLIANCE = [3000, 3000, 3000, 400, 400, 400]
# Speed at which to exit the hole to start the probing for the surface orientation
PROBE_HOLE_AXIS_SYSTEM_HOLE_EXIT_SPEED = 45
# Set the force. The force should be in range of 10-20N -
# small enough not to bend the material but high enough to reach surface in shortest time
PROBE_COMPLIANCE_FORCE = 20.0
 
#General move settings
MOVE_SPEED = 100
MOVE_COMPLIANCE = [3000, 3000, 3000, 400, 400, 400]
 
#Pick up
PICK_UP_ENGAGEMENT_SPEED = 60
PICK_UP_ENGAGEMENT_COMPLIANCE = [1500,1500,1500,400,400,400] #was 500,500,500,400,400,400
PICK_UP_FORCE = 40 # was 40
 
#Insertion
INSERTION_FORCE = 40 #FIND_HOLE_ENTRY_COMPLIANCE_FORCE = 40
INSERTION_COMPLIANCE = [500,500,500,300,300,300] #INSERT_IN_PROBED_HOLE_COMPLIANCE_AT_ENTRY = [500,500,500,300,300,300]
INSERTION_IN_CSK_SPEED = 35
 
#Installation
TIGHTENING_COMPLIANCE = [20, 20, 20, 20, 20, 20] #Not used atm
 
 
#Retraction
HOLE_RETRACTION_SPEED = 45
RETRACT_FROM_HOLE_COMPLIANCE = [20, 20, 20, 100, 100, 100]
 
 
# TODO !!!! get proper bin location
BIN_POSITION = posx(500,0,500,0,0,0)
 
 
# types of actions by the action class
ACTION_TYPE_MOVE_WAYPOINT = "move_to_waypoint"  
ACTION_TYPE_INSTALL_PERMF = "install_permf" 
ACTION_TYPE_INSTALL_TEMPF = "install_tempf" 
ACTION_TYPE_REMOVE_TEMPF = "remove_fastener"   
 
TIGHTEN_PROGRAM = 2
UNTIGHTEN_PROGRAM = 1
BURST_PROGRAM = 1
 
#******************************************************************************
# ATTENTION setting this blend to large will cause errors
# The program cannot blend two movements if the blend is larger than half the distance
# In case of weird errors: try setting these radii to zero.
#
# Product or storage approach position MUST also be further away from the
# nearest fastener position than 3x the BLEND_RADIUS_LARGE
#******************************************************************************
BLEND_RADIUS_SMALL = 2
BLEND_RADIUS_LARGE = 10
 
TCP_NAME_DIAM_5_TIP = "Lisi_d5_tempf_tip"
TCP_NAME_LISI_TIP_NO_TEMPF = "Lisi_no_tempf"
 
#TODO verify values below
DIAM_5_SHAFT_HEIGHT = 60   # how much the tempf sticks out when installed
DIAM_5_MIN_STACK = 3
DIAM_5_MAX_STACK = 17
DIAM_5_TCP_TIP_DIST = 25   # distance between hole entry point and tip if inserted in a hole
DIAM_5_TCP_TOP_DIST = 21   # distance between hole entry point and top if inserted in a hole
                           # the top is where the fastener end effector is when engaged with the tempf
 
#Permanent fastening
TCP_NAME_PERM_HAND_TOOL = "permf_hand_tool"
 
TCP_NAME_DIAM_6_AND_GRIP_9_TIP = "EN6122_06_09_tip" # + dimension K & N = 24.33 + 4.06 = 28.39. Did not take in to account tolerances
DIAM_6_AND_GRIP_9_SHAFT_HEIGHT = 26.92 # X + J1 + N = 1.78 + 21.08 + 4.06 = 26.92
DIAM_6_AND_GRIP_9_MIN_STACK = 13.49 # Waar komt dit terug
DIAM_6_AND_GRIP_9_MAX_STACK = 15.11 # Waar komt dit terug
DIAM_6_AND_GRIP_9_TCP_TIP_DIST = 24.33  
DIAM_6_AND_GRIP_9_TCP_TOP_DIST = 4.06
 
TCP_NAME_DIAM_6_AND_GRIP_6_TIP = "EN6122_06_06_tip"
DIAM_6_AND_GRIP_6_SHAFT_HEIGHT = 26.92  # X + J1 + N = 1.78 + 21.08 + 4.06  =   26.92
DIAM_6_AND_GRIP_6_MIN_STACK =  8.74
DIAM_6_AND_GRIP_6_MAX_STACK =  10.34
DIAM_6_AND_GRIP_6_TCP_TIP_DIST = 19.58   
DIAM_6_AND_GRIP_6_TCP_TOP_DIST = 4.06
 
 
 
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# varaibles for cobot - server messaging
# Thy must be similar to the ones used in the server
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
 
OPEN_TAG = "<"
CLOSE_TAG = ">"
PROVIDE_STATUS_MSG = OPEN_TAG + "PROVIDE_STATUS" + CLOSE_TAG
UID_TAG = "uid" + OPEN_TAG
TEMPF_STORAGE_LOC_TAG = "tempf_storage_loc" + OPEN_TAG
PERMF_STORAGE_LOC_TAG = "permf_storage_loc" + OPEN_TAG
PRODUCT_TAG = "product" + OPEN_TAG
LOCATIONS_TAG = "locations" + OPEN_TAG
LOC_UID_TAG = "loc_uid" + OPEN_TAG
MAX_OBST_HEIGHT_TAG = "max_obstacle_height" + OPEN_TAG
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
ACTIONS_TAG = "actions" + OPEN_TAG
ACTION_TAG = "action" + OPEN_TAG
A_TYPE_TAG = "action_type" + OPEN_TAG
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
FAST_END_EFFECTOR_UID = "fast_end_effector"
TEMPF_END_EFFECTOR_UID = "tempf_end_effector"
EXECUTE_TAG = "execute" + OPEN_TAG


# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# error classes and enumerators for the TCP-IP connection
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$


class MessageTypeError(Exception):
    """Raised if the message is not of type TCPMessage or TCPResponse."""

    def __init__(self):
        message = ("The message is not of type TCPMessage or TCPResponse!")
        super().__init__(message)


class TargetPoseSizeError(Exception):
    """Raised if the size of the new target pose is not equal to 6."""

    def __init__(self):
        message = ("The new target pose is not of the correct size!")
        super().__init__(message)

class TargetSizeError(Exception):
    """Raised if the size of the new target is not equal to 6."""

    def __init__(self):
        message = ("The new target is not of the correct size!")
        super().__init__(message)


class WorkflowParameterInputError(Exception):
    """Raised if the workflow parameter is set to an unknown value."""

    def __init__(self):
        message = ("The new workflow parameter is not recognized!")
        super().__init__(message)


class StatusInputError(Exception):
    """Raised if the status is set to an unknown value."""

    def __init__(self):
        message = ("The new status is not recognized!")
        super().__init__(message)


class MessageNames:
    RESPOND = "respond"
    STOP = "stop"
    PAUSE = "pause"
    RESPONSE = "response"
    PROCESSED = "processed"


class StatusOptions:
    IDLE = "idle"
    MOVING = "moving"
    EVADING = "evading"
    STOPPED = "stopped"
    COMPLETED = "completed"


class WorkflowParameterOptions:
    STATIONARY = "stationary"
    MOVE = "move"
    REMOVE_TEMPORARY_FASTENER = "remove_temporary_fastener"

# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# classes for the TCP-IP connection
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$


class MessageUID:
    """Class to construct uids for messages.

	The class needs to be accessible in multiple parts of the code, hence the
	use of class variables.
	"""
    value = 0

    def __repr__(self):
        return "{0}".format(self.__class__.__name__)

    @classmethod
    def get_new_uid(cls):
        cls.value += 1
        return cls.value

    @classmethod
    def reset(cls):
        cls.value = 0


class TCPOutbox:
    messages = []

    def __repr__(self):
        return "{0}".format(self.__class__.__name__)

    @classmethod
    def reset(cls):
        cls.messages = []

    @classmethod
    def add_message(cls, message):
        if not isinstance(message, (TCPMessage, TCPResponse)):
            raise MessageTypeError
        # tp_popup("Message: {0} added to Outbox <{1}>".format(message.uid, message.message), DR_PM_MESSAGE)
        tp_log("Message: {0} added to Outbox <{1}>".format(message.uid, message.message))
        cls.messages.append(message)

    @classmethod
    def _get_first_message(cls):
        if cls.messages:
            return cls.messages[0]
        return None

    @classmethod
    def remove_message(cls, uid):
        cls.messages = [msg for msg in cls.messages if msg.uid != uid]

    @classmethod
    def get_message(cls):
        message = cls._get_first_message()
        if message:
            tp_log("Message: {0} collected from Outbox <{1}>".format(message.uid, message.message))
            cls.remove_message(message.uid)
        return message


class TCPInbox:
    messages = []
    responses = []

    def __repr__(self):
        return "{0}".format(self.__class__.__name__)

    @classmethod
    def reset(cls):
        cls.messages = []
        cls.responses = []

    @classmethod
    def add_message(cls, message):
        if not isinstance(message, (TCPMessage, TCPResponse)):
            raise MessageTypeError
        tp_log("Message: {0} added to Inbox <{1}>".format(message.uid, message.message))
        # tp_popup("Message: {0} added to Inbox <{1}>".format(message.uid, message.message), DR_PM_MESSAGE)

        if isinstance(message, TCPResponse):
            cls.responses.append(message)
        else:
            cls.messages.append(message)

    @classmethod
    def remove_message(cls, uid):
        cls.messages = [msg for msg in cls.messages if msg.uid != uid]
        cls.responses = [msg for msg in cls.responses if msg.uid != uid]
        tp_log("Message with uid: {0} is removed from Inbox".format(uid))

    @classmethod
    def get_response(cls, uid):
        tp_log("Getting response to message with uid: {0}".format(uid))
        response = next((msg for msg in cls.responses if msg.response_uid == uid), None)
        if response:
            cls.responses = [msg for msg in cls.responses if msg.uid != response.uid]
            tp_log("Response to message {0} found: {1}".format(uid, response.message))
        else:
            tp_log("No response found for message {0}".format(uid))
        return response

    @classmethod
    def _get_first_message(cls):
        if cls.messages:
            return cls.messages[0]
        return None

    @classmethod
    def get_message(cls):
        message = cls._get_first_message()
        if message:
            tp_log("Message: {0} collected from Inbox <{1}>".format(message.uid, message.message))
            cls.remove_message(message.uid)
        return message


class TCPMessage:
    def __repr__(self):
        return "{0} (uid: {1}, message: {2})".format(
            self.__class__.__name__,
            self.uid,
            self.message,
        )

    def __init__(self, message, uid, encoder=DEFAULT_ENCODER, response_required=True):
        self.uid = uid
        self.message = message
        self.encoder = encoder
        self.response_required = response_required
        self.encoded = self.construct_encoded_tcp_message()


    def construct_encoded_tcp_message(self):
        expanded_message = "/{0}/{1}<{2}:{3}>".format(
                self.uid, self.message, MessageNames.RESPOND, self.response_required)
        expanded_message = "{0:0>4d}{1}".format(len(expanded_message) + 4, expanded_message)
        return expanded_message.encode(self.encoder)


class TCPResponse(TCPMessage):
    def __init__(self, uid, response_uid, response="processed", encoder=DEFAULT_ENCODER, response_required=False):
        self.response_uid = response_uid
        message = "{0}_{1}".format(MessageNames.RESPONSE, self.response_uid)
        super().__init__(uid=uid, message=message, input_data=response, encoder=encoder,
                         response_required=response_required)


class TCPInputProcessor:
    def __repr__(self):
        return "{0}".format(self.__class__.__name__)

    def __init__(self, encoder=DEFAULT_ENCODER):
        self.encoder = encoder
        self.raw_input = "".encode(self.encoder)

    def set_raw_input(self, raw_input):
        self.raw_input = raw_input

    def update_raw_input(self, reading_input):
        # print("The raw input is updated using: {0}".format(reading_input))
        self.raw_input += reading_input

    # print("The current raw input is: {0}".format(self.raw_input))

    def process_raw_input(self):
        tp_log("processing the raw input: {0}".format(self.raw_input))
        # tp_popup("processing the raw input: {0}".format(self.raw_input), DR_PM_MESSAGE)
        byte_size_length = 4
        if len(self.raw_input) > byte_size_length:
            byte_size = int(self.raw_input[:byte_size_length].decode(self.encoder))
            if len(self.raw_input) >= byte_size:
                isolated_message = self.raw_input[:byte_size].decode(self.encoder)
                tp_popup("Raw data: {0}".format(isolated_message), DR_PM_MESSAGE)
                tcp_message = self.reconstruct_tcp_message(isolated_message)
                TCPInbox().add_message(tcp_message)
                self.set_raw_input(self.raw_input[byte_size:])
                self.process_raw_input()

    def reconstruct_tcp_message(self, raw_tcp_message):
        tp_log("reconstructing the raw tcp input: {0}".format(raw_tcp_message))
        # determine size of preamble
        byte_size, uid = raw_tcp_message.split("/")[:2]
        preamble_size = len(byte_size) + len(uid) + 2
        raw_message = raw_tcp_message[preamble_size:]

        # remove the <respond: > section from the raw message
        raw_respond = raw_message.split("<{0}:".format(MessageNames.RESPOND))[-1].split(">")[0].lower()
        respond = raw_respond == "true"
        message_end = len(raw_message) - (len(MessageNames.RESPOND) + 3 + len(raw_respond))
        message = raw_message[:message_end]
        tp_popup("TCP_Message message: {0}, uid: {1}".format(message, uid), DR_PM_MESSAGE)
        return TCPMessage(
                message=message,
                uid=uid,
                encoder=self.encoder,
                response_required=respond,
            )

class DoosanTCPServer:
    def __init__(self, port, encoder=DEFAULT_ENCODER):
        self.port = port
        self.encoder = encoder
        self.socket = server_socket_open(self.port)
        self.input_processor = TCPInputProcessor(self.encoder)

    def _send_message(self, message):
        try:
            self.socket.sendall(message.encoded)
            tp_log("Message {0} send <{1}>".format(message.uid, message.message))
            #tp_popup(" Message: {0} has been send - message: {1}".format(message.uid, message.message), DR_PM_MESSAGE)
            return 0
        except ConnectionResetError:
            self._reconnect()
            self._send_message(message)

    def _send_messages(self):
        #tp_log("sending messages")
        continue_sending = True
        while continue_sending:
            message = TCPOutbox().get_message()
            if message:
                self._send_message(message)
            else:
                continue_sending = False

    def _reconnect(self):
        tp_popup("Reconnecting", DR_PM_MESSAGE)
        try:
            server_socket_close(self.socket)
        except:
            pass
        self.socket = server_socket_open(self.port)
        wait(0.005)

    def _listen(self):
        #tp_log("started listening")
        response, raw_input = server_socket_read(self.socket, timeout=0.01)
        if response in [-1, -2]:
            self._reconnect()
            self._listen()
        elif response > 0:
            tp_popup("Listening - raw input is being updated: {0}".format(raw_input), DR_PM_MESSAGE)
            self.input_processor.update_raw_input(raw_input)
            self.input_processor.process_raw_input()
        elif response == -3:
            return 0
        else:
            return 0
        return 0

    def run(self):
        global STOP_SERVER

        tp_log("Server running")
        while not STOP_SERVER:
            self._listen()
            self._send_messages()
        tp_popup("Stopped running server", DR_PM_MESSAGE)
        return 0


# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# functions for TCP-IP communication
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$


def construct_tcp_message(message, encoder=DEFAULT_ENCODER, response_required=False):
	return TCPMessage(
		message=message,
		uid=MessageUID.get_new_uid(),
		encoder=encoder,
		response_required=response_required,
		)


def construct_tcp_response(response_uid, response="processed", encoder=DEFAULT_ENCODER, response_required=False):
	return TCPResponse(
		uid=MessageUID.get_new_uid(),
		response_uid=response_uid,
		response=response,
		encoder=encoder,
		response_required=response_required,
		)


def send_message(message, feedback=False):
	tcp_message = construct_tcp_message(message=message, response_required=feedback)
	TCPOutbox().add_message(tcp_message)
	if feedback:
		response = False
		while not response:
			# check inbox response for uid
			response = TCPInbox.get_response(tcp_message.uid)
		return response
	return True


def send_response(original_message_uid, response="processed", feedback=False):
	tcp_response = construct_tcp_response(
		response_uid=original_message_uid,
		response=response,
		response_required=feedback,
	)
	TCPOutbox().add_message(tcp_response)
	if feedback:
		response = None
		while not response:
			# check inbox response for uid
			response = TCPInbox.get_response(tcp_response.uid)
		return response
	return True


# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# thread functions for TCP-IP communication
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$


def th_run_server():
    tcp_server = DoosanTCPServer(port=20002, encoder=DEFAULT_ENCODER)
    tcp_server.run()


# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# functions to build string messages to be sent to the server
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
 
def tempf_storage_str_to_server(storage_in):
    """
    Function to send the tempf storage location container to the server
 
    :param storage_in: cl_fl_container with loc: cl_fastener_location and tempf: cl_fastener,
    """ 
    str_out = TEMPF_STORAGE_LOC_TAG + _get_hole_location_container_to_server_str(storage_in) + CLOSE_TAG
 
    return str_out
 
def permf_storage_str_to_server(storage_in):
    """
    Function to send the permf storage location container to the server
 
    :param storage_in: cl_fl_container with loc: cl_fastener_location and permf: cl_fastener,
    """ 
    str_out = PERMF_STORAGE_LOC_TAG + _get_hole_location_container_to_server_str(storage_in) + CLOSE_TAG
 
    return str_out
 
def products_str_to_server(product_in):
    """
    Function to send a product container with holes to the server
 
    :param product_in: cl_fl_container
    """ 
    str_out = PRODUCT_TAG + _get_hole_location_container_to_server_str(product_in) + CLOSE_TAG
 
    return str_out
 
 
def waypoints_str_to_server(waypoints_in):
    """
    Function to send list of defined waypoints to the server
 
    :param waypoints_in: list of cl_waypoint
    """
    str_out = WAYPOINTS_TAG
 
    for waypoint in waypoints_in:
        str_out = str_out + _get_waypoint_to_server_str(waypoint)
 
    str_out = str_out + CLOSE_TAG
 
    return str_out
 
def actions_str_to_server(actions_in):
    """
    Function to send list of defined actions to the server
 
    :param actions_in: list of cl_action
    """
    str_out = ACTIONS_TAG
 
    for action in actions_in:
        str_out = str_out + _get_action_to_server_str(action)
 
    str_out = str_out + CLOSE_TAG
 
    return str_out
 
def drill_tasks_str_to_server(drill_tasks_in):
    """
    Function to send list of holes to be drilled to the server
 
    :param drill_tasks_in: list of cl_action
    """
    # str_out = DRILL_TASKS_TAG
 
    # for drill_task in drill_tasks_in:
    #     str_out = str_out + _get_drill_task_to_server_str(drill_task)
 
    # str_out = str_out + CLOSE_TAG
 
    # return str_out
    return ""
 
def fasteners_str_to_server(fl_container_lst_in): 
    """
    Function to send list of available fasteners to the server
 
    :param fasteners_in: list of cl_fl_container
    """
    str_out = FASTENERS_TAG
 
    for fl_container in fl_container_lst_in:
        str_out = str_out + _get_fastener_to_server_str(fl_container.fast, fl_container.loc.uid)
 
    str_out = str_out + CLOSE_TAG
 
    return str_out
 
def tempfs_str_to_server(fl_container_lst_in):
    """
    Function to send list of available fasteners to the server
 
    :param tempfs_in: list of cl_fl_container
    """
    str_out = TEMPFS_TAG
 
    for fl_container in fl_container_lst_in:
        str_out = str_out + _get_fastener_to_server_str(fl_container.fast, fl_container.loc.uid)
 
    str_out = str_out + CLOSE_TAG
 
    return str_out
 
def docking_pos_str_to_server(docking_pos_in):
    """
    Function to send list of available docking positions for End Effectors to the server
   
    TODO define docking positions for end effectors
    :param docking_pos_in: list of cl_TBD
    """
    # str_out = DOCKING_POSS_TAG
 
    # for docking_pos in docking_pos_in:
    #     str_out = str_out + _get_docking_pos_to_server_str(docking_pos)
 
    # str_out = str_out + CLOSE_TAG
 
    # return str_out
    return ""
    
def ee_str_to_server(ee_in):
    """
    Function to send list of available End Effectors to the server
 
    :param ee_in: list of cl_temp_fast_ee
    """
    # str_out = END_EFFECTORS_TAG
 
    # for ee in ee_in:
    #     str_out = str_out + _get_end_effector_to_server_str(ee)
 
    # str_out = str_out + CLOSE_TAG
 
    # return str_out
    return ""
 
def _get_hole_location_container_to_server_str(cont_in):
    """
    Function to send list of available End Effectors to the server
 
    :param cont_in: cl_f_container
    """
    # uid of the container
    str_out = UID_TAG + cont_in.uid() + CLOSE_TAG
 
    # list of hole locations
    str_out = str_out + LOCATIONS_TAG
    for tl_container in cont_in.holes_and_fast_lst:
        str_out = str_out + _get_hole_location_to_server_str(tl_container.loc)
    str_out = str_out + CLOSE_TAG
 
    # max_obstacle_height
    str_out = str_out + MAX_OBST_HEIGHT_TAG + str(cont_in.max_obstacle_height) + CLOSE_TAG
 
    return str_out
 
 
def _get_hole_location_to_server_str(loc_in):
    """
    Function to send a hole loaction to the server
 
    :param loc_in: cl_fastener_location
    """
    str_out = HOLE_LOCATION_TAG
    # uid of the hole position: string uid
    str_out = str_out + UID_TAG + loc_in.uid() + CLOSE_TAG                         
 
    # Nominal location of the hole: geometry_msgs/Pose nom_pos
    str_out = str_out + _get_pose_str(loc_in.nom_pos())            
 
    # Diameter of the hole: float32 diam
    str_out = str_out + DIAM_TAG + str(loc_in.diam()) + CLOSE_TAG                
 
    # Total thickness at the hole
    # Must be equal to the sum of layer thicknesses: float32 stack_t
    str_out = str_out + STACK_T_TAG + str(loc_in.stack_thickness()) + CLOSE_TAG       
 
    # distance of the drill jig hole entry above the surface: float32 drill_jig_dist                 
    str_out = str_out + DRILL_JIG_DIST_TAG + str(loc_in.drill_jig_dist()) + CLOSE_TAG
 
    # Whether or not the hole has been drilled: bool drilled
    str_out = str_out + DRILLED_TAG + str(loc_in.is_drilled()) + CLOSE_TAG            
 
    # Material definition for each layer: AssemblyMaterialLayer[] layers
    #TODO add layers to the hole location
    #str_out = str_out + LAYERS_TAG
    #for layer in loc_in.layers:
    #    str_out = str_out + _get_material_layer_to_server_str(layer)
    #str_out = str_out + CLOSE_TAG
 
    return str_out + CLOSE_TAG
 
 
def _get_pose_str(pose_in):
    """
    Function to send a posx to the server
 
    :param pose_in: posx (pose_in is in Doosan format)
    """
    if pose_in is not None:
        str_out = POSE_TAG
    
        # Get position
        str_out = str_out + POSE_PX_TAG + str(pose_in[0]) + CLOSE_TAG
        str_out = str_out + POSE_PY_TAG + str(pose_in[1]) + CLOSE_TAG
        str_out = str_out + POSE_PZ_TAG + str(pose_in[2]) + CLOSE_TAG
    
        # Get orientation
        str_out = str_out + POSE_OX_TAG + str(pose_in[3]) + CLOSE_TAG
        str_out = str_out + POSE_OY_TAG + str(pose_in[4]) + CLOSE_TAG
        str_out = str_out + POSE_OZ_TAG + str(pose_in[5]) + CLOSE_TAG
    
        return str_out + CLOSE_TAG

    return ""
    
 
 
def _get_material_layer_to_server_str(layer_in):
    """
    Function to send a layer to the server
    layers not implemented yet
 
    :param pose_in: posx (pose_in is in Doosan format)
    """
    # str_out = MAT_LAYER_TAG
 
    # # uid of the layer: string uid  
    # str_out = str_out + UID_TAG + layer_in.uid() + CLOSE_TAG
 
    # # Thickness of the layer:float32 thickness
    # str_out = str_out + LAYER_THICKNESS_TAG + str(layer_in.thickness) + CLOSE_TAG
 
    # # Drill specifications during the drilling in this layer
    # # Speed of the drill:float32 speed    
    # str_out = str_out + DRILL_SPEED_TAG + str(layer_in.speed) + CLOSE_TAG 
 
    # # Feed rate of the drill:float32 feed 
    # str_out = str_out + DRILL_FEED_TAG + str(layer_in.feed) + CLOSE_TAG
 
    # # Lower limit(s) of the torque bandwidth(s):float32 lower_torque_limits 
    # str_out = str_out + LOWER_TORQUE_LIMIT_TAG + str(layer_in.lower_torque_limits) + CLOSE_TAG
 
    # # Upper limit(s) of the torque bandwidth(s):float32 upper_torque_limits 
    # str_out = str_out + UPPER_TORQUE_LIMIT_TAG + str(layer_in.upper_torque_limits) + CLOSE_TAG 
 
    # # Torque level/threshold to switch to the next layer in the stack: float32 threshold
    # str_out = str_out + TORQUE_THRESHOLD_TAG + str(layer_in.threshold) + CLOSE_TAG
 
    # # Temporary fastening specifications for this layer
    # # Maximum fastener clamp force:float32 max_clamp_force                
    # str_out = str_out + MAX_TEMPF_CLAMP_FORCE_TAG + str(layer_in.max_clamp_force) + CLOSE_TAG
 
    # return str_out + CLOSE_TAG
    return ""

 
# get message string for AssemblyWaypoint
def _get_waypoint_to_server_str(waypoint_in):
    """
    Function to send a waypoint to the server
 
    :param waypoint_in: cl_waypoint
    """
    str_out = WAYPOINT_TAG
 
    # uid: uid of the hole Waypoint
    str_out = str_out + UID_TAG + waypoint_in.uid() + CLOSE_TAG
 
    # pos: location of the waypoint
    str_out = str_out + _get_pose_str(waypoint_in.pos())
 
    return str_out + CLOSE_TAG
   
 
def _get_action_to_server_str(action_in):
    """
    Function to send an action to the server
 
    :param action_in: cl_action
    """
    is_done = action_in.is_done()
    is_cancelled = action_in.is_cancelled()
    is_waiting = action_in.is_waiting()

    str_out = ACTIONS_TAG
 
    # string uid: uid of the hole Action
    str_out = str_out + UID_TAG + action_in.uid() + CLOSE_TAG
 
    # string a_type: type of the action object to create
    # ACTION_TYPE_MOVE_WAYPOINT = "move_to_waypoint"  
    # ACTION_TYPE_INSTALL_PERMF = "install_permf" 
    # ACTION_TYPE_INSTALL_TEMPF = "install_tempf" 
    # ACTION_TYPE_REMOVE_TEMPF = "remove_fastener" 
    str_out = str_out + A_TYPE_TAG + action_in.a_type() + CLOSE_TAG
 
    # string loc_uid: uid of the target location of the object
    str_out = str_out + LOC_UID_TAG + action_in.loc_uid() + CLOSE_TAG

    # AssemblyActionState state: Status of the action (uint8)
    # ACCEPTED = 2
    # IN_PROGRESS = 3
    # PAUSED_WAITING = 4
    # WAITING_FOR_OPERATOR_ACTION = 5
    # SUCCESS = 6
    # CANCELLED = 7
    if is_done:
        str_out = str_out + ACTION_STATE_TAG + "6" + CLOSE_TAG
    elif is_cancelled:
        str_out = str_out + ACTION_STATE_TAG + "7" + CLOSE_TAG
    elif is_waiting:
        str_out = str_out + ACTION_STATE_TAG + "4" + CLOSE_TAG
    else:
        str_out = str_out + ACTION_STATE_TAG + "2" + CLOSE_TAG
 
    # uint8 speed: the speed as percentage of the maximum speed
    str_out = str_out + SPEED_TAG + str(action_in.speed()) + CLOSE_TAG
 
    # add the uids that are passed before and after the action
    str_out = str_out + PASSING_UIDS_TAG
    for passing_wp in action_in.passing_wps:
        str_out = str_out + PASSING_UID_TAG + passing_wp + CLOSE_TAG
   
    str_out = str_out + CLOSE_TAG
 
    return str_out + CLOSE_TAG

 
# get message string for AssemblyDrillTask
def _get_drill_task_to_server_str(drill_task_in):
    """
    Function to send a drill task to the server
    Drill tasks not implemented yet
 
    """
    # str_out = DRILL_TASK_TAG
 
    # #string ee_uid                           # uid of the end effector needed drill this hole
    # str_out = str_out + UID_TAG + drill_task_in.uid + CLOSE_TAG
 
    # #float32 diam                            # diameter of the drill
    #                                             # for reference only because real diameter defined by ee_uid
    # str_out = str_out + DIAM_TAG + str(drill_task_in.diam) + CLOSE_TAG
 
    # #geometry_msgs/Pose jig_pos              # Location of the drill jig drill guiding hole
    #                                             # Only available after drilling
    # str_out = str_out + _get_pose_str(drill_task_in.jig_pos)
 
    # #AssemblyMaterialLayer[] layers          # Material layers as encountered during drilling
    #                                             # Data filled during and_or after drilling
    # str_out = str_out + LAYERS_TAG
    # for layer in drill_task_in.layers:
    #     str_out = str_out + _get_material_layer_to_server_str(layer)
    # str_out = str_out + CLOSE_TAG
 
    # return str_out + CLOSE_TAG
    return ""

 
# get message string for AssemblyFastener
def _get_fastener_to_server_str(fastener_in, loc_uid_in):
    """
    Function to send a fastener to the server
   
    :param fastener_in: cl_fastener
    :param loc_uid_in:  str, the uid of the location where the object is
    """
   
    is_tempf = fastener_in.is_tempf()
 
    if is_tempf:
        str_out = TEMPF_TAG
    else:
        str_out = FASTENER_TAG
 
    #string uid                              # uid of the fastener
    str_out = str_out + UID_TAG + fastener_in.uid() + CLOSE_TAG
 
    #string loc_uid                          # uid of the location of the fastener in one of the containers
    if not loc_uid_in == "":
        str_out = str_out + LOC_UID_TAG + loc_uid_in + CLOSE_TAG
 
    #string ee_uid                           # uid of the end effector needed to manipulate this (temporary) fastener
    if is_tempf:
        str_out = str_out + END_EFFECTOR_UID_TAG + TEMPF_END_EFFECTOR_UID + CLOSE_TAG
    else:
        str_out = str_out + END_EFFECTOR_UID_TAG + FAST_END_EFFECTOR_UID + CLOSE_TAG
 
    #AssemblyFastState state                 # The state of the fastener
    # IN_STORAGE = 1
    # IN_EE = 2
    # IN_PRODUCT = 3
    # DISCARDED = 4
    if fastener_in.in_storage():
        str_out = str_out + FASTENER_STATE_TAG + "1" + CLOSE_TAG
    elif fastener_in.in_ee():
        str_out = str_out + FASTENER_STATE_TAG + "2" + CLOSE_TAG
    elif fastener_in.in_product():
        str_out = str_out + FASTENER_STATE_TAG + "3" + CLOSE_TAG
    elif fastener_in.in_bin():
        str_out = str_out + FASTENER_STATE_TAG + "4" + CLOSE_TAG
 
    #geometry_msgs/Pose inst_pos             # Installed location of the fastener
    # Only available after installation
    str_out = str_out + _get_pose_str(fastener_in.installed_pos())
 
    #float32 diam                            # diameter of the fastener
    str_out = str_out + DIAM_TAG + str(fastener_in.diam()) + CLOSE_TAG
 
    #float32 shaft_height                    # the height of the shaft that is sticking out when in storage location
    str_out = str_out + SHAFT_HEIGHT_TAG + str(fastener_in.shaft_height()) + CLOSE_TAG
 
    #float32 min_stack                       # the minimum stack
    str_out = str_out + MIN_STACK_TAG + str(fastener_in.min_stack()) + CLOSE_TAG
 
    #float32 max_stack                       # the maximum stack
    str_out = str_out + MAX_STACK_TAG + str(fastener_in.max_stack()) + CLOSE_TAG
 
    #float32 tcp_tip_distance                 # distance between hole entry point and tip if inserted in a hole
    str_out = str_out + TCP_TIP_DIST_TAG + str(fastener_in.tcp_tip_distance()) + CLOSE_TAG
 
    #float32 tcp_top_distance                 # distance between hole entry point and top if inserted in a hole
                                                # the top is where the tcp is when engaging the tempf
    str_out = str_out + TCP_TOP_DIST_TAG + str(fastener_in.tcp_tip_distance()) + CLOSE_TAG
 
    return str_out + CLOSE_TAG
 

# get message string for AssemblyEeDockingPos
def _get_docking_pos_to_server_str(docking_pos_in):
    """
    Function to send a fastener to the server
    Docking positions not implemented yet
   
    :param docking_pos_in:
    """
    # str_out = DOCKING_POS_TAG
 
    # #string uid                  # uid of the Docking Position
    # str_out = str_out + UID_TAG + docking_pos_in.uid + CLOSE_TAG
 
    # #geometry_msgs/Pose pos      # location of the Docking Position
    # str_out = str_out + _get_pose_str(docking_pos_in.pos)
 
    # return str_out + CLOSE_TAG
    return ""
   
 
def _get_end_effector_to_server_str(ee_in):
    """
    Function to send a end effector to the server
    Return message to server not implemented yet
   
    :param ee_in: cl_temp_fast_ee or cl_perm_fast_ee
    """
    # str_out = END_EFFECTOR_TAG
 
    # #string uid                      # uid of the End Effector
    # str_out = str_out + UID_TAG + ee_in.uid + CLOSE_TAG
 
    # #string loc_uid                  # uid of the location of the End Effector in one of
    #                                  # possible docking positions
    # str_out = str_out + LOC_UID_TAG + ee_in.loc_uid + CLOSE_TAG
 
    # str_out = str_out + DOCKING_POSS_TAG
    # #string[] poss_dock_pos_uids     # list of possible docking position uid's
    # for poss_docking_pos_uid in ee_in.poss_dock_pos_uids:
    #     str_out = str_out + DOCKING_POS_TAG + poss_docking_pos_uid + CLOSE_TAG
    # str_out = str_out + CLOSE_TAG
 
    # #AssemblyEeState state           # The state of the End Effector
    # #uint8 STORED = 1, uint8 ON_COBOT = 2, uint8 STORED_NEED_SERVICE = 3
    # str_out = str_out + END_EFFECTOR_STATE_TAG + str(ee_in.state) + CLOSE_TAG
 
    # return str_out + CLOSE_TAG
    return ""
 

# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# Functions to unpack a string
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
 
# function to get a substring from an original_string
# will return the string after the first search_string
# the substring is that part of the original_string after a search_string
def _find_substring(original_string, search_string):
 
    # Find the position of the search string
    position = original_string.find(search_string)
 
    if position != -1:
        # Extract the part of the string after the search string
        return original_string[position + len(search_string):]
    else:
        return None
 

# function to get the content of a leaf object between open_tag and close_tag
# Example usage:
#input_string = "tag1<tag2<content1>more<tag3<content3>>>tag4<content4>"
#tag1_content = extract_leaf_content(input_string, "tag2<", ">")
def extract_leaf_content(input_string, open_tag, close_tag):
    pattern = re.compile(r'{}(.*?)(?={})'.format(open_tag, close_tag), re.DOTALL)
    match = pattern.search(input_string)
 
    if match:
        return match.group(1)
    else:
        return None


def handle_ros_msg():
    """
    Function that modifies a cl_agent instance using a message string.
   
    :param msg_str: str, the string from the ROS server to modify the agent instance.
    :param agent: cl_agent, the agent instance to be modified.
    """

    global agent
    global STOP_SERVER

    while not STOP_SERVER:
        wait(0.01)
        message = TCPInbox.get_message()
        if message:
            
            msg_str = message.message
            msg_id = message.uid

            tp_popup("message being processed by handler: {0}".format(msg_str), DR_PM_MESSAGE)
            
            tp_popup("message being processed by handler: {0}".format(_find_substring(msg_str, EXECUTE_TAG)), DR_PM_MESSAGE)

            # tempf_storage: storage location container
            tempf_st_str = _find_substring(msg_str, TEMPF_STORAGE_LOC_TAG)
            if tempf_st_str is not None:
                handle_container_str(tempf_st_str, agent, TEMPF_STORAGE_LOC_TAG, msg_id)
        
            # permf_storage: storage location container
            permf_st_str = _find_substring(msg_str, PERMF_STORAGE_LOC_TAG)
            if permf_st_str is not None:
                handle_container_str(permf_st_str, agent, PERMF_STORAGE_LOC_TAG, msg_id)
        
            # product: storage location container
            pr_str = _find_substring(msg_str, PRODUCT_TAG)
            if pr_str is not None:
                handle_container_str(pr_str, agent, PRODUCT_TAG, msg_id)
        
            # waypoints
            wps_str = _find_substring(msg_str, WAYPOINTS_TAG)
            if wps_str is not None:
                wp_str = _find_substring(wps_str, WAYPOINT_TAG)
                while wp_str is not None:
                    handle_waypoint_str(wp_str, agent, msg_id)
                    wp_str = _find_substring(wp_str, WAYPOINT_TAG)
        
            # actions
            actions_str = _find_substring(msg_str, ACTIONS_TAG)
            if actions_str is not None:
                action_str = _find_substring(actions_str, ACTION_TAG)
                while action_str is not None:
                    handle_action_str(action_str, agent, msg_id)
                    action_str = _find_substring(action_str, ACTIONS_TAG)
        
            # holes to be drilled
            # NOT IMPLEMENTED YET
        
            # available fasteners
            pfs_str = _find_substring(msg_str, FASTENERS_TAG)
            pf_str = _find_substring(pfs_str, FASTENER_TAG)
            while pf_str is not None:
                handle_fastener_str(pf_str, agent, FASTENER_TAG, msg_id)
                pf_str = _find_substring(pf_str, FASTENER_TAG)
        
            # available fasteners
            tfs_str = _find_substring(msg_str, TEMPFS_TAG)
            tf_str = _find_substring(tfs_str, TEMPF_TAG)
            while tf_str is not None:
                handle_fastener_str(tf_str, agent, TEMPF_TAG, msg_id)
                tf_str = _find_substring(tf_str, TEMPF_TAG)
        
            # available docking positions for End Effectors
            # NOT IMPLEMENTED YET
        
            # available End Effectors
            # NOT IMPLEMENTED YET
        
            # actions: uid's to execute
            # execution actions are always single actions
            ex_str = _find_substring(msg_str, EXECUTE_TAG)
            if ex_str is not None:
                tp_popup("Message is recognized, action is to be defined: {0}".format(ex_str), DR_PM_MESSAGE)
                handle_execution_str(ex_str, agent, msg_id)
    
    
def handle_container_str(msg_str, agent, type, msg_id):
    """
    Function that modifies containers in an agent
    using a message string and adds a return to the queue_out

    :param msg_str: str, the string from the ROS server to modify the agent instance.
    :param agent: cl_agent, the agent instance to be modified.
    :param type: str The container type
                    temporary fastener container if TEMPF_STORAGE_LOC_TAG
                    permanent fastener container if PERMF_STORAGE_LOC_TAG
                    product container if PRODUCT_TAG
    :param msg_id: str Unique reference to original message
    """
    # create the container object
    uid = extract_leaf_content(msg_str, UID_TAG, CLOSE_TAG)
    max_obstacle_heigth = float(extract_leaf_content(msg_str, MAX_OBST_HEIGHT_TAG, CLOSE_TAG))
    obj = cl_f_container(uid, max_obstacle_heigth)

    if type == TEMPF_STORAGE_LOC_TAG:
        agent.tempf_storage = obj
    elif type == PERMF_STORAGE_LOC_TAG:
        agent.permf_storage = obj
    elif type == PRODUCT_TAG:
        agent.product = obj
    else:
        raise Exception("Unknown storage type encountered in handle_container_str in container with uid {}.".format(uid))

    # add the locations
    locs_str = _find_substring(msg_str, LOCATIONS_TAG)
    loc_str = _find_substring(locs_str, HOLE_LOCATION_TAG)
    while loc_str is not None:
        loc_uid = extract_leaf_content(loc_str, UID_TAG, CLOSE_TAG)
        diam = float(extract_leaf_content(loc_str, DIAM_TAG, CLOSE_TAG))         
        stack_thickness = float(extract_leaf_content(loc_str, STACK_T_TAG, CLOSE_TAG))
        nom_pos = _get_posx_from_str(_find_substring(loc_str, POSE_TAG))
    
        obj.add_loc_to_holes_and_fast_lst(loc_uid, diam, stack_thickness, nom_pos)

        loc_str = _find_substring(loc_str, HOLE_LOCATION_TAG)

    return_str = "container {} received by cobot".format(uid)

    send_response(msg_id, return_str)
 
 
def handle_waypoint_str(msg_str, agent, msg_id):
    """
    Function that modifies waypoints in an agent
    using a message string and adds a return to the queue_out
   
    :param msg_str: str, the string from the ROS server to modify the agent instance.
    :param agent: cl_agent, the agent instance to be modified.
    :param msg_id: str Unique reference to original message
    """
    # get the waypoint inputs from the string
    uid = extract_leaf_content(msg_str, UID_TAG, CLOSE_TAG)
    wp_pos = _get_posx_from_str(_find_substring(msg_str, POSE_TAG))
 
    # add the waypoint
    agent._add_waypoint(uid, wp_pos)
 
    send_response(msg_id, "waypoint {} received by cobot".format(uid))
   
 
def handle_action_str(msg_str, agent, msg_id):
    """
    Function that modifies actions in an agent
    using a message string and adds a return to the queue_out
   
    Supported types (a_type)
    if a_type == 1: ACTION_TYPE_MOVE_WAYPOINT = "move_to_waypoint"  
    if a_type == 2: ACTION_TYPE_INSTALL_PERMF = "install_permf" 
    if a_type == 3: ACTION_TYPE_INSTALL_TEMPF = "install_tempf" 
    if a_type == 4: ACTION_TYPE_REMOVE_TEMPF = "remove_fastener" 
    
    :param msg_str: str, the string from the ROS server to modify the agent instance.
    :param agent: cl_agent, the agent instance to be modified.
    :param msg_id: str Unique reference to original message
    """
    a_type = int(extract_leaf_content(msg_str, A_TYPE_TAG, CLOSE_TAG))
    a_uid = extract_leaf_content(msg_str, UID_TAG, CLOSE_TAG)
    a_loc_uid = extract_leaf_content(msg_str, LOC_UID_TAG, CLOSE_TAG)
   
    # uint8 RECEIVED = 1
    # uint8 ACCEPTED = 2
    # uint8 IN_PROGRESS = 3
    # uint8 PAUSED_WAITING = 4
    # uint8 WAITING_FOR_OPERATOR_ACTION = 5
    # uint8 SUCCESS = 6
    # uint8 CANCELLED = 7
    a_state = int(extract_leaf_content(msg_str, ACTION_STATE_TAG, CLOSE_TAG))
   
    a_is_cancelled = False
    a_is_waiting = False
 
    if a_state < 6:
        a_is_done = False
    elif a_state == 6:
        a_is_done = True
    elif a_state == 4:
        a_is_waiting = True
    elif a_state == 7:
        a_is_cancelled = True
    else:
        raise Exception("Unknown state encountered in handle_action_str in action with uid {}.".format(a_uid))
   
    a_speed = float(extract_leaf_content(msg_str, SPEED_TAG, CLOSE_TAG))
 
    if a_type == 1:
        agent._add_move_to_waypoint_action(a_uid, a_loc_uid, a_is_done, a_speed)  
    if a_type == 2:
        agent._add_install_permf_action(a_uid, a_loc_uid, a_is_done, a_speed)
    if a_type == 3:
        agent._add_install_tempf_action(a_uid, a_loc_uid, a_is_done, a_speed)
    if a_type == 4:
        agent._add_remove_tempf_action(a_uid, a_loc_uid, a_is_done, a_speed)
 
    if a_is_cancelled:
        action = agent._get_from_lst_by_uid(agent.actions, a_uid, "", False)
        action.set_as_cancelled()
 
    if a_is_waiting:
        action = agent._get_from_lst_by_uid(agent.actions, a_uid, "", False)
        action.set_as_waiting()
 
    passing_lst = []
    passing_str = _find_substring(msg_str, PASSING_UIDS_TAG)
    while passing_str is not None:
        passing_lst.append(extract_leaf_content(passing_str, PASSING_UID_TAG, CLOSE_TAG))
       
        # check if there is another string after an ACTION_TAG
        passing_str = _find_substring(msg_str, PASSING_UIDS_TAG)
 
    # set the passing waypoints
    action.passing_wps = passing_lst
 
    return_str = actions_str_to_server(agent.actions)
 
    send_response(msg_id, return_str)
 
   
def handle_fastener_str(msg_str, agent, f_tag, msg_id):
    """
    Function that modifies fastener information of an agent
    using a message string and adds a return to the queue_out
   
    :param msg_str: str, the string from the ROS server to modify the agent instance.
    :param agent: cl_agent, the agent instance to be modified.
    :param f_tag: str, FASTENER_TAG or TEMPF_TAG
    :param msg_id: str Unique reference to original message
    """
    obj = cl_f_container()
 
    f_uid = extract_leaf_content(msg_str, UID_TAG, CLOSE_TAG)
 
    if f_tag == TEMPF_TAG:
        obj = agent.tempf_storage
        is_tempf = True
    elif f_tag == FASTENER_TAG:
        obj = agent.permf_storage
        is_tempf = False
    else:
        raise Exception("Unknown fastener type encountered in handle_fastener_str in container with uid {}.".format(f_uid))
   
    f_loc_uid = extract_leaf_content(msg_str, LOC_UID_TAG, CLOSE_TAG)
    # f_ee_uid not implemeneted yet, but can be retreived with END_EFFECTOR_UID_TAG
    f_state = int(extract_leaf_content(msg_str, FASTENER_STATE_TAG, CLOSE_TAG))
 
    f_in_storage = False
    f_in_ee = False
    f_in_product=False
    f_in_bin=False
 
    if f_state == 1:
        f_in_storage = True
    elif f_state == 2:
        f_in_ee = True
    elif f_state == 3:
        f_in_product=True
    elif f_state == 4:
        f_in_bin=True
 
    f_diam = float(extract_leaf_content(msg_str, DIAM_TAG, CLOSE_TAG))
    f_shaft_height = float(extract_leaf_content(msg_str, SHAFT_HEIGHT_TAG, CLOSE_TAG))
    f_min_stack = float(extract_leaf_content(msg_str, MIN_STACK_TAG, CLOSE_TAG))
    f_max_stack = float(extract_leaf_content(msg_str, MAX_STACK_TAG, CLOSE_TAG))
    f_tcp_tip_dist = float(extract_leaf_content(msg_str, TCP_TIP_DIST_TAG, CLOSE_TAG))
    f_tcp_top_dist = float(extract_leaf_content(msg_str, TCP_TOP_DIST_TAG, CLOSE_TAG))
 
    pos_str = _find_substring(msg_str, POSE_TAG)
    if pos_str is not None:
        f_install_pos = _get_posx_from_str(pos_str)
    else:
        f_install_pos = None
 
    obj.add_fast_to_loc_with_uid(f_uid, f_loc_uid, f_install_pos, f_diam, f_shaft_height,
                                 f_min_stack, f_max_stack, f_tcp_tip_dist, f_tcp_top_dist,
                                 f_in_storage, f_in_ee, f_in_product, f_in_bin, is_tempf)
   
    send_response(msg_id, "fastener {} received by cobot".format(f_uid))
 
   
def handle_execution_str(msg_str, agent, msg_id):
    """
    Function that triggers execution of actions in an agent
    using a message string and adds a return to the queue_out
   
    :param msg_str: str, the string from the ROS server to modify the agent instance.
    :param agent: cl_agent, the agent instance to be modified.
    :param msg_id: str Unique reference to original message
    """
    a_uid = extract_leaf_content(msg_str, UID_TAG, CLOSE_TAG)
    tp_popup("message received. about to execute {}".format(a_uid), DR_PM_MESSAGE)
    agent.execute_uid(a_uid)

    #TODO Ronald: add workflow parameter to allow messages during execution (e.g. stop msg)
 
    send_response(msg_id, "action {} received and sent to be axecuted.".format(a_uid))
 
 
def _get_posx_from_str(str_in):
    """
    Function to get a posx object from a string
   
    :param str_in: str, the string with the position definition.
    """
    # get the position
    x = float(extract_leaf_content(str_in, POSE_PX_TAG, CLOSE_TAG))
    y = float(extract_leaf_content(str_in, POSE_PY_TAG, CLOSE_TAG))
    z = float(extract_leaf_content(str_in, POSE_PZ_TAG, CLOSE_TAG))
 
    # Get orientation
    a = float(extract_leaf_content(str_in, POSE_OX_TAG, CLOSE_TAG))
    b = float(extract_leaf_content(str_in, POSE_OY_TAG, CLOSE_TAG))
    c = float(extract_leaf_content(str_in, POSE_OZ_TAG, CLOSE_TAG))
 
    return posx(x, y, z, a, b, c)
 

# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# Cobot functions
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

def get_closest_posj(target_posx):
    """
    Function that finds the closest joint orientation from a posx.  
   
    :param target_posx: posx, The position in task space (x,y,z,a,b,c format)

    :return: posj, The position defined by joint rotations close to the current position
    """
    # read the current joint rotations
    current_posj = get_current_posj()

    # find the best target joint orientation
    # this is the orientation that is closest to the current one 
    # we square the angle differences, 
    # so bigger rotations make a bigger contribution
    r_min = 9e9
    for i in range(0, 7, 1):
        solj = ikin(target_posx, i)
        
        r_val = 0
        for j in range(0, 6, 1):
            s_j = solj[j]
            c_j = current_posj[j]
            r_val += (s_j - c_j) * (s_j - c_j)
        
        if r_val < r_min:
            r_min = r_val
            target_posj = solj
    
    return target_posj


def scale_targetj_speed(targetj, percentage):
    """
    Function to scale a target speed with a percentage. 
    The target speed will always remain below the JOINT_SPEED_LIMIT
   
    :param targetj: [float, float, float, float, float, float], The target speed for each joint
    :param percentage: float, The percentage with which to scale the target speed of each joint
    :param JOINT_SPEED_LIMIT: [float, float, float, float, float, float], The speed limit for each joint

    :return: [float, float, float, float, float, float], The scaled target speed
    """
    
    # speed must reain below the JOINT_SPEED_LIMIT
    r1 = min(percentage * targetj[0] / 100.0, JOINT_SPEED_LIMIT[0])
    r2 = min(percentage * targetj[1] / 100.0, JOINT_SPEED_LIMIT[1])
    r3 = min(percentage * targetj[2] / 100.0, JOINT_SPEED_LIMIT[2])
    r4 = min(percentage * targetj[3] / 100.0, JOINT_SPEED_LIMIT[3])
    r5 = min(percentage * targetj[4] / 100.0, JOINT_SPEED_LIMIT[4])
    r6 = min(percentage * targetj[5] / 100.0, JOINT_SPEED_LIMIT[5])

    return [r1, r2, r3, r4, r5, r6]


def speed_limited_movej_on_posx(target_posx, speed):
    """
    Function that moves to a position defined in task space (x,y,z,a,b,c format).
    It first finds the closest position in joint space and then moves there
    while limiting the speed of the TCP
   
    :param target_posx: posx, The target position in task space to move to
    :param speed: float, Speed definition defined as percentage of the current speed
    """
    speed_limited_movej_on_posj(get_closest_posj(target_posx), speed)


def speed_limited_movej_on_posj(target_posj, speed):
    """
    Function that moves to a position defined in task space (x,y,z,a,b,c format).
    It first finds the closest position in joint space and then moves there
    while limiting the speed of the TCP
   
    :param target_posx: posj, The target position to move to in joint space
    :param speed: float, Speed definition defined as percentage of the current speed
    """
    change_operation_speed(speed)
    targetj = scale_targetj_speed(JOINT_SPEED_LIMIT, speed)

    # start moving
    amovej(target_posj)

    # the following while loop keeps the tcp speed and rotation between 0.7 and 0.8 the speed limit
    while check_motion() > 0:
        velx = get_current_velx()

        tcp_speed = sqrt(velx[0] * velx[0] + velx[1] * velx[1] + velx[2] * velx[2])
        s_f = (tcp_speed / TCP_SPEED_LIMIT) * (speed / 100.0)

        tcp_rot = sqrt(velx[3] * velx[3] + velx[4] * velx[4] + velx[5] * velx[5])
        r_f = (tcp_rot / TCP_ROT_LIMIT) * (speed / 100.0)

        vel_f = max(s_f, r_f)
        #send_message("speed: {} mm/s". format(tcp_speed))

        if vel_f > 0.8:
            #speed reduction with 5%
            targetj = scale_targetj_speed(targetj, 95)
            set_velj(targetj)
            #send_message("j1 reduced to: {} deg/s". format(targetj[0]))

            # do not wait because many decreases might be needed very fast

        if vel_f < 0.7:
            #speed increase with 5%
            set_velj(scale_targetj_speed(targetj, 105))

            # only wait when speed is reduced 
            wait(0.1)

    # restore the desired rotational speeds to the original values
    set_velj(JOINT_SPEED_LIMIT)



def adjust_xy_location(movement_per_newton = 0.06):
    """
    Function to sense the force and move in the direction of the force.
   
    :param movement_per_newton: float, The distance to move per Newton force
    """
    wait(0.05)
    fx_t0, fy_t0, fz_t0 = get_tool_forces_in_tool()
    wait(0.05)
    fx_t1, fy_t1, fz_t1 = get_tool_forces_in_tool()
    wait(0.05)
    fx_t2, fy_t2, fz_t2 = get_tool_forces_in_tool()
    wait(0.05)
    fx_t3, fy_t3, fz_t3 = get_tool_forces_in_tool()
   
    fx_av0 = 0.25 * (fx_t0 + fx_t1 + fx_t2 + fx_t3)
    fy_av0 = 0.25 * (fy_t0 + fy_t1 + fy_t2 + fy_t3)
   
    max_x_difference = max(abs(fx_av0 - fx_t0), abs(fx_av0 - fx_t1), abs(fx_av0 - fx_t2), abs(fx_av0 - fx_t3))
    max_y_difference = max(abs(fy_av0 - fy_t0), abs(fy_av0 - fy_t1), abs(fy_av0 - fy_t2), abs(fy_av0 - fy_t3))
    max_diff = max(max_x_difference, max_y_difference, 0.2)
 
    xy_force_magnitude = sqrt(fx_av0 * fx_av0 + fy_av0 * fy_av0)
   
    dx = 0.0
    dy = 0.0
    
    if xy_force_magnitude > max_diff:
       
        dx = fx_av0 / xy_force_magnitude * movement_per_newton
        dy = fy_av0 / xy_force_magnitude * movement_per_newton
       
        movel(posx(dx, dy, 0, 0, 0, 0), ref=DR_TOOL)
   
        wait(0.05)
        fx_t0, fy_t0, fz_t0 = get_tool_forces_in_tool()
        wait(0.05)
        fx_t1, fy_t1, fz_t1 = get_tool_forces_in_tool()
        wait(0.05)
        fx_t2, fy_t2, fz_t2 = get_tool_forces_in_tool()
        wait(0.05)
        fx_t3, fy_t3, fz_t3 = get_tool_forces_in_tool()
       
        fx_av1 = 0.25 * (fx_t0 + fx_t1 + fx_t2 + fx_t3)
        fy_av1 = 0.25 * (fy_t0 + fy_t1 + fy_t2 + fy_t3)
           
        send_message("adjust_xy_location___Before: Fx = {}; Fy = {}; max_variation: {}\nAfter: Fx = {}; Fy = {}\ndx = {}; dy = {}".format(round(fx_av0, 3), round(fy_av0, 3), round(max_diff, 3), round(fx_av1, 3), round(fy_av1, 3), round(dx, 4), round(dy, 4)))
 
 
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
 
 
def create_axis_syst_on_current_position():
    """
    Function to create User defined axis system based on the current orientation
 
    ATTENTION: Do not use too often. Only limited amount of axis systems can exist in the program.
    """
    current_pos_for_cord, sol = get_current_posx(ref=DR_BASE)
 
    vx_axis, vy_axis, vz_axis = transpose(eul2rotm([current_pos_for_cord[3], current_pos_for_cord[4], current_pos_for_cord[5]]))
 
    return set_user_cart_coord(vx_axis, vy_axis, current_pos_for_cord)
 
    
    
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
 
def move_into_hole(fast):
    """
    Function to move inside the CSK and hole
 
    Assumptions:
        DR_USER_NOM will be set to the fastener corrected position
        This is at the nominal position of the fastener if no correction can be made.
 
    :param fast: cl_fastener,
   
    :return: bool, whether the insertion is succesful
    """
  
    #set the DR_USER_NOM on the corrected position
    overwrite_user_cart_coord(DR_USER_NOM, fast.corrected_pos(), ref=DR_BASE)
 
    # make sure the coordinate frame is DR_USER_NOM
    set_ref_coord(DR_USER_NOM)
       
    # Need to fix the corrected hole calculation first
    # This has been switched off for now
    # Def weighted_f_position()
    # Def Reevaluate_deviations()
    # Def get_weighted_pos_dev()
    # Def calc_and_set_corrected_pos()

    #move to the side of the hole
    movel(posx(10, 0, -SAFE_Z_GAP, 0, 0, 0), ref=DR_USER_NOM)
    
    #Compliance mode and force control
    task_compliance_ctrl(PROBE_COMPLIANCE)
    set_desired_force([0, 0, PROBE_COMPLIANCE_FORCE, 0, 0, 0], [0, 0, 1, 0, 0, 0])

    reached_force = False

    #Loop waiting for fastener tip to touch product
    while not reached_force:
        f_z = get_tool_forces_in_tool()[2]
        reached_force = abs(f_z) > 0.8 * PROBE_COMPLIANCE_FORCE

    z0, sol = get_current_posx(ref=DR_USER_NOM)
    
    release_force()

    z_comp = z0[2]

    movel(posx(10, 0, z_comp-SAFE_Z_GAP, 0, 0, 0), ref=DR_USER_NOM)
    movel(posx(0, 0, z_comp-SAFE_Z_GAP, 0, 0, 0), ref=DR_USER_NOM)
    movel(posx(0, 0, z_comp, 0, 0, 0), ref=DR_USER_NOM)

    z_stop = fast.tcp_tip_distance() * 0.95 + z_comp
    CSK_stop = fast.tcp_tip_distance() * 0.05 + z_comp
 
    #wait a bit to get a good force reading
    wait(0.15)
    f_x0, f_y0, f_z0 = get_tool_forces_in_nom()
 
    # set the values to allow the while loop to start
    in_hole = False
    t0 = time.time()
    p0, sol = get_current_posx(ref=DR_USER_NOM)
    reached_force = False
    in_CSK = False
 
    # Speed for moving tip of fastener in countersink
    change_operation_speed(INSERTION_IN_CSK_SPEED)

    # Compliance stiffness to move tip of fastener in countersink
    # High to low stiffness to counter weight of hose and capsule system         
    task_compliance_ctrl(INSERTION_COMPLIANCE)

    # Movement command to go in to countersink   
    amovel(posx(0, 0, (fast.tcp_tip_distance()*0.10), 0, 0, 0), ref=DR_USER_NOM)
 
    # Loop to prevent safety stop / damage to part.
    # A force detection (can) indicate a misalignment 
    
    while not in_CSK and (time.time() - t0) < 2.5:
        p0, sol = get_current_posx(ref=DR_USER_NOM)
        in_CSK = p0[2] > CSK_stop
 
        f_z = get_tool_forces_in_tool()[2]
        reached_force = abs(f_z - f_z0) > 0.9 * INSERTION_FORCE
           
        if reached_force:
            # this could be the impuls from a collision
            # wait to see if the force is maintained
            wait(0.5)
                   
            # check if the force is still there
            f_z = get_tool_forces_in_tool()[2]
            reached_force = abs(f_z - f_z0) > 0.9 * INSERTION_FORCE
            if reached_force:
                stop(DR_SSTOP)
                break
   
    send_message("move_into_hole____in_CSK={0}, reached_force={1},z_pos = {2}, z_stop={3}".format(in_CSK,reached_force,p0[2],CSK_stop))
   
    # Failure, not in CSK
    if not in_CSK:
        #Move back a bit, so that the force does not intefere with spiral movement
        movel(posx(0, 0, -2, 0, 0, 0), ref=DR_USER_NOM)
        reached_force = False   
        
        #Spiral move to slip in to correct position
        set_desired_force([0, 0, 11, 0, 0, 0], [0, 0, 1, 0, 0, 0])
       
        amove_spiral(rev= 5, rmax= 10, time= 5, axis= DR_AXIS_Z, ref= DR_USER_NOM)
        t0 = time.time()
       
        while not in_CSK and (time.time() - t0) < 50:
            p0, sol = get_current_posx(ref=DR_USER_NOM)
            in_CSK = p0[2] > CSK_stop
           
            if reached_force:
                # this could be the impuls from a collision
                # wait to see if the force is maintained
                wait(0.5)
                       
                # check if the force is still there
                f_z = get_tool_forces_in_tool()[2]
                reached_force = abs(f_z - f_z0) > 0.9 * INSERTION_FORCE
                if reached_force:
                    stop(DR_SSTOP)
                    break
       
        #Stops the spiral, but continous the force control
        stop(DR_SSTOP)
       
    # if the countersink was not found
    if not in_CSK:
        tp_log("Fastener did not go into countersink\nz_location = {}mm (z_stop = {}mm)".format(round(p0[2], 3), round(z_stop, 3)))
       
        return False
         
    #Set values for force control to get in to hole
    reached_force = False

    stop(DR_SSTOP)
    release_force()
    release_compliance_ctrl()

    #send_message("move_into_hole____starting init task_compliance_ctrl in CSK")
 
    task_compliance_ctrl([20000,20000,20000,400,400,400])
                    
    #send_message("move_into_hole____starting init set_desired_force in CSK")
    set_desired_force([0, 0, 11, 0, 0, 0], [0, 0, 1, 0, 0, 0])
        
    wait(0.1)
   
    #send_message("move_into_hole____starting final task_compliance_ctrl in CSK")
    task_compliance_ctrl(INSERTION_COMPLIANCE)
   
    #send_message("move_into_hole____starting final set_desired_force in CSK")
    set_desired_force([0, 0, INSERTION_FORCE + f_z0, 0, 0, 0], [0, 0, 1, 0, 0, 0])
   
    t0 = time.time()
   
    #Loop to check z-forces during insertion and position
    while not in_hole and (time.time() - t0) < 5:
        p0, sol = get_current_posx(ref=DR_USER_NOM)
        in_hole = p0[2] > z_stop
   
        f_z = get_tool_forces_in_tool()[2]
        reached_force = abs(f_z - f_z0) > 0.9 * INSERTION_FORCE
    
    send_message("move_into_hole____in_hole={0}, reached_force={1},".format(in_hole,reached_force))
               
    # #Moeten even kijken als we dit uberhaubt wel wilt doen, of als je gewoon gelijk moet probe?      
    # #Failure 1
    # #Angles / orientation not OK
    # if not in_hole:
       
    #     #Get the position where the fastener is stuck
    #     Pos_stuck, sol = get_current_posx(ref=DR_USER_NOM)
       
    #     #Release force to move backwards.
    #     release_force()
    #     movel(posx(0,0,-5,0,0,0), ref=DR_TOOL, mod= DR_MV_MOD_ABS)
       
    #     #Set force control       
    #     set_desired_force([0, 0, INSERTION_FORCE + f_z0, 0, 0, 0], [0, 0, 1, 0, 0, 0])
       
    #     #Periodic move to find the correct a & b orientation
    #     amove_periodic(amp = [0,0,0,1,2.12,0], period = [0,0,0,1,1,0], repeat = 4, ref = DR_USER_NOM)
       
    #     t0 = time.time()
       
    #     while not in_hole and (time.time() - t0) < 8:
    #         p0, sol = get_current_posx(ref=DR_USER_NOM)
    #         in_hole = p0[2] > z_stop
           
    #         #If OK orientation is found, stop the periodic move to prevent safety stop, 1.5mm is extra delta.
    #         if (p0[2] - 1.5) > Pos_stuck[2]:
    #             stop(DR_SSTOP)
        
      
    # #Failure 2 
    # #Fastener is stuck in between stacks
    # if not in_hole:  
        
    #     #Get the position where the fastener is stuck
    #     Pos_stuck, sol = get_current_posx(ref=DR_USER_NOM)
       
    #     #Release force to move backwards.
    #     release_force()
    #     movel(posx(0,0,-5,0,0,0), ref=DR_TOOL, mod= DR_MV_MOD_ABS)
       
    #     #Set force control
    #     set_desired_force([0, 0, INSERTION_FORCE + f_z0, 0, 0, 0], [0, 0, 1, 0, 0, 0])
       
    #     #Spiral move
    #     amove_spiral(rev= 4, rmax= 0.1, time= 4, axis= DR_AXIS_Z, ref= DR_USER_NOM)
       
    #     t0 = time.time()
    #     # The while loop below senses whether the fastener is able to un-stuck itself
    #     while not in_hole and (time.time() - t0) < 8:
    #         p0, sol = get_current_posx(ref=DR_USER_NOM)
    #         in_hole = p0[2] > z_stop
           
    #         #If OK orientation is found, stop the periodic move to prevent safety stop, 1.5mm is delta
    #         if (p0[2] - 1.5) > Pos_stuck[2]:
    #             stop(DR_SSTOP)
 
    #Misschien moet dit wel als eerst. Gewoon geen periodic/spiral in gat gebruiken is het beste.
    #Probing and last try
    if not in_hole:
        #tp_popup("start failure 3")
        release_force()
       
        #Uit gat en re-orienteren
        change_operation_speed(20)
        movel(posx(0, 0, -5, 0, 0, 0), ref=DR_USER_NOM)
        change_operation_speed(60)
   
        #Start re-orientatie / probing
        probe_hole_axis_syst(fast)
       
        release_compliance_ctrl()
       
        set_ref_coord(DR_USER_PROBE)
       
        movel(posx(0, 0, -20, 0, 0, 0), ref=DR_USER_NOM)
       
        # use xy of Pos_stuck, otherwise it can potentially use a misaligned xy value
        movel(posx(Pos_stuck[0], Pos_stuck[1], -5, 0, 0, 0), ref=DR_USER_PROBE)
       
        #Alles hierna moet dan in nieuwe REF + moet weer in CSK, en in hole etc.
       
        #Try insertion again
        task_compliance_ctrl([20000,20000,20000,400,400,400])
                    
        set_desired_force([0, 0, 11, 0, 0, 0], [0, 0, 1, 0, 0, 0])
        
        wait(0.1)
       
        task_compliance_ctrl(INSERTION_COMPLIANCE)
       
        set_desired_force([0, 0, INSERTION_FORCE + f_z0, 0, 0, 0], [0, 0, 1, 0, 0, 0])
       
        t0 = time.time()
       
        #Loop to check z-forces during insertion and position
        while not in_hole and (time.time() - t0) < 5:
           p0, sol = get_current_posx(ref=DR_USER_NOM)
           in_hole = p0[2] > z_stop
       
           f_z = get_tool_forces_in_tool()[2]
           reached_force = abs(f_z - f_z0) > 0.9 * INSERTION_FORCE
   
    t0 = time.time()
   
    #Loop to ensure correct position of fastener
    while not reached_force and (time.time() - t0) < 5:
        f_x, f_y, f_z = get_tool_forces_in_nom()
        reached_force = abs(f_z) > 0.85 * abs(INSERTION_FORCE + f_z0)           
                    
    release_force()
 
    # if the hole was not found
    if not in_hole:
        tp_log("Fastener did not go into hole\nz_location = {}mm (z_stop = {}mm)"
               .format(round(p0[2], 3), round(z_stop, 3)))
       
        return False
    else:   
        tp_log("Fastener went inside the hole.\nz_location = {}mm (z_stop = {}mm)"
              .format(round(p0[2], 3), round(z_stop, 3)))
        #tp_popup("in_hole true")
        return True
 
    
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
 
 
def get_tool_forces_in_tool():
    """
    Function to get the tool forces in tool axis system
       
    :return: list[float, float, float]: forces in tool axis system
    """
    # wait a bit until the force has settled
    wait(0.1)
           
    # get the forces
    forces = get_tool_force(ref=DR_BASE)
 
    # create the force vector in DR_BASE
    force_vector_base = [forces[0], forces[1], forces[2]]
 
    # get the position of the DR_TOOL in DR_BASE
    cp, sol = get_current_posx(ref=DR_BASE)
 
    # get the axis system vectors in DR_BASE
    vx_axis, vy_axis, vz_axis = transpose(eul2rotm([cp[3], cp[4], cp[5]]))
 
    # Get the vector components in DR_TOOL
    fx_t = dot_vect_prod(force_vector_base, vx_axis)
    fy_t = dot_vect_prod(force_vector_base, vy_axis)
    fz_t = dot_vect_prod(force_vector_base, vz_axis)
   
    # send_message("move_spiral_into_hole____Force is Fx = {}N, Fy = {}N, Fz = {}N\n".format(forces[0], forces[1], forces[2]) +
    #            "in DR_TOOL Fx = {}N, Fy = {}N, Fz = {}N".format(fx_t, fy_t, fz_t))
 
    return fx_t, fy_t, fz_t
       
 
 
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
 
 
def get_force_magnitude():
    """
    Function to get the force magnitude
        
    :return: float, the magnitude of the forces
    """
    # get the forces
    f = get_tool_force()
 
    # create the force vector in DR_BASE
    return sqrt(f[0] * f[0] + f[1] * f[1] + f[2] * f[2])
 
 
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
 
 
def get_tool_forces_in_nom():
    """
    Function to get the tool forces in DR_USER_NOM
        
    :return: list[float, float, float]: forces in DR_USER_NOM axis system
    """
    # get the forces
    forces = get_tool_force()
 
    # create the force vector in DR_BASE
    force_vector_base = [forces[0], forces[1], forces[2]]
 
    # get the axis of DR_USER_NOM
    cp = coord_transform(posx(0, 0, 0, 0, 0, 0), DR_USER_NOM, DR_BASE)
 
    # get the axis system vectors in DR_BASE
    vx_axis, vy_axis, vz_axis = transpose(eul2rotm([cp[3], cp[4], cp[5]]))
 
    # Get the vector components in DR_TOOL
    fx_n = dot_vect_prod(force_vector_base, vx_axis)
    fy_n = dot_vect_prod(force_vector_base, vy_axis)
    fz_n = dot_vect_prod(force_vector_base, vz_axis)
 
    return fx_n, fy_n, fz_n
 
 
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
 
 
def get_xy_force_in_nom(f_x0, f_y0):
    """
    Function to get the tool force in the xy plane of DR_USER_NOM
 
    :param f_x0: float, force in x direction of DR_USER_NOM axis system; to be subtracted
    :param f_y0: float, force in y direction of DR_USER_NOM axis system; to be subtracted
       
    :return: float, force in xy plane in DR_USER_NOM axis system
    """
    # get the forces in the nominal axis system
    fx_n, fy_n, fz_n = get_tool_forces_in_nom()
   
    # remove the zero fx and fy
    fx_n -= f_x0
    fy_n -= f_y0
 
    return sqrt(fx_n * fx_n + fy_n * fy_n)
 
 
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
 
 
 
def probe_hole_axis_syst(fast):
    """
    Function to create an axis system at the hole location.
    Z-axis of the position of the fastener must be into the hole.
 
    The function:   
        1) moves to a probing position
        2) probes the surface around the hole
        3) determines the surface orientation
        4) assumes the hole centerline, normal to the surface
        5) overwrites DR_USER_PROBE axis system
        6) stores the probed position in the fastener instance
 
    :param fast: cl_fastener, fast location to be probed
 
   :return: Axis System, Change DR_USER_PROBE to a coordinate system at the probed entry of the hole
    """

    probe_dist = fast.z_pos_prediction_accuray() + SAFE_Z_GAP + SAFE_Z_GAP
 
    # set the DR_USER_PROBE axis system above the hole location
    overwrite_user_cart_coord(DR_USER_PROBE, translate_pos(fast.installed_pos(), 0, 0, -probe_dist), ref=DR_BASE)
 
    release_force()
    release_compliance_ctrl()
 
    # Exit the hole (not too fast) to the origin of the DR_USER_PROBE axis system
    change_operation_speed(PROBE_HOLE_AXIS_SYSTEM_HOLE_EXIT_SPEED)
 
    movel(posx(0, 0, 0, 0, 0, 0), ref=DR_USER_PROBE)
    change_operation_speed(MOVE_SPEED)
 
    # Calculate the possible probe variation,
    # assuming the probe orientation is maximum 10 degrees misaligned with the hole
    probe_variation = 0.3526 * probe_dist
 
    send_message("probe_hole_axis_syst____Probing aroud the hole.")
   
    # Move in +x direction and probe the surface
    P_p = posx(probe_dist, 0, 0, 0, 0, 0)
    ppx_x, ppx_y, ppx_z, ppx_xu, ppx_yu, ppx_zu = probe(P_p)
 
    # Move in -x direction
    # Depending on the first measured probe distance we go back less -
    # using the the calculated probe_variation
   
    P_p = posx(-probe_dist, 0, ppx_zu - probe_variation - SAFE_Z_GAP, 0, 0, 0)
    pmx_x, pmx_y, pmx_z, pmx_xu, pmx_yu, pmx_zu = probe(P_p)
 
    # Calculate the X vector over the surface in DR_BASE
    x_dir = normalize_vect([ppx_x - pmx_x, ppx_y - pmx_y, ppx_z - pmx_z])
 
    # Move in +y direction
    # We can use half of the probe_variation now we know the avarage z from +x and -x probes
  
    P_p = posx(0, probe_dist, 0.5 * (ppx_zu + pmx_zu - probe_variation) - SAFE_Z_GAP, 0, 0, 0)
    ppy_x, ppy_y, ppy_z, ppy_xu, ppy_yu, ppy_zu = probe(P_p)
 
    # Move in -y direction
   
    P_p = posx(0, -probe_dist, 0.5 * (ppx_zu + pmx_zu - probe_variation) - SAFE_Z_GAP, 0, 0, 0)
   
    pmy_x, pmy_y, pmy_z, pmy_xu, pmy_yu, pmy_zu = probe(P_p)
 
    
    # Calculate the Y vector over the surface in DR_BASE
    y_dir = normalize_vect([ppy_x - pmy_x, ppy_y - pmy_y, ppy_z - pmy_z])
   
    # The z-direction is calculated from the x_dir and y_dir in DR_BASE
    z_dir = normalize_vect(cross_vect_prod(x_dir, y_dir))
   
    # Create a user coordinate system based on the probe points.
    # first we determine the orientation in DR_BASE
    a_angle, b_angle, c_angle = rotm2eul(transpose([x_dir, y_dir, z_dir]))
   
    P_install_in_DR_USER_PROBE = coord_transform(fast.installed_pos(), DR_BASE, DR_USER_PROBE)
   
    # Calculate the average probing point z-coord in DR_USER_PROBE
    z_av = 0.25 * (ppx_zu + pmx_zu + ppy_zu + pmy_zu)
   
    P_new_in_DR_USER_PROBE = posx(P_install_in_DR_USER_PROBE[0], P_install_in_DR_USER_PROBE[1], z_av, 0, 0, 0)
   
    # Get the average probing point coordiates in the DR_BASE axis system
    P_pos = coord_transform(P_new_in_DR_USER_PROBE, DR_USER_PROBE, DR_BASE)
   
    P_out = posx(P_pos[0], P_pos[1], P_pos[2], a_angle, b_angle, c_angle)
   
    send_message("probe_hole_axis_syst____Hole location probed at position:\n" + pos_string(P_out))
   
    wait(0.5)
    #  Overwrite DR_USER_PROBE towards the hole entry point
    overwrite_user_cart_coord(DR_USER_PROBE, P_out, ref=DR_BASE)
   
    # store the information in the fastener instance
    fast.set_installed_pos(P_out)
   
    # set the deviation to a low number, assuming we probed correctly
    fast.set_z_pos_prediction_accuray(Z_POS_THRESHOLD * 0.5)
    fast.set_dir_prediction_accuray(Z_ANGLE_THRESHOLD * 0.5)
 
    
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
 
 

def retract_tempf(tempf, ee, retract = True):
    """
    Function to retract with the tempf in the end effector.
   
    :param tempf: cl_fastener, Tempf location to be probed
    :param ee: the end effector object
       
    :return: bool, Whether there is a fastener in the end effector
    """
   
    release_force()
    release_compliance_ctrl()
   
    # retract away from the fastener location in any case
    # Exit the hole (not too fast) to the origin of the DR_USER_PROBE axis system
    change_operation_speed(HOLE_RETRACTION_SPEED)
   
    # Set the compliance and force
    # Set DR_TOOL as ref coordinate to ensure that the desired forces are in the too axis system
    set_ref_coord(DR_TOOL)
   
    if retract:
        movel(posx(0, 0, -tempf.tcp_tip_distance() - SAFE_Z_GAP, 0, 0, 0), ref=DR_TOOL)

        current_pos, sol = get_current_posx(ref=DR_BASE)

        overwrite_user_cart_coord(DR_USER_PROBE, current_pos)

        bp0, bp1, bp2, up0, up1, up2 = probe(start_pos = posx(10, 0, 0, 0, 0, 0), tighten = True, ee = ee)

        # the ee cannot move forward more than 10mm if there is a fastener
        return up2 < 10 

    return True

 
 
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
 
 
def probe(start_pos, force = PROBE_COMPLIANCE_FORCE, compl = PROBE_COMPLIANCE, tighten = False, ee = None):
    """
    Function to probe a location. Probes from start position in z-direction of the given axis system
   
    The function will also start to engage the thread inside the fastener while
    the fastener is pressed against the pick-up location
 
    :param start_pos: posx, Position that is the startpoint of the probing in the given axis_system
    :param force: float,
    :param compl: [float x6],
    :param tighten: bool, Whether the temp must be shortly tightened when pressed aganst the product
    :param ee: cl_tfee, the temporary fastener object
    :param ee: the end effector object
       
    Global Constants:
        DR_USER_PROBE: [axis system] Axis system that defines the start_pos.
                            The z-axis is the direction where the cobot will look for contact
        MOVE_SPEED: float,
        PROBE_COMPLIANCE: [float, float, float, float, float, float]
       
    :return: list[float,float,float,float,float,float], probe position coordinates in DR_BASE and DR_USER_PROBE
    """
 
    change_operation_speed(MOVE_SPEED)
   
    movel(start_pos, ref=DR_USER_PROBE)
   
    # wait a little so the deceleration doesn't affect force sensor
    wait(0.15)
 
    # Get a reference force because a force can already be present (example: hanging cables)
    f_z0 = get_tool_forces_in_tool()[2]
   
    f_z0 = 0 #Bram
 
   # Set the compliance and force
    # Set DR_TOOL as ref coordinate to ensure that the desired forces are in the too axis system
    set_ref_coord(DR_TOOL)
 
    # Do this with maximum stiffness for the best accuracy
    task_compliance_ctrl(compl)
 
    # Set the force. The force should be in range of 10-20N -
    # small enough not to bend the material but high enough to reach surface in shortest time
    set_desired_force([0, 0, force + f_z0, 0, 0, 0], [0, 0, 1, 0, 0, 0])
 
    # Wait until the force reaches a value
    not_reached_force = True
    while not_reached_force:
     
        not_reached_force = abs(get_tool_forces_in_tool()[2] - f_z0) < 0.9 * PROBE_COMPLIANCE_FORCE
 
    #    Get the current position (in BASE and in USER cord.sys.) when the force reached the value
    base_probe_pos, sol = get_current_posx(ref=DR_BASE)
    user_probe_pos, sol = get_current_posx(ref=DR_USER_PROBE)

    if tighten:
        #prepare the end effector
        ee.reset_cobot_output_pins()
        ee.start_new_cycle()
        ee.set_select_program(1)
    
        # start tightening the fastener
        ee.set_start_on()
    
        # tightening so the temp does not fit in the hole anymore
        # shorter than 0.8 seconds will not do anything. Seems like responsetime is long
        wait(1.6)

        #stop the tightening
        ee.reset_cobot_output_pins()
        ee.start_new_cycle()
        
    release_force()
    release_compliance_ctrl()
    set_ref_coord(DR_BASE)
     
     # Move away a bit from the surface
    movel([0, 0, -SAFE_Z_GAP, 0, 0, 0], ref=DR_TOOL)
     
     #   Return the probe position coordinates in DR_BASE and DR_USER_PROBE.
    return base_probe_pos[0], base_probe_pos[1], base_probe_pos[2], user_probe_pos[0], user_probe_pos[1], user_probe_pos[2]
 
 
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
 
 
def add_timestamp(s):
    """
    Function to add a timestamp to a filename.
    It removes the extension, adds the timestamp and adds the extension again.
 
    :param s: str, the filename
       
    :return: str, renamed filename
    """
    str_date_time = datetime.now().strftime("_%d_%m_%Y_%H_%M_%S")
    base, extension = os.path.splitext(s)
   
    return base + str_date_time + extension
   
 
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
 
 
def cross_vect_prod(a, b):
    """
    Function to calculate the cross product
 
    :param a: list[float, float, float], First input vector
    :param b: list[float, float, float], Second input vector
 
    :return: list[float, float, float], cross product vector
    """
    c = [0, 0, 0]
 
    c[0] = a[1] * b[2] - a[2] * b[1]
    c[1] = a[2] * b[0] - a[0] * b[2]
    c[2] = a[0] * b[1] - a[1] * b[0]
 
    return c
 
 
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
 
 
def dot_vect_prod(a, b):
    """
    Function to calculate the dot product
 
    :param a: list[float, float, float], First input vector
    :param b: list[float, float, float], Second input vector
 
    :return: float, dot product value
    """
    return a[0] * b[0] + a[1] * b[1] + a[2] * b[2]
 
 
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
 
 
def normalize_vect(a):
    """
    Function to normalize a vector
 
    :param a: list[float, float, float], Input vector
 
    :return: list[float, float, float], Normalized vector
    """
    vl = vector_length(a)
    return [a[0] / vl, a[1] / vl, a[2] / vl]
 
 
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
 
 
def vector_length(a):
    """
    Function to calculate the length of a vector
 
    :param a: list[float, float, float], Input vector
 
    :return: float, length of the vector
    """
    try:
        return sqrt(a[0] * a[0] + a[1] * a[1] + a[2] * a[2])
    except:
        return 999999.0
 
 
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
 
 
def point_distance(p1, p2):
    """
    Function to calculate the distance between the two points
 
    :param p1: list[float, float, float], Point 1
   :param p2: list[float, float, float], Point 2
 
    :return: float, Distance between the two points
    """
    try:
        # create a vector from point 2 to point 1
        a = [p1[0] - p2[0], p1[1] - p2[1], p1[2] - p2[2]]
   
        return vector_length(a)
    except:
        return 999999.0
 
 
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
 
 
def vector_angle(a, b):
    """
    Function to calculate the angle between two vectors in radians
 
    :param a: list[float, float, float], First input vector
    :param b: list[float, float, float], Second input vector
 
    :return: float, angle between the input vectors in radians
    """
    # return zero if it is the same vector
    if (abs(a[0] - b[0]) + abs(a[1] - b[1]) + abs(a[2] - b[2])) < 0.0001:
        return 0.0

    return acos(dot_vect_prod(a, b) / (vector_length(a) * vector_length(b)))
 
 
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
 
 
 
def project_pt_to_xy_pln(pt, p_ref):
    """
    Function to project a point or position on the xy_plane of a position
    ATTENTION: Will set the DR_USER_NOM to the p_ref position
 
    :param pt: list[float, float, float] | posx, point to be projected
    :param p_ref: posx, position containing the xy_plane
 
    :return: posx, position of the point projected on the xy plane of p_ref
    """
    # set DR_USER_NOM at position p_ref
    overwrite_user_cart_coord(DR_USER_NOM, p_ref, ref=DR_BASE)
   
    # get the coordinates in DR_USER_NOM
    pu = coord_transform(posx(pt[0], pt[1], pt[2], 0, 0, 0), DR_BASE, DR_USER_NOM)
 
    # get the coordinates in DR_BASE
    pb = coord_transform(posx(pu[0], pu[1], 0, 0, 0, 0), DR_USER_NOM, DR_BASE)
 
    return posx(pb[0], pb[1], pb[2], p_ref[3], p_ref[4], p_ref[5])
 
 
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
 
 
 
def translate_pos(p_in, dx, dy, dz):
    """
    Function to translate a position with a vector
    It leaves the orientation the same
 
    :param p_in: posx, position that is the reference position
    :param dx:   float, translation in x-direction
    :param dy:   float, translation in y-direction
    :param dz:   float, translation in z-direction
 
    :return: posx, translated position
    """
 
    #  Get the current vectors of the xyz axis
    vx_axis, vy_axis, vz_axis = transpose(eul2rotm([p_in[3], p_in[4], p_in[5]]))
   
    # transklate the position
    x = p_in[0] + dx * vx_axis[0] + dy * vy_axis[0] + dz * vz_axis[0]
    y = p_in[1] + dx * vx_axis[0] + dy * vy_axis[0] + dz * vz_axis[1]
    z = p_in[2] + dx * vx_axis[0] + dy * vy_axis[0] + dz * vz_axis[2]
 
    return posx(x, y, z, p_in[3], p_in[4], p_in[5])
       
 
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
 
 
 
def get_weighted_averages(fastener_list):
    """
    Function that calculates a list of weighted average positions deviations from a list of fastener objects
    The closer the fastener, the more its position deviation counts.
 
    The average of two fasteners is only taken if these fasteners are more or less
    on opposite sides of the fastener to be installed. This way the average is really
    the situation between two fasteners. If this would not be required it could be that two fasteners
    on one side of the fastener to be installed determine the deviation, while
    the other side could be tilted the other way.
 
    :param fastener_list: list[cl_fastener], the list of fasteners that provide the correction
 
    :return: list[tuple(float, posx, float, float, float)]
 
        Average distance: float, average distance of the fastener to the to be installed fastener
        Average position: posx, weighted average position deviation of the fastener
        Average xy positional deviation: float, average distance between the corrected position and the installed position
        Average z positional deviation: float, average distance between the corrected position and the installed position
        Average directional deviation: float, average angle between z-axis of the corrected position and the installed position
    """
 
    lst = []
 
    # only do the len = 1 and len = 2 case if the initial len is that small.
    # lists with len = 1 or len = 2 must be prevented in a nested call of this function.
    if len(fastener_list) == 1:
        df = fastener_list[0].distance_to_fastener()
        ip = fastener_list[0].get_installed_position_in_axis_system_at_nom_pos()
        xy_dist = fastener_list[0].xy_pos_prediction_accuray()
        z_dist = fastener_list[0].z_pos_prediction_accuray()
        ang = fastener_list[0].dir_prediction_accuray()
        lst.append((df, ip, xy_dist, z_dist, ang))
    elif len(fastener_list) == 2:
        lst.append(weighted_f_position(fastener_list[0], fastener_list[1]))
    else:
        # find the other fastener that is most opposite to the closest fastener
        a_old = 0.0
        f_i = -1
 
        # find the other fastener, opposite to the first fastener in the list
        for i in range(1, len(fastener_list)):
            a_new = fastener_list[0].vector_to_fastener_angle(fastener_list[i])
            # remember this fastener if it has a bigger angle
            # smaller than 120 degrees is not considered opposite
            if a_new > GET_WEIGHTED_AVERAGES_MIN_ANGLE and a_new > a_old:
                a_old = a_new
                f_i = i
 
        if f_i > -1:
            # add the weighing factor and the weighted average position deviation
            lst.append(weighted_f_position(fastener_list[0], fastener_list[f_i]))
 
        # make a new list with the remaining fastners from the list
        f_lst = [fastener_list[i] for i in range(1, len(fastener_list)) if i != f_i]
 
        if len(f_lst) > 2:
            # process the new fastener object list
            # NOTICE: this causes nested behavior of the function
            lst.extend(get_weighted_averages(f_lst))
        elif len(f_lst) == 2:
            # if there are two fasteners remaining their vector angle must be at least 2 radians
            a_new = f_lst[0].vector_to_fastener_angle(f_lst[1])
            if a_new > GET_WEIGHTED_AVERAGES_MIN_ANGLE:
                # call the function one last time for this branch
                lst.extend(get_weighted_averages(f_lst))
 
    return lst
 
 
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
 
 
 
def weighted_f_position(f1, f2):
    """
    Function that calculates a weighted average position based on two fastener objects.
    It gets the distances and installed_position_in_nom_axis_system from both fastener
    objects and calculates a weighted average
 
    :param f1: cl_fastener, fastener object 1
    :param f2: cl_fastener, fastener object 2
 
    :return: tuple(float, posx, float, float, float)
                  
                   average distance,
                   weighted average position,
                   average positional xy deviation,
                   average positional z deviation,
                   direction deviation)
    """
   
    d1 = f1.distance_to_fastener()
    d2 = f2.distance_to_fastener()
    p1 = f1.get_installed_position_in_axis_system_at_nom_pos()
    p2 = f2.get_installed_position_in_axis_system_at_nom_pos()
    xy1 = f1.xy_pos_prediction_accuray()
    xy2 = f2.xy_pos_prediction_accuray()
    z1 = f1.z_pos_prediction_accuray()
    z2 = f2.z_pos_prediction_accuray()
    dir1 = f1.dir_prediction_accuray()
    dir2 = f2.dir_prediction_accuray()
 
    # calculate the average distance
    av_d = 0.5 * (d1 + d2)
 
    # invert the number because the bigger the distance the smaller its influence must be
    d1 = 1 / d1
    d2 = 1 / d2
 
    # total distance
    dt = d1 + d2
 
    # make distance factors dimensionless
    d1 = d1 / dt
    d2 = d2 / dt
 
    # create the weighted position
    x = d1 * p1[0] + d2 * p2[0]
    y = d1 * p1[1] + d2 * p2[1]
    z = d1 * p1[2] + d2 * p2[2]
    a = d1 * p1[3] + d2 * p2[3]
    b = d1 * p1[4] + d2 * p2[4]
    c = d1 * p1[5] + d2 * p2[5]
 
    # calculate the average positional and directional deviation
    av_xy = d1 * xy1 + d2 * xy2
    av_z = d1 * z1 + d2 * z2
    av_dir = d1 * dir1 + d2 * dir2
 
    return av_d, posx(x, y, z, a, b, c), av_xy, av_z, av_dir
 
 
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
 
 
def reevaluate_deviations(latest_fastener, f_list):
    """
    Function that evaluates how accurate the corrected position was.
    It redefines the accuracy of the closest fastener if it is significantly
    larger (1.25) than the latest fastener.
 
    This is because the closest fastener was installed early when no good
    corrected position could be calculated yet. This routine redefines the
    accuracy of those fasteners based on the accuracy they cause in
    subsequent fasteners.
 
    ATTENTION: the distance_to_fastener and vector_to_fastener must be
               calculated towards latest_fastener
 
    :param latest_fastener cl_fastener, fastener installed last
    :param f_list: list[cl_fastener], Fasteners in a fastener group.
                                The f_list must be in the order of instalation.
 
    :return: None, xy_pos_deviation, z_pos_deviation and/or dir_deviation re-evaluated
    """  
    
    # find the closest installed fastener
    dist = 1000000
    closest_fastener = f_list[0]
    found = False
   
    for f in f_list:
       
        # the loop can stop if the latest fastener is reached
        if f == latest_fastener:
            break
           
        if f.distance_to_fastener() < dist and f.installed():
            dist = f.distance_to_fastener()
            closest_fastener = f
            found = True
           
    if found:
        # redefine the xy_pos_deviation of the closest fastener if it led to significantly better accuracy
        if closest_fastener.xy_pos_prediction_accuray() > 1.25 * latest_fastener.xy_pos_prediction_accuray():
            closest_fastener.set_xy_pos_prediction_accuray(latest_fastener.xy_pos_prediction_accuray())
           
        # redefine the z_pos_deviation of the closest fastener if it led to significantly better accuracy
        if closest_fastener.z_pos_prediction_accuray() > 1.25 * latest_fastener.z_pos_prediction_accuray():
            closest_fastener.set_z_pos_prediction_accuray(latest_fastener.z_pos_prediction_accuray())
       
        # redefine the dir_deviation of the closest fastener if it led to significantly better accuracy
        if closest_fastener.dir_prediction_accuray() > 1.25 * latest_fastener.dir_prediction_accuray():
            closest_fastener.set_dir_prediction_accuray(latest_fastener.dir_prediction_accuray())
 
 
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
 
 
 
def get_weighted_pos_dev(dev_lst):
    """
    Function that calculates the weighted average position deviation from a list of tuples
    The smaller the average distance, the more its position deviation counts.
 
    :param dev_lst: list[tuple(average distance,
                               weighted average position deviation,
                               weighted average positional deviation,
                               weighted average directional deviation)]
 
        Average distance: float, average distance of the fastener to the to be installed fastener
        Average position: posx, weighted average position deviation of the fastener
        Average positional deviation: float, average deviation of the corrected position with respect to the installed position
        Average direction deviation: float, average deviation of the corrected position with respect to the installed position
       
    :return: tuple(posx, float, float, float)
  
        Average position: posx,
        Average xy position deviation: float, in mm
        Average z position deviation: float, in mm
        Average direction deviation: float, in degrees
    """

    # invert the distances because the bigger the distance the smaller its influence must be
    # NOTICE this defines the weighing factors
    # alternatively the square of the distance can be used.
    finv_lst = [1/i[0] for i in dev_lst]
 
    # calculate the total of the factors
    f_tot = sum(finv_lst)
 
    # calculate all weighing factors
    f_lst = [f_i/f_tot for f_i in finv_lst]
 
    # get the positions
    p_lst = [i[1] for i in dev_lst]
    xy_lst = [i[2] for i in dev_lst]
    z_lst = [i[3] for i in dev_lst]
    d_lst = [i[4] for i in dev_lst]
 
    x, y, z, a, b, c, xyd, zd, ad = 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0
 
    for f_i, p_i, xy_i, z_i, d_i in zip(f_lst, p_lst, xy_lst, z_lst, d_lst):
        x += f_i * p_i[0]
        y += f_i * p_i[1]
        z += f_i * p_i[2]
        a += f_i * p_i[3]
        b += f_i * p_i[4]
        c += f_i * p_i[5]
        xyd += f_i * xy_i
        zd += f_i * z_i
        ad += f_i * d_i
 
    return posx(x, y, z, a, b, c), xyd, zd, ad
 
 
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
 
 
 
def pos_string(p, d = 3):
    """
    Creates a string with the position in three decimals.
 
    :param p posx, position to be logged
    :param d float, the number of decimals to output
       
    :return: str, description the position
    """
    try:
        return "x={}; y={}; z={}; a={}; b={}; c={}".format(round(p[0], d), round(p[1], d), round(p[2], d), round(p[3], d), round(p[4], d), round(p[5], d))
    except:
        return "Invalid Position."
 
         
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
 
class cl_digital_output:
    """
    Class that maintains the status of a digital output
    """
   
    def __init__(self, outp_pin_no, state = False):
        """
        :param outp_pin_no: int, the cobot output pin linked to this output
        :param state: bool, whether the output must be on or off at init.
            The default is False.
 
        :return: None
        """
        self.__outp_pin_no = outp_pin_no
        self.__state = state
        self._ensure_state()
   
    def outp_pin_no(self):
        """
        Function that returns which cobot output pin it is linked to
 
        :return: int, the output pin number
        """
        return self.__outp_pin_no
   
    def set_outp_pin_no(self, outp_pin_no):
        """
        Function that returns which cobot output pin it is linked to
 
        :return: None
        """
        self.__outp_pin_no = outp_pin_no
       
        # ensure that the new state is also in the new pin
        self._ensure_state()
   
    def switch_on(self):
        """
        Function to switch the digital output on if not already on
 
        :return: None
        """
        if not self.__state:
            set_digital_output(self.__outp_pin_no, 1)
            self.__state = True
           
    def switch_off(self):
        """
        Function to switch the digital output off if not already off
 
        :return: None
        """
        if self.__state:
            set_digital_output(self.__outp_pin_no, 0)
            self.__state = False
   
    def is_on(self):
        """
        :return: bool, True if the output is on
        """
        return self.__state
           
    def is_off(self):
        """
        :return: bool, True if the output is off
        """
        return not self.__state
   
    def _ensure_state(self):
        """
        Function to ensure that the output pin corresponds to the state
 
        :return: None
        """
        if self.__state:
            set_digital_output(self.__outp_pin_no, 1)
        else:
            set_digital_output(self.__outp_pin_no, 0)
      
 
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
 
 
# TODO Future iterations should make all hardcoded numbers configurable
class cl_temp_fast_ee:
    """
    Class that defines the fastener end effector
 
    It can be used to control the Lisi fastener end effector
    The class hes been written so that it contains all relevant initiation data itself
    """
   
    def __init__(self):
        """
        List of cobot output pin connections below
        Pin number zero means that it is not connected yet"""
       
        """
        Output pin number on Cobot connected to EE Pin 2 START
        Clockwise cycle start"""
        self.I2_START = 3
        """
        Output pin number on Cobot connected to EE Pin 3 REVERSE
        Counterclockwise cycle start"""
        self.I3_REVERSE = 4
        """
        Output pin number on Cobot connected to EE Pin 4 NEW CYCLE
        Start new cycle"""
        self.I4_NEW_CYCLE = 5
        """
        Output pin number on Cobot connected to EE Pin 5 STOP MOTOR
        stops the motor in any situation"""
        self.I5_STOP_MOTOR = 6
        """
        Output pin number on Cobot connected to EE Pin 6 RESET CYCLE
        resets any partial values of the cycle you are working in"""
        self.I6_RESET_CYCLE = 7
        """
        Output pin number on Cobot connected to EE Pin 7 PRINT LABEL
        prints on request a 50 letters label
        Needs to be set up in the EE controller"""
        self.I7_PRINT_LABEL = 0
        """
        Output pin number on Cobot connected to EE Pin 8-15 for PR1-PR8
        to choose the desired programs 1-8; only if EXT program is active"""
        self.I_PR = (8,9,0,0,0,0,0,0)
        """
        Maximum time in seconds of the installation per program.
        Note PR2 is slower, so takes more time
        ATTENTION: maximum time allowed in the end effector controller is 10sec"""
        self.INST_TIME = (5,10,5,5,5,5,5,5)
        """
        Maximum time in seconds of the removal per program.
        Note PR2 is slower, so takes more time
        ATTENTION: maximum time allowed in the end effector controller is 10sec"""
        self.REM_TIME = (5,10,5,5,5,5,5,5)
       
        
        """
        List of cobot output pin connections for air control below
        Pin number zero means that it is not connected yet"""
       
        """
        Cobot output pin that switches the solenoid
        valve to clamp the fastener"""
        self.AIR_CLAMP = 2
        """
        Cobot output pin that switches the solenoid
        valve to eject the fastener"""
        self.AIR_EJECT = 1
 
        # class instances that store the current solenoid valve setting
        self.clamp = cl_digital_output(self.AIR_CLAMP)
        self.eject = cl_digital_output(self.AIR_EJECT)
       
        """
        List of cobot input pin connections below
        Pin number zero means that it is not connected yet"""
       
        """
        Input pin number on Cobot connected to EE Pin 2 SINGLE OK
        Correct screwing done between min and max time.
        Signal starts when the screwing is done
        and it resets when a new screwing is started."""
        self.O2_SINGLE_OK = 13
        """
        Input pin number on Cobot connected to EE Pin 3 SINGLE NOK
        Incorrect screwing done under min or over max time.
        Signal starts at the end of a screwing
        it resets when a new screwing is started."""
        self.O3_SINGLE_NOK = 14
        """
        Input pin number on Cobot connected to EE Pin 4 CYCLE OK
        Cycle done well not exceeding the pre-set reject screws.
        Signal starts at the end of a cycle
        and it resets when a new cycle is started."""
        self.O4_CYCLE_OK = 0
        """
        Input pin number on Cobot connected to EE Pin 5 CYCLE NOK
        Incorrect cycle where in one or more screws the pre-set rejected screws have been gone over.
        Signal starts at the end of a cycle
        and it resets when a new cycle is started."""
        self.O5_CYCLE_NOK = 0
        """
        Input pin number on Cobot connected to EE Pin 6 TOTAL END
        End of cycle or of sequence.
        Signal starts at the end of a cycle
        and it resets when a new cycle is started."""
        self.O6_TOTAL_END = 0
        """
        Input pin number on Cobot connected to EE Pin 7 LEVER
        Signal starts when the lever is pressed or at input start
        and it stops when it is released."""
        self.O7_LEVER = 0
        """
       Input pin number on Cobot connected to EE Pin 8 MOTOR ON
        Signal starts when the motor starts
        and it switches off when the motor stops."""
        self.O8_MOTOR_ON = 15
        """
        Input pin number on Cobot connected to EE Pin 9 STOP TIME
        Signal starts when the screwing exceeds the max time
        It resets when a new screwing is started."""
        self.O9_STOP_TIME = 0
        """
        Input pin number on Cobot connected to EE Pin 10 REV TIME
        Signal starts if the REV TM is on when the unscrewing cycle is over
        Signal ends when a new screwing is started."""
        self.O10_REV_TIME = 0
        """
        Input pin number on Cobot connected to EE Pin 11 FAILURE
        Signal starts at any error detected by the unit."""
        self.O11_FAILURE = 16 
        
        # make sure all known pins are off
        self.reset_cobot_output_pins_incl_air()
       
        # variable that stores whether a fastener is in the end effector
        self.tempf_in_end_effector = False
       
 
    def reset_cobot_output_pins(self):
        """
        Switches off all cobot controller output pins to
        the end effector controller.
        No reset of pins to the solenoid valves.
        """
        # switch pins 3 to 10 off
        #TODO: add when more pins are connected
        set_digital_outputs([-3, -4, -5, -6, -7, -8, -9, -10])
       
 
    def reset_cobot_output_pins_incl_air(self):
        """
        Switches off all cobot controller output pins
        including pins to the solenoid valves.
        """
        self.reset_cobot_output_pins()
 
        #instruct the clamp and eject instances tot switch off
        self.clamp.switch_off()
        self.eject.switch_off()
   
 
    def is_clamping(self):
        """
        Is the end effector clamping a fastener.
       
        :return: bool
        """
        return self.clamp.is_on()
       
 
    def is_ejecting(self):
        """
        Is the end effector ejecting a fastener.
       
        :return: bool
        """
        return self.eject.is_on()
       
 
    def is_output_single_ok(self):
        """
        True when the screwing is done when a correct
        screwing done between min and max time.
        and it resets when a new screwing is started.
        """
        return get_digital_input(self.O2_SINGLE_OK) == 1
   
 
    def is_output_single_nok(self):
        """
        True at the end of a screwing when an incorrect
        screwing done under min or over max time.
        it resets when a new screwing is started.
        """
        return get_digital_input(self.O3_SINGLE_NOK) == 1
   
 
    def is_output_cycle_ok(self):
        """
        True at the end of a cycle when a cycle is done well
        not exceeding the pre-set reject screws.
        and it resets when a new cycle is started.
        """
        return get_digital_input(self.O2_CYCLE_OK) == 1
   
 
    def is_output_cycle_nok(self):
        """
        True at the end of a cycle when cycle is incorrect in one or more
        screws the pre-set rejected screws have been gone over.
        and it resets when a new cycle is started.
        """
        return get_digital_input(self.O3_CYCLE_NOK) == 1
   
 
    def is_output_total_end(self):
        """
        True at the end of a cycle or of sequence.
        and it resets when a new cycle is started.
        """
        return get_digital_input(self.O6_TOTAL_END) == 1
 
 
    def is_output_lever_on(self):
        """
        True when the lever is pressed or at input start
        and it stops when it is released.
        """
        return get_digital_input(self.O7_LEVER) == 1
       
 
    def is_output_motor_on(self):
        """
        True when the motor starts
        and it switches off when the motor stops.
        """
        return get_digital_input(self.O8_MOTOR_ON) == 1
   
 
    def is_stop_time(self):
        """
        True when the screwing exceeds the max time
        It resets when a new screwing is started.
        """
        return get_digital_input(self.O9_STOP_TIME) == 1
 
 
    def is_rev_time_on(self):
        """
        True if the REV TM is on when the unscrewing cycle is over
        Signal ends when a new screwing is started.
        """
        return get_digital_input(self.O10_REV_TIME) == 1
   
 
    def has_output_failure(self):
        """
        True at any error detected by the unit.
        """
        return get_digital_input(self.O11_FAILURE) == 1
   
 
    def set_start_on(self):
        """
        Start clockwise cycle
        """
        set_digital_output(self.I2_START, 1)  
        # wait until the motor signals that it is on
        while not self.is_output_motor_on():
            wait(0.01)
 
 
    def set_reversestart_on(self):
        """
        Start counterclockwise cycle
        """
       
        set_digital_output(self.I3_REVERSE, 1) 
        # no need to wait until the motor is on because it is not used here
       
 
    def start_new_cycle(self):
        """
        Start new cycle
        """       
        set_digital_output(self.I4_NEW_CYCLE, 1)
        wait(0.1)
        set_digital_output(self.I4_NEW_CYCLE, 0)
   
 
    def set_stop_motor(self):
        """
        stop the motor in any situation
        """
        set_digital_output(self.I5_STOP_MOTOR, 1)  
        wait(0.1)
        set_digital_output(self.I5_STOP_MOTOR, 0)
   
 
    def set_reset_cycle(self):
        """
        reset any partial values of the cycle you are working in
        """
        set_digital_output(self.I6_RESET_CYCLE, 1)
        wait(0.1)
        set_digital_output(self.I6_RESET_CYCLE, 0)
   
 
    def request_print_label(self):
        """
        print on request a 50 letters label
        Needs to be set up in the EE controller
        """
        set_digital_output(self.I7_PRINT_LABEL, 1)
        wait(0.1)
        set_digital_output(self.I7_PRINT_LABEL, 0)
 
 
    def start_clamping(self):
        """
        Start clamping a fastener.
        """
        self.clamp.switch_on()
 
 
    def start_ejection(self):   
        """
        Start ejection of a fastener.
        """
        self.eject.switch_on()
   
 
    def stop_clamping(self):
        """
        stop clamping a fastener.
        """
        self.clamp.switch_off()
 
 
    def stop_ejection(self):
        """
        close ejection valve to stop ejecting a fastener.
        """
        self.eject.switch_off()
 
 
    def set_select_program(self, program):
        """
        Selects a program between 1 and 8
       
        :param  program: int, the progam to use
        """
        # check if a valid program number has been selected; must be 1-8
        if program < 9 and program > 0:   
                                    
            # if the pin connection is defined
            if self.I_PR[program - 1] > 0:  
                
                # switch on the selected output pin
                set_digital_output(self.I_PR[program - 1], 1) 
                return True               
            else:
               
                # Exit the function with an error
                tp_popup("Trying to install a fastener using PR" + program + ". Pin not connected.", DR_PM_WARNING)
                self.reset_output_pins()
                return False                                                  
        else:
            
            # exit the function with an error
            tp_popup("No proper fastener program selected. Number has to be 1-8", DR_PM_WARNING)
            self.reset_output_pins()
            return False 
    
    def engagement_burst(self, program = BURST_PROGRAM, in_tight_dir = False, duration = 0.8):
        """
        function to make a short rotation burst to help engagement of the end
        effector with the fastener.
       
        burst usually when temp must be picked up,
        so the default burst must be in untightening direction
       
        :param  program: int, which program to use for this burst
        :param  in_tight_dir: bool, whether to run in the tightening direction or the untightening direction
        :param  duration: real, duration of the burst
       
        returns True if succesful
        """
        # lets make sure all pins are off first
        self.reset_cobot_output_pins()
        self.start_new_cycle()
       
        # check if program number has been selected correctly
        if not self.set_select_program(program):   
            send_message("engagement_burst____Unsuccesful fastener engagement burst; wrong program selected.")
            return False
       
        if in_tight_dir:
            self.set_start_on()
        else:
            self.set_reversestart_on()
       
        wait(duration) # shorter than 0.8 seconds will not do anything. Seems like responsetime is long
        #TODO measure response time
       
        self.reset_cobot_output_pins()
        self.start_new_cycle()
       
        return True
       
 
    #TODO: maybe tell the cobot to brace for any kickback from the fastener installation.
    #TODO: monitor cobot for errors as well
    def tighten_temp(self, program):
        """
        function to tighten a fastener
       
        :param  program: int, the progam to use
       
        returns True when successful; False if failed to tighten
        """
       
        # lets make sure all pins are off first
        self.reset_cobot_output_pins()
       
        #Shift the EE if needed
        #adjust_xy_location()
       
        #start new cycle
        self.start_new_cycle()
       
        if not self.tempf_in_end_effector:
            send_message("tighten_temp____Unsuccesful fastener tightening; There was no fastener in the end effector to install.")
            return False
       
        if not self.is_clamping():
            send_message("tighten_temp____clamping solenoid valve was disengaged when tightening started. Clamping valve will be switched on.")
            self.start_clamping()
           
        if self.has_output_failure():
            send_message("tighten_temp____system indicates a failure when tightening started. End Effector will be reset.")
            self.set_reset_cycle()
       
        if self.is_output_single_nok():
            send_message("tighten_temp____system indicates the previous tightening failed. End Effector will be reset.")
            self.set_reset_cycle()
 
        # check how long this is.
        # do a fast start for two seconds
        self.set_select_program(1)
        self.set_start_on()
        wait(2)
        #TODO make this dependent on the stack thickness and time it takes to reach that thickness
        self.reset_cobot_output_pins()
        wait(0.2)
        
        # if the the tempf was accidentally fully tightened
        if self.is_output_single_ok():
            send_message("tighten_temp____Pre-tightening of fastener tightening using PR{} instead of {}\nfastener might be too tight" .format(1, program))
            return True
           
        # check if program number has been selected correctly
        if not self.set_select_program(program):    
            send_message("tighten_temp____Unsuccesful fastener tightening; wrong program selected.")
            return False
       
        start_time = time.time()   
        
        self.start_new_cycle()
        self.set_select_program(program)
                                        
        # switch on the pin for an installation
        self.set_start_on()                                  
        
        # wait until everything was set in motion
        wait(0.1)
        timed_out = False 
        #TODO make the duration dependent on the stack thickness
        max_duration = self.INST_TIME[program - 1]
 
        while self.is_output_motor_on() and not self.is_output_single_ok() and not self.is_output_single_nok() and not self.has_output_failure() and not timed_out:
            current_time = time.time()
            duration = current_time - start_time
            timed_out = (duration > max_duration)
            if timed_out:
                self.reset_cobot_output_pins()
                # exit the function with an error
                send_message("tighten_temp____Time out during fastener tightening using PR{} in {}seconds.".format(program, duration))           
                return False
            wait(0.1)
            
        current_time = time.time()
        duration = current_time - start_time
       
        # we can reset all output pins now
        self.reset_cobot_output_pins()
        self.start_new_cycle()
       
        if self.has_output_failure():
           
            # exit the function with an error
            send_message("tighten_temp____Failure during fastener tightening using PR{} in {}seconds.".format(program, duration))           
            # clamp the fastener again
            self.start_clamping()
            return False
        
        if self.is_output_single_nok():
           
            # exit the function with an error
            send_message("tighten_temp____Unsuccesful fastener tightening using PR{} in {}seconds.".format(program, duration))
            # clamp the fastener again
            self.start_clamping()
            return False
        
        # Exit the function with a success
        send_message("tighten_temp____Succesful fastener tightening using PR{} in {}seconds.".format(program, duration))
                      
        return True 
 
    
    #TODO: maybe tell the cobot to brace for any kickback from the fastener installation.
    #TODO: monitor cobot for errors as well
    def untighten_temp(self, program):
        """
        Function to untighten a fastener
       
        :param  program: int, the progam to use
       
        returns True when successful; False if failed to untighten
        """
      
        # lets make sure all pins are off first
        self.reset_cobot_output_pins()
        self.start_new_cycle()
       
        #Shift the EE if needed
        #adjust_xy_location()
       
        if not self.tempf_in_end_effector:
            send_message("untighten_temp____Unsuccesful fastener untightening; There was no fastener in the end effector to remove.")
            return False
       
        # check if a valid program number has been selected; must be 1-8
        if not self.set_select_program(program):
            send_message("untighten_temp____Unsuccesful fastener untightening; wrong PR selected.")
            return False
                                     
        start_time = time.time()  
        
        #start clamping the fastener
        self.start_clamping()
                                        
        # switch on the pin for a removal
        self.set_reversestart_on()                                  
        
        # wait until everything is set in motion
        wait(0.2) 
        max_duration = self.REM_TIME[program - 1]
        timed_out = False           
        
        while not self.is_output_single_ok() and not self.is_output_single_nok() and not self.has_output_failure() and not timed_out:
            current_time = time.time()
            duration = current_time - start_time
            timed_out = (duration > max_duration)
            if timed_out:
                self.set_stop_motor()
                self.reset_cobot_output_pins()
                # exit the function with an error
                send_message("untighten_temp____fastener untightening using PR{} in {}seconds.".format(program, duration))           
                return True
            wait(0.01)
       
        current_time = time.time()
        duration = current_time - start_time
       
        # we can reset all output pins now
        self.reset_cobot_output_pins()
        self.start_new_cycle()
              
        if self.is_output_single_nok():
           
            # exit the function with an error
            send_message("untighten_temp____Unsuccesful fastener untightening using PR{} in {}seconds.".format(program, duration))
            return False
        
        if self.has_output_failure():
           
            # exit the function with an error
            send_message("untighten_temp____Failure during fastener untightening using PR{} in {}seconds.".format(program, duration))           
            return False
        
        # Exit the function with a success
        send_message("untighten_temp____Succesful fastener untightening using PR{} in {}seconds.".format(program, duration))                         
        
        return True 
            
 
    def eject_temp(self):
        """
        Eject a fastener.
        returns True when finished
        """
        # stop the clamping by closing the clamp solenoid valve
        self.stop_clamping()
       
        # wait until the air is blown off and the clamping disengaged
        wait(0.3)
       
        # open the ejecting solenoid valve
        self.start_ejection()
       
        # wait for the air to blow out the temp
        wait(1)
       
        # close the solenoid valve
        self.stop_ejection()
       
        # store that the end effector does not have a fastener anymore
        self.tempf_in_end_effector = False
       
        return True
 
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
 
 
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
 
 
# TODO Future iterations should make all hardcoded numbers configurable
class cl_perm_fast_ee:
    """
    Class that defines the permanent fastener end effector
 
    It can be used to control the permanent fastener end effector
    The class hes been written so that it contains all relevant initiation data itself
    """
   
    def __init__(self):
        """
        List of cobot flange output pin connections below
        """
       
        """
        Output pin number on Cobot tool connected to EE to TRIGGER EE
        Unlocks EE or puls fastener"""
        self.I2_TRIGGER = 1 #Moet 1 zijn, maar staat op 8 om geen nagel te trekken
                                
        # make sure all known tool pins are off
        self.reset_cobot_tool_output_pins()
       
        # variable that stores whether a permanent fastener is in the end effector
        self.permf_in_end_effector = False
        
 
    def reset_cobot_tool_output_pins(self):
        """
        Switches off all cobot tool output pins to
        the end effector.
            """
        # switch pins 1 off
        #TODO: add when more pins are connected
        set_tool_digital_outputs([-1, -2, -3, -4, -5, -6])
          
        
    def start_trigger(self):
        """
        Triggers the EEF to unlock or pull a fastener
        """
        wait(0.5) # Nagel wordt gelijk getrokken als die in positie zit, heel even wachten zodat de nagel goed in positie zit
        #tp_popup("start complaince control")
        #task_compliance_ctrl([20,20,20,400,400,400])
       
        set_tool_digital_output(self.I2_TRIGGER, 1)  
 
        wait(1.5) #Checken als trigger aan moet blijven tijdends nagel trekken. Of dat 1x triggeren voldoende is. Moet zoiezo ff wachten totdat nagel getrokken is
       # wait(0.1) #Weet niet zeker als anders het singaal goed door komt
        #set_tool_digital_output(self.I2_TRIGGER, 0)
        #tp_popup("start_trigger returned True")
       
        release_compliance_ctrl()
       
        return True
 
       
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
 
 
 
class cl_uid():
    """Class that has a uid"""
    
    def __init__(self, uid):
        """
        :param uid: str, the uid of the instance
        """
        self.__uid = uid
 
 
    def __eq__(self, other):
        """
        The object is considered equal if the uid is the same.
       
        :param other: [cl_fastener_action] the other cl_uid object
        """
 
        return self.uid() == other.uid()
   
 
    def uid(self):
        """
        Returns the uid of the instance.
        """
        return self.__uid
 
 
    def set_uid(self, uid):
        """
        Sets the uid of the instance.
       
        :param uid: str, the uid of the object
        """
        self.__uid = uid
       
        
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
 
 
class cl_fastener_location(cl_uid):
    """
    Class that describes a fastener location
    """
 
    
    def __init__(self, uid, diam, stack_thickness, fast_nom_pos, drill_jig_dist = 0, is_drilled = True):
        """
        Initiation of the class cl_fastener_location that describes a fastener location
 
        :param uid: str, the uid of the fastener
        :param diam: int, the diameter of the fastener in mm
        :param stack_thickness: int, the stack thickness of the current position
        :param fast_nom_pos: posx, The nominal position of the fastener in DR_BASE
        :param drill_jig_dist: float, the distance between drill jig and product in mm
        :param is_drilled: bool, Whether the hole has been drilled
        """
       
        super().__init__(uid)
 
        self.__drill_jig_dist = drill_jig_dist
        self.__diam = diam
        self.__stack_thickness = stack_thickness
        self.__nom_pos = fast_nom_pos
        self.__grip_length = self.calculate_grip_length()
        self.__is_drilled = is_drilled
 
    def __eq__(self, other):
        """
        The location is considered equal if it is at the same xyz coordinate.
        ATTENTION: Redefines the uid class equal function
       
        :param other: cl_fastener_location, the other cl_fastener_location instance
        """
        if other is not None:
            xyz1 = self.nom_xyz_coordinate()
            xyz2 = other.nom_xyz_coordinate()
   
            dx = abs(xyz1[0] - xyz2[0])
            dy = abs(xyz1[1] - xyz2[1])
            dz = abs(xyz1[2] - xyz2[2])
   
            return dx < 0.01 and dy < 0.01 and dz < 0.01
        else:
            return False
       
 
    def diam(self):
        """
        returns the diameter of the pin in mm
        """
        return self.__diam
   
    
    def set_diam(self, diam):
        """
        sets the diameter of the pin in mm
        """
        self.__diam = diam
        
        
    def drill_jig_dist(self):
        """
        returns the drill jig dist in mm
        """
        return self.__drill_jig_dist
   
    
    def set_drill_jig_dist(self, drill_jig_dist):
        """
        sets the drill jig dist in mm
        """
        self.__drill_jig_dist = drill_jig_dist
 
    
    def is_drilled(self):
        """
        returns whether the hole is drilled or not
        """
        return self.__is_drilled
   
    
    def set_is_drilled(self, is_drilled):
        """
        sets the hole to drilled or not
        """
        self.__is_drilled = is_drilled
       
    
    def stack_thickness(self):
        """
        returns the stack thickness in mm of the product or storage location it is currently installed in
        """
        return self.__stack_thickness
   
 
    def set_stack_thickness(self, t):
        """
        Sets the stack code based on the stack thickness in mm.
        """
        self.__stack_thickness = t
       
    
    def nom_pos(self):
        """
        gets a new nominal position in DR_BASE
        """
        return self.__nom_pos
 
    
    def set_nom_pos(self, p):
        """
        sets a new nominal position in DR_BASE
        to be used when the temp is to be placed at a new location."""
        self.__nom_pos = p
       
 
    def nom_xyz_coordinate(self):
        """
        returns a list with the x, y, z coordinates of the nominal hole position.
        """
        return [self.__nom_pos[0], self.__nom_pos[1], self.__nom_pos[2]]
 
    def fast_nom_pos_string(self):
        return "nominal position: \n" + pos_string(self.__nom_pos)
       
    def log_nom_pos(self):
        send_message("log_nom_pos___", self.fast_nom_pos_string())
 
    def pop_up_nom_pos(self):
        tp_popup(self.fast_nom_pos_string())
       
    def calculate_grip_length(self):
        """
        Calculates the grip length based on the stack thickness. Grip range information taken from PREN 6122.pdf page 7
        For diameter codes 5, 6 & 8
       
        Deviation in data sheet for 06 - 02 min grip = 3.048
        """
        if 3.048 <= self.__stack_thickness <= 3.99 and self.diam() == 4.80:
            return 2
       
        if 2.39 <= self.__stack_thickness <= 3.99 and self.diam() != 4.80:
            return 2
       
        if 3.96 <= self.__stack_thickness <= 5.59:
            return 3
 
        if 5.56 <= self.__stack_thickness <= 7.16:
            return 4
 
        if 7.14 <= self.__stack_thickness <= 8.76:
            return 5
 
        if 8.74 <= self.__stack_thickness <= 10.34:
            return 6
 
        if 10.31 <= self.__stack_thickness <= 11.94:
            return 7
 
        if 11.91 <= self.__stack_thickness <= 13.51:
            return 8
 
        if 13.49 <= self.__stack_thickness <= 15.11:
            return 9
 
        if 15.09 <= self.__stack_thickness <= 16.69:
            return 10
 
        if 16.66 <= self.__stack_thickness <= 18.29:
            return 11
 
        if 18.26 <= self.__stack_thickness <= 19.86:
            return 12
       
        if 19.84 <= self.__stack_thickness <= 21.46:
            return 13
 
        if 21.44 <= self.__stack_thickness <= 23.04:
            return 14
 
        if 23.01 <= self.__stack_thickness <= 24.64:
            return 15
 
        if 24.61 <= self.__stack_thickness <= 26.21:
            return 16
       
        if 26.19 <= self.__stack_thickness <= 27.81:
            return 17
 
        if 27.79 <= self.__stack_thickness <= 29.39:
            return 18
 
        if 29.36 <= self.__stack_thickness <= 30.99:
            return 19
 
        if 30.96 <= self.__stack_thickness <= 32.56:
            return 20
   
    def grip_length(self):
        """
        Returns the grip length code
        """
        return self.__grip_length
   
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
       
 
 
class cl_fastener(cl_fastener_location):
    """Class that defines the temp or perm fastener information
 
    derived from cl_fastener_location
 
    Assumes existence of the following axis systems:
        DR_USER_NOM
        DR_USER_NOM_OPP
        DR_BASE
      
    """
 
    
    def __init__(self, uid, diam, stack_thickness, fast_nom_pos,
                 fast_corrected_pos=None, fast_install_pos=None,
                 in_storage = False, in_ee = False, in_product=False, in_bin=False, is_tempf = True):
        """
        If corrected_pos or install_pos are specified the init assumes
        that the installation has already taken place and will calculate the
        correct numbers.
       
        cl_fastener_location inputs:
        :param uid: str, the uid or ID of the fastener
        :param diam: int, the diameter of the fastener in mm
        :param stack_thickness: int, the stack thickness of the current position
        :param fast_nom_pos: posx, The nominal position of the fastener in DR_BASE
           
        Additional Inputs:
            corrected_pos: posx, The position in DR_BASE that was originally calculated from the other positions
            install_pos: posx, The actual installed position of the fastener in DR_BASE
           
            Only one of the follwing booleans can be True
            in_storage: [bool] Whether the fastener is in the storage location
            in_ee: [bool] Whether the fastener is in the end effector
            in_product: [bool] Whether the fastener is installed in the product
            in_bin: [bool] Whether the fastener is ejected into the bin
        """
        super().__init__(uid, diam, stack_thickness, fast_nom_pos)
       
        # positions
        self.__corrected_pos = None
        self.__installed_pos = None
        self.__tcp_target_pos = None
        self.__tcp_approach_pos = None
        self.__is_tempf = is_tempf
       
        self.__distance_to_fastener = 999999.0
        self.__vector_to_fastener = [0, 0, 0]
       
        self.__in_storage = in_storage
        self.__in_ee = in_ee
        self.__in_product = in_product
        self.__in_bin = in_bin
        
        self.__shaft_height = 0
        self.__min_stack = 0
        self.__max_stack = 0
        self.__tcp_tip_distance = 0
        self.__tcp_top_distance = 0
       
        no_true = 0
        if in_storage:
            no_true += 1
        if in_ee:
            no_true += 1
        if in_product:
            no_true += 1
        if in_bin:
            no_true += 1
       
        if no_true > 1:
            send_message("cl_fastener_init____wrong input in cl_fastener {}.\n\
                       More than one in_storage, in_ee, in_product, in_bin is true.\n\
                       Must be only one.".format(uid))         
        
        # properly respond to the given positions
        if fast_corrected_pos is None and fast_install_pos is None:
            # if there was no installation yet
            self.reset_to_nom_pos_only()
        else:
            if fast_corrected_pos is None and fast_install_pos is not None:
                # if only the installation position are given
                self.__corrected_pos = fast_nom_pos
                self.__installed_pos = fast_install_pos
            elif fast_corrected_pos is not None and fast_install_pos is None:
                # if only the corrected position are given
                self.__corrected_pos = fast_corrected_pos
                self.__installed_pos = fast_nom_pos
            else:
                # if both are given
                self.__corrected_pos = fast_corrected_pos
                self.__installed_pos = fast_install_pos
           
            self.calc_xy_pos_pred_acc()
            self.calc_z_pos_pred_acc()
            self.calc_dir_pred_acc()
            self.calc_tcp_target_pos_from_corrected_hole_pos()
            self.calc_tcp_approach_pos_from_corrected_hole_pos()
           
 
 
    def __lt__(self, other):
        """
        This will cause fastener objects to be sorted based on the distance value.
        """
        return self.distance_to_fastener() < other.distance_to_fastener()
 
 
    def distance_to_fastener(self):
        """
        Gets the stored distance to a fastener that has been calculated earlier.
       
        :return: float, distance in mm
        """
        return self.__distance_to_fastener
 
 
    def vector_to_fastener(self):
        """
        Gets the stored vector to a fastener that has been calculated earlier.
       
        :return: list[float, float, float], vector
        """
        return self.__vector_to_fastener
 
 
    def z_pos_prediction_accuray(self):
        """
        Get expected deviation between corrected and installed fastener position.
        After installation this value represents the accuracy with which the correction can be estimated.
       
        :return: float, deviation in z-direction between corrected and installed in mm
        """
        return self.__z_pos_pred_acc
 
 
    def set_z_pos_prediction_accuray(self, a):
        """
        Set expected deviation between corrected and installed fastener position.
        After installation this value represents the accuracy with which the correction can be estimated.
       
        :param a: float, the deviation between corrected and installed in mm
        """
        self.__z_pos_pred_acc = a
       
 
    def xy_pos_prediction_accuray(self):
        """
        Get expected deviation between corrected and installed fastener position.
        After installation this value represents the accuracy with which the correction can be estimated.
       
        :return: float, deviation in xy plane between corrected and installed in mm
        """
        return self.__xy_pos_pred_acc
 
 
    def set_xy_pos_prediction_accuray(self, a):
        """
        Set expected deviation between corrected and installed fastener position.
        After installation this value represents the accuracy with which the correction can be estimated.
       
        :param a: float, the deviation between corrected and installed in mm
        """
        self.__xy_pos_pred_acc = a
 
 
    def dir_prediction_accuray(self):
        """
        Get expected angle between corrected and installed z-axis in degrees.
        After installation this value represents the accuracy with which the correction can be estimated.
        
        :return: float, angle deviation between corrected and installed in radians
        """
        return self.__dir_pred_acc
 
 
    def set_dir_prediction_accuray(self, a):
        """
        Set expected angle between corrected and installed z-axis in degrees.
        After installation this value represents the accuracy with which the correction can be estimated.
       
        :param a: float, the deviation between corrected and installed in radians
        """
        self.__dir_pred_acc = a
   
    def is_xy_pos_well_predicted(self):
        """
        :return: bool, whether it is well predicted in xy plane
        """
        return self.xy_pos_prediction_accuray() < XY_POS_THRESHOLD
   
    def is_z_pos_well_predicted(self):
        """
        :return: bool, whether it is well predicted in z-direction
        """
        return self.z_pos_prediction_accuray() < Z_POS_THRESHOLD
   
    def is_z_dir_well_predicted(self):
        """
        :return: bool, whether the angle is well predicted
        """
        return self.dir_prediction_accuray() < Z_ANGLE_THRESHOLD
   
    def is_well_predicted(self):
        """
        :return: bool, whether it is well predicted
        """
        return self.is_xy_pos_well_predicted() and self.is_z_pos_well_predicted() and self.is_z_dir_well_predicted()
   
 
    def vector_to_fastener_angle(self, f):
        """
        Calculates the angle between the vector_to_fastener of this fastener
        and the vector_to_fastener of another fastener in radians. Always returns a positive value
       
        :param f: cl_fastener, other fastener object
       
        :return: float, angle in radians
        """
        return abs(vector_angle(self.__vector_to_fastener, f.vector_to_fastener()))
 
 
    def set_distance_to_fastener(self, f):
        """
        calculates the distance to another fastener
       
        :param f: cl_fastener, other fastener object to which the distance will be calculated
        """
        self.__distance_to_fastener = point_distance(self.nom_xyz_coordinate(), f.nom_xyz_coordinate())
 
 
    def set_vector_to_fastener(self, f):
        """
        calculates the vector to another fastener
       
        :param f: cl_fastener, other fastener object to which the distance will be calculated
        """
        if f is not None:
            xyz1 = self.nom_xyz_coordinate()
            xyz2 = f.nom_xyz_coordinate()
            self.__vector_to_fastener = [xyz2[0] - xyz1[0], xyz2[1] - xyz1[1], xyz2[2] - xyz1[2]]
        else:
            self.__vector_to_fastener = []
 
 
    def corrected_pos(self):
        """
        returns the corrected position at the hole entry point in DR_BASE.
       
        :return: posx
        """
        return self.__corrected_pos
   
    
    def tcp_target_pos(self):
        """
        Get the target tcp position from the corrected hole position in DR_BASE
        The TCP is at the tip of the fastener, when it is fully inserted into the hole.
        """
        return self.__tcp_target_pos
 
    
    def tcp_approach_pos(self):
        """
        Get the target tcp position for safe approach from the hole position in DR_BASE
       
        :return: posx
        """
        return self.__tcp_approach_pos
   
    
    def get_dist_to_target_pos(self):
        """
        Function that returns the distance of the TCP to the target position when fully installed.
        """
        # get the current position of the TCP (tip of the fastener)
        curr_pos, sol = get_current_posx(ref=DR_BASE)
       
        return point_distance(self.tcp_target_pos(), curr_pos)
   
 
    def get_install_ratio(self):
        """
       Function that returns the ratio that depicts how close the fastener
        is towards the destination point.
        >1 before hole entry point
        1 = at the hole entry point
        0 = at the corrected install position
        """
        if self.in_ee():
            # the tip has to sink in the hole with the length of the tcp_dictance
            depth = self.__tcp_tip_distance
        else:
            # the tip has to sink over the top of the fastener to engage it
            depth = self.__shaft_height - self.__tcp_top_distance
       
        return self.get_dist_to_target_pos() / depth
   
    
    def installed_pos(self):
        """
        the position where the fastener is installed in DR_BASE
       
        :return: posx
        """
        return self.__installed_pos
   
 
    def set_installed_pos(self, p):
        """
        stores the installed position value. Also sets the fastener object as installed.
       
        :param p: posx, the new installed positionn
        """
        self.__installed_pos = p
 
 
    def in_storage(self):
        """
        returns whether the fastener is in the storage location.
       
        :return: bool
        """
        return self.__in_storage
   
 
    def set_as_in_storage(self):
        """
        sets that the fastener is installed in the storage.
        Will also report the change to the connected system.
        """
        self.__in_storage = True
        # it is not in any of the other locations
        self.__in_ee = False
        self.__in_product = False
        self.__in_bin = False
       
        self.set_tool_center_point()
        self.report_to_system()
        
 
    def in_ee(self):
        """
        returns whether the fastener is in the end effector.
        """
        return self.__in_ee
   
 
    def set_as_in_ee(self):
        """
        sets that the fastener is in the end effector.
        Will also report the change to the connected system.
        """
        self.__in_ee = True
        # it is not in any of the other locations
        self.__in_storage = False
        self.__in_product = False
        self.__in_bin = False
       
        self.set_tool_center_point()
        self.report_to_system()
   
    
    def in_product(self):
        """
        returns whether the fastener is installed in the product.
        """
        return self.__in_product
   
 
    def set_as_in_product(self):
        """
        sets that the fastener is installed in the product.
        Will also report the change to the connected system.
        """
        self.__in_product = True
        # it is not in any of the other locations
        self.__in_storage = False
        self.__in_ee = False
        self.__in_bin = False
       
        self.set_tool_center_point()
        self.report_to_system()
 
 
    def in_bin(self):
        """returns whether the fastener has been ejected into the bin."""
        return self.__in_bin
   
 
    def set_as_in_bin(self):
        """
        sets that the fastener is ejected into the bin.
        Will also report the change to the connected system.
        """
        self.__in_bin = True
        # it is not in any of the other locations
        self.__in_storage = False
        self.__in_ee = False
        self.__in_product = False
       
        self.set_tool_center_point()
        self.report_to_system()
 
 
    def report_to_system(self):
        """
        Let the connected systen know the fastener status.
        The uid of the location is not known in this class.
        """
        if self.__is_tempf:
            str_out = TEMPFS_TAG + _get_fastener_to_server_str(self, "") + CLOSE_TAG
        else:
            str_out = FASTENERS_TAG + _get_fastener_to_server_str(self, "") + CLOSE_TAG
 
        send_message(str_out)
 
 
    def is_tempf(self):
        """returns whether the fastener is a temporary fastener."""
        return self.__is_tempf
 
 
    def is_permf(self):
        """returns whether the fastener is a permanent fastener."""
        return not self.__is_tempf
   
 
    def set_as_tempf(self):
        """
        sets the fastener to be a tepmporary fastener.
        """
        self.__is_tempf = True
 
    
    def set_as_permf(self):
        """
        sets the fastener to be a permanent fastener.
        """
        self.__is_tempf = False
 
 
    def reset_to_nom_pos_only(self):
        """
        Resets the positions of install_pos and corrected_pos to the nominal position
        resets corresponding calculated deviations to default values.
        """
        self.__installed_pos = self.nom_pos()
        self.__corrected_pos = self.nom_pos()
        self.calc_tcp_target_pos_from_corrected_hole_pos()
        self.calc_tcp_approach_pos_from_corrected_hole_pos()
        self.__xy_pos_pred_acc = TEMPF_DEFAULT_POSITIONAL_DEVIATION
        self.__z_pos_pred_acc = TEMPF_DEFAULT_POSITIONAL_DEVIATION
        self.__dir_pred_acc = TEMPF_DEFAULT_ORIENTATION_DEVIATION
 
 
    def reset_to_installed_pos(self):
        """
        Sets the corrected_pos to the install_pos and
        calculates the corresponding derived attributes.
        """
       
        self.__corrected_pos = self.__installed_pos
        self.calc_tcp_target_pos_from_corrected_hole_pos()
        self.calc_tcp_approach_pos_from_corrected_hole_pos()
        self.__xy_pos_pred_acc = self.calc_xy_pos_pred_acc()
        self.__z_pos_pred_acc = self.calc_z_pos_pred_acc()
        self.__dir_pred_acc = self.calc_dir_pred_acc()
 
 
    def tcp_tip_distance(self):
        """
        returns the distance of the tip of the fastener to where the hole entry point is in mm
        """
        return self.__tcp_tip_distance
 
 
    def set_tcp_tip_distance(self, val):
        """
        sets the distance of the tip of the fastener to where the hole entry point is in mm
        """
        self.__tcp_tip_distance = val
   
 
    def tcp_top_distance(self):
        """
        returns the distance of the top of the fastener to where the hole entry point is in mm
        """
        return self.__tcp_top_distance
 
 
    def set_tcp_top_distance(self, val):
        """
        sets the distance of the top of the fastener to where the hole entry point is in mm
        """
        self.__tcp_top_distance = val
   
    
    def set_tool_center_point(self):
        """
        sets the correct tool center point location at the tip of the fastener
       
        Supported tool center points
        TCP_NAME_DIAM_5_TIP
        TCP_NAME_LISI_TIP_NO_TEMPF
       
        ATTENTION: TCP can only be changed if the compliance is off
        ATTENTION: function needs update every time a new fastener is purchased.
        ATTENTION: tcp names in this code and in the Cobot Controller must align.
           
        :return: bool, whether the tcp has been set correctly
        """
        # compliance must be turned off to enable TCP change.
        release_force()
        release_compliance_ctrl()
       
        # apparently the tcp needed to change, so there is a good chance that
        # the tcp install and approach pos needs recalculation
        self.calc_tcp_target_pos_from_corrected_hole_pos()
        self.calc_tcp_approach_pos_from_corrected_hole_pos()
       
        if self.__is_tempf:
            if abs(self.diam() - 5.055) < 0.1:
                if self.__in_ee:
                    send_message("set_tool_center_point____setting TCP to " + TCP_NAME_DIAM_5_TIP + " for fastener " + self.uid() + "\nForce and compliance are turned off to enable this.")
                    set_tcp(TCP_NAME_DIAM_5_TIP)
                    return True
                else:
                    send_message("set_tool_center_point____setting TCP to " + TCP_NAME_LISI_TIP_NO_TEMPF + " for fastener " + self.uid() + "\nForce and compliance are turned off to enable this.")
                    set_tcp(TCP_NAME_LISI_TIP_NO_TEMPF)
                    return True
        else:
            if abs(self.diam() - 5.055) < 0.1:
                if abs(self.grip_length() - 9) < 0.1: #For dia code 6 and grip code 9
                    if self.__in_ee:
                        send_message("set_tool_center_point____setting TCP to " + TCP_NAME_DIAM_6_AND_GRIP_9_TIP + " for fastener " + self.uid() + "\nForce and compliance are turned off to enable this.")
                        set_tcp(TCP_NAME_DIAM_6_AND_GRIP_9_TIP)
                        return True
                    else:
                        send_message("set_tool_center_point____setting TCP to " + TCP_NAME_PERM_HAND_TOOL + " for fastener " + self.uid() + "\nForce and compliance are turned off to enable this.")
                        set_tcp(TCP_NAME_PERM_HAND_TOOL)
                        return True
               
                elif abs(self.grip_length() - 6) < 0.1: #For dia code 6 and grip code 6
                    if self.__in_ee:
                        send_message("set_tool_center_point____setting TCP to " + TCP_NAME_DIAM_6_AND_GRIP_6_TIP + " for fastener " + self.uid() + "\nForce and compliance are turned off to enable this.")
                        set_tcp(TCP_NAME_DIAM_6_AND_GRIP_6_TIP)
                        return True
                    else:
                        send_message("set_tool_center_point____setting TCP to " + TCP_NAME_PERM_HAND_TOOL + " for fastener " + self.uid() + "\nForce and compliance are turned off to enable this.")
                        set_tcp(TCP_NAME_PERM_HAND_TOOL)
                        return True             
        
        send_message("set_tool_center_point____tool center point could not be set for fastener " + self.uid())
       
        return False
   
 
    def shaft_height(self):
        """
        returns the height of the shaft that is sticking out when installed in mm
        """
        return self.__shaft_height
 
 
    def set_shaft_height(self, val):
        """
        sets the height of the shaft that is sticking out when installed in mm
        """
        self.__shaft_height = val
 
 
    def min_stack(self):
        """
       returns the minimum stack in mm
        """
        return self.__min_stack
 
 
    def set_min_stack(self, val):
        """
        sets the minimum stack in mm
        """
        self.__min_stack = val
 
 
    def max_stack(self):
        """
        returns the maximum stack in mm
        """
        return self.__max_stack
 
 
    def set_max_stack(self, val):
        """
        sets the maximum stack in mm
        """
        self.__max_stack = val
 
 
    def set_nom_axis_system_to_fast_nom_position(self):
        """
        Set DR_USER_NOM on the nominal hole position of this fastener
        """
        overwrite_user_cart_coord(DR_USER_NOM, self.nom_pos(), ref=DR_BASE)
       
        # also set the opposite axis system to enable clockwise and counterclockwise spiral moves
        x, y, z, a, b, c = self.nom_pos()
        overwrite_user_cart_coord(DR_USER_NOM_OPP, posx(x, y, z, a - 90, b + 90, c - 90), ref=DR_BASE)
 
 
    def calc_and_set_corrected_pos(self, corr_lst):
        """
        Function that corrects the nominal fastener position based on earlier installed positions
       
        :param corr_lst: list[cl_fastener], the list of fasteners that provide the correction
       
        1.  Get all installed fasteners from the input list
        2.  Calculate all distances between all nominal holes already inserted and the next to be inserted fastener.
            Calculate the vector from the next to be inserted fastener to all nominal holes already inserted and .
        3.  Order the list of inserted holes: smallest distance first
        4.  Loop through the list of nominal hole positions already inserted. Start a loop until all points are processed
            a.           Get the first unprocessed hole location from the hole position in the list (this is the closest position)
            b.           Get the next unprocessed hole location from the hole position in the list
                i.        Calculate the angle between the vectors to â€˜aâ€™ and â€˜bâ€™. 
                    (Notice that +1 will be in the same direction of the vector to the closest hole position.
                    -1 will mean that the point is in the opposite direction).
                ii.       If the value is smaller than GET_WEIGHTED_AVERAGES_MIN_ANGLE then both hole locations are more or less
                    in opposite direction as seen from the next to be inserted hole. We only want holes that are more or less opposite to each other,
                    so the next to be inserted hole is more or less between them. Calculate the weighted average from these two hole positions.
                    1.   Calculate the sum of both distances to the next to be inserted hole
                    2.   Calculate the factors by dividing the sum by the individual distances of both hole positions
                    3.   Sum the factors
                    4.   Divide the factors by this sum, so the sum of the factors becomes one.
                    5.   Multiply the deviations (dx, dy, dz, da, db, dc) of each hole position with the normalized factors and sum them.
                    6.   Calculate the average distance of the hole positions to the next to be inserted hole position.
                    7.   Remember the estimated deviation of the next to be inserted hole together with the average distance of the hole.
                   8.   Remove the hole positions from the list and process the remaining list.
                iii.      Remove the hole positions from the list and process the remaining list if none of the values is smaller than -.5.
                        This can be because the fastener is near the end of a row or at the corner of a square pattern,
                        or just simply because the list has an uneven amount of hole locations.
            c.           Exit loop 4 if all hole locations have been processed.
        5.  Now we have a list of estimates for the deviation of the next to be inserted hole based on earlier inserted hole deviations.
            Each estimate has an average distance of the points it is based on.
        6.  Create a weighted average from this list.
            a.           Calculate the sum of all estimate distances
            b.           Calculate the factors by dividing the sum by the individual distances of both hole positions
            c.           Sum the factors
            d.           Divide the factors by this sum, so the sum of the factors becomes one.
            e.           Multiply the deviations (dx, dy, dz, da, db, dc) of each estimate with the normalized factors and sum them.
            f.            This sum is the expected deviation for the next to be inserted hole
        7.  Return the expected deviation for the next to be inserted hole
 
        ATTENTION: Will set DR_USER_NOM on the nominal hole position of this fastener.
        """

        # to make sure this object is not included in the corr_lst
        # and this is the case if no fasteners are found to correct with
        self.__xy_pos_pred_acc = TEMPF_DEFAULT_POSITIONAL_DEVIATION
        self.__z_pos_pred_acc = TEMPF_DEFAULT_POSITIONAL_DEVIATION
        self.__dir_pred_acc = TEMPF_DEFAULT_ORIENTATION_DEVIATION
        self.__corrected_pos = self.nom_pos()
 
        # At least three fasteners must be installed first
        if len(corr_lst) < 4:
            send_message("calc_and_set_corrected_pos____fastener " + self.uid() + " has no fasteners to correct with.")
            return 0
 
        send_message("calc_and_set_corrected_pos____fastener " + self.uid() + " has {} fasteners to correct with.".format(len(corr_lst)))
 
        # calculate all distances and vectors to the fastener and set all fasteners to unprocessed
        for f in corr_lst:
            f.set_distance_to_fastener(self)
            f.set_vector_to_fastener(self)
 
        # sort the list. The shortest distance fastener first
        corr_lst.sort()
 
        # get a list of tuples with (average distance, weighted average position deviation, pos deviation, dir deviation)
        ap_lst = get_weighted_averages(corr_lst)
 
        # ensure that DR_USER_NOM is at the nominal location of this fastener
        self.set_nom_axis_system_to_fast_nom_position()
           
        if len(ap_lst) > 0:
 
            # calculate the corrected position and potential position and direction deviation
            a_pos, self.__xy_pos_pred_acc, self.__z_pos_pred_acc, self.__dir_pred_acc = get_weighted_pos_dev(ap_lst)
 
            # store it in DR_BASE axis system
            self.__corrected_pos = coord_transform(a_pos, DR_USER_NOM, DR_BASE)
           
            self.calc_tcp_target_pos_from_corrected_hole_pos()
            self.calc_tcp_approach_pos_from_corrected_hole_pos()
           
            send_message("calc_and_set_corrected_pos____fastener " + self.uid() + self.corr_pos_string())
           
            return 1
        else:
 
            send_message("calc_and_set_corrected_pos____fastener " + self.uid() + " has no fastener pairs to correct with.")
            return 0
 
 
    def set_install_pos_from_tcp_position(self):
        """
        Function used to store the position where the fastener is installed in DR_BASE
        from the current position. This position is at the hole entry point.
       
        The tcp is at the tip of the fastener if self.in_ee() is True
        In all other cases the tcp is at the top of the fastener.
        """
       
        #Shift the EE if slightly stressed
        #adjust_xy_location()
           
        # get the current position of the TCP (tip of the fastener)
        insert_pos, sol = get_current_posx(ref=DR_BASE)
       
        if self.in_ee():
            delta = -self.__tcp_tip_distance
        else:
            delta = self.__tcp_top_distance
       
        # calculate the position of the hole entry point
        self.set_installed_pos(translate_pos(insert_pos, 0, 0, delta))
       
        # set the deviations between corrected and installed position
        self.calc_xy_pos_pred_acc()
        self.calc_z_pos_pred_acc()
        self.calc_dir_pred_acc()
       
        self.log_inst_pos()
 
    
    def calc_xy_pos_pred_acc(self):
        """
        Calculate and store the distance in the xy plane of DR_USER_NOM between
        the installed position and the corrected position.
        This can be used to estimate the accuracy of the correction.
        """
        cp = coord_transform(self.__corrected_pos, DR_BASE, DR_USER_NOM)
        ci = coord_transform(self.__installed_pos, DR_BASE, DR_USER_NOM)
       
        dx = cp[0] - ci[0]
        dy = cp[1] - ci[1]
      
        self.__xy_pos_pred_acc = sqrt(dx * dx + dy * dy)
 
    
    def calc_z_pos_pred_acc(self):
        """
        Calculate and store the distance in the z-dir of DR_USER_NOM between
        the installed position and the corrected position.
       This can be used to estimate the accuracy of the correction.
        """
        cp = coord_transform(self.__corrected_pos, DR_BASE, DR_USER_NOM)
        ci = coord_transform(self.__installed_pos, DR_BASE, DR_USER_NOM)
       
        self.__z_pos_pred_acc =  abs(cp[2] - ci[2])
 
    
    def calc_dir_pred_acc(self):
        """
        Calculate and store the angle between the z-dir of
        the installed position and the corrected position.
        This can be used to estimate the accuracy of the correction.
        """
        ix, iy, iz, ia, ib, ic = self.__installed_pos
        cx, cy, cz, ca, cb, cc = self.__corrected_pos
 
        # get the vectors of the x-axis, y-axis and z-axis from the euler angles
        i_vx_axis, i_vy_axis, i_vz_axis = transpose(eul2rotm([ia, ib, ic]))
        c_vx_axis, c_vy_axis, c_vz_axis = transpose(eul2rotm([ca, cb, cc]))
 
        self.__dir_pred_acc =  Pi * vector_angle(i_vz_axis, c_vz_axis) / 180.0
 
    
    def calc_tcp_target_pos_from_corrected_hole_pos(self):
        """
        Calculate the target tcp position from the corrected hole position in DR_BASE
        The TCP is at the tip of the fastener, when the fastener is in the end effector.
        """
        if self.in_ee():
            delta = self.__tcp_tip_distance
        else:
            delta = -self.__tcp_top_distance

        self.__tcp_target_pos = translate_pos(self.__corrected_pos, 0, 0, delta)
 
    
    def calc_tcp_approach_pos_from_corrected_hole_pos(self):
        """
        Calculate the target tcp position for safe approach from corrected hole position in DR_BASE
        """
        self.__tcp_approach_pos = translate_pos(self.__corrected_pos, 0, 0, -GLOBAL_CLEARANCE_DURING_MOVEMENTS - SAFE_Z_GAP - SAFE_Z_GAP)
   
 
    def get_installed_position_in_axis_system_at_nom_pos(self):
        """
        returns the installed position in axis system at nominal position.
        Notice: a,b,c rotations cannot be simply subtracted from each other.
        ATTENTION: Will set DR_USER_NOM on the nominal hole position of this fastener.
        """
        # ensure that DR_USER_NOM is at the nominal location of this fastener
        self.set_nom_axis_system_to_fast_nom_position()
 
        # return the installed position in the DR_USER_NOM axis system
        return coord_transform(self.__installed_pos, DR_BASE, DR_USER_NOM)
 
 
    def get_corrected_position_in_axis_system_at_nom_pos(self):
        """
        returns the corrected position in axis system at nominal position.
        ATTENTION: Will set DR_USER_NOM on the nominal hole position of this fastener.
        """
        # ensure that DR_USER_NOM is at the nominal location of this fastener
        self.set_nom_axis_system_to_fast_nom_position()
 
        # return the installed position in the DR_USER_NOM axis system
        return coord_transform(self.__corrected_pos, DR_BASE, DR_USER_NOM)
   
 
    def corr_pos_string(self):
        """
        returns the corrected position in axis system at nominal position and DR_BASE.
        ATTENTION: Will set DR_USER_NOM on the nominal hole position of this fastener.
        """
        # get the installed position in the DR_USER_NOM axis system
        s1 = "\ncorrected position w.r.t. nominal position:\n" + pos_string(self.get_corrected_position_in_axis_system_at_nom_pos())
 
        s2 = "\n" + pos_string(self.__corrected_pos)
       
        s3 = "\nest xy pos tol: {}mm; est z pos tol: {}mm; est dir tol: {}deg".format(round(self.__xy_pos_pred_acc, 3), round(self.__z_pos_pred_acc, 3), round(self.__dir_pred_acc, 3))
 
        return s1 + s2 + s3
 
    def log_corr_pos(self):
        send_message("log_corr_pos____fastener " + self.uid() + self.corr_pos_string())
 
    def pop_up_corr_pos(self):
        tp_popup("fastener " + self.uid() + self.corr_pos_string())
 
 
    def inst_pos_string(self):
        """
        returns the installed position in axis system at nominal position and DR_BASE.
        ATTENTION: Will set DR_USER_NOM on the nominal hole position of this fastener.
        """
        # get the installed position in the DR_USER_NOM axis system
        s1 = " installed position w.r.t. nominal position:\n" + \
            pos_string(self.get_installed_position_in_axis_system_at_nom_pos())
 
        s2 = "\ninstalled position:\n" + pos_string(self.__installed_pos)
 
        return s1 + s2
 
    def log_inst_pos(self):
        send_message("log_inst_pos____fastener " + self.uid() + self.inst_pos_string())
 
    def pop_up_inst_pos(self):
        tp_popup("fastener " + self.uid() + self.inst_pos_string())
 
 
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
       
 
class cl_fl_container():
    """
    Class that contains a location and a fastener object.
 
    This could be either a product or a fastener storage location.
    """ 
    
    def __init__(self, loc: cl_fastener_location = None, fast: cl_fastener = None):
        """
        Function
       
        :param loc: cl_fastener_location,
        :param fast: cl_fastener,
        """
        self.loc = loc
        self.fast = fast
       
        if self.has_both():
            if not self.is_similar(loc, fast):
                send_message("cl_fl_container_init____fastener {} has been added to location {} \n\
                           fastener location was not the same as the location\n\
                           fastener location has been made similar.".format(fast.uid(), loc.uid()))
                self.set
   
    
    def is_similar(self, loc = None, fast = None, diff = 0.01):
        """
        Function
       
        :param loc: cl_fastener_location, a fastener instance
        :param fast: cl_fastener, a location instance
        :param diff: float, the difference that is allowed while still regarded as similar
 
        :return: bool
        """
        d = self.is_same_diam(loc, fast, diff)
        s = self.is_same_stack(loc, fast, diff)
        p = self.is_same_pos(loc, fast)
        t = self.is_loc_within_fast_stack_limits(fast)
       
        return d and s and p and t
   
    def is_same_diam(self, loc = None, fast = None, diff = 0.01):
        """
        Function
       
        :param loc: cl_fastener_location, a fastener instance
        :param fast: cl_fastener, a location instance
        :param diff: float, the difference that is allowed while still regarded as similar
 
        :return: bool, False if nothing to compare
        """
        if loc is None and fast is None:
            if self.has_both():
                return abs(self.fast.diam() - self.loc.diam()) < diff
            else:
                return False
        elif loc is not None and fast is not None:
            return abs(fast.diam() - loc.diam()) < diff
        elif self.has_loc() and fast is not None:
            return abs(fast.diam() - self.loc.diam()) < diff
        elif loc is not None and self.has_fast():
            return abs(self.fast.diam() - loc.diam()) < diff
        else:
            return False
   
    
    def is_same_stack(self, loc = None, fast = None, diff = 0.01):
        """
        Function
       
        :param loc: cl_fastener_location, a fastener instance
        :param fast: cl_fastener, a location instance
        :param diff: float, the difference that is allowed while still regarded as similar
 
        :return: bool, False if nothing to compare
        """
        if loc is None and fast is None:
            if self.has_both():
                return abs(self.fast.stack_thickness() - self.loc.stack_thickness()) < diff
            else:
                return False
        elif loc is not None and fast is not None:
            return abs(fast.stack_thickness() - loc.stack_thickness()) < diff
        elif self.has_loc() and fast is not None:
            return abs(fast.stack_thickness() - self.loc.stack_thickness()) < diff
        elif loc is not None and self.has_fast():
            return abs(self.fast.stack_thickness() - loc.stack_thickness()) < diff
        else:
            return False
 
    
    def is_loc_within_fast_stack_limits(self, fast):
        """
        Function to check whether the stack thickness is within the
        fastener limits.
   
        :param fast: cl_fastener, the fastener object
        :return: bool, True if within limits
        """
        if fast is not None and self.loc is not None:
            stack_thickness = self.loc.stack_thickness()
            t_max = fast.max_stack()
            t_min = fast.min_stack()
            if stack_thickness <= t_max and stack_thickness >= t_min:
                return True
            else:
                return False
        else:
            return True
       
    
    def is_same_pos(self, loc = None, fast = None):
        """
        Function
       
        Using the cl_fastener_location __eq__ functionality
       
        :param loc: cl_fastener_location, a fastener instance
        :param fast: cl_fastener, a location instance
 
        :return: bool, False if nothing to compare
        """
        if loc is None and fast is None:
            if self.has_both():
                return self.fast == self.loc
            else:
                return False
        elif loc is not None and fast is not None:
            return loc == fast
        elif fast is not None and self.has_loc():
            return fast == self.loc
        elif loc is not None and self.has_fast():
            return self.fast == loc
        else:
            return False
        
            
    def has_no_loc(self):
        """
        Function
 
        :return: bool
        """
        return self.loc is None
   
    
    def has_no_fast(self):
        """
        Function
 
        :return: bool
        """
        return self.fast is None
   
    
    def has_loc(self):
        """
        Function
 
        :return: bool
        """
        return self.loc is not None
   
    
    def has_fast(self):
        """
        Function
 
        :return: bool
        """
        return self.fast is not None
   
    
    def has_nothing(self):
        """
        Function
 
        :return: bool
        """
        return self.has_no_loc() and self.has_no_fast()
   
    
    def has_both(self):
        """
        Function that will return whether there is both a fastener as
        a location as object.
 
        :return: bool, whether there is both a fastener as
                       a location as object.
        """
        return self.has_loc() and self.has_fast()
   
    
    def has_uid(self, uid):
        """
        Function
 
        :return: bool
        """
        return self.loc.uid() == uid or self.fast.uid() == uid
       
    
    def add_loc(self, uid, diam, stack_thickness, nom_pos):
        """
        Function to add a location to the fastener and location container
       
        :param uid: str,
        :param diam: float,
        :param stack_thickness: float,
        :param nom_pos: posx,
           
        :return: bool, whether the location has been succeesfully added
        """
        if self.has_no_loc():
            loc = cl_fastener_location(uid, diam, stack_thickness, nom_pos)
            if self.has_no_fast():
                self.loc = loc
                return True
            elif self.is_same_pos(loc = loc) and self.is_same_stack(loc = loc) and self.is_same_diam(loc = loc):
                self.loc = loc
                return True
           
        send_message("add_loc____location with uid {} could not be added to the fastener and location container.".format(uid))
        return False
   
    
    def add_fast(self, uid, fast_install_pos, diam, shaft_height,
                  min_stack, max_stack, tcp_tip_dist, tcp_top_dist,
                  in_storage, in_ee, in_product, in_bin, is_tempf):
        """
        Function to add a fastener to the fastener and location container
 
        :param uid: str,
        :param fast_install_pos: posx, will take the nominal position if not specified
        :param shaft_height
        :param min_stack
        :param max_stack
        :param tcp_tip_dist
        :param tcp_top_dist
        :param in_storage: bool,
        :param in_ee: bool,
        :param in_product: bool,
        :param in_bin: bool,
        :param is_tempf: bool
           
        :return: bool, whether the fastener has been succeesfully added
        """
        if self.has_no_loc():
            return False
           
        if fast_install_pos is None:
            fast_install_pos = self.loc.nom_pos() #fast_nom_pos
           
        if self.has_no_fast():
            fast_nom_pos = self.loc.nom_pos()
            diam = self.loc.diam()
            stack_thickness = self.loc.stack_thickness()     
            fast_corrected_pos = fast_nom_pos
 
            self.fast = cl_fastener(uid, diam, stack_thickness, fast_nom_pos,
                                     fast_corrected_pos, fast_install_pos,
                                     in_storage, in_ee, in_product, in_bin, is_tempf)
 
        else:
            self.fast.set_installed_pos(fast_install_pos)
            if in_storage:
                self.fast.set_as_in_storage()
            elif in_ee:
                self.fast.set_as_in_ee()
            elif in_product:
                self.fast.set_as_in_product()
            elif in_bin:
                self.fast.set_as_in_bin()
 
            if is_tempf:
                self.fast.set_as_tempf()
            else:
                self.fast.set_as_permf()
 
        self.fast.set_shaft_height(shaft_height)
        self.fast.set_min_stack(min_stack)
        self.fast.set_max_stack(max_stack)
        self.fast.set_tcp_tip_distance(tcp_tip_dist)
        self.fast.set_tcp_top_distance(tcp_top_dist)
 
 
        return True
   
    
    def remove_loc(self):
        l = self.loc
        self.loc = None
        return l
   
    
    def remove_fast(self):
        tf = self.fast
        self.fast = None
        return tf
   
    
    def has_diam(self, diam, diff = 0.01):
        """
        Function
       
        :param diam: float,
        :param diff: float, the difference that is allowed while still regarded as similar
 
        :return: bool
        """
        if self.has_loc():
            o_diam = self.loc.diam()
        elif self.has_fast():
            o_diam = self.fast.diam()
        else:
            o_diam = 0
           
        return abs(o_diam - diam) < diff
 
 
    def has_stack(self, stack, diff = 0.01):
        """
        Function
       
        :param stack_thickness: float,
        :param diff: float, the difference that is allowed while still regarded as similar
 
        :return: bool
        """
        if self.has_loc():
            o_stack = self.loc.stack_thickness()
        elif self.has_fast():
            o_stack = self.fast.stack_thickness()
        else:
            o_stack = 0
           
        return abs(o_stack - stack) < diff
 
    def has_grip(self, grip, diff = 0.01):
        """
        Function
       
        :param grip: float,
        :param diff: float, the difference that is allowed while still regarded as similar
 
        :return: bool
        """
        if self.has_loc():
            o_grip = self.loc.grip_length()
        elif self.has_fast():
            o_grip = self.fast.grip_length()
        else:
            o_grip = 0
           
        return abs(o_grip - grip) < diff
 
 
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
       
 
class cl_f_container(cl_uid):
    """
    Class that contains a fastener container.
 
    This could be either a product or a temproary or permanent fastener storage location.
    """ 
    
    def __init__(self, uid = "", max_obstacle_heigth = GLOBAL_CLEARANCE_DURING_MOVEMENTS):
        """
        Init function of the fastener container.
       
        :param uid: str, the uid of the fastener container.
        :param max_obstacle_heigth: float, the height of the largest obstacle.
        """
        super().__init__(uid)
       
        self.holes_and_fast_lst = []    # list with list cl_fl_container
        self.bin_contents = []              # list with cl_fastener instances
        self.bin_location = None                               # posx
        self.max_obstacle_height = max_obstacle_heigth         # height of the biggest obstacle
        #TODO make sure the program uses this max_obstacle_height
 
 
    def add_loc_to_holes_and_fast_lst(self, uid, diam, stack_thickness, nom_pos):
        """
        Function to add a location to the holes_and_fast_lst
       
        :param uid: str,
        :param diam: float,
        :param stack_thickness: float,
        :param nom_pos: posx,
           
        :return: bool, whether the location has been succeesfully added
        """
        loc = cl_fastener_location(uid, diam, stack_thickness, nom_pos)
       
        # add to list if the same location
        for s in self.holes_and_fast_lst:
            if s.has_loc():
                if s.is_same_pos(loc = loc) and s.is_same_stack(loc = loc) and s.is_same_diam(loc = loc):
                    send_message("add_loc_to_holes_and_fast_lst____Location with uid {} overwritten with location with uid {}.".format(s.loc.uid() ,uid))
                    s.loc = loc
                    return True
               
        # add the location to a new spot in holes_and_fast_lst
        self.holes_and_fast_lst.append(cl_fl_container(loc = loc))
       
        return True
 
    def add_fast_to_loc_with_uid(self, uid, loc_uid, fast_install_pos,
                                 diam, shaft_height, min_stack, max_stack, tcp_tip_dist, tcp_top_dist,
                                 in_storage, in_ee, in_product, in_bin, is_tempf):
        """
        Function to add a fastener to the holes_and_fast_lst using
        the uid of the location.
       
        The nominal position, diameter and stack thickness of the
        fastener are taken from the hole location
       
        :param uid: str,
        :param loc_uid: str,
           
        :return: bool, whether the fastener has been succeesfully added
        """
       
        loc_lst_id = self.get_loc_lst_id_by_uid(loc_uid)
       
        if loc_lst_id >= 0:
            return self.holes_and_fast_lst[loc_lst_id].add_fast(uid, fast_install_pos, diam, shaft_height,
                                                                min_stack, max_stack, tcp_tip_dist, tcp_top_dist,
                                                                in_storage, in_ee, in_product, in_bin, is_tempf)
 
        return False
 
 
    def add_fast_to_holes_and_fast_lst(self, uid, diam, stack_thickness, fast_nom_pos,
                                       fast_corrected_pos=None, fast_install_pos=None,
                                       in_storage = False, in_ee = False, in_product=False, in_bin=False, is_tempf = True):
        """
        Function to add a fastener to the holes_and_fast_lst
       
        :param uid: str,
        :param diam: float,
        :param stack_thickness: float,
        :param fast_nom_pos: posx,
        :param fast_corrected_pos: posx,
        :param fast_install_pos: posx,
        :param in_storage: bool,
        :param in_ee: bool,
        :param in_product: bool,
        :param in_bin: bool,
           
        :return: bool, whether the fastener has been succeesfully added
        """
       
        if fast_corrected_pos is None:
            fast_corrected_pos = fast_nom_pos
           
        if fast_install_pos is None:
            fast_install_pos = fast_nom_pos
       
        #create the cl_fastener instance
        tf = cl_fastener(uid, diam, stack_thickness, fast_nom_pos,
                         fast_corrected_pos, fast_install_pos,
                         in_storage, in_ee, in_product, in_bin, is_tempf)
       
        # add to list if the same location
        for s in self.holes_and_fast_lst:
            if s.is_same_pos(fast = tf) and s.is_same_stack(fast = tf) and s.is_same_diam(fast = tf):
                s.fast = tf
                return True
 
        # add the fast to a new spot in holes_and_fast_lst
        self.holes_and_fast_lst.append(cl_fl_container(fast = tf))
       
        return True
   
    
    def remove_loc_from_holes_and_fast_lst(self, uid):
        """
        Function to remove a location from the holes_and_fast_lst
       
        :param uid: str, the location to be removed
           
        :return: cl_fastener_location, the removed location
        """
        loc_lst_id = self.get_loc_lst_id_by_uid(uid)
       
        if loc_lst_id > 0:
            if self.holes_and_fast_lst[loc_lst_id].has_no_fast():
                # remove the entire position from the list
                c = self.holes_and_fast_lst[loc_lst_id].pop()
                loc = c.loc
            else:
                loc = self.holes_and_fast_lst[loc_lst_id].remove_loc()
            return loc
        else:
            send_message("remove_loc_from_holes_and_fast_lst____unable to remove location {} from the holes_and_fast_lst".format(uid))
            return None
 
 
    def remove_fast_from_holes_and_fast_lst(self, uid):
        """
        Function to add a fastener to the holes_and_fast_lst
       
        :param uid: str,
           
        :return: cl_fastener, the fastener that has been removed
        """
        loc_lst_id = self.get_loc_lst_id_by_uid(uid)
       
        return self.remove_fast_from_location(loc_lst_id)
   
    
    def check_lst_lenght(self, loc_lst_id):
        """
        Function to check whether the location list ID is within the list length.
       
        Notice that the zero location is not used.
       
        :param loc_lst_id: int, the location number
       
        :return: bool, whether the location list ID is within the list length
        """
        if loc_lst_id < 0:
            return False
        else:
            if loc_lst_id >= len(self.holes_and_fast_lst):
                send_message("check_lst_lenght____{} location id {} is larger than the list length.".format(self.uid(), loc_lst_id))
                return False
            else:
                return True
       
        
    def loc_is_empty(self, loc_lst_id):
        """
        Function to check whether a location is empty.
       
        :param loc_lst_id: int, the location number
       
        :return: bool, True if there is no fastener in that location
        """
        if not self.check_lst_lenght(loc_lst_id):
            return False
        else:
            if self.holes_and_fast_lst[loc_lst_id].has_no_fast():
                send_message("loc_is_empty____Action {}: location {} is already occupied.".format(self.uid(), self.holes_and_fast_lst[loc_lst_id].loc.uid()))
                return False
            else:
                return True
   
    
    def check_diam(self, fast, loc_lst_id, diff = 0.01):
        """
        Function to check whether the diameters of a fastener and
        storage location match.
       
        :param fast: cl_fastener, the fastener object
        :param loc_lst_id: int, the location number
       
        :return: bool, True if the difference in diameter is smaller than diff
        """
        if self.check_lst_lenght(loc_lst_id):
            if self.holes_and_fast_lst[loc_lst_id].is_same_diam(fast = fast, diff = diff):
                send_message("check_diam____Action {}: fastener {} and location {} have a different diameter."
                      .format(self.uid(), fast.uid(), self.holes_and_fast_lst[loc_lst_id].fast.uid()))
                return False
            else:
                return True
        else:
            return False
   
    
    def check_stack_thickness(self, fast, loc_lst_id):
        """
        Function to check whether the stack thickness is within the
        fastener limits.
       
        :param fast: cl_fastener, the fastener object
        :param loc_lst_id: int, the location number
               
        :return: bool, True if within the limits
        """
        if self.check_lst_lenght(loc_lst_id):
            return self.holes_and_fast_lst[loc_lst_id].is_loc_within_fast_stack_limits(fast)
        else:
            return False
               
    
    def same_pos(self, fast, loc_lst_id):
        """
        Function to check whether the locations of a fastener and
        storage location match.
       
        Using the cl_fastener_location __eq__ functionality
       
        :param fast: cl_fastener, the fastener object
        :param loc_lst_id: int, the location number
       
        :return: bool, True if the location is similar
        """
        if self.check_lst_lenght(loc_lst_id):
            return self.holes_and_fast_lst[loc_lst_id].is_same_pos(fast = fast)
        else:
            return False
   
    
    def check_fast_and_location(self, fast, loc_lst_id):
        """
        Function to check whether
        - the location list ID is within the list length
        - a location is empty
        - the diameters of a fastener and storage location match
        - the locations of a fastener and storage location match
        - the stack thickness is within the min and max of the fastener
       
        :param fast: cl_fastener, the fastener object
        :param loc_lst_id: int, the location number
       
        :return: bool, True if it passes all tests
        """
        if self.check_lst_lenght(loc_lst_id):
            s = self.holes_and_fast_lst[loc_lst_id].is_similar(fast = fast)
            e = self.holes_and_fast_lst[loc_lst_id].has_no_fast()
            return s and e
        else:
            return False
   
    
    def add_fast_to_location(self, fast, loc_lst_id):
        """
        Function to add a fastener object to a storage location
       
        :param fast: cl_fastener, the fastener object
        :param loc_lst_id: int, the location number
       
        :return: bool, True if successful (also passed check_fast_and_location function)
        """
        if self.check_fast_and_location(fast, loc_lst_id):
            self.holes_and_fast_lst[loc_lst_id].fast = fast
            return True
        else:
            return False
 
    
    def add_fast_to_bin(self, fast):
        """
        Function to add a fastener into the bin
        Can only be done when the container is a storage location.
       
        :param fast: cl_fastener, the fastener object
       
        :return: bool, success
        """
        self.bin_contents.append(fast)
        fast.set_as_in_bin()
        return True
 
    
    def set_location_as_fast_target(self, fast: cl_fastener, loc_lst_id: int):
        """
        Function to set the storage location as the target of a
        fastener object.
       
        :param fast: cl_fastener, the fastener object
        :param loc_lst_id: int, the location number
       
        :return: int, loc_lst_id if successful (also passed checks), -1 if unsuccessful
        """
        if self.check_lst_lenght(loc_lst_id):
            tl = self.holes_and_fast_lst[loc_lst_id]
            if tl.has_no_fast():
                if tl.is_same_diam(fast = fast) and tl.is_loc_within_fast_stack_limits(fast = fast):
                    fast.set_nom_pos(self.holes_and_fast_lst[loc_lst_id].loc.nom_pos())
                    fast.set_stack_thickness(self.holes_and_fast_lst[loc_lst_id].loc.stack_thickness())
                    fast.reset_to_nom_pos_only()
                    return loc_lst_id
        return -1
       
    
    def set_bin_location_as_fast_target(self, fast: cl_fastener):
        """
        Function to set the bin location as the target of a fastener object.
        Can only be done when the container is a storage location.
       
        :param fast: cl_fastener, the fastener object
       
        :return: bool, success
        """
        fast.set_nom_pos(self.bin_location)
        fast.set_stack_thickness(-1)
        fast.reset_to_nom_pos_only()
        return True

    
    def get_loc_lst_id_by_uid(self, uid):
        """Function to get the location id based on a fastener or location uid
       
        :param uid: str, the uid of the fastener
       
        :return: int, the id number if successful, -1 if unsuccessful
        """
        for i, ht in enumerate(self.holes_and_fast_lst):
            if ht.has_loc():
                if ht.loc.uid() == uid:
                    return i
            if ht.has_fast():
                if ht.fast.uid() == uid:
                    return i
        send_message("get_loc_lst_id_by_uid____unable to find a fastener or location with uid {}.".format(uid))
        return -1
       
    
    def remove_fast_from_location(self, loc_lst_id):
        """
        Function to remove a fastener object from a container location
        
        :param loc_lst_id: int, the location number
       
        :return: cl_fastener | None
        """
        if not self.check_lst_lenght(loc_lst_id):
            return None
        else:
            return self.holes_and_fast_lst[loc_lst_id].remove_fast()
       
        
    def find_fast_id_of_diam(self, diam):
        """
        Function to find the list ID of a location with a fastener
        in the container with a certain diameter
       
        returns the ID of the storage location if successful
        returns 0 if no emty spot can be found
       
        :param diam: float, the diameter of the fastener
        """
        for i, s in enumerate(self.holes_and_fast_lst):
            if s.has_fast():
                if s.has_diam(diam):
                    return i
               
        send_message("find_fast_id_of_diam____no fastener available with diameter {}.".format(diam))
        return 0
   
    
    def find_empty_spot_of_diam(self, diam):
        """
        Function to find the ID of an empty spot with a certain diameter
       
        :param diam: float, the diameter of the fastener
       
        :return: int, the ID of the location if successful, -1 if no empty spot can be found
        """
        for i, s in enumerate(self.holes_and_fast_lst):
            if s.has_no_fast():
                if s.has_diam(diam):
                    return i
               
        send_message("find_empty_spot_of_diam____no empty spot available with diameter {}.".format(diam))
        return -1
   
 
    def find_empty_spot_and_set_as_target(self, fast: cl_fastener):
        """
        Function to find the ID of an empty spot with a certain diameter
        and set the location as target of the fastener
       
        :param fast: cl_fastener, the location number
       
        :return: int, the ID of the location if successful, -1 if no empty spot can be found
        """
        loc_lst_id = self.find_empty_spot_of_diam(fast.diam())
 
        return self.set_location_as_fast_target(fast, loc_lst_id)
   
 
    def number_fasts_of_diam(self, diam):
        """
        Function that returns the number of fasteners available with a certain diameter.
        
        :param diam: float, the diameter of the fastener
       
        :return: int, the number of fasteners available with a certain diameter
        """
        n = 0
        for s in self.holes_and_fast_lst:
            if s.has_fast():
                if s.has_diam(diam):
                    n += 1
       
        return n
   
    
    def number_empty_spots_of_diam(self, diam):
        """
        Function that returns the number of empty spots available with a certain diameter.
        
        :param diam: float, the diameter of the fastener
       
        :return: int, the number of empty spots available with a certain diameter
        """
        n = 0
        for s in self.holes_and_fast_lst:
            if s.has_no_fast():
                if s.has_diam(diam):
                    n += 1
       
        return n
   
    
    def number_fasteners_in_bin(self):
        """
       Function that returns the number of fasteners in the bin.
       
        :return: int, the number of fasteners in the bin
        """
        return len(self.bin_contents)
   
    
    def log_holes_and_fast_lst(self):
        """
        """
        string_out = "{} instances exist in the container {}.\n[".format(len(self.holes_and_fast_lst), self.uid())
        for i, ht in enumerate(self.holes_and_fast_lst):
            if ht.has_loc():
                string_out += "loc:{}; d{}, ".format(ht.loc.uid(), ht.loc.diam())
            if ht.has_fast():
                string_out += "temp:{}; d{}, ".format(ht.fast.uid(), ht.fast.diam())
        string_out += "]"
        send_message("log_holes_and_fast_lst___", string_out)
   
    
    def number_fasteners_of_diam_grip(self, diam, grip):
        """
        Function that returns the number of fasteners available with a certain diameter and grip length.
        
        :param diam: float, the diameter of the fastener
        :param grip: float, the grip length code of the fastener
        :return: int, the number of fasteners available with a certain diameter and grip length code
        """
        n = 0
        for s in self.holes_and_fast_lst:
            if s.has_fast():
                if s.has_diam(diam) and s.has_grip(grip):
                    n += 1
       
        return n   
        
    
    def find_fastener_id_of_diam_grip(self, diam, grip):
        """
        Function to find the list ID of a location with a fastener
        in the container with a certain diameter and grip
       
        returns the ID of the storage location if successful
        returns 0 if no empty spot can be found
       
        :param diam: float, the diameter of the fastener
        :param grip: float, the grip length code of the fastener
        """
        for i, s in enumerate(self.holes_and_fast_lst):
            f = s
            if f.has_fast():
                if f.has_diam(diam) and f.has_grip(grip) and not f.fast.in_bin():
                    return i
               
        send_message("find_fast_id_of_diam____no fastener available with diameter {}.".format(diam)) #add grip to error message
        return 0
 
 
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
  
 
class cl_agent():
    """
    Class that contains a list of actions that need to be done
    It also contains the functions to execute these actions
 
    The following actions are identified
 
    - Move to waypoint
    - Install a temp or perm fastener
    - Remove a fastener
    - Check whether the system has enough fasteners or free locations to work with
 
    """
 
    # TODO check this sometime     
    def __init__(self, tempf_storage: cl_f_container, permf_storage: cl_f_container, product: cl_f_container, pf_ee: cl_perm_fast_ee, tf_ee: cl_temp_fast_ee):
        """
        Function that initializes the cl_agent class.
       
        :param uid: str, the uid of the fastener container.
        :param tempf_storage: cl_f_container, fastener storage location.
        :param permf_storage: cl_f_container, permanent fastener storage location.
        :param product: cl_f_container, product.
        :param pf_ee: cl_perm_fast_ee, the active permanent fastener end effector instance
        :param tf_ee: cl_temp_fast_ee, the active fastener end effector instance
        """
 
        self.tempf_storage = tempf_storage
        self.permf_storage = permf_storage
        self.product = product
        self.pf_ee = pf_ee
        self.tf_ee = tf_ee
       
        self.actions = []    # list of cl_action
        self.waypoints = []  # list of cl_waypoint  
    
    
    def execute_uid(self, uid):
        """
        Function that executes an action with a certain uid
       
        :param uid: str, The uid of the action to execute
           
        :return: bool, returns True if successful
        """
        a = self._get_from_lst_by_uid(self.actions, uid, "", False)
           
        if a.is_cancelled():
            a.set_as_not_cancelled()
            send_message("execute____Action with uid {} was uncancelled and will be executed.".format(a.uid()))
 
        if not a.is_done():
            succes = False
 
            if a.is_move_waypoint():
                succes = self.move_to_waypoint(a.loc_uid(), a.speed())
            elif a.is_install_permf():
                succes = self.install_permf(a.loc_uid(), a.passing_wps, a.speed())
            elif a.is_install_tempf():
                succes = self.install_tempf(a.loc_uid(), a.passing_wps, a.speed())
            elif a.is_remove_tempf():
                succes = self.remove_tempf(a.loc_uid(), a.passing_wps, a.speed())
            else:
                send_message("execute____{}: unknown ation type: {}".format(a.uid(), a.a_type()))
 
            if succes:
                a.set_as_done()
 
        return_str = actions_str_to_server(agent.actions)
 
        send_message("", return_str)
       
        
    def execute_all(self, check_inventory = True):
        """
        Function that will execute all actions in the order given

        :param check_inventory: bool, Whether to check for correct inventory
           
        :return: bool, returns True if successful
        """
        if check_inventory:
            if not self.check_inventory():
                return False
       
        for a in self.actions:
            if not a.is_cancelled():
                self.execute_uid(a.uid())
           
    
    def move_to_waypoint(self, wp_uid, wait = True, speed = 100):
        """
        Function that
        
        :param wait: bool, Whether to continue directly or to wait until move is finished
            default: True, which will make the program wait untill the move is finished
           
        :return: bool, returns True if successful
        """
        w = self.get_waypoint_by_uid(wp_uid)
        change_operation_speed(speed)
        if wait:
            movel(w, ref=DR_BASE, r = BLEND_RADIUS_LARGE)
        else:
            amovel(w, ref=DR_BASE, r = BLEND_RADIUS_LARGE)
           
        return 1
 
    def install_permf(self, target_loc_uid = "", passing_wp = [], speed = 100):
        """
        Function to install a permanent fastener in the product.
       
        The function will
        1) find out what diameter is needed
        2) find a compatible fastener that is available in the storage location
        3) pick up the fastener
        4) move to the target location in the product through passing_wp
        5) insert and install the fastener
        6) retract the end effector away from the product
       
        :param target_loc_uid: str, the uid of the target location in the product
        :param speed: float, the speed as percentage of the maximum speed
        :param passing_wp: list[str] The waypoints to pass between pick up and install
           
        :return: bool, returns True if successful
        """
       
        prod_lst_id = self.product.get_loc_lst_id_by_uid(target_loc_uid)
       
        if prod_lst_id < 0:
            return False
       
        target_obj = self.product.holes_and_fast_lst[prod_lst_id]
       
        # find the diameter that needs to be installed
        diam = target_obj.loc.diam()
       
        # find the grip that needs to be installed
        grip = target_obj.loc.grip_length()
       
        storage_loc_id = self.permf_storage.find_fastener_id_of_diam_grip(diam, grip)
 
        source_obj = self.permf_storage.holes_and_fast_lst[storage_loc_id]
 
        # get the permf object
        permf = source_obj.fast
       
        # set the tcp correctly
        permf.set_tool_center_point()
       
        # pick up the fastener from the storage
        if not self._pick_up_fast(permf, False):
            # discard the fastener
            permf.set_as_in_bin()
           
            # return failure; the ee will be above the permf location
            return False
        else:   
            # remove the permf object from the storage location
            self.permf_storage.remove_fast_from_location(storage_loc_id)
 
            # set the product location as the permf target
            self.product.set_location_as_fast_target(permf, prod_lst_id)
           
            # move to the hole apprach position
            speed_limited_movej_on_posx(permf.tcp_approach_pos(), 100)
 
            # calculate the corrected position of the fastener
            # based on all inserted fasteners in the product
            # TODO perform calculation earlier in a seperate stream if this takes a while
            # permf.calc_and_set_corrected_pos(self._get_all_permfs_in_product())
           
            # insert the fastener into the product
            if self._insert_fast(permf, False):
                # add the fastener to the product
                if self.product.add_fast_to_location(permf, prod_lst_id):
                    # Not used for now
                    # reevaluate_deviations(permf, self._get_all_permfs_in_product())
                    permf.set_as_in_product()

                    return True
           
            return False
           
        
    def install_tempf(self, target_loc_uid = "", passing_wp = [], speed = 100):
        """
        Function to install a fastener in the product.
       
        The function will
        1) find out what diameter is needed
        2) find a compatible fastener that is available in the storage location
        3) pick up the fastener
        4) move to the target location in the product through passing_wp
        5) insert the fastener
        6) retract the end effector away from the product
       
        :param target_loc_uid: str, the uid of the target location in the product
        :param speed: float, the speed as percentage of the maximum speed
        :param passing_wp: list[str] The waypoints to pass between pick up and install
                   
        :return: bool, returns True if successful
        """
        # go to intended speed
        change_operation_speed(speed)

        prod_lst_id = self.product.get_loc_lst_id_by_uid(target_loc_uid)
       
        if prod_lst_id < 0:
            return False
       
        # find the diameter that needs to be installed
        diam = self.product.holes_and_fast_lst[prod_lst_id].loc.diam()
       
        # find the grip that needs to be installed
        # current assumption is that tempf is suitable for all grips
        # grip = self.product.holes_and_fast_lst[prod_lst_id].loc.grip_length()
       
        storage_loc_id = self.tempf_storage.find_fast_id_of_diam(diam)
       
        # get the tempf object
        tempf = self.tempf_storage.holes_and_fast_lst[storage_loc_id].fast
       
        # we do not use the installed position as correction 
        # since this position is not accurate due to cobot compliance
        # e.g. due to sagging during installation
        tempf.reset_to_nom_pos_only()
       
        # set the tempf tcp correctly
        tempf.set_tool_center_point()
        #tp_popup("Check fastener")

        # pick up the fastener from the storage
        if not self._pick_up_fast(tempf, True):
            # discard the fastener
            tempf.set_as_in_bin()
           
            # return failure; the ee will be above the tempf location
            return False
        else:   
            # remove the tempf object from the storage location
            self.tempf_storage.remove_fast_from_location(storage_loc_id)
 
            #tp_popup("Check fastener")
            # set the product location as the tempf target
            self.product.set_location_as_fast_target(tempf, prod_lst_id)

            speed_limited_movej_on_posx(tempf.tcp_approach_pos(), 100)
 
            # calculate the corrected position of the fastener
            # based on all inserted fasteners in the product
            # tempf.calc_and_set_corrected_pos(self._get_all_tempfs_in_product())
           
            # insert the fastener into the product
            if self._insert_fast(tempf, True):
                # add the fastener to the product
                if self.product.add_fast_to_location(tempf, prod_lst_id):
                    # Nor used for now
                    # reevaluate_deviations(tempf, self._get_all_tempfs_in_product())
                    tempf.set_as_in_product()

                    return True
           
            return False
           
    
    def remove_tempf(self, fastener_uid = "", passing_wp = [], speed = 100):
        """
        Function to remove a fastener from the product.
       
        The function will
        1) find out what diameter is needed
        2) find a compatible fastener that is available in the storage location
        3) pick up the fastener
        4) move to the target location in the storage through passing_wp
        5) insert the fastener
        6) retract the end effector away from the product
       
        :param fastener_uid: str, the uid of the fastener to be removed from the product
        :param speed: float, the speed as percentage of the maximum speed
        :param passing_wp: list[str] The waypoints to pass between pick up and install
          
        :return: bool, returns True if successful
        """
        prod_lst_id = self.product.get_loc_lst_id_by_uid(fastener_uid)
       
        if prod_lst_id < 0:
            return False
       
        # get the fastener object that needs to be removed
        tempf = self.product.holes_and_fast_lst[prod_lst_id].fast
       
        # find an empty spot with the correct diameter in the storage location
        storage_loc_id = self.tempf_storage.find_empty_spot_of_diam(tempf.diam())
        
        change_operation_speed(MOVE_SPEED)
 
        # we do not use the installed position as correction 
        # since this position is not accurate due to cobot compliance
        # e.g. due to sagging during installation
        tempf.reset_to_nom_pos_only()
       
        # set the tcp correctly
        tempf.set_tool_center_point()
       
        # pick up the fastener from the product
        if not self._pick_up_fast(tempf, True):
           
            self.tf_ee.reset_cobot_output_pins_incl_air()
 
            # return failure; the ee will be above the tempf location
            return False
        else:   
            # remove the tempf object from the storage location object
            self.product.remove_fast_from_location(prod_lst_id)
           
            # pass any defined waypoints
            for wp in passing_wp:
                self.move_to_waypoint(wp)
           
            # set the product location as the tempf target
            self.tempf_storage.set_location_as_fast_target(tempf, storage_loc_id)
                
            # we do not use the installed position as correction 
            # since this position is not accurate due to cobot compliance
            # e.g. due to sagging during installation
            tempf.reset_to_nom_pos_only()
           
            # insert the fastener into the storage location
            if self._drop_tempf_in_storage(tempf):
                # add the fastener to the product
                if self.tempf_storage.add_fast_to_location(tempf, storage_loc_id):

                    return True          
           
            return False
     
    
    def check_inventory(self):
        """
        Function that checks whether all fasteners are available for the
        actions that are defined.
       
        Function must be re-run whenever a defective fastener is ejected into a bin.
           
        :return: bool, returns True if enough inventory and free space is available in the storage
        """
        return self.enough_locs() and self.enough_fast()
   
    
    def enough_locs(self):
        """
        Function that checks whether enough empty spots are available
        in the storage location for the fasteners that need to be removed.
       
        Function must be re-run whenever a defective fastener is ejected into a bin.
            
        :return: bool, returns True if enough locations are available.
        """
        # create a list of diameters from all removal actions
        tempf_diam_rem_lst = []
        number_loc_needed_per_diam = []
       
        success = True
        is_in = False
        i_where = 0
       
        for a in self.actions:
            if a.is_remove_tempf():
                loc = self._get_location_by_uid(a.loc_uid())
                if loc is not None:
                    d_needed = loc.diam()
                else:
                    send_message("enough_locs____No location with uid {} could be found in action {}".format(a.loc_uid(), a.uid()))
                    d_needed = 0
                is_in = False
                for i, known_diam in enumerate(tempf_diam_rem_lst):
                    if abs(known_diam - d_needed) < 0.01:
                        is_in = True
                        i_where = i
                if not is_in:
                    tempf_diam_rem_lst.append(d_needed)
                    number_loc_needed_per_diam.append(1)
                else:
                    number_loc_needed_per_diam[i_where] += 1               
        
        if len(tempf_diam_rem_lst) > 0:
            # get all temps available in storage for each diameter
            storage_loc_available = [0 for a in tempf_diam_rem_lst]
           
            for i, d in enumerate(tempf_diam_rem_lst):
                storage_loc_available[i] = self.tempf_storage.number_empty_spots_of_diam(d)
           
            # check if there is a shortage anywhere
            for available, needed, diam in zip(storage_loc_available, number_loc_needed_per_diam, tempf_diam_rem_lst):
                if available < needed:
                    send_message("enough_locs____{} empty locations of diameter {} in storage; {} needed.".format(available, diam, needed))
                    success = False
       
        # report there is no shortage
        return success
 
    
    def enough_fast(self):
        """
        Function that checks whether enough fasteners are available
        in the storage location for the fasteners that need to be installed.
       
        Function must be re-run whenever a defective fastener is ejected into a bin.
           
        :return: bool, returns True if enough fasteners are available.
        """
       
        #First the temporary fasteners
        # create a list of diameters from all installation actions
        tempf_diam_inst_lst = []
        number_tempf_needed_per_diam = []
               
        tempf_succes = True
        is_in = False
        i_where = 0

        for a in self.actions:
            if a.is_install_tempf():
                loc = self._get_location_by_uid(a.loc_uid())

                if loc is not None:
                    d_needed = loc.diam()
                else:
                    send_message("enough_fast____No tempf location with uid {} could be found for action {}".format(a.loc_uid(), a.uid()))
                    d_needed = 0
                
                is_in = False
                
                for i, known_diam in enumerate(tempf_diam_inst_lst):
                    if abs(known_diam - d_needed) < 0.01:
                        is_in = True
                        i_where = i
                if not is_in:
                    tempf_diam_inst_lst.append(d_needed)
                    number_tempf_needed_per_diam.append(1)
                else:
                    number_tempf_needed_per_diam[i_where] += 1               
         
        if len(tempf_diam_inst_lst) > 0:      
            # get all temps available in storage for each diameter
            tempf_in_storage = [0 for a in tempf_diam_inst_lst]
 
            for i, d in enumerate(tempf_diam_inst_lst):
                tempf_in_storage[i] = self.tempf_storage.number_fasts_of_diam(d)
 
            # check if there is a shortage anywhere
            for available, needed, diam in zip(tempf_in_storage, number_tempf_needed_per_diam, tempf_diam_inst_lst):
                if available < needed:
                    send_message("enough_fast____{} fasteners of diameter {} in storage; {} needed.".format(available, diam, needed))
                    tempf_succes = False
                   
        
        #Permanent fasteners check     
        
        #Diameter, grip and quantity linked by index in list
        fastener_grip_inst_lst = []
        fastener_diam_inst_lst = []
        number_fastener_needed_per_diam_and_grip = []     
        permf_succes = True
        is_in = False
        i_where = 0
        j_where = 0
        
        for a in self.actions:
            if a.is_install_permf():
                loc = self._get_location_by_uid(a.loc_uid())
                if loc is not None:
                    grip_needed = loc.grip_length()
                    d_needed = loc.diam()
                   
                else:
                    send_message("enough_fast____No permf location with uid {} could be found for action {}".format(a.loc_uid(), a.uid()))
                    grip_needed = 0
                
                is_in = False
            
                for i, known_diam in enumerate(fastener_diam_inst_lst):
                    if abs(known_diam - d_needed) < 0.01:
                        i_where = i
                
                        for j, known_grip in enumerate(fastener_grip_inst_lst):   
                            if abs(known_grip - grip_needed) < 0.01 and j == i_where:
                                is_in = True
                                j_where = j      
                            
                if not is_in:
                    fastener_grip_inst_lst.append(grip_needed)
                    fastener_diam_inst_lst.append(d_needed)
                    number_fastener_needed_per_diam_and_grip.append(1)
                else:
                    number_fastener_needed_per_diam_and_grip[j_where] += 1
                
          
        if len(fastener_diam_inst_lst) > 0:      
            # get all fastener available in storage for each diameter & grip
           
            fasteners_in_storage = []
           
            z = 0
            for k in enumerate(fastener_diam_inst_lst):            
                dia = fastener_diam_inst_lst[z]
                grip = fastener_grip_inst_lst[z]
                fasteners_in_storage.append(self.permf_storage.number_fasteners_of_diam_grip(dia,grip))
                a = z
                z = a+1
           
            # check if there is a shortage anywhere
            for available, needed, diam, grip in zip(fasteners_in_storage, number_fastener_needed_per_diam_and_grip, fastener_diam_inst_lst, fastener_grip_inst_lst):
                if available < needed:
                    #send_message("Not enough fasteners")("enough_fast____{} fasteners of diameter {} and grip {} in storage; {} needed.".format(available, diam, grip, needed)) #grip toevoegen in bericht
                    permf_succes = False
       
        # report the result
        if tempf_succes == False or permf_succes == False:
            return False
        else:
            return True
       
    
    def _pick_up_fast(self, fast: cl_fastener, is_tempf: bool):
        """
        Function that picks up a fastener.
        The pick-up location can be found in the fast object
       
        :param fast: cl_fastener,   the fastener object with
                                    information on where to install it
        :param is_tempf: bool,      Wheteher we are dealing with a temporary fastener
                                    or a permanent fastener

        :return: bool, returns True if successful
        """
        if is_tempf:
            self.tf_ee.stop_clamping()

        self._approach_fast(fast)
        is_untightened = False

        # remember where the fast is.
        was_in_product = fast.in_product()

        is_engaged = False
        if is_tempf:
            is_engaged = self._engage_tempf(fast, PICK_UP_FORCE, PICK_UP_ENGAGEMENT_COMPLIANCE, PICK_UP_ENGAGEMENT_SPEED, True)
        else:
            is_engaged = self._engage_permf(fast, PICK_UP_FORCE, PICK_UP_ENGAGEMENT_COMPLIANCE, PICK_UP_ENGAGEMENT_SPEED, True)

        if is_engaged:
           
            # wait to properly settle
            wait(0.1)
    
            # get and log the pick-up location to enable fine tuning of the storage location
            fast.set_install_pos_from_tcp_position()
           
            # let the ee know there is a fast in its beak
            if is_tempf:
                self.tf_ee.tempf_in_end_effector = True
                if was_in_product:
                    send_message("start untightening")
                    # clamp and tighten the fastener
                    is_untightened = self.tf_ee.untighten_temp(UNTIGHTEN_PROGRAM)
                else:
                    # no need to untighten in the storage location
                    # start clamping the fastener
                    is_untightened = True

                    self.tf_ee.start_clamping()
            else:
                self.pf_ee.permf_in_end_effector = True
                is_untightened = True # permf never is fixed
                    
        else:
            # start ejecting to help disengage the fastener
            if is_tempf:
                self.tf_ee.start_ejection()
           
            release_force()
            release_compliance_ctrl()
            change_operation_speed(HOLE_RETRACTION_SPEED)
            movel(posx(0, 0, -(fast.shaft_height() + fast.tcp_tip_distance() + SAFE_Z_GAP + SAFE_Z_GAP), 0, 0, 0), ref=DR_TOOL)
 
            if is_tempf:
                self.tf_ee.stop_ejection()  
            
            return False
       
        if is_untightened:
           
            # let the fast know its new location, will also change the TCP
            fast.set_as_in_ee()
        else:
            self.tf_ee.reset_cobot_output_pins()
           
            release_force()
            release_compliance_ctrl()
            change_operation_speed(HOLE_RETRACTION_SPEED)
            movel(posx(0, 0, -(fast.shaft_height() + fast.tcp_tip_distance() + SAFE_Z_GAP + SAFE_Z_GAP), 0, 0, 0), ref=DR_TOOL)
           
            return False
           
        # check if the fast is really in the ee
        if is_tempf:
            if is_untightened:   
                if was_in_product:        
                    in_ee = retract_tempf(fast, self.tf_ee)
                    if not in_ee:
                        if was_in_product:
                            fast.set_as_in_product()
                        else:
                            fast.set_as_in_storage()
                else:
                    in_ee = True
        else:
            #TODO check whether the fastener is in
            in_ee = True 
        
        
        # change to move speed
        change_operation_speed(MOVE_SPEED)
       
        # move away from storage
        movel(posx(0, 0, -fast.shaft_height() - SAFE_Z_GAP, 0, 0, 0), ref=DR_TOOL, r = BLEND_RADIUS_SMALL)
       
        # return the success
        return in_ee
 
    
    def _drop_tempf_in_storage(self, tempf):
        """
        Function that drops a tempf into the storage location.
        The function assumes that the target location is in the fast object
       
        :param tempf: cl_fastener, the fastener object with
                                   information on where to drop it
           
        :return: bool, returns True if successful
        """
        # move to the hole apprach position
        speed_limited_movej_on_posx(tempf.tcp_approach_pos(), 100)

        # set the DR_USER_PROBE axis system above the storage location before the movel with radius
        overwrite_user_cart_coord(DR_USER_PROBE, tempf.nom_pos())
        change_operation_speed(MOVE_SPEED)

        # move down into the hole (10mm lower than the hole entry)
        movel(posx(0, 0, 2 * SAFE_Z_GAP, 0, 0, 0), ref=DR_USER_PROBE)
        
        # Set the compliance and force
        # Set DR_TOOL as ref coordinate to ensure that the desired forces are in the too axis system
        set_ref_coord(DR_TOOL)

        # now move against surface next to hole
        # set the correct complance and speed
        task_compliance_ctrl(PICK_UP_ENGAGEMENT_COMPLIANCE)
            
        # Set the force. The force should be in range of 10-20N -
        # small enough not to bend the material but high enough to reach surface in shortest time
        set_desired_force([0, 0, PROBE_COMPLIANCE_FORCE, 0, 0, 0], [0, 0, 1, 0, 0, 0])
 
        # Wait until the force reaches a value
        not_reached_force = True
        while not_reached_force:

            not_reached_force = abs(get_tool_forces_in_tool()[2]) < 0.9 * PROBE_COMPLIANCE_FORCE

        tip_pos, sol = get_current_posx(ref=DR_BASE)

        overwrite_user_cart_coord(DR_USER_PROBE, tip_pos)
    
        # slowly untighten
        self.tf_ee.set_select_program(2)
        self.tf_ee.set_reversestart_on()

        tip_pos, sol = get_current_posx(ref=DR_USER_PROBE)
   
        # when the movement into the hole is regarded as inside the hole
        # not too soon because the fastener has not yet been fully untightened
        # not too late because the fastener will untighten too much
        not_went_in_hole = True
        while not_went_in_hole:
            tip_pos, sol = get_current_posx(ref=DR_USER_PROBE)
            not_went_in_hole = tip_pos[2] < 1

        tip_pos, sol = get_current_posx(ref=DR_USER_PROBE)

        # stop the motor before it turns dull again
        self.tf_ee.reset_cobot_output_pins()

        self.tf_ee.stop_clamping()
        self.tf_ee.start_ejection()

        # tell the tempf object it is in the storage location
        tempf.set_as_in_storage()

        # set the tcp to the tip of the ee
        # compliance will also be turned off to enable TCP change.
        tempf.set_tool_center_point()

        # move back
        movel(posx(0, 0, -(tempf.shaft_height() + tempf.tcp_tip_distance() + SAFE_Z_GAP + SAFE_Z_GAP), 0, 0, 0), ref=DR_TOOL)

        self.tf_ee.stop_ejection()

        return True


    def _insert_fast(self, fast, is_tempf):
        """
        Function that inserts and tightens a fastener.
        The function assumes that the target location is in the fast object
       
        :param fast: cl_fastener, the fastener object with
                                        information on where to install it
        :param is_tempf: bool, Whteher we are dealing with a temporary fastener
                               or a permanent fastener
           
        :return: bool, returns True if successful
        """
       
        #self._approach_fast(fast)

        # remember where the fast is.
        was_in_product = fast.in_product()
       
        if not move_into_hole(fast):
            movel(posx(0, 0, -(fast.shaft_height() + fast.tcp_tip_distance() + SAFE_Z_GAP + SAFE_Z_GAP), 0, 0, 0), ref=DR_TOOL)
            if is_tempf:
                self.tf_ee.stop_clamping()
           
            return False
       
        if is_tempf:
            if was_in_product:
                is_tightened = True
            else:
                is_tightened = self.tf_ee.tighten_temp(TIGHTEN_PROGRAM)
           
            # try again if not tightened
            if not is_tightened:
                self.tf_ee.engagement_burst(BURST_PROGRAM, True)
                is_tightened = self.tf_ee.tighten_temp(TIGHTEN_PROGRAM)
           
            if is_tightened:      
                
                # get and log the place location to enable fine tuning of the storage location
                fast.set_install_pos_from_tcp_position()
               
                # let the fast and the ee know everything is in position, will also change the TCP
                fast.set_as_in_product()
 
                self.tf_ee.tempf_in_end_effector = False
 
            else:
                send_message("insert_fast____fastener with uid {} not tightened.".format(fast.uid()))
               
                # TODO move to bin location must never cause collision
                movel(BIN_POSITION, ref=DR_BASE)
 
                is_ejected = self.tf_ee.eject_temp()
 
                if is_ejected:
                    fast.set_as_in_bin()
                    self.tf_ee.tempf_in_end_effector = False
              
                return False
 
            self.tf_ee.stop_clamping()
 
            # start ejecting to help disengage the fastener
            self.tf_ee.start_ejection()
 
        else:
            # get and log the place location to enable fine tuning of the storage location
            fast.set_install_pos_from_tcp_position()
 
            is_tightened = self.pf_ee.start_trigger()
 
            # let the fast and the ee know everything is in position, will also change the TCP
            fast.set_as_in_product()
 
            self.pf_ee.permf_in_end_effector = False
 
        # retract away from the fastener location in any case
        change_operation_speed(HOLE_RETRACTION_SPEED)
       
        movel(posx(0, 0, -(fast.shaft_height() + fast.tcp_tip_distance() + SAFE_Z_GAP + SAFE_Z_GAP), 0, 0, 0), ref=DR_TOOL)
 
        if is_tempf:
            self.tf_ee.stop_ejection()       
 
        # change to move speed
        change_operation_speed(MOVE_SPEED)
 
        # return the result
        return is_tightened
   
    
    def _approach_fast(self, fast: cl_fastener):
        """
        Function that approaches a fastener.
        The function uses the location in the fast object
       
        :param fast: cl_fastener, the fastener object with
                                  information on where to approach it
           
        :return: bool, returns True if successful
        """
       
        # make sure the coordinate frame is DR_BASE
        set_ref_coord(DR_BASE)
       
        change_operation_speed(MOVE_SPEED)

        speed_limited_movej_on_posx(fast.tcp_approach_pos(), 100)
       
    
    def _engage_permf(self, fast: cl_fastener, force, comp, speed, burst):
        """
        Function that engages an installed fastener or hole.
        The function uses the location in the fast object.
       
        :param fast: cl_fastener, the fastener object with
                            information on where to engage it
        :param force: float, the force applied to the fastener
        :param comp: list[float, float, float, float, float, float], the definition of the compliance
        :param speed: float, the speed as percentage
        :param burst: bool, whether an engagement burst must be done
       
        :return: bool, returns True if successful
        """
        reqd_ratio = 0.1 #Was 0.2
              
        task_compliance_ctrl(comp)
        change_operation_speed(speed)
        movel(posx(0,0,GLOBAL_CLEARANCE_DURING_MOVEMENTS+SAFE_Z_GAP+SAFE_Z_GAP-fast.shaft_height()+2,0,0,0),ref=DR_TOOL)      
        
        wait(0.5)
        # Get a reference force because a force can already be present (example: hanging cables)
        f_z0 = get_tool_forces_in_tool()[2]
       
        release_compliance_ctrl()

        # Set DR_TOOL as ref coordinate to ensure that the desired forces are in the too axis system
        set_ref_coord(DR_TOOL)
          
        # The following prevents drifting of the Cobot position
        task_compliance_ctrl([20000,20000,20000,400,400,400])
        set_desired_force([0, 0, 11, 0, 0, 0], [0, 0, 1, 0, 0, 0])
        wait(0.1)
       
        # set the correct complance and speed
        task_compliance_ctrl(comp)
       
        set_desired_force([0, 0, force + f_z0, 0, 0, 0], [0, 0, 1, 0, 0, 0])
        
        t0 = time.time()
       
        reached_force, reached_pos, reached_max_time = False, False, False
        
        # Wait until the force reaches a value or max time is passed
        while not reached_max_time and not reached_pos:
           
            f_z = get_tool_forces_in_tool()[2]
            reached_force = abs(f_z - f_z0) > 0.9 * force
           
            if reached_force:
                # this could be the impuls from a collision
                # wait to see if the force is maintained
                wait(0.5)
               
                # check if the force is still there
                f_z = get_tool_forces_in_tool()[2]
                reached_force = abs(f_z - f_z0) > 0.9 * force
                if reached_force:
                    break
            r_i = fast.get_install_ratio()
            reached_pos = r_i < reqd_ratio
           
            reached_max_time = (time.time() - t0) > 8
       
        # do a short burst of the motor to help engagement if it did not reach pos yet
        if burst and not reached_pos:
            # burst usually when temp must be picked up,
            # so the burst must be in untightening direction
            if is_tempf:
                self.tf_ee.engagement_burst()
           
                # wait to see if it reached position now
                wait(1)
       
            # get the position progress
            r_i = fast.get_install_ratio()
            reached_pos = r_i < reqd_ratio
           
        if reached_force and not reached_pos:
            send_message("engage_permf____starting periodic move to get from {} to {}".format(r_i, reqd_ratio))
            #start a spiral move to see if it will slide over the temp
            #   Periodic move to wiggle the fastener in
            amove_periodic(amp = [5,5,0,0.35,0.35,0], period = [5,5,0,1.0,0.5,0], atime = 0.1, repeat = 3, ref = DR_TOOL)
           
            # also do a second burst in the meantime
            if burst and not reached_pos:
                # burst usually when temp must be picked up,
                # so the burst must be in untightening direction
                if is_tempf:
                    self.tf_ee.engagement_burst()
         
            # The while loop below senses whether the end effector slips onto the fastener
            while check_motion() != 0 and not reached_pos:
               
                r_i = fast.get_install_ratio()
                reached_pos = r_i < reqd_ratio
         
            # stop the spiral motion
            stop(DR_SSTOP)
       
        if not reached_force and reached_pos:
            send_message("engage_permf____waiting for force to increase from {}N to {}N".format(f_z, force))
            t0 = time.time()
 
            while not reached_max_time:
                f_z = get_tool_forces_in_tool()[2]
                reached_force = abs(f_z - f_z0) > 0.9 * force
               
                reached_max_time = (time.time() - t0) > 5
                if reached_force and reached_pos:
                    break
        #tp_popup("reached_force={0},reached_pos={1}".format(reached_force,reached_pos))
        if reached_pos:
            if reached_force:
                send_message("engage_permf____did reach force and position when engaging fastener {}\n".format(fast.uid()) +
                           "force in tool z-direction is {} and {} at the start.\n".format(f_z, f_z0) +
                           "install ratio is {}; time is {}.".format(r_i, (time.time() - t0)))
            else:
                send_message("engage_permf____did not reach force but reached position when engaging fastener {}\n".format(fast.uid()) +
                           "force in tool z-direction is {} and {} at the start.\n".format(f_z, f_z0) +
                           "install ratio is {}; time is {}.".format(r_i, (time.time() - t0)))
           
            # let the system know the fastener is in the ee
            fast.set_as_in_ee()
            return True   
        
        else:
            if reached_force:
                send_message("engage_permf____reached force but not reached position when engaging fastener {}\n".format(fast.uid()) +
                        "force in tool z-direction is {} and {} at the start.\n".format(f_z, f_z0) +
                        "install ratio is {}; time is {}.".format(r_i, (time.time() - t0)))
            else:
                send_message("engage_permf____did not reach force or position when engaging fastener {}\n".format(fast.uid()) +
                        "force in tool z-direction is {} and {} at the start.\n".format(f_z, f_z0) +
                        "install ratio is {}; time is {}.".format(r_i, (time.time() - t0)))
       
            # discard the fastener and let the system know the fastener is in the ee
            fast.set_as_in_bin()
 
        return False     
 
    def _engage_tempf(self, fast: cl_fastener, force, comp, speed, burst):
        """
        Function that engages an installed fastener or hole.
        The function uses the location in the fast object.

        assuming the end effector is in the fast.tcp_approach_pos

        :param fast: cl_fastener, the fastener object with
                            information on where to engage it
        :param force: float, the force applied to the fastener
        :param comp: list[float, float, float, float, float, float], the definition of the compliance
        :param speed: float, the speed as percentage
        :param burst: bool, whether an engagement burst must be done

        :return: bool, returns True if successful
        """
        reqd_ratio = 0.1

        # move to right above the tempf
        movel(translate_pos(fast.tcp_approach_pos(), 0, 0, 3 * SAFE_Z_GAP), ref=DR_BASE)

        release_compliance_ctrl()

        # Set DR_TOOL as ref coordinate to ensure that the desired forces are in the too axis system
        set_ref_coord(DR_TOOL)

        # Get a reference force because a force can already be present (example: hanging cables)
        f_z0 = get_tool_forces_in_tool()[2]
            
        # The following prevents drifting of the Cobot position
        task_compliance_ctrl([20000,20000,20000,400,400,400])
        set_desired_force([0, 0, 11, 0, 0, 0], [0, 0, 1, 0, 0, 0])
        wait(0.1)

        # set the correct complance and speed
        task_compliance_ctrl(comp)
        set_desired_force([0, 0, force + f_z0, 0, 0, 0], [0, 0, 1, 0, 0, 0])

        t0 = time.time()

        reached_force, reached_pos, reached_max_time = False, False, False

        # Wait until the force reaches a value or max time is passed
        while not reached_max_time and not reached_pos:
            
            f_z = get_tool_forces_in_tool()[2]
            reached_force = abs(f_z - f_z0) > 0.9 * force
            
            if reached_force:
                # this could be the impuls from a collision
                # wait to see if the force is maintained
                wait(0.5)
                
                # check if the force is still there
                f_z = get_tool_forces_in_tool()[2]
                reached_force = abs(f_z - f_z0) > 0.9 * force
                if reached_force:
                    break
            r_i = fast.get_install_ratio()
            reached_pos = r_i < reqd_ratio
            
            reached_max_time = (time.time() - t0) > 8

        # do a short burst of the motor to help engagement if it did not reach pos yet
        if burst and not reached_pos:
            # burst usually when temp must be picked up,
            # so the burst must be in untightening direction
            self.tf_ee.engagement_burst()
            
            # wait to see if it reached position now
            wait(3)

            # get the position progress
            r_i = fast.get_install_ratio()
            reached_pos = r_i < reqd_ratio
            
        if reached_force and not reached_pos:
            send_message("engage_tempf____starting periodic move to get from {} to {}".format(r_i, reqd_ratio))
            #start a spiral move to see if it will slide over the temp
            #   Periodic move to wiggle the fastener in
            amove_periodic(amp = [5,5,0,0.35,0.35,0], period = [5,5,0,1.0,0.5,0], atime = 0.1, repeat = 3, ref = DR_TOOL)
            
            # also do a second burst in the meantime
            if burst and not reached_pos:
                # burst usually when temp must be picked up,
                # so the burst must be in untightening direction
                self.tf_ee.engagement_burst()
            
            # The while loop below senses whether the end effector slips onto the fastener
            while check_motion() != 0 and not reached_pos:
                
                r_i = fast.get_install_ratio()
                reached_pos = r_i < reqd_ratio
            
            # stop the spiral motion
            stop(DR_SSTOP)

        if not reached_force and reached_pos:
            send_message("engage_tempf____waiting for force to increase from {}N to {}N".format(f_z, force))
            t0 = time.time()

            while not reached_max_time:
                f_z = get_tool_forces_in_tool()[2]
                reached_force = abs(f_z - f_z0) > 0.9 * force
                
                reached_max_time = (time.time() - t0) > 5
                if reached_force and reached_pos:
                    break
        #tp_popup("reached_force={0},reached_pos={1}".format(reached_force,reached_pos))
        if reached_pos:
            if reached_force:
                send_message("engage_tempf____did reach force and position when engaging fastener {}\n".format(fast.uid()) +
                            "force in tool z-direction is {} and {} at the start.\n".format(f_z, f_z0) +
                            "install ratio is {}; time is {}.".format(r_i, (time.time() - t0)))
            else:
                send_message("engage_tempf____did not reach force but reached position when engaging fastener {}\n".format(fast.uid()) +
                            "force in tool z-direction is {} and {} at the start.\n".format(f_z, f_z0) +
                            "install ratio is {}; time is {}.".format(r_i, (time.time() - t0)))
            
            # let the system know the fastener is in the ee
            fast.set_as_in_ee()
            return True   

        else:
            if reached_force:
                send_message("engage_tempf____reached force but not reached position when engaging fastener {}\n".format(fast.uid()) +
                        "force in tool z-direction is {} and {} at the start.\n".format(f_z, f_z0) +
                        "install ratio is {}; time is {}.".format(r_i, (time.time() - t0)))
            else:
                send_message("engage_tempf____did not reach force or position when engaging fastener {}\n".format(fast.uid()) +
                        "force in tool z-direction is {} and {} at the start.\n".format(f_z, f_z0) +
                        "install ratio is {}; time is {}.".format(r_i, (time.time() - t0)))

            # discard the fastener and let the system know the fastener is in the ee
            fast.set_as_in_bin()

        return False     

    
    def _get_all_locs(self):
        """
        Function that returns a list with all locations in the storage and product
           
        :return: list[cl_fastener_location]
        """
       
        lst1 = [l.loc for l in self.tempf_storage.holes_and_fast_lst if l.loc is not None]
        lst2 = [l.loc for l in self.permf_storage.holes_and_fast_lst if l.loc is not None]
        lst3 = [l.loc for l in self.product.holes_and_fast_lst if l.loc is not None]
        return lst1 + lst2 + lst3
 
    
    def _get_location_by_uid(self, uid):
        """
        Function that gets a location from the storage or product with a certain uid
       
        :param uid: str, The uid of the location to be returned
           
        :return: cl_fastener_location, the location with the specified uid
        """      
        return self._get_from_lst_by_uid(self._get_all_locs(), uid, "location")
   
 
    def _get_all_permfs_in_storage(self):
        """
        Function that returns a list with all fasteners in the storage
           
        :return: list cl_fastener,
        """
        return [f.fast for f in self.permf_storage.holes_and_fast_lst if f.fast is not None]
   
 
    def _get_all_tempfs_in_storage(self):
        """
        Function that returns a list with all fasteners in the storage
           
        :return: list cl_fastener,
        """
        return [f.fast for f in self.tempf_storage.holes_and_fast_lst if f.fast is not None]
       
 
    def _get_all_permfs_in_product(self):
        """
        Function that returns a list with all fasteners in the product
           
        :return: list cl_fastener,
        """
        lst = [f.fast for f in self.product.holes_and_fast_lst if f.fast is not None]
        return [f for f in lst if f.is_permf()]
   
 
    def _get_all_tempfs_in_product(self):
        """
        Function that returns a list with all fasteners in the product
           
        :return: list cl_fastener,
        """
        lst = [f.fast for f in self.product.holes_and_fast_lst if f.fast is not None]
        return [f for f in lst if f.is_tempf()]
       
    
    def _get_all_tempfs(self):
        """
        Function that returns a list with all fasteners in the product and storage
           
        :return: list cl_fastener,
        """
        return self._get_all_tempfs_in_storage + self._get_all_tempfs_in_product
           
    
    def _get_fastener_by_uid(self, uid, log = True):
        """
        Function that gets a fastener from the storage or product with a certain uid
       
        :param uid: str, The uid of the fastener to be returned
        :param: log: bool, whether to log the proceedings of the function
           
        :return: cl_fastener, the fastener with the specified uid
        """       
        return self._get_from_lst_by_uid(self._get_all_tempfs(), uid, "fastener", log)
       
    
    def _get_waypoint_by_uid(self, uid, log = True):
        """
        Function that gets a waypoint with a certain uid
       
        :param uid: str, The uid of the waypoint to be returned
        :param: log: bool, whether to log the proceedings of the function
           
        :return: cl_waypoint, the waypoint with the specified uid
        """
        return self._get_from_lst_by_uid(self.waypoints, uid, "waypoint", log)
   
    
    def _get_from_lst_by_uid(self, lst_in, uid, o_name, log = True):
        """
        Function that gets an object with a certain uid
       
        :param lst_in: list[cl_fastener_location] |
                       listcl_fastener, | list[cl_waypoint],
                       The list to select from
        :param uid: str, The uid of the object to be returned
        :param o_name: str, the name of the object.
                            Will only be used to make messages more meaningful
        :param: log: bool, whether to log the proceedings of the function
           
        :return: cl_fastener_location | cl_fastener | cl_waypoint,
                 the waypoint with the specified uid | None
        """ 
        lst = [o for o in lst_in if o.uid() == uid]
 
        if len(lst) == 1:
            return lst[0]
        elif len(lst) > 1:
            if log:
                send_message("get_from_lst_by_uid____Multiple " + o_name + "s with uid " + uid + " exist.\n\
                           Please make sure you have unique " + o_name + " uids.")
            return lst[0]
        else:
            if log:
                uids = [o.uid() for o in lst_in]
                uid_string = "["
                for s in uids:
                    uid_string += s + ", "
                uid_string += "]"
                send_message("get_from_lst_by_uid___" + o_name + " with uid " + uid + " does not exist in list:\n" + uid_string)
               
            return None
       
 
    def _add_waypoint(self, uid, pos):
        """
        Function that adds a cl_waypoint to the list waypoints
       
        :param uid: str, the uid of the waypoint
        :param pos: pos, position of the waypoint
        :param w_type: str, the type of waypoint. Some waypoints have special type
           
        :return: bool, returns True if successful
        """
        # check if the uid does not already exist
        # do not log when no waypoint has been found
        if self._get_waypoint_by_uid(uid, False) is None:
            for w in self.waypoints:
                if get_distance(w.pos(), pos) < 3 * BLEND_RADIUS_LARGE:
                    tp_popup("distance between waypoints to small.\nWill cause problems with blend radius.")
            self.waypoints.append(cl_waypoint(uid, pos))
            return True
        else:
            return False
          
    
    def _add_action(self, uid, a_type, loc_uid, is_done = False, speed = 100):
        """
        Function that adds a cl_action to the list actions
       
        Supported types (a_type)
        ACTION_TYPE_MOVE_WAYPOINT = "move_to_waypoint"  
        ACTION_TYPE_INSTALL_PERMF = "install_permf" 
        ACTION_TYPE_INSTALL_TEMPF = "install_tempf" 
        ACTION_TYPE_REMOVE_TEMPF = "remove_fastener"   
        
        :param uid: str, the uid of the action
        :param a_type: str, the type of action. Some actions have special type
        :param loc_uid: str, the location involved in the action
        :param is_done: bool, whether the action is done already, True when finished
        :param speed: float, the speed as percentage of the maximum speed
            
        :return: bool, returns True if successful
        """
        if self._is_action_uid_unique(uid):
            self.actions.append(cl_action(uid, a_type, loc_uid, is_done, speed))
           
            return True
        else:
           
            return False
            
    
    def _add_move_to_waypoint_action(self, uid, loc_uid, is_done = False, speed = 100):
        """
        Function that adds a waypoint type cl_action to the list actions
       
        :param uid: str, the uid of the action
        :param loc_uid: str, the waypoint where the cobot must mmove to
        :param is_done: bool, whether the action is done already, True when finished
        :param speed: float, the speed as percentage of the maximum speed
           
        :return: bool, returns True if successful
        """
        return self._add_action(uid, ACTION_TYPE_MOVE_WAYPOINT, loc_uid, is_done, speed)
 
    
    def _add_install_permf_action(self, uid, loc_uid, is_done = False, speed = 100):
        """
        Function that adds an install type cl_action to the list actions
       
        :param uid: str, the uid of the action
        :param loc_uid: str, the target location of the fastener
        :param is_done: bool, whether the action is done already, True when finished
        :param speed: float, the speed as percentage of the maximum speed
           
        :return: bool, returns True if successful
        """
        return self._add_action(uid, ACTION_TYPE_INSTALL_PERMF, loc_uid, is_done, speed)
 
    
    def _add_install_tempf_action(self, uid, loc_uid, is_done = False, speed = 100):
        """
        Function that adds an install type cl_action to the list actions
       
        :param uid: str, the uid of the action
        :param loc_uid: str, the target location of the fastener
        :param is_done: bool, whether the action is done already, True when finished
        :param speed: float, the speed as percentage of the maximum speed
           
        :return: bool, returns True if successful
        """
        return self._add_action(uid, ACTION_TYPE_INSTALL_TEMPF, loc_uid, is_done, speed)
   
    
    def _add_remove_tempf_action(self, uid, loc_uid, is_done = False, speed = 100):
        """
        Function that adds a remove fastener type cl_action to the list actions
       
        :param uid: str, the uid of the action
        :param loc_uid: str, the location where the fastener must be removed
        :param is_done: bool, whether the action is done already, True when finished
        :param speed: float, the speed as percentage of the maximum speed
           
        :return: bool, returns True if successful
        """
        return self._add_action(uid, ACTION_TYPE_REMOVE_TEMPF, loc_uid, is_done, speed)
   
    
    def _is_action_uid_unique(self, uid):
        """
        Function that returns whether the action uid is unique
       
        :param uid: str, the uid of the action
           
        :return: bool, returns True if the uid is unique
        """
        for a in self.actions:
            if a.uid() == uid:
                return False
        return True
   
    
    def log_waypoints_lst(self):
        """
        """
        string_out = "{} waypoint instances exist in the agent {}.\n[".format(len(self.waypoints), self.uid())
        for i, wp in enumerate(self.waypoints):
            string_out += "uid:{}, ".format(wp.uid())
        string_out += "]"
        send_message("log_waypoints_lst___", string_out)
   
 
 
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
 
 
 
class cl_waypoint(cl_uid):
    """
    Class that describes a waypoint
    """
   
    def __init__(self, uid, pos, blend_radius = 0):
        """
        Initiation of a class that describes a waypoint
 
        :param uid: str, the uid of the action
        :param pos: posx, the position of the waypoint
        :param w_type: str the type of the waypoint
        :param blend_radius: float The blend radius the robot can make
        """
        super().__init__(uid)
 
        self.__pos = pos
        self.__blend_radius = blend_radius
 
    
    def pos(self):
        """
        Gets the waypoint position.
       
        :return: posx, the position of the waypoint
        """
        return self.__pos
 
    def set_pos(self, pos):
        """
        Sets the waypoint position.
       
        :param pos: posx, the position of the waypoint
        """
        self.__pos = pos
       
    def blend_radius(self):
        """
        Gets the blend radius.
       
        :return: blend radius of the waypoint
        """
        return self.__blend_radius
 
    def set_blend_radius(self, blend_radius):
        """
       Sets the waypoint blend radius.
       
        :param blend_radius: Blend radius
        """
        self.__blend_radius = blend_radius
 
 
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
 
class cl_action(cl_uid):
   
    """
    Class that describes a fastener action
    """
   
    def __init__(self, uid, a_type, loc_uid, is_done, speed = 100.0):
        """
        Initiation of the action.
       
        Supported types (a_type)
            ACTION_TYPE_MOVE_WAYPOINT = "move_to_waypoint"  
            ACTION_TYPE_INSTALL_PERMF = "install_permf" 
            ACTION_TYPE_INSTALL_TEMPF = "install_tempf" 
            ACTION_TYPE_REMOVE_TEMPF = "remove_fastener"
        
        :param uid: str, the uid of the action
        :param a_type: str, the type of action. Some actions have special type
        :param loc_uid: str, the location involved in the action
        :param is_done: bool, whether the action is done already, True when finished
        :param speed: float, the speed as percentage of the maximum speed
        """
        super().__init__(uid)
 
        self.set_a_type(a_type)
        self.__loc_uid = loc_uid
        self.__is_done = is_done
        self.__is_cancelled = False
        self.__is_waiting = False
        self.__speed = speed
       
        self.passing_wps = []
 
    
    def a_type(self):
        """
        returns the action type.
       
        :return: str, returns the type of the action
        """
        return self.__a_type
 
    
    def set_a_type(self, a_type):
        """
        sets the type of the action
       
        Supported types
            ACTION_TYPE_MOVE_WAYPOINT = "move_to_waypoint"  
            ACTION_TYPE_INSTALL_PERMF = "install_permf" 
            ACTION_TYPE_INSTALL_TEMPF = "install_tempf" 
            ACTION_TYPE_REMOVE_TEMPF = "remove_fastener"   
        
        :param a_type: str, the type of action. Some actions have special type
        """
        if a_type == ACTION_TYPE_MOVE_WAYPOINT:
            self.__a_type = a_type
        elif a_type == ACTION_TYPE_INSTALL_PERMF:
            self.__a_type = a_type
        elif a_type == ACTION_TYPE_INSTALL_TEMPF:
            self.__a_type = a_type
        elif a_type == ACTION_TYPE_REMOVE_TEMPF:
            self.__a_type = a_type
        else:
            raise Exception("Unknown type specified in set_a_type.")
   
    def is_move_waypoint(self):
        """
        Returns true if this action is a move to a waypoint.
       
        :return: bool, returns True if it is ACTION_TYPE_MOVE_WAYPOINT
        """
        return self.__a_type == ACTION_TYPE_MOVE_WAYPOINT
   
    def is_install_permf(self):
        """
        Returns true if this action defines the installation of a permanent fastener.
       
        :return: bool, returns True if it is ACTION_TYPE_INSTALL_PERMF
        """
        return self.__a_type == ACTION_TYPE_INSTALL_PERMF
   
    def is_install_tempf(self):
        """
        Returns true if this action defines the installation of a fastener.
       
        :return: bool, returns True if it is ACTION_TYPE_INSTALL_TEMPF
        """
        return self.__a_type == ACTION_TYPE_INSTALL_TEMPF
   
    
    def is_remove_tempf(self):
        """
        Returns true if this action defines the removal of a fastener.
       
        :return: bool, returns True if it is ACTION_TYPE_REMOVE_TEMPF
        """
        return self.__a_type == ACTION_TYPE_REMOVE_TEMPF
 
    
    def loc_uid(self):
        """
        Gets the location uid. This is the location of the waypoint or where a
        fastener needs to be removed or installed.
       
        :return: str, the uid of the action
        """
        return self.__loc_uid
   
 
    def set_loc_uid(self, loc_uid):
        """
        Sets the location uid. This is the location of the waypoint or where a
        fastener needs to be removed or installed.
       
        :param loc_uid: str, the uid of the action
        """
        self.__loc_uid = loc_uid
       
    
    def is_done(self):
        """
        Gets whether the action is finished.
        
        :return: bool, whether the action is finished.
        """
        return self.__is_done
   
 
    def set_as_done(self):
        """
        Sets the action as finished.
        """
        self.__is_cancelled = False
        self.__is_waiting = False
        self.__is_done = True
       
 
    def set_as_not_done(self):
        """
        Sets the action as unfinished.
        """
        self.__is_done = False
   
 
    def is_waiting(self):
        """
        Gets whether the action is waiting.
       
        :return: bool, whether the action is waiting.
        """
        return self.__is_waiting
   
 
    def set_as_waiting(self):
        """
        Sets the action as is waiting.
        """
        self.__is_cancelled = False
        self.__is_done = False
        self.__is_waiting = True
       
 
    def set_as_not_waiting(self):
        """
        Sets the action as not waiting.
        """
        self.__is_waiting = False
       
    
    def is_cancelled(self):
        """
        Gets whether the action is cancelled.
       
        :return: bool, whether the action is cancelled.
        """
        return self.__is_cancelled
   
 
    def set_as_cancelled(self):
        """
        Sets the action as cancelled.
        """
        self.__is_done = False
        self.__is_waiting = False
        self.__is_cancelled = True
       
 
    def set_as_not_cancelled(self):
        """
        Sets the action as uncancelled.
        """
        self.__is_cancelled = False
   
 
    def speed(self):
        """
        Gets the speed as percentage of the maximum speed.
       
        :return: float, percentage of maximum speed.
        """
        return self.__speed
 
 
    def set_speed(self, s):
        """
        Sets the speed as percentage of the maximum speed.
       
        :param s: float, the percentage of maximum speed
        """
        self.__speed = s
       
    
###########################################             START             ###################################################
  
set_velx(TCP_SPEED_LIMIT, TCP_ROT_LIMIT)  # The global task velocity is set to ...(mm/sec) and ...(deg/sec).
set_accx(120, 20) # The global task acceleration is set to ...(mm/sec2) and ...(deg/sec2).
change_operation_speed(100)

# create the axis systems used throughout the program
DR_USER_NOM = create_axis_syst_on_current_position()
DR_USER_PROBE = create_axis_syst_on_current_position()
DR_USER_NOM_OPP = create_axis_syst_on_current_position()
 
STOP_SERVER = False

# open a connection and a thread with the pc 
server_thread = thread_run(th_run_server, loop=False)
handler_thread = thread_run(handle_ros_msg, loop=False)
 
pos1=posx(0,0,0,0,0,0)
set_user_cart_coord(pos1, ref=DR_BASE)
set_user_cart_coord(pos1, ref=DR_BASE)
set_user_cart_coord(pos1, ref=DR_BASE)
 
sync_data_with_PC = True
 
###########################################
 
# instantiate the end effector
pf_ee = cl_perm_fast_ee()
tf_ee = cl_temp_fast_ee()
 
###########################################
 
# create a class that contains all actions
agent = cl_agent(None, None, None, pf_ee, tf_ee)
    
send_message("start program")
 
# create a class that contains all available storage locations
agent.tempf_storage = cl_f_container("tempf_storage")
agent.permf_storage = cl_f_container("permf_storage")
 
# add hole locations, stack thickness and diameter in the permanent fastener storage list 
# uid, diam, stack thickness, nom_pos 
agent.tempf_storage.add_loc_to_holes_and_fast_lst("tfst_01", 5, 10, posx(122.4,476.77,38,35,180,-35))
 
# add permanent fastener in storage
# uid, loc uid, fast_install_pos, diam, shaft height, min stack, max stack, tcp_tip_dist, tcp_top_dist, in_storage, in_ee, in_product, in_bin, is_tempf
agent.tempf_storage.add_fast_to_loc_with_uid("tempf_01", "tfst_01", None, 5 , DIAM_5_SHAFT_HEIGHT,DIAM_5_MIN_STACK, DIAM_5_MAX_STACK,DIAM_5_TCP_TIP_DIST, DIAM_5_TCP_TOP_DIST,True, False, False, False, True)

# create a class that contains all available hole positions in the product
agent.product = cl_f_container("product")
 
# add hole locations, stack thickness and diameter in the product list 
agent.product.add_loc_to_holes_and_fast_lst("pr_01_01", 5, 9, posx(-162,796,1155,89.16,75.8,-158.73))
agent.product.add_loc_to_holes_and_fast_lst("pr_01_02", 5, 9, posx(-126.5,796,1155,89.16,75.8,-158.73))
agent.product.add_loc_to_holes_and_fast_lst("pr_01_03", 5, 9, posx(-92,796,1155,89.16,75.8,-158.73))
agent.product.add_loc_to_holes_and_fast_lst("pr_01_04", 5, 9, posx(-56,796,1154.5,89.16,75.8,-158.73))
agent.product.add_loc_to_holes_and_fast_lst("pr_01_05", 5, 9, posx(-10,796,1154.5,89.16,75.8,-158.73))
agent.product.add_loc_to_holes_and_fast_lst("pr_01_06", 5, 9, posx(25.5,796,1154,89.16,75.8,-158.73))
agent.product.add_loc_to_holes_and_fast_lst("pr_01_07", 5, 9, posx(60,796,1154,89.16,75.8,-158.73))
agent.product.add_loc_to_holes_and_fast_lst("pr_01_08", 5, 9, posx(96,796,1154,89.16,75.8,-158.73))

# add permanent fastener in the product
# uid, loc uid, fast_install_pos, diam, shaft height, min stack, max stack, tcp_tip_dist, tcp_top_dist, in_storage, in_ee, in_product, in_bin, is_tempf
#agent.product.add_fast_to_loc_with_uid("tempf_01", "pr_01_01", None, 5 , DIAM_5_SHAFT_HEIGHT,DIAM_5_MIN_STACK, DIAM_5_MAX_STACK,DIAM_5_TCP_TIP_DIST, DIAM_5_TCP_TOP_DIST,False, False, True, False, True)

###########################################
# product.log_holes_and_fast_lst()

# go to home
speed_limited_movej_on_posj(posj(90,-30,120,0,0,0), 100)

# insert and install a permf from storage to product
agent._add_install_tempf_action("A01", "pr_01_01")
agent._add_remove_tempf_action("A02", "pr_01_01")

# agent.execute_all(check_inventory = False)
while True:
    wait(0.1)

# go to home
speed_limited_movej_on_posj(posj(90,-30,120,0,0,0), 100)
 
send_message("end program")
 
# close sockets and stop threads
STOP_SERVER = True
