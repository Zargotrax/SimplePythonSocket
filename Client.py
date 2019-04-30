#Client
import socket
import subprocess


hote = "localhost"
port = 15555

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.connect((hote, port))
print ("Connection on {}".format(port))

while True:
    msg = socket.recv(255)
    if msg == (b'exit'):
        socket.close()
        break
    else: 
        print(msg)

print ("Close")
socket.close()