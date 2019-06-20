"""Main Class - Initiates Components"""
from PyQt5 import QtWidgets
from App.login_window import LoginWindow
import sys


def main():
    app = QtWidgets.QApplication(sys.argv)
    login_window = LoginWindow()
    login_window.show()
    app.exec_()


if __name__ == '__main__':
    main()
