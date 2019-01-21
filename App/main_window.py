from PyQt5 import QtCore, QtWidgets
from customer import Customer
from handler import Handler
import threading
import socket


IP = "192.168.1.174"
PORT = 8882


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.setup_ui(self)
        self.send_request_button.clicked.connect(self.send_request)
        self.listen_button.clicked.connect(self.listen_for_requests)
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.socket.bind((IP, PORT))

    def send_request(self):
        iden = self.id_customer_text.toPlainText()
        pass_iden = int(self.id_customer_pass_text.toPlainText())

        self.socket.sendto("Connect", (iden, pass_iden))
        ans = self.socket.recv(8192)
        if ans == "y":
            self.socket.sendto("Connecting", (iden, pass_iden))
            self.close()
            self.socket.close()
            handler = Handler(IP, PORT, iden, pass_iden)
            handler_thread = threading.Thread(target=handler.run)
            handler_thread.start()
            handler_thread.join()
        elif ans == 'n':
            self.access_denied()

    def listen_for_requests(self):
        print(1)
        ans_1 = self.socket.recv(1024) # check this
        print(1)
        iden = ans_1[:ans_1.find("PASS:")]
        pass_iden = ans_1[ans_1.find("PASS:") + 5:]
        ans_2 = self.get_text()
        self.socket.sendto(ans_2, (iden, pass_iden))

        ans_3 = self.socket.recv(1024)
        if ans_3 is "Connecting":
            self.close()
            self.socket.close()
            customer = Customer(IP, PORT, iden, pass_iden)
            customer_thread = threading.Thread(target=customer.run)
            customer_thread.start()
            customer_thread.join()

    def get_text(self):
        text, ok_pressed = QtWidgets.QInputDialog.getText(self, "Connection Request", "YES or NO:",
                                                          QtWidgets.QLineEdit.Normal, "")
        if ok_pressed and text != '':
            return text

    def failed_request(self):
        msg = QtWidgets.QMessageBox()
        msg.setIcon(QtWidgets.QMessageBox.Critical)
        msg.setText("Could not connect to client")
        msg.setWindowTitle("Error")
        msg.exec_()

    def access_denied(self):
        msg = QtWidgets.QMessageBox()
        msg.setIcon(QtWidgets.QMessageBox.Critical)
        msg.setText("Access was denied by the client")
        msg.setWindowTitle("test-1")
        msg.exec_()

    def setup_ui(self, main_window):
        main_window.setObjectName("main_window")
        main_window.resize(800, 600)

        self.central_widget = QtWidgets.QWidget(main_window)
        self.central_widget.setObjectName("central_widget")

        self.id_customer = QtWidgets.QTextBrowser(self.central_widget)
        self.id_customer.setGeometry(QtCore.QRect(130, 360, 141, 31))
        self.id_customer.setObjectName("id_customer")

        self.id_customer_pass = QtWidgets.QTextBrowser(self.central_widget)
        self.id_customer_pass.setGeometry(QtCore.QRect(130, 390, 141, 31))
        self.id_customer_pass.setObjectName("id_customer_pass")

        self.main_text = QtWidgets.QTextBrowser(self.central_widget)
        self.main_text.setGeometry(QtCore.QRect(160, 40, 471, 81))
        self.main_text.setObjectName("main_text")

        self.id_main = QtWidgets.QTextBrowser(self.central_widget)
        self.id_main.setGeometry(QtCore.QRect(130, 180, 141, 51))
        self.id_main.setObjectName("id_main")

        self.id_main_text = QtWidgets.QTextBrowser(self.central_widget)
        self.id_main_text.setGeometry(QtCore.QRect(270, 180, 381, 51))
        self.id_main_text.setObjectName("id_main_text")

        self.id_main_password = QtWidgets.QTextBrowser(self.central_widget)
        self.id_main_password.setGeometry(QtCore.QRect(270, 230, 381, 51))
        self.id_main_password.setObjectName("id_main_password")

        self.id_main_pass = QtWidgets.QTextBrowser(self.central_widget)
        self.id_main_pass.setGeometry(QtCore.QRect(130, 230, 141, 51))
        self.id_main_pass.setObjectName("id_main_pass")

        self.id_customer_text = QtWidgets.QTextEdit(self.central_widget)
        self.id_customer_text.setGeometry(QtCore.QRect(270, 360, 381, 31))
        self.id_customer_text.setObjectName("id_customer_text")

        self.id_customer_pass_text = QtWidgets.QTextEdit(self.central_widget)
        self.id_customer_pass_text.setGeometry(QtCore.QRect(270, 390, 381, 31))
        self.id_customer_pass_text.setObjectName("id_customer_pass_text")

        self.send_request_button = QtWidgets.QPushButton(self.central_widget)
        self.send_request_button.setGeometry(QtCore.QRect(160, 470, 181, 71))
        self.send_request_button.setObjectName("send_request_button")

        self.listen_button = QtWidgets.QPushButton(self.central_widget)
        self.listen_button.setGeometry(QtCore.QRect(450, 470, 181, 71))
        self.listen_button.setObjectName("listen_button")

        main_window.setCentralWidget(self.central_widget)

        self.retranslateUi(main_window)
        QtCore.QMetaObject.connectSlotsByName(main_window)

    def retranslateUi(self, main_window):
        _translate = QtCore.QCoreApplication.translate
        main_window.setWindowTitle(_translate("main_window", "MainWindow"))
        self.id_customer.setHtml(_translate("main_window",
                                            "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                            "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                            "p, li { white-space: pre-wrap; }\n"
                                            "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
                                            "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt; color:#118cff;\">Identification Code:</span></p></body></html>"))
        self.id_customer_pass.setHtml(_translate("main_window",
                                                 "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                                 "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                                 "p, li { white-space: pre-wrap; }\n"
                                                 "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
                                                 "<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt; color:#2b6bff;\">Password Identifier:</span></p></body></html>"))
        self.main_text.setHtml(_translate("main_window",
                                          "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                          "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                          "p, li { white-space: pre-wrap; }\n"
                                          "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
                                          "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:36pt; font-weight:600; color:#820002;\">ScreenShare BETA</span></p></body></html>"))
        self.id_main.setHtml(_translate("main_window",
                                        "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                        "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                        "p, li { white-space: pre-wrap; }\n"
                                        "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
                                        "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt; color:#118cff;\">Personal Identification Code:</span></p></body></html>"))
        self.id_main_pass.setHtml(_translate("main_window",
                                             "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                             "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                             "p, li { white-space: pre-wrap; }\n"
                                             "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
                                             "<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt; color:#2b6bff;\">Personal Password Identifier:</span></p></body></html>"))
        self.send_request_button.setText(_translate("main_window", "Send Request"))
        self.listen_button.setText(_translate("main_window", "Listen For Requests"))
