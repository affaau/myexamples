#!/usr/bin/env python3
'''Simple Client
>>> python simpleClient textToSend

When textToSend equals exit, program terminates
'''

# Import socket module
import socket
import sys      

# Create a socket object
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)         

# Define the port on which you want to connect
port = 12345                

# connect to the server on local computer
s.connect(('127.0.0.1', port))

str_as_bytes = str.encode(sys.argv[1])   # argv[1]==textToSend
#s.sendall(b'Hello!')
s.sendall(str_as_bytes)
# receive data from the server
print(s.recv(1024))

# close the connection
s.close()     
