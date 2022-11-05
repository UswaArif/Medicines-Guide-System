from re import search
import sys
from tkinter import Widget
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5 import QtWidgets,uic,QtCore
from PyQt5 import *
from PyQt5.QtWidgets import QMainWindow,QApplication,QTableWidgetItem,QStackedWidget,QMessageBox,QDialog,QSizePolicy,QPushButton,QComboBox
import pandas as pd
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5 import QtWidgets,uic,QtCore
from PyQt5 import *
from PyQt5.QtWidgets import QMainWindow,QApplication,QTableWidgetItem,QStackedWidget,QMessageBox,QDialog,QSizePolicy,QPushButton,QComboBox
import pandas as pd
from AdvancedSearch import Ui_MainWindow
import search
from loadUI import read


class AdvancedWindow(QMainWindow):
    def __init__(self):
        super(AdvancedWindow, self).__init__()
        loadUi("AdvancedSearch.UI", self)
        self.columnComboBox.activated.connect(self.ChangeLabelText)
        #self.columnComboBox.activated.connect(self.ConnectComboBox)
        self.okButton.clicked.connect(lambda: self.ControlSearching(self.columnComboBox.currentText(),self.typecomboBox.currentText(),self.FilterComboBox.currentText(),self.showLabel.text()))
        self.show()
        self.exec()


    MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description = read()
   
    def ChangeLabelText(self):
        if(self.columnComboBox.currentText()=="Name"):
            self.showLabel.setText("Name")
        elif(self.columnComboBox.currentText()=="Old Price"):
            self.showLabel.setText("Old Price")
        elif(self.columnComboBox.currentText()=="New Price"):
            self.showlabel.setText("New Price")
        elif(self.columnComboBox.currentText()=="Quantity"):
            self.showLabel.setText("Quantity")
        elif(self.columnComboBox.currentText()=="Stars"):
            self.showLabel.setText("Stars")
        elif(self.columnComboBox.currentText()=="Orders"):
            self.showLabel.setText("Orders")  #ConnectComboBox()
        elif(self.columnComboBox.currentText()=="Discount"):
            self.showLabel.setText("Discount")
        elif(self.columnComboBox.currentText()=="Description"):
            self.showLabel.setText("Description")

    
    def ControlSearching(SearchThrough,typecomboBox,FilterComboBox,showLabel,self):
        print(SearchThrough)
        res=[]
        MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description=self.read()
        if(SearchThrough == "Name"):
            res = search.SearchingFunction_call(MedicineName,typecomboBox,FilterComboBox,showLabel)
        elif(SearchThrough=="Old Price"):
            res = search.SearchingFunction_call(OldpriceInt,typecomboBox,FilterComboBox,showLabel)
        elif(SearchThrough == "New Price"):
            res = search.SearchingFunction_call(NewPriceInt,typecomboBox,FilterComboBox,showLabel)
        elif(SearchThrough=="Quantity"):
            res = search.SearchingFunction_call(Quantity,typecomboBox,FilterComboBox,showLabel)
        elif(SearchThrough=="Stars"):
            res=search.SearchingFunction_call(Stars,typecomboBox,FilterComboBox,showLabel)
        elif(SearchThrough=="Orders"):
            res=search.SearchingFunction_call(RatingInt,typecomboBox,FilterComboBox,showLabel)
        elif(SearchThrough=="Discount"):
            res=search.SearchingFunction_call(Discount,typecomboBox,FilterComboBox,showLabel)
        elif(SearchThrough=="Description"):
            res=search.SearchingFunction_call(Description,typecomboBox,FilterComboBox,showLabel)
        self.LoadDataIntoTable(res)
    

    def LoadDataIntoTable(DataList,self):
        print(DataList)
        MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description = self.read()
        RowCount=0
        self.tableWidget.setRowCount(len(DataList))
        for data in DataList :
            self.tableWidget.setItem(RowCount,0,QtWidgets.QTableWidgetItem(data))
            RowCount = RowCount + 1


app = QApplication(sys.argv)
mainwindow = AdvancedWindow()
widget = QtWidgets.QStackedWidget()
widget.addWidget(mainwindow)
widget.setFixedHeight(600)
widget.setFixedWidth(800)
widget.show()

try:
    sys.exit(app.exec_())
except:
    print("Exiting")