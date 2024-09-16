from tcp_communication.defaults import DEFAULT_ENCODER
from tcp_communication.message_processor import TCPInputProcessor
from tcp_communication.message_service_class import MessageService
import socket
import time
import traceback


class TCPClient:
    def __repr__(self):
        return "{0} (host: {1}, port: {2})".format(self.__class__.__name__, self.host, self.port)

    def __init__(self, host, port, encoder=DEFAULT_ENCODER):
        self.host = host
        self.port = port
        self.uid = "{0}/{1}".format(self.host, self.port)
        self.encoder = encoder
        self.input_processor = TCPInputProcessor(uid=self.uid, encoder=self.encoder)
        self.socket = socket.socket()
        self._connect()

    def _connect(self):
        self.socket.connect((self.host, self.port))

    def _reconnect(self):
        # FIXME: add check to verify if the socket is already closed
        print("Reconnecting")
        self.socket.close()
        self.socket = socket.socket()
        self._connect()

    def _send_message(self, message):
        try:
            self.socket.sendall(message.encoded)
            #print("message is send: {0}".format(message))
            return 0
        except ConnectionResetError:
            self._reconnect()
            self._send_message(message)

    def _send_messages(self):
        continue_sending = True
        while continue_sending:
            message = MessageService().get_outbox_message(uid=self.uid)
            if message:
                #print("Sending message: {0} <{1}>".format(message.uid, message.message))
                self._send_message(message)
            else:
                return 0

    def _listen(self):
        self.socket.settimeout(0.1)
        try:
            raw_input = self.socket.recv(1024)
            self.input_processor.update_raw_input(raw_input)
        except ConnectionResetError as e:
            print(e)
            self._reconnect()
            self._listen()
        except socket.timeout:
            return 0
        except Exception:
            print(traceback.format_exc())
            self._reconnect()
            return 0

        self.input_processor.process_raw_input()
        return 0

    def run(self):
        while True:
            # print("Start listening")
            self._listen()
            # print("Start sending")
            self._send_messages()
            time.sleep(0.01)


def run_tcp_client(ip_address: str, port: int) -> None:
    client = TCPClient(
        host=ip_address,
        port=port,
    )
    client.run()
