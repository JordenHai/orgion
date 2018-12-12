# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'NewTest.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import socket
import sys
from PyQt5.QtWidgets import QApplication , QMainWindow

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(220, 140, 201, 141))
        self.pushButton.setIconSize(QtCore.QSize(16, 16))
        self.pushButton.setAutoRepeatInterval(97)
        self.pushButton.setAutoDefault(False)
        self.pushButton.setObjectName("pushButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 23))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuEdit = QtWidgets.QMenu(self.menubar)
        self.menuEdit.setObjectName("menuEdit")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionclose = QtWidgets.QAction(MainWindow)
        self.actionclose.setObjectName("actionclose")
        self.actionIP_CONFIG = QtWidgets.QAction(MainWindow)
        self.actionIP_CONFIG.setObjectName("actionIP_CONFIG")
        self.actionIP_ROUTER = QtWidgets.QAction(MainWindow)
        self.actionIP_ROUTER.setObjectName("actionIP_ROUTER")
        self.menuFile.addAction(self.actionclose)
        self.menuEdit.addAction(self.actionIP_CONFIG)
        self.menuEdit.addAction(self.actionIP_ROUTER)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())

        self.retranslateUi(MainWindow)
        self.pushButton.clicked.connect(self.NewTest_button_click)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "点我弹窗"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuEdit.setTitle(_translate("MainWindow", "Edit"))
        self.actionclose.setText(_translate("MainWindow", "close"))
        self.actionIP_CONFIG.setText(_translate("MainWindow", "IP CONFIG"))
        self.actionIP_ROUTER.setText(_translate("MainWindow", "IP ROUTER"))

    def NewTest_button_click(self):
        QtWidgets.QMessageBox.information(self.pushButton, "标题", "这是第一个PyQt5 GUI程序")

class Gui_socket(object):
    def __init__(self,server_host,server_port):
        self.host = server_host
        self.port = server_port
        self.sever = None
        self.conn = None
        self.addr = None
    def runc(self):
        self.sever = socket.socket()
        self.sever.bind(self.host,self.port)
        self.sever.listen(5)
        self.conn,self.addr = self.sever.accept()
    def sent_message(self,data):
        if isinstance(data,(bytes,)):
            self.conn.send(data)
        else:
            self.conn.send(data.encode())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(mainWindow)
    mainWindow.show()
    sys.exit(app.exec_())