import socket
import time

## Add a fixed length header in front of new message
## to tell the number of bytes transmitted

HEADERSIZE = 10
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # IPv4, TCP
s.bind((socket.gethostname(), 1234))
s.listen(5)

while True:
    # keyboard interrupt can't terminate accept()
    clientsocket, address = s.accept()   
    print(f"Connection from {address} has been established!")

    msg = "Welcome to the server!"
    # reserve fixed 10 characters space & align to the left
    msg = f'{len(msg):<{HEADERSIZE}}' + msg

    clientsocket.send(bytes(msg, "utf-8"))
    # connection remains open

    # as an example
    # continue to send SOMETHING very few seconds
    while True:
        time.sleep(3)
        msg = f'The time is {time.time()}'
        msg = f'{len(msg):<{HEADERSIZE}}' + msg
        # can be interrupted when remote client is terminated
        clientsocket.send(bytes(msg, "utf-8"))  
##
