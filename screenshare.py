"""Main Class - Initiates Components"""
from PyQt5 import QtWidgets
from App.main_window import MainWindow
import sys
import multiprocessing


def setup_main():
    app = QtWidgets.QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    app.exec_()


def main():
    main_thread = multiprocessing.Process(target=setup_main)
    main_thread.start()
    main_thread.join()


if __name__ == '__main__':
    main()
