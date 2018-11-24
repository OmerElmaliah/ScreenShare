from PyQt5 import QtWidgets
from App.main_window_ui import MainWindowUi
from customer import Customer
from handler import Handler
import threading
import multiprocessing


class MainWindow(QtWidgets.QMainWindow, MainWindowUi):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.setup_ui(self)
        self.customer_button.clicked.connect(self.create_customer)
        self.handle_button.clicked.connect(self.create_handler)

    """Creates a variable type Customer and starts working"""
    def create_customer(self):
        customer = Customer('10.0.0.1', 8886, '10.0.0.4', 8887)
        customer_process = multiprocessing.Process(target=customer.start_work)
        customer_process.daemon = True
        customer_process.start()

    """Creates a variable type Handler and starts working"""
    def create_handler(self):
        handler = Handler('10.0.0.1', 8886, '10.0.0.4', 8887)
        handler_thread = threading.Thread(target=handler.recv_img)
        handler_thread.daemon = True
        handler_thread.start()
        self.close()
