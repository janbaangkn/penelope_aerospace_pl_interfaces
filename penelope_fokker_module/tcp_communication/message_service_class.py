from __future__ import annotations
from tcp_communication.message_classes import TCPMessage, TCPResponse


class MessageTypeError(Exception):
    """Raised if the message is not of type TCPMessage or TCPResponseMessage."""

    def __init__(self):
        message = "The message is not of type TCPMessage or TCPResponseMessage!"
        super().__init__(message)


class MessageService:
    inboxes = {}
    outboxes = {}

    @classmethod
    def reset_inboxes(cls):
        cls.inboxes = {}

    @classmethod
    def reset_outboxes(cls):
        cls.outboxes = {}

    @classmethod
    def reset(cls):
        cls.reset_inboxes()
        cls.reset_outboxes()

    @classmethod
    def add_inbox_message(cls, uid, message):
        if not cls.inboxes.get(uid):
            cls.inboxes[uid] = TCPInbox()

        cls.inboxes[uid].add_message(message)

    @classmethod
    def add_outbox_message(cls, uid, message):
        if not cls.inboxes.get(uid):
            cls.outboxes[uid] = TCPOutbox()

        cls.outboxes[uid].add_message(message)

    @classmethod
    def get_inbox_message(cls, uid):
        if cls.inboxes.get(uid):
            return cls.inboxes[uid].get_message()
        return None

    @classmethod
    def get_outbox_message(cls, uid):
        if cls.outboxes.get(uid):
            return cls.outboxes[uid].get_message()
        return None

    @classmethod
    def get_response(cls, uid, message_uid):
        if cls.inboxes.get(uid):
            return cls.inboxes[uid].get_response(message_uid)

    @classmethod
    def remove_inbox_message(cls, uid, message_uid):
        if cls.inboxes.get(uid):
            cls.inboxes[uid].remove_message(message_uid)

    @classmethod
    def remove_outbox_message(cls, uid, message_uid):
        if cls.outboxes.get(uid):
            cls.outboxes[uid].remove_message(message_uid)


class TCPOutbox:
    """Class to collect messages that are to be send via the TCP connection.

    In contrary to the TCPInbox, the outbox only has a single class variable, which is used to store messages.
    The TCP Client or Server will call the 'get_message' method to collect a message that it will send. This method
    automatically removes the message once it is collected.

    The class needs to be accessible in multiple parts of the code, hence the
    use of class variables.
    """

    def __repr__(self):
        return "{0}".format(self.__class__.__name__)

    def __init__(self):
        self.messages = []

    def reset(self):
        """Reset the class variables."""
        self.messages = []

    def add_message(self, message):
        """Add a message to the class variable 'messages'.

        The message needs to be of type TCPMessage or TCPResponse.
        """
        if not isinstance(message, (TCPMessage, TCPResponse)):
            raise MessageTypeError
        self.messages.append(message)
        print("Message {0} added to outbox <{1}>".format(message.uid, message.message))

    def _get_first_message(self):
        """Collect the first message stored in 'self.messages'.

        If the class variable 'messages' is empty, the method returns a None.
        """
        if self.messages:
            return self.messages[0]
        return None

    def remove_message(self, uid):
        """Remove the message with the given uid from 'self.messages'."""
        self.messages = [msg for msg in self.messages if msg.uid != uid]

    def get_message(self):
        """"""
        message = self._get_first_message()
        if message:
            self.remove_message(message.uid)
        return message


class TCPInbox:
    def __repr__(self):
        return "{0}".format(self.__class__.__name__)

    def __init__(self):
        self.priority_messages = []
        self.messages = []
        self.responses = []

    def reset(self):
        self.priority_messages = []
        self.messages = []
        self.responses = []

    def add_message(self, message):
        if not isinstance(message, (TCPMessage, TCPResponse)):
            raise MessageTypeError
        
        print(f"Message {message.uid} added to inbox: {message.message}")

        if isinstance(message, TCPResponse):
            self.responses.append(message)
        else:
            self.messages.append(message)
        # print("Message: {} is added with text: {}".format(message.uid, message.message))

    def remove_message(self, uid):
        self.priority_messages = [msg for msg in self.priority_messages if msg.uid != uid]
        self.messages = [msg for msg in self.messages if msg.uid != uid]
        self.responses = [msg for msg in self.responses if msg.uid != uid]

    def get_response(self, uid):
        response = next((msg for msg in self.responses if msg.response_uid == uid), None)
        if response:
            self.responses = [msg for msg in self.responses if msg.uid != response.uid]
        return response

    def _get_first_message(self):
        if self.priority_messages:
            return self.priority_messages[0]
        if self.messages:
            return self.messages[0]
        return None

    def get_message(self):
        message = self._get_first_message()
        if message:
            self.remove_message(message.uid)
        return message
