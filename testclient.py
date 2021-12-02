import socket
import sys
import time

HOST, PORT = "127.0.1.1", 6666
# data = " ".join(sys.argv[1:])
socket_open = False


def send_message(connection):
    msg = input()
    connection.sendall(bytes(msg + "\n", "utf-8"))


def receive_message(connection):
    received = str(connection.recv(1024), "utf-8")
    print(received)


try:
    data = input()
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Connect to server and send data
    sock.connect((HOST, PORT))

    socket_open = True

    while True:
        try:
            print('hii')
        except Exception as e:
            print(e)
            break

    if socket_open:
        sock.close()
    # sock.sendall(bytes(data + "\n", "utf-8"))

    # Receive data from the server and shut down
    # received = str(sock.recv(1024), "utf-8")

    # print("Sent:     {}".format(data))
    # print("Received: {}".format(received))
    # time.sleep(0.2)
except Exception as e:
    print(e)

# sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Connect to server and send data
# sock.connect((HOST, PORT))
