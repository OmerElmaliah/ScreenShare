from PyQt5 import QtCore, QtWidgets


class MainWindowUi(object):
    def setup_ui(self, window):
        window.setObjectName("MainWindow")
        window.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(window)
        self.centralwidget.setObjectName("centralwidget")

        self.handle_button = QtWidgets.QPushButton(self.centralwidget)
        self.handle_button.setGeometry(QtCore.QRect(150, 210, 201, 91))
        self.handle_button.setObjectName("handle_button")

        self.customer_button = QtWidgets.QPushButton(self.centralwidget)
        self.customer_button.setGeometry(QtCore.QRect(460, 210, 201, 91))
        self.customer_button.setObjectName("customer_button")

        window.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(window)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        window.setMenuBar(self.menubar)

        self.statusbar = QtWidgets.QStatusBar(window)
        self.statusbar.setObjectName("statusbar")
        window.setStatusBar(self.statusbar)

        self.retranslateUi(window)
        QtCore.QMetaObject.connectSlotsByName(window)

    def retranslateUi(self, window):
        _translate = QtCore.QCoreApplication.translate
        window.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.handle_button.setText(_translate("MainWindow", "Handle"))
        self.customer_button.setText(_translate("MainWindow", "Customer"))
