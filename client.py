# import socket
# import sys
# from threading import Thread
#
#
# class Client:
#     def __init__(self, path):
#         s_name = socket.gethostname()
#         self.host = socket.gethostbyname(s_name)
#         self.port = 6666
#         self.thread_count = 0
#         self.main_socket = socket.socket()
#         try:
#             self.main_socket.bind((self.host, self.port))
#         except socket.error as e:
#             print(str(e))
#             sys.exit(1)
#
#         self.main_socket.listen(10)
#         self.clients = []
#
#     def save_client(self, name, ip, port, password):
#         client = {
#             'name': name,
#             'ip': ip,
#             'port': port,
#             'password': password,
#             'datetime': ''
#         }
#         self.clients.append(client)
#
#     def connect(self):
#         obj, address = self.main_socket.accept()
#         ip, port = address
#         print(f'Connected to: {ip}:{port}')
#
#     def listen(self):
#         print(f'Server started {self.host}:{self.port}')
#         while True:
#             Thread(target=self.connect()).start()
#
#
# s = Server('Admin')
# s.listen()
#
