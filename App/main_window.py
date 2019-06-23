from PyQt5 import QtWidgets, QtCore
from customer import Customer
from handler import Handler
import threading
import socket
from DB.idbase import IdBase


class MainWindow(QtWidgets.QMainWindow):
    ip = '192.168.1.174'
    port = 8883
    new_port = 8885

    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.setup_ui(self)
        self.init_db_instance()
        self.send_request_button.clicked.connect(self.send_request)
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.socket.bind((self.ip, self.port))
        self.con = True

        listen_thread = threading.Thread(target=self.listen_for_requests)
        listen_thread.daemon = True
        listen_thread.start()

    def listen_for_requests(self):
        """Creates a variable type Customer and starts working"""
        while self.con:
            try:
                iden = self.socket.recv(2048).decode('utf-8')

                customer = Customer(self.ip, self.new_port, iden, self.new_port, self.id_main_password.toPlainText())
                customer_thread = threading.Thread(target=customer.run)
                customer_thread.daemon = True
                customer_thread.start()
                customer_thread.join()
                self.con = False
            except:
                pass

    def send_request(self):
        """Creates a variable type Handler and starts working"""
        invalid_input = "Invalid Input Given"
        server_connection = "Could Not Connect To Client"
        no_user = "Could Not Find User"

        try:
            iden = self.id_customer_text.toPlainText()
            pass_iden = self.id_customer_pass_text.toPlainText()

            db = IdBase()
            con, cust = db.get_id(iden, pass_iden)
            if con:
                try:
                    self.socket.sendto(self.ip.encode('utf-8'), (cust, self.port))

                    handler = Handler(self.ip, self.new_port, cust, self.new_port, pass_iden)
                    handler_thread = threading.Thread(target=handler.run)
                    handler_thread.daemon = True
                    handler_thread.start()
                    self.close()
                except:
                    self.dialog_window(server_connection, "Connection Failed")
            else:
                self.dialog_window(no_user, "Invalid User")
        except:
            self.dialog_window(invalid_input, "Invalid Input")

    def dialog_window(self, text, title):
        msg = QtWidgets.QMessageBox()
        msg.setIcon(QtWidgets.QMessageBox.Critical)
        msg.setText(text)
        msg.setWindowTitle(title)
        msg.exec_()

    def init_db_instance(self):
        db = IdBase()
        idu, idp = db.create_new_instance(self.ip)
        self.id_main_text.setPlainText(idu)
        self.id_main_password.setPlainText(idp)
        db.close()

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
        self.send_request_button.setGeometry(QtCore.QRect(310, 470, 181, 71))
        self.send_request_button.setObjectName("send_request_button")

        main_window.setCentralWidget(self.central_widget)

        self.retranslateUi(main_window)
        QtCore.QMetaObject.connectSlotsByName(main_window)

    def retranslateUi(self, main_window):
        _translate = QtCore.QCoreApplication.translate
        main_window.setWindowTitle(_translate("main_window", "ScreenShare"))
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
