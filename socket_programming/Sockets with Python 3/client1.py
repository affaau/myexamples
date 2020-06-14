import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
## Initialize server connection
print(socket.gethostname())
s.connect((socket.gethostname(), 1234))

# msg = s.recv(1024)
# print(msg.decode("utf-8"))

# If a much smaller buffer is used...
full_msg = ''
while True:
    msg = s.recv(8)
    if len(msg) <= 0:  # Happen when connection is terminated
        break
    full_msg += msg.decode("utf-8")

print(full_msg)
#

s.close()
