from PyQt5 import QtCore, QtWidgets
from App.signup_window import SignUpWindow
from DB.userbase import UserBase


class LoginWindow(QtWidgets.QMainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.setup_ui(self)
        self.login_button.clicked.connect(self.login)
        self.signup_button.clicked.connect(self.signup)
        self.logged_in = False

    def login(self):
        id_text = self.username_check.toPlainText()
        pass_text = self.password_check.text()

        db = UserBase()
        if db.verification(id_text, pass_text):
            self.logged_in = True
            db.close()
            self.close()
        else:
            db.close()
            self.failed_login()

    def signup(self):
        self.su = SignUpWindow()
        self.su.show()

    def failed_login(self):
        msg = QtWidgets.QMessageBox()
        msg.setIcon(QtWidgets.QMessageBox.Critical)
        msg.setText("Username or password are incorrect!")
        msg.setWindowTitle("Error")
        msg.exec_()

    def setup_ui(self, main_window):
        main_window.setObjectName("main_window")
        main_window.resize(800, 600)
        self.central_widget = QtWidgets.QWidget(main_window)
        self.central_widget.setObjectName("central_widget")

        self.main_text = QtWidgets.QTextBrowser(self.central_widget)
        self.main_text.setGeometry(QtCore.QRect(170, 70, 471, 101))
        self.main_text.setObjectName("main_text")

        self.username_check = QtWidgets.QPlainTextEdit(self.central_widget)
        self.username_check.setGeometry(QtCore.QRect(310, 240, 181, 31))
        self.username_check.setObjectName("username_check")

        self.username_text = QtWidgets.QTextBrowser(self.central_widget)
        self.username_text.setGeometry(QtCore.QRect(360, 200, 81, 31))
        self.username_text.setObjectName("username_text")

        self.password_check = QtWidgets.QLineEdit(self.central_widget)
        self.password_check.setGeometry(QtCore.QRect(310, 320, 181, 31))
        self.password_check.setObjectName("password_check")
        self.password_check.setEchoMode(QtWidgets.QLineEdit.Password)

        self.password_text = QtWidgets.QTextBrowser(self.central_widget)
        self.password_text.setGeometry(QtCore.QRect(360, 280, 81, 31))
        self.password_text.setObjectName("password_text")

        self.login_button = QtWidgets.QPushButton(self.central_widget)
        self.login_button.setGeometry(QtCore.QRect(260, 430, 81, 31))
        self.login_button.setObjectName("login_button")

        self.signup_button = QtWidgets.QPushButton(self.central_widget)
        self.signup_button.setGeometry(QtCore.QRect(450, 430, 81, 31))
        self.signup_button.setObjectName("signup_button")

        main_window.setCentralWidget(self.central_widget)
        self.statusbar = QtWidgets.QStatusBar(main_window)
        self.statusbar.setObjectName("statusbar")
        main_window.setStatusBar(self.statusbar)

        self.retranslateUi(main_window)
        QtCore.QMetaObject.connectSlotsByName(main_window)

    def retranslateUi(self, main_window):
        _translate = QtCore.QCoreApplication.translate
        main_window.setWindowTitle(_translate("main_window", "MainWindow"))
        self.main_text.setHtml(_translate("main_window",
                                          "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                          "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                          "p, li { white-space: pre-wrap; }\n"
                                          "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
                                          "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:36pt; font-weight:600; color:#900013;\"> ScreenShare BETA</span></p>\n"
                                          "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt; font-weight:600; color:#900013;\">Please enter username and password</span></p></body></html>"))
        self.username_text.setHtml(_translate("main_window",
                                              "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                              "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                              "p, li { white-space: pre-wrap; }\n"
                                              "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
                                              "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; text-decoration: underline;\">Username</span></p></body></html>"))
        self.password_text.setHtml(_translate("main_window",
                                              "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                              "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                              "p, li { white-space: pre-wrap; }\n"
                                              "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
                                              "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; text-decoration: underline;\">Password</span></p></body></html>"))
        self.login_button.setText(_translate("main_window", "Login"))
        self.signup_button.setText(_translate("main_window", "Signup"))
