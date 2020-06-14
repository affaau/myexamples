import socket
import pickle

HEADERSIZE = 10
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
## Initialize server connection
print(socket.gethostname())
s.connect((socket.gethostname(), 1234))

# If a much smaller buffer is used...
full_msg = b''
new_msg = True
while True:
    msg = s.recv(16)   # larger than HEADERSIZE 
    if new_msg:
        print(f'new message length: {msg[:HEADERSIZE]}')
        msglen = int(msg[:HEADERSIZE])
        new_msg = False

    full_msg += msg

    if len(full_msg) - HEADERSIZE == msglen:
        print("full msg recvd")
        print(full_msg[HEADERSIZE:])

        d = pickle.loads(full_msg[HEADERSIZE:])
        print(d)

        new_msg = True
        full_msg = b''
#
s.close()
