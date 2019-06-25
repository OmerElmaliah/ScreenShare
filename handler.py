"""Handler Class - Receives Images From Customer And Displays Them"""
import socket
from PyQt5.QtGui import QPixmap
from PyQt5 import QtWidgets
import os.path
import threading
from pynput import mouse, keyboard
import pickle
import encryption as enc


class Handler(object):
    def __init__(self, ip_src, port_src, ip_dst, port_dst, key):
        self.comb = {'1': '!',
                     '2': '@',
                     '3': '#',
                     '4': '$',
                     '5': '%',
                     '6': '^',
                     '7': '&',
                     '8': '*',
                     '9': '(',
                     '0': ')',
                     '-': '_',
                     '=': '+',
                     '`': '~',
                     '\\': '|',
                     '[': '{',
                     ']': '}',
                     ';': ':',
                     "'": '"',
                     ',': '<',
                     '.': '>',
                     '/': '?'}
        self.num = 0
        self.cap_shift = False
        self.shift = False
        self.ip_src = ip_src
        self.port_src = port_src
        self.ip_dst = ip_dst
        self.port_dst = port_dst
        self.key = key
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.socket.bind((self.ip_src, self.port_src))
        self.window = QtWidgets.QLabel()
        self.window.showFullScreen()
        self.window.show()

    def run(self):
        """Calls 2 functions necessary to the handler's functioning, recv_img via thread and event_listener"""
        recv_img_thread = threading.Thread(target=self.recv_img)
        recv_img_thread.start()
        self.event_listener()

    def recv_img(self):
        """Creates an empty image on the computer, receives data from customer and 'builds' a new image with the data"""
        while True:
            rewrite_data = None
            if os.path.isfile('img.png'):
                os.remove('img.png')
            img = open('img.png', 'wb')
            while True:
                data = pickle.loads(self.socket.recv(16384))
                if data != "Image sent!":
                    data = enc.decrypt(data, self.key).encode('ISO-8859-1')
                    if rewrite_data is None:
                        rewrite_data = data
                    else:
                        rewrite_data = rewrite_data + data
                else:
                    img.write(rewrite_data)
                    img.close()

                    img_display = QPixmap('img.png')
                    self.window.setPixmap(img_display)
                    self.window.setScaledContents(True)
                    self.window.update()
                    break

    def event_listener(self):
        """Listens for commands committed on the computer and calls relevant functions"""
        listener_keyboard = keyboard.Listener(
                on_press=self.on_press,
                on_release=self.on_release)

        listener_mouse = mouse.Listener(
                on_move=self.on_move,
                on_click=self.on_click,
                on_scroll=self.on_scroll)

        listener_mouse.start()
        listener_keyboard.start()
        listener_keyboard.join()
        listener_mouse.join()

    def on_click(self, x, y, button, pressed):
        """Filters commands committed via mouse clicks, sends the customer which command to make

        ARGS:
            x && y(int) - Represents the location of the mouse on the screen
            button(custom) - Represents the button pressed on the mouse
            pressed(boolean) - True if button is down, False if up
        """
        if button == mouse.Button.left and pressed:
            self.socket.sendto(pickle.dumps("left pressed"), (self.ip_dst, self.port_dst))
        elif button == mouse.Button.left:
            self.socket.sendto(pickle.dumps("left released"), (self.ip_dst, self.port_dst))
        elif button == mouse.Button.right and pressed:
            self.socket.sendto(pickle.dumps("right pressed"), (self.ip_dst, self.port_dst))
        else:
            self.socket.sendto(pickle.dumps("right released"), (self.ip_dst, self.port_dst))

    def on_move(self, x, y):
        """Sends the customer the current location of the mouse on the screen

        ARGS:
            x && y(int) - Represents the location of the mouse on the screen
        """
        cords = (x, y)
        if self.num == 10:
            self.socket.sendto(pickle.dumps(cords), (self.ip_dst, self.port_dst))
            self.num = 0
        else:
            self.num += 1

    def on_scroll(self, x, y, dx, dy):
        """Filters mouse scroll commands and sends which command to make to the customer

        ARGS:
            x && y(int) - Represents the location of the mouse on the screen when scrolling
            dy(int) - Vertical scrolling, Value is 1 if scrolling up, -1 if down
            dx(int) - Horizontal scrolling, Value is 1 if scrolling right, -1 if left
        """
        if dy == 1:
            self.socket.sendto(pickle.dumps("up"), (self.ip_dst, self.port_dst))
        elif dy == -1:
            self.socket.sendto(pickle.dumps("down"), (self.ip_dst, self.port_dst))
        elif dx == 1:
            self.socket.sendto(pickle.dumps("rig2"), (self.ip_dst, self.port_dst))
        elif dx == -1:
            self.socket.sendto(pickle.dumps("lef2"), (self.ip_dst, self.port_dst))

    def on_press(self, key):
        """Filters keyboard presses, sends the customer which key to press"""
        if 'shift' in str(key) and (not self.shift):
            self.shift = True

        elif self.shift and ('Key' not in str(key)) and (str(key)[1] in self.comb):
            key = self.comb[str(key)[1]]
            self.socket.sendto(pickle.dumps("press: '" + str(key) + "'"), (self.ip_dst, self.port_dst))

        elif self.cap_shift and ('Key' not in str(key)):
            key = str(key)[1].upper()
            self.socket.sendto(pickle.dumps("press: '" + str(key) + "'"), (self.ip_dst, self.port_dst))

        elif 'shift' not in str(key):
            self.socket.sendto(pickle.dumps("press: " + str(key)), (self.ip_dst, self.port_dst))

    def on_release(self, key):
        """Filters keyboard releases, sends the customer which key to releases"""
        if 'caps_lock' in str(key) and (not self.cap_shift):
            self.cap_shift = True
        elif 'caps_lock' in str(key) and self.cap_shift:
            self.cap_shift = False

        if self.shift and 'alt_l' in str(key):
            self.socket.sendto(pickle.dumps("change_lang"), (self.ip_dst, self.port_dst))

        if 'shift' in str(key) and self.shift:
            self.shift = False
        elif 'shift' not in str(key):
            self.socket.sendto(pickle.dumps("release: " + str(key)), (self.ip_dst, self.port_dst))

    def close_connection(self):
        """Closes connection with the customer"""
        self.socket.close()
