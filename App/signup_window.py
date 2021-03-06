from PyQt5 import QtCore, QtWidgets
from DB.userbase import UserBase


class SignUpWindow(QtWidgets.QMainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.setup_ui(self)
        self.signup_button.clicked.connect(self.sign_up)

    def sign_up(self):
        """Receives input(Username and password) and verifies if the given input already exists in the database,
        if not adds the input to the database for future sign ins"""
        try:
            user = self.username_edit.toPlainText()
            psw = self.password_edit.text()

            user_create = "User created, You may now login"
            user_taken = "Username already taken!"
            inv_input = "Please enter valid input"
            server_connection = "Could not connect to server"

            if user and psw:
                db = UserBase()
                if db.create_account(user, psw):
                    self.dialog_window(user_create, "User", "suc")
                    db.close()
                    self.close()
                else:
                    self.dialog_window(user_taken, "User", "er")
            else:
                self.dialog_window(inv_input, "Invalid Input", "er")
        except:
            self.dialog_window(server_connection, "Connection Issue", "er")

    def dialog_window(self, text, title, msg_type):
        """Opens up a dialog window for various uses

                ARGS:
                    text(string) - The text displayed in the dialog window
                    title(string) - The text of the title of the dialog window
                    msg_type(string) - Indicates which type of dialog will it be
                """
        msg = QtWidgets.QMessageBox()
        msg.setText(text)
        if msg_type == "er":
            msg.setWindowTitle(title)
            msg.setIcon(QtWidgets.QMessageBox.Critical)
        elif msg_type == "suc":
            msg.setWindowTitle("Success")
        msg.exec_()

    def setup_ui(self, signup_screen):
        """Designs the main window's properties"""
        signup_screen.setObjectName("signup_screen")
        signup_screen.resize(400, 300)
        self.username_text = QtWidgets.QTextBrowser(signup_screen)
        self.username_text.setGeometry(QtCore.QRect(60, 140, 121, 31))
        self.username_text.setObjectName("username_text")

        self.password_text = QtWidgets.QTextBrowser(signup_screen)
        self.password_text.setGeometry(QtCore.QRect(60, 170, 121, 31))
        self.password_text.setObjectName("password_text")

        self.username_edit = QtWidgets.QTextEdit(signup_screen)
        self.username_edit.setGeometry(QtCore.QRect(180, 140, 161, 31))
        self.username_edit.setObjectName("username_edit")

        self.password_edit = QtWidgets.QLineEdit(signup_screen)
        self.password_edit.setGeometry(QtCore.QRect(180, 170, 161, 31))
        self.password_edit.setObjectName("password_edit")
        self.password_edit.setEchoMode(QtWidgets.QLineEdit.Password)

        self.signup_button = QtWidgets.QPushButton(signup_screen)
        self.signup_button.setGeometry(QtCore.QRect(150, 230, 101, 31))
        self.signup_button.setObjectName("signup_button")

        self.main_text = QtWidgets.QTextBrowser(signup_screen)
        self.main_text.setGeometry(QtCore.QRect(60, 40, 281, 41))
        self.main_text.setObjectName("main_text")

        self.retranslateUi(signup_screen)
        QtCore.QMetaObject.connectSlotsByName(signup_screen)

    def retranslateUi(self, signup_screen):
        """Designs the main window's texts"""
        _translate = QtCore.QCoreApplication.translate
        signup_screen.setWindowTitle(_translate("signup_screen", "Signup"))
        self.username_text.setHtml(_translate("signup_screen", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600;\">Username:</span></p></body></html>"))
        self.password_text.setHtml(_translate("signup_screen", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600;\">Password:</span></p></body></html>"))
        self.signup_button.setText(_translate("signup_screen", "Signup"))
        self.main_text.setHtml(_translate("signup_screen", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt; font-weight:600; color:#a10000;\">ScreenShare - Signup</span></p></body></html>"))
