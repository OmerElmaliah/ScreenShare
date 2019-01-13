"""Main Class - Initiates Components"""
from PyQt5 import QtWidgets
from App.login_window import LoginWindow
import sys
import multiprocessing

LOGIN_CONDITION = False


def setup_login():
    global LOGIN_CONDITION
    """Initiates the login page"""
    app = QtWidgets.QApplication(sys.argv)
    login_window = LoginWindow()
    login_window.show()
    app.exec_()
    LOGIN_CONDITION = login_window.logged_in


def main():
    login_process = multiprocessing.Process(target=setup_login)
    login_process.start()
    login_process.join()

    # fix this
    if LOGIN_CONDITION:
        print(1)


if __name__ == '__main__':
    main()

"CURRENT BUGS:" \
    "- Keyboard not working properly if launched from an alternate language other than English" \
    "..."
