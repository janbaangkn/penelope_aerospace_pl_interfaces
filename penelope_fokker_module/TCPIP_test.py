from tcp_communication.tcp_client import run_tcp_client
from tcp_communication.communication_functions import send_message
import threading

ip_address = "10.237.20.101"
port = 20002
robot_uid = f"{ip_address}/{port}"

tcp_client_thread = threading.Thread(target=run_tcp_client, args=(ip_address, port))
tcp_client_thread.start()
message = "execute<uid<A01>>"

send_message(uid=robot_uid, message=message)

# agent._add_install_tempf_action("A01", "pr_01_01")
# agent._add_remove_tempf_action("A02", "pr_01_01")
