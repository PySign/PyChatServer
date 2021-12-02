import socket
import sys
import rsa
import json
from threading import Thread


class Server:
    def __init__(self):
        self.name = 0
        self._port = 0
        self.__key = ''
        self.__pub = ''
        self._key_size = 0
        self._clients = []
        s_name = socket.gethostname()
        self._host = socket.gethostbyname(s_name)
        self.thread_count = 0
        self.main_socket = socket.socket()
        # try:
        #     self.main_socket.bind((self._host, self.port))
        # except socket.error as e:
        #     print(str(e))
        #     sys.exit(1)
        #
        # self.main_socket.listen(10)
        # self._clients = []

    def get_data(self):
        try:
            with open('.config', 'r') as f:
                data = json.load(f)

                self.name = data['name']
                self._port = data['port']
                self._key_size = data['key_size']
        except FileNotFoundError:
            # sys.exit({'message': 'Config file not found !!'})
            self.generate_file()

    def generate_key(self):
        if not self._key_size:
            self.get_data()

        self.__pub, self.__key = rsa.newkeys(int(self._key_size))
        print(self.__pub)
        print(self.__key)

    def generate_file(self):
        done = False
        while not done:
            try:
                name = input('Enter server name[press enter for Root]: ')
                port = input('Choose a port[press enter for 6666]: ')
                key_size = input('Choose key size[press enter for 1024]: ')
                data = {
                    'name': name if name else 'Root',
                    'port': int(port) if port else 6666,
                    'key_size': int(key_size) if key_size else 1024,
                }
                with open('.config', 'w') as f:
                    json.dump(data, f)
                done = True
            except Exception as e:
                print(e)
                print('Try again!!\n\n')

        self.get_data()

    def save_client(self, name, ip, port, password):
        client = {
            'name': name,
            'ip': ip,
            'port': port,
            'password': password,
            'datetime': ''
        }
        self._clients.append(client)

    def connect(self):
        obj, address = self.main_socket.accept()
        ip, port = address
        print(f'Connected to: {ip}:{port}')

    def config(self):
        self.get_data()
        self.generate_key()

    def listen(self):
        self.config()
        print(f'Server started {self._host}:{self._port}')
        # while True:
        #     Thread(target=self.connect()).start()


s = Server()
print('Hello')
s.config()
# s.listen()
