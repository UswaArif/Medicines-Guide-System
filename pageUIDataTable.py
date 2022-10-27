from os import remove
from re import I
from PyQt5 import QtWidgets, uic
from PyQt5 import *
from PyQt5.QtWidgets import QDialog, QApplication
from PyQt5.QtWidgets import QMainWindow,QApplication,QTableWidgetItem,QStackedWidget
from PyQt5 import QtCore, QtGui, QtWidgets
import pandas as pd

app = QtWidgets.QApplication([])
dlg = uic.loadUi("D:\MidTerm\cs261f22pid36\Medicine Guide 2.UI")

df = pd.read_csv("newdata.csv")
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
    print(Starsfloat)

    for i in NewPrice:
        NewPriceInt.append(int(i))
    print(NewPriceInt)

    for i in Oldprice:
        OldpriceInt.append(i)
    print(OldpriceInt)

    for i in Rating:
        RatingInt.append(int(i))
    print(RatingInt)
    #stars_modified = []
    #for i in Stars:
    #    stars_modified.append(int(i))
    def InsertionSort(array):
        for i in range(0, len(array)):
            j = i 
            while(array[j] < array[j - 1] and j  > 0):
                array[j], array[j - 1] = array[j - 1],array[j]
                j = j - 1
        return array

    def dataMedicineName(data):
        MedicineNameRow = 0
        dlg.tableWidget.setRowCount(len(data))
        for names in data:
            dlg.tableWidget.setItem(MedicineNameRow, 0, QtWidgets.QTableWidgetItem(names))
            MedicineNameRow = MedicineNameRow  + 1

    def dataOldprice(p2):
        OldpriceRow = 0
        for oldPrice in p2:
            dlg.tableWidget.setItem(OldpriceRow, 1, QtWidgets.QTableWidgetItem(str(oldPrice)))
            OldpriceRow = OldpriceRow  + 1
        
    def dataNewPrice(p3):
        NewPriceRow = 0
        for newPrice in p3:
            dlg.tableWidget.setItem(NewPriceRow, 2, QtWidgets.QTableWidgetItem(str(newPrice)))
            NewPriceRow = NewPriceRow  + 1

    def dataQuantity(p4):
        QuantityRow = 0
        for Quantity in p4:
            dlg.tableWidget.setItem(QuantityRow, 3, QtWidgets.QTableWidgetItem(Quantity))
            QuantityRow = QuantityRow  + 1

    def dataStars(p5):
        StarsRow = 0
        for Stars in p5:
            dlg.tableWidget.setItem(StarsRow, 4, QtWidgets.QTableWidgetItem(str(Stars)))
            StarsRow = StarsRow  + 1

    def dataRating(p6):
        RatingRow = 0
        for Rating in p6:
            dlg.tableWidget.setItem(RatingRow, 5, QtWidgets.QTableWidgetItem(str(Rating)))
            RatingRow = RatingRow  + 1

    def dataDiscount(p7):
        DiscountRow = 0
        for Discount in p7:
            dlg.tableWidget.setItem(DiscountRow, 6, QtWidgets.QTableWidgetItem(Discount))
            DiscountRow = DiscountRow  + 1

    def dataDescription(p8):
        DescriptionRow = 0
        for Description in p8:
            dlg.tableWidget.setItem(DescriptionRow, 7, QtWidgets.QTableWidgetItem(Description))
            DescriptionRow = DescriptionRow  + 1

    def InsertionSortingList(MedicineName):
        insertionList = InsertionSort(MedicineName)
        print(insertionList)
        MedicineNameRow = 0
        dlg.tableWidget.setRowCount(len(insertionList))
        for names in insertionList:
            dlg.tableWidget.setItem(MedicineNameRow, 0, QtWidgets.QTableWidgetItem(names))
            MedicineNameRow = MedicineNameRow  + 1

    
dataMedicineName(MedicineName)
dataOldprice(Oldprice)
dataNewPrice(NewPrice)
dataQuantity(Quantity)
dataStars(Stars)
dataRating(Rating)
dataDiscount(Discount)
dataDescription(Description)
insertionList = InsertionSort(Oldprice)
dlg.sortButton.clicked.connect((insertionList))

dlg.show()
app.exec()