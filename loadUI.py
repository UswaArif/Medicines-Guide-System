from re import search
import sys
from tkinter import Widget
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow,QApplication,QTableWidgetItem,QStackedWidget,QMessageBox
import pandas as pd
from Search import Ui_MainWindow
import insertionSort

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        loadUi("Medicine Guide.UI", self)
        
        #print(RatingInt)
        #print(self.InsertionSort(MedicineName,OldpriceInt,NewPriceInt,Quantity,Starsfloat,RatingInt,Discount,Description))
        self.startButton.clicked.connect(self.load)
        self.sortButton.clicked.connect(self.InsertionSortImplement)
        self.advancedButton.clicked.connect(self.show_new_window)
        
    def read(self):
        df = pd.read_csv("newdata2.csv")
        MedicineName = df["MedicineName"].values.tolist() 
        Oldprice = df["Old price"].values.tolist() 
        NewPrice = df["NewPrice"].values.tolist() 
        Quantity = df["Quantity"].values.tolist() 
        Stars = df["Stars"].values.tolist() 
        Rating = df["Rating"].values.tolist() 
        Discount = df["Discount"].values.tolist() 
        Description = df["Description"].values.tolist()

        Starsfloat = []
        NewPriceInt = []
        OldpriceInt = []
        RatingInt = []
        for i in Stars:          
            Starsfloat.append(float(i))
        #print(Starsfloat)

        for i in NewPrice:
            NewPriceInt.append(int(i))
        #print(NewPriceInt)

        for i in Oldprice:
            OldpriceInt.append(int(i))
        #print(OldpriceInt)

        for i in Rating:
            RatingInt.append(int(i))

        return MedicineName,OldpriceInt,NewPriceInt,Quantity,Starsfloat,RatingInt,Discount,Description

    def show_new_window(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.window)
        self.window.show()

    def load(self):
        df = pd.read_csv("newdata2.csv")
        rows=df.shape[0]
        col=df.shape[1]
        self.tableWidget.setColumnCount(col)
        self.tableWidget.setRowCount(rows)
        a=df.values
        #print(a)
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