"""Main Class - Initiates Components"""
from PyQt5 import QtWidgets
from app.main_window import MainWindow
import sys


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = QtWidgets.QMainWindow()
    MainWindow(window)
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
