"""Handler Class - Receives Images From Customer And Displays Them"""
import socket
from PyQt5.QtGui import QPixmap
from PyQt5 import QtWidgets
import os.path
import win32api
import time
import pickle


class Handler(object):
    def __init__(self, ip_src, port_src, ip_dst, port_dst):
        self.ip_src = ip_src
        self.port_src = port_src
        self.ip_dst = ip_dst
        self.port_dst = port_dst
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.socket.bind((self.ip_src, self.port_src))
        self.window = QtWidgets.QLabel()
        self.window.showMaximized()
        self.window.show()

    def run(self):
        while True:
            self.recv_img()
            self.send_mouse_click()

    def recv_img(self):
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

    def send_mouse_click(self):
        state_left = win32api.GetKeyState(0x01)
        state_right = win32api.GetKeyState(0x02)
        con = True

        if state_left == -127 or state_left == -128:
            self.socket.sendto(pickle.dumps("left"), (self.ip_dst, self.port_dst))
            con = False

        if (state_right == -127 or state_right == -128) and con:
            self.socket.sendto(pickle.dumps("right"), (self.ip_dst, self.port_dst))
            con = False

        if con:
            self.socket.sendto(pickle.dumps(win32api.GetCursorPos()), (self.ip_dst, self.port_dst))

    def close_connection(self):
        self.socket.close()
