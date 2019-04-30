#Server
import socket

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.bind(('', 15555))

print("Waiting for connection...")
socket.listen(5)
client, address = socket.accept()
print ("Connection from {}".format( address ))

while True:
    command = input(">>")

    if command == ('exit'):
        client.send(b'exit')
        client.close()
        break
    else:
        client.send(command.encode())

print ("Close")
client.close()
socket.close()