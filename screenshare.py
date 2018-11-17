"""Main Class - Initiates Components"""
from PyQt5 import QtWidgets
from App.main_window import MainWindow
import sys
import threading


app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QMainWindow()


def initiat_main():
    MainWindow(window)


def main():
    main_thread = threading.Thread(target=initiat_main)
    main_thread.daemon = True
    main_thread.start()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()
