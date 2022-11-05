import sys
from tkinter import Widget
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5 import QtWidgets,uic,QtCore
from PyQt5 import *
from PyQt5.QtWidgets import QMainWindow,QApplication,QTableWidgetItem,QStackedWidget,QMessageBox,QDialog,QSizePolicy,QPushButton,QComboBox
import pandas as pd
from loadUI import MainWindow

class PageMainWindow(QMainWindow):
    def __init__(self):
        super(PageMainWindow, self).__init__()
        loadUi("FirstPage.UI", self)
        self.pushButton.clicked.connect(self.show_new_window)

    def show_new_window(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = MainWindow()
        self.ui.setupUi(self.window)
        self.window.show()

app = QApplication(sys.argv)
mainwindow = PageMainWindow()
widget = QtWidgets.QStackedWidget()
widget.addWidget(mainwindow)
widget.setFixedHeight(600)
widget.setFixedWidth(800)
widget.show()

try:
    sys.exit(app.exec_())
except:
    print("Exiting")