from tcp_communication.enums import MessageNames
from tcp_communication.defaults import DEFAULT_ENCODER


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


class TCPMessage:
    def __repr__(self):
        return "{0} (uid: {1}, message: {2})".format(
            self.__class__.__name__,
            self.uid,
            self.message,
        )

    def __init__(self, message, uid, input_data=None, encoder=DEFAULT_ENCODER, response_required=False):
        self.uid = uid
        self.message = message
        self.input_data = input_data
        self.encoder = encoder
        self.response_required = response_required
        self.message_type = self.determine_message_type()
        self.encoded = self.construct_encoded_tcp_message()

    def determine_message_type(self):
        if self.message[:len(MessageNames.STOP)] == MessageNames.STOP:
            return MessageNames.STOP
        if self.message[:len(MessageNames.PAUSE)] == MessageNames.PAUSE:
            return MessageNames.PAUSE
        if self.message[:len("get")] == "get":
            return "getter"
        if self.message[:len("set")] == "set":
            return "setter"
        if self.message[:len(MessageNames.RESPONSE)] == MessageNames.RESPONSE:
            return MessageNames.RESPONSE

    def construct_encoded_tcp_message(self):
        if self.input_data is not None:
            expanded_message = "/{0}/{1}<{2}><{3}:{4}>".format(
                self.uid, self.message, self.input_data, MessageNames.RESPOND, self.response_required)
        else:
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
