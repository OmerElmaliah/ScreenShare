"""Customer Class - Sends current screen image"""
import socket
from PIL import ImageGrab, Image


class Customer(object):
    def __init__(self, ip, port):
        self.ip = ip
        self.port = port
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.socket.bind((self.ip, self.port))
        self.main_con = True

    def start_work(self):
        while self.main_con:
            img = ImageGrab.grab()
            img.thumbnail((1080, 1920), Image.ANTIALIAS)
            img.save('img.png')

            with open('img.png', 'rb') as screen_image:
                img_data = screen_image.read(8192)
                while img_data:
                    self.socket.sendto(img_data, (self.ip, self.port))
                    img_data = screen_image.read(8192)
                self.socket.sendto("Image sent!".encode('utf-8'), (self.ip, self.port))
                screen_image.close()

        self.socket.close()

    def set_connection_status(self, con):
        self.main_con = con

    def close_connection(self):
        self.main_con = False
        self.socket.close()
