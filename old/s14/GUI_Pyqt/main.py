# -*- coding: utf-8 -*-

import sys

from PyQt5.QtWidgets import QApplication , QMainWindow

from NewTest import *

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(mainWindow)
    mainWindow.show()
    sys.exit(app.exec_())