#!/usr/bin/env python3

import socket, requests

def getSocketAdr():
    s_adr = socket.gethostbyname(socket.gethostname())
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect((s_adr, 0))
    # Allocated socket address & port number
    adr, port = s.getsockname()
    print('Your Socket is {}, port is {}'.format(adr, port))
    s.close()
    return (adr, port)  
    
def getPublicIPAdr():
    r = requests.get(r'http://jsonip.com')
    ip= r.json()['ip']
    # Likely the IP assigned to your router by ISP
    print('Your Public IP is', ip)
    return ip

def server():
    s = socket.socket()         
    print("Socket successfully created")

    port = 12345                

    s.bind(('127.0.0.1', port))        
    print("socket binded to %s" %(port))

    s.listen(5)     
    print("socket is listening")

    while True:
       c, addr = s.accept()     
       print('Got connection from', addr)
       msg = c.recv(1024)
       print(msg)
       c.send(b'Thank you for connecting')
       c.close()
       if msg == b'exit': break

if __name__ == '__main__':
    getSocketAdr()
    getPublicIPAdr()
    #server()
    
