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

    def create_customer(self):
        customer = Customer('10.0.0.1', 8886, '10.0.0.1', 8887)
        customer_thread = threading.Thread(target=customer.start_work)
        customer_thread.daemon = True
        customer_thread.start()

    def create_handler(self):
        handler = Handler('10.0.0.1', 8886, '10.0.0.1', 8887)
        handler_thread = threading.Thread(target=handler.recv_img)
        handler_thread.daemon = True
        handler_thread.start()
        self.close()
