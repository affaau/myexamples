import socket
import time
# module pickle
#   serialize object and save
#   load and deserialize into object
import pickle

## Add a fixed length header in front of new message
## to tell the number of bytes transmitted

HEADERSIZE = 10
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # IPv4, TCP
s.bind((socket.gethostname(), 1234))
s.listen(5)

while True:
    clientsocket, address = s.accept()
    print(f"Connection from {address} has been established!")

    d = {1:"Hey", 2:"There"}
    msg = pickle.dumps(d) # serialize the data
    msg = bytes(f'{len(msg):<{HEADERSIZE}}', 'utf-8') + msg

    clientsocket.send(msg)
##
