import socket
from pynput import mouse


SOCKET = None
IP = None
PORT = None


def setup(client_socket, ip, port):
    global SOCKET, IP, PORT
    SOCKET = client_socket
    IP = ip
    PORT = port


def on_click(x, y, button, pressed):
    if button == mouse.Button.left and pressed:
        SOCKET.sendto("left pressed".encode('utf-8'), (IP, PORT))
    elif button == mouse.Button.left:
        SOCKET.sendto("left released".encode('utf-8'), (IP, PORT))
    elif button == mouse.Button.right and pressed:
        SOCKET.sendto("right pressed".encode('utf-8'), (IP, PORT))
    else:
        SOCKET.sendto("right released".encode('utf-8'), (IP, PORT))


def on_move(x, y):
    SOCKET.sendto(("cords: X" + str(x) + " Y" + str(y)).encode('utf-8'), (IP, PORT))


def on_scroll():
    pass
