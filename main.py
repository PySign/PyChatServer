#!/usr/bin/python3

import _thread
import socket
import sys

name = 'Server'

soc = socket.socket()
host_name = socket.gethostname()
ip = socket.gethostbyname(host_name)
port = 6666
soc.bind((host_name, port))

# name = input('Enter name: ')
soc.listen(1)  # Try to locate using socket
print('Waiting for incoming connections...')
connection, address = soc.accept()
print("Received connection from ", address[0], "(", address[1], ")\n")
print(f'Connection Established. Connected From: {address[0]}, ({address[0]})')

client_name = connection.recv(1024)
client_name = client_name.decode()

print(client_name + ' has connected...')
print('Enter -q to exit.')
connection.send(name.encode())

run = True


def print_msg(thread_name):
    while run:
        msg = connection.recv(1024)
        msg = msg.decode()
        if msg == "-q":
            print(f'{client_name} exit the chat room\n\n')
            sys.exit(1)
        elif msg != "":
            print(f'{client_name}: {msg}')


while True:
    try:
        _thread.start_new_thread(print_msg, ("Thread-1",))
    except Exception as e:
        print(e)
        break

    try:
        message = input(f'{name}: ')
        if message == '-q':
            connection.send(message.encode())
            print("\n")
            break
        connection.send(message.encode())
    except KeyboardInterrupt:
        print('Enter -q to close the connection.')
