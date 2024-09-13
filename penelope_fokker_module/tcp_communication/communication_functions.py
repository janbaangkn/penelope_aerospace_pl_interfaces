from __future__ import annotations
from tcp_communication.defaults import DEFAULT_ENCODER
from tcp_communication.message_service_class import MessageService
from tcp_communication.message_classes import TCPMessage, TCPResponse, MessageUID
from utils.not_applicatble_classes import NoFeedbackReceived
import time


def construct_tcp_message(message, input_data=None, encoder=DEFAULT_ENCODER, response_required=False):
	return TCPMessage(
		message=message,
		uid=MessageUID.get_new_uid(),
		input_data=input_data,
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


def send_message(uid, message, input_data=None, feedback=True):
	tcp_message = construct_tcp_message(message=message, input_data=input_data, response_required=feedback)
	MessageService().add_outbox_message(uid=uid, message=tcp_message)
	if feedback:
		return collect_response(uid=uid, message_uid=tcp_message.uid)
	return None


def send_response(uid, original_message, response="processed", feedback=False):
	tcp_response = construct_tcp_response(
		response_uid=original_message.uid,
		response=response,
		response_required=feedback,
	)
	MessageService().add_outbox_message(uid=uid, message=tcp_response)
	if feedback:
		return collect_response(uid=uid, message_uid=tcp_response.uid)
	return None


def collect_response(uid, message_uid, time_out=300.0):
	start_time = time.time()
	while time.time() - start_time < time_out:
		response = MessageService().get_response(uid=uid, message_uid=message_uid)
		if response:
			return response
	raise NoFeedbackReceived(message=message_uid)
