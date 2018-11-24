"""Handler Class - Receives Images From Customer And Displays Them"""
import socket
from PyQt5.QtGui import QPixmap
from PyQt5 import QtWidgets
import os.path


class Handler(object):
    def __init__(self, ip_src, port_src, ip_dst, port_dst):
        self.ip_src = ip_src
        self.port_src = port_src
        self.ip_dst = ip_dst
        self.port_dst = port_dst
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.socket.bind((self.ip_src, self.port_src))
        self.window = QtWidgets.QLabel()
        self.window.show()

    def recv_img(self):
        while True:
            rewrite_data = None
            if os.path.isfile('D:\images\img.png'):
                os.remove('D:\images\img.png')
            img = open('D:\images\img.png', 'wb')
            while True:
                data = self.socket.recv(8192)
                if rewrite_data is None:
                    rewrite_data = data
                else:
                    rewrite_data = rewrite_data + data
                if "Image sent!".encode('utf-8') in data:
                    img.write(rewrite_data)
                    img.close()

                    img_display = QPixmap('D:\images\img.png')
                    self.window.setPixmap(img_display)
                    self.window.setScaledContents(True)
                    self.window.update()
                    break

    def close_connection(self):
        self.socket.close()
