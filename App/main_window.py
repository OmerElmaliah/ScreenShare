from PyQt5 import QtWidgets
from App.main_window_ui import MainWindowUi
from customer import Customer
from handler import Handler
import threading


class MainWindow(QtWidgets.QMainWindow, MainWindowUi):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.setup_ui(self)
        self.customer_button.clicked.connect(self.create_customer)
        self.handle_button.clicked.connect(self.create_handler)

    """Creates a variable type Customer and starts working"""
    def create_customer(self):
        customer = Customer('192.168.1.157', 8882, '192.168.1.174', 8883)
        customer_thread = threading.Thread(target=customer.run)
        customer_thread.daemon = True
        customer_thread.start()

    """Creates a variable type Handler and starts working"""
    def create_handler(self):
        handler = Handler('192.168.1.157', 8882, '192.168.1.174', 8883)
        handler_thread = threading.Thread(target=handler.run)
        handler_thread.daemon = True
        handler_thread.start()
        self.close()
