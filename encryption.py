import ssl
import socket


socket_init = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket = ssl.wrap_socket(socket_init, ssl_version=ssl.PROTOCOL_TLSv1, ciphers="ADH-AES256-SHA")
socket.bind(('127.0.0.1', 8888))