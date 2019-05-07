import socket
import pickle


IP = '192.168.1.174'
PORT = 8888


class UserBase(object):
    # TODO: Reorganize accordingly to dataserver(qthread?)
    def __init__(self):
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_socket.connect(('192.168.1.174', 8888))

    def create_account(self, user, psw):
        self.client_socket.send("ub-ca".encode('utf-8'))
        self.client_socket.send(user.encode('utf-8'))
        self.client_socket.send(psw.encode('utf-8'))

        return pickle.loads(self.client_socket.recv(1024))

    def verification(self, user, psw):
        self.client_socket.send("ub-ver".encode('utf-8'))
        self.client_socket.send(user.encode('utf-8'))
        self.client_socket.send(psw.encode('utf-8'))

        return pickle.loads(self.client_socket.recv(1024))

    def close(self):
        self.client_socket.close()
