"""Main Class - Initiates Components"""
from PyQt5 import QtWidgets
from App.main_window import MainWindow
from App.login_window import LoginWindow
import sys
import multiprocessing
import threading


LOGIN_CONDITION = False


def setup_login():
    """Initiates the login page"""
    global LOGIN_CONDITION
    app = QtWidgets.QApplication(sys.argv)
    login_window = LoginWindow()
    login_window.show()
    app.exec_()
    LOGIN_CONDITION = login_window.logged_in


def setup_main():
    """Initiates the app"""
    app = QtWidgets.QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    app.exec_()


def main():
    login_thread = threading.Thread(target=setup_login)
    login_thread.start()
    login_thread.join()

    if LOGIN_CONDITION:
        main_process = multiprocessing.Process(target=setup_main)
        main_process.start()
        main_process.join()


if __name__ == '__main__':
    main()

"CURRENT BUGS:" \
    "- Keyboard not working properly if launched from an alternate language other than English" \
    "..."
