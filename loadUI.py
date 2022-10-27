from re import search
import sys
from tkinter import Widget
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow,QApplication,QTableWidgetItem,QStackedWidget
import pandas as pd

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        loadUi("MedicineGuide.UI", self)
        self.stopButton.clicked.connect(self.load)
        
    def load(self):
        df = pd.read_csv("newdata2.csv")
        rows=df.shape[0]
        col=df.shape[1]
        self.tableWidget.setColumnCount(col)
        self.tableWidget.setRowCount(rows)
        a=df.values
        for i in range(rows):
            for j in range(col):
                self.tableWidget.setItem(i,j,QTableWidgetItem(str(a[i][j])))
        self.tableWidget.resizeColumnsToContents()
        self.tableWidget.resizeRowsToContents()


app = QApplication(sys.argv)
mainwindow = MainWindow()
widget = QtWidgets.QStackedWidget()
widget.addWidget(mainwindow)
widget.setFixedHeight(600)
widget.setFixedWidth(800)
widget.show()
try:
    sys.exit(app.exec_())
except:
    print("Exiting")