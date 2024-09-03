from tcp_communication.defaults import DEFAULT_ENCODER
from tcp_communication.enums import MessageNames
from tcp_communication.message_service_class import MessageService
from tcp_communication.message_classes import TCPMessage, TCPResponse


class TCPInputProcessor:
    def __repr__(self):
        return "{0}".format(self.__class__.__name__)

    def __init__(self, uid, encoder=DEFAULT_ENCODER):
        self.uid = uid
        self.encoder = encoder
        self.raw_input = "".encode(self.encoder)

    def set_raw_input(self, raw_input):
        self.raw_input = raw_input

    def update_raw_input(self, reading_input):
        self.raw_input += reading_input
        print(f"raw input is set to: {self.raw_input}")

    def process_raw_input(self):
        byte_size_length = 4
        if len(self.raw_input) > byte_size_length:
            byte_size = int(self.raw_input[:byte_size_length].decode(self.encoder))
            if len(self.raw_input) >= byte_size:
                isolated_message = self.raw_input[:byte_size].decode(self.encoder)
                print(f"Raw incoming message: {isolated_message}")
                tcp_message = self.reconstruct_tcp_message(isolated_message)
                MessageService().add_inbox_message(self.uid, tcp_message)
                self.set_raw_input(self.raw_input[byte_size:])
                self.process_raw_input()

    def reconstruct_tcp_message(self, raw_tcp_message):
        # determine size of preamble
        byte_size, uid = raw_tcp_message.split("/")[:2]
        preamble_size = len(byte_size) + len(uid) + 2
        raw_message = raw_tcp_message[preamble_size:]

        # remove the <respond: > section from the raw message
        raw_respond = raw_message.split("<{0}:".format(MessageNames.RESPOND))[-1].split(">")[0].lower()
        respond = raw_respond == "true"
        message_end = len(raw_message) - (len(MessageNames.RESPOND) + 3 + len(raw_respond))
        message = raw_message[:message_end]

        # check if message contains <data>
        input_data = None
        if "<" in message:
            message = message.split("<")[0]
            input_data = raw_message[len(message) + 1: message_end - 1]

        # determine if the message is a response
        if message.split("_")[0] == MessageNames.RESPONSE:
            response_uid = int(message.split("_")[-1])
            return TCPResponse(
                response=input_data,
                uid=uid,
                response_uid=response_uid,
                encoder=self.encoder,
                response_required=respond,
            )
        else:
            return TCPMessage(message, uid, input_data, self.encoder, respond)
