from PyQt5 import QtWidgets
from App.main_window_ui import MainWindowUi
from customer import Customer
from handler import Handler
import multiprocessing


class MainWindow(QtWidgets.QMainWindow, MainWindowUi):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.setup_ui(self)
        self.customer_button.clicked.connect(self.create_customer)

    def create_customer(self):
        customer = Customer('192.168.1.174', 8888)
        customer_process = multiprocessing.Process(target=customer.start_work)
        customer_process.daemon = True
        customer_process.start()

    def create_handler(self):
        handler = Handler('192.168.1.174', 8889)
        handler_process = multiprocessing.Process(target=handler.recv_img)
        handler_process.daemon = True
        handler_process.start()
