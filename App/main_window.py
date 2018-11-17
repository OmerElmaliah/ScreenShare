from PyQt5 import QtCore, QtWidgets
from customer import Customer
from handler import Handler
import threading


class MainWindow(object):
    def __init__(self, window):
        self.window = window
        self.window.setObjectName("main_window")
        self.window.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(self.window)
        self.centralwidget.setObjectName("centralwidget")

        self.handler_button = QtWidgets.QPushButton(self.centralwidget)
        self.handler_button.setGeometry(QtCore.QRect(120, 210, 201, 101))
        self.handler_button.setObjectName("handler_button")
        self.handler_button.clicked.connect(self.create_handler)

        self.customer_button = QtWidgets.QPushButton(self.centralwidget)
        self.customer_button.setGeometry(QtCore.QRect(480, 210, 221, 101))
        self.customer_button.setObjectName("customer_button")
        self.customer_button.clicked.connect(self.create_customer)

        self.window.setCentralWidget(self.centralwidget)

        self.menubar = QtWidgets.QMenuBar(self.window)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        self.window.setMenuBar(self.menubar)

        self.statusbar = QtWidgets.QStatusBar(self.window)
        self.statusbar.setObjectName("statusbar")
        self.window.setStatusBar(self.statusbar)

        self.retranslate_ui()
        QtCore.QMetaObject.connectSlotsByName(self.window)

    def retranslate_ui(self):
        _translate = QtCore.QCoreApplication.translate
        self.window.setWindowTitle(_translate("main_window", "Main Window"))
        self.handler_button.setText(_translate("main_window", "Handle"))
        self.customer_button.setText(_translate("main_window", "Customer"))

    def create_customer(self):
        customer = Customer('10.0.0.1', 8888)
        customer_thread = threading.Thread(target=customer.start_work)
        customer_thread.daemon = True
        customer_thread.start()

    def create_handler(self):
        handler = Handler('10.0.0.1', 8888, self.window)
        handler_thread = threading.Thread(target=handler.start_work)
        handler_thread.daemon = True
        handler_thread.start()
