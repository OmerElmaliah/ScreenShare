"""Customer Class - Sends current screen image"""
import socket
import cv2
import threading
import pickle
import pyautogui
from mss import mss
import encryption as enc


class Customer(object):
    def __init__(self, ip_src, port_src, ip_dst, port_dst, key):
        self.ip_src = ip_src
        self.port_src = port_src
        self.ip_dst = ip_dst
        self.port_dst = port_dst
        self.key = key
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.socket.bind((self.ip_src, self.port_src))
        self.main_con = True
        pyautogui.FAILSAFE = False

    def run(self):
        """Calls 2 functions necessary to the customer's functioning, start_work via thread and event_filter"""
        work_thread = threading.Thread(target=self.start_work)
        work_thread.start()
        self.event_filter()

    def start_work(self):
        """Captures and saves an image of the screen, sends the image encrypted to the handler"""
        while True:
            mss().shot(output="img.png")
            img = cv2.imread("img.png")
            img_resized = cv2.resize(img, (1080, 720))
            cv2.imwrite("img.png", img_resized)

            with open('img.png', 'rb') as screen_image:
                img_data = screen_image.read(8192).decode('ISO-8859-1')
                while img_data:
                    self.socket.sendto(pickle.dumps(enc.encrypt(img_data, self.key)), (self.ip_dst, self.port_dst))
                    img_data = screen_image.read(8192).decode('ISO-8859-1')
                self.socket.sendto(pickle.dumps("Image sent!"), (self.ip_dst, self.port_dst))
                screen_image.close()

    def event_filter(self):
        """Filters commands sent by the handler and executes them"""
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
                pyautogui.scroll(175)
            elif "down" in data:
                pyautogui.scroll(-175)
            elif "rig2" in data:
                pyautogui.hscroll(175)
            elif "lef2" in data:
                pyautogui.hscroll(-175)
            elif "change_lang" in data:
                pyautogui.hotkey('shift', 'altleft')
            elif "press:" in data:
                if 'Key' in data:
                    pyautogui.keyDown(data[data.find('.') + 1:])
                else:
                    pyautogui.keyDown(data[data.find(':') + 3])
            elif "release:" in data:
                if 'Key' in data:
                    pyautogui.keyUp(data[data.find('.') + 1:])
                else:
                    pyautogui.keyUp(data[data.find(':') + 3])
            else:
                pyautogui.moveTo(data)

    def set_connection_status(self, con):
        """Sets connection status with the handler

        ARGS:
            con(boolean) - True if connection exists, False if not
        """
        self.main_con = con

    def close_connection(self):
        """Closes connection with the handler"""
        self.main_con = False
        self.socket.close()
