"""Customer Class - Sends current screen image"""
import socket
from PIL import ImageGrab, Image
import threading
import pickle
import pyautogui


class Customer(object):
    def __init__(self, ip_src, port_src, ip_dst, port_dst):
        self.ip_src = ip_src
        self.port_src = port_src
        self.ip_dst = ip_dst
        self.port_dst = port_dst
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.socket.bind((self.ip_src, self.port_src))
        self.main_con = True
        # TODO: Add an exit button with exit_button_ui.py

    def run(self):
        work_thread = threading.Thread(target=self.start_work)
        work_thread.start()
        self.event_filter()

    def start_work(self):
        while True:
            img = ImageGrab.grab()
            img.thumbnail((1080, 720), Image.ANTIALIAS)
            img.save('img.png')

            with open('img.png', 'rb') as screen_image:
                img_data = screen_image.read(8192)
                while img_data:
                    self.socket.sendto(img_data, (self.ip_dst, self.port_dst))
                    img_data = screen_image.read(8192)
                self.socket.sendto("Image sent!".encode('utf-8'), (self.ip_dst, self.port_dst))
                screen_image.close()

    def event_filter(self):
        while self.main_con:
            data = pickle.loads(self.socket.recv(1024))
            if "right" in data and "pressed" in data:
                pyautogui.mouseDown(button='right')
            elif "right" in data and "released" in data:
                pyautogui.mouseUp(button='right')
            elif "left" in data and "pressed" in data:
                pyautogui.mouseDown(button='left')
            elif "left" in data and "released" in data:
                pyautogui.mouseUp(button='left')
            elif "up" in data:
                pyautogui.scroll(10)
            elif "down" in data:
                pyautogui.scroll(-10)
            elif "rig2" in data:
                pyautogui.hscroll(10)
            elif "lef2" in data:
                pyautogui.hscroll(-10)
            else:
                pyautogui.moveTo(data)

    def set_connection_status(self, con):
        self.main_con = con

    def close_connection(self):
        self.main_con = False
        self.socket.close()
