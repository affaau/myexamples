import socket
# allow to connect multiple clients
import select

HEADER_LENGTH = 10
IP = "127.0.0.1"
PORT  = 1234

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# allows to reconnect
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)

server_socket.bind((IP, PORT))
server_socket.listen()

sockets_list = [server_socket]

# use clientss sockets as keys
clients = {}

def receive_message(client_socket):
    try:
        message_header = client_socket.recv(HEADER_LENGTH)
        if not len(message_header):  # connection closed
            return False

        message_length = int(message_header.decode('utf-8').strip())
        return {"header": message_header, "data":client_socket.recv(message_length)}

    except:
        return False

while True:
    # select([read list], [write list], [error list])
    read_sockets, _, exception_sockets = select.select(sockets_list, [], sockets_list)

    for notified_socket in read_sockets:
        if notified_socket == server_socket:
            client_socket, client_address = server_socket.accept()
            user = receive_message(client_socket)
            if user is False:
                continue

            sockets_list.append(client_socket)
            clients[client_socket] = user
