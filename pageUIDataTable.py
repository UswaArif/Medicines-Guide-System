from re import I
from PyQt5 import QtWidgets, uic
from PyQt5 import *
from PyQt5.QtWidgets import QDialog, QApplication
import pandas as pd

app = QtWidgets.QApplication([])
dlg = uic.loadUi("D:\MidTerm\cs261f22pid36\Medicine Guide.UI")

df = pd.read_csv("D:\MidTerm\cs261f22pid36\newdata.csv")
MedicineName = df["MedicineName"].values.tolist() 
Oldprice = df["Old price"].values.tolist() 
NewPrice = df["NewPrice"].values.tolist() 
Quantity = df["Quantity"].values.tolist() 
Stars = df["Stars"].values.tolist() 
Rating = df["Rating"].values.tolist() 
Discount = df["Discount"].values.tolist() 
Description = df["Description"].values.tolist() 

def InserionSort(array, start, end):
    for i in range(start,end):
        j = i 
        while(array[j] < array[j - 1] and j  > 0):
            array[j], array[j - 1] = array[j - 1],array[j]
            j = j - 1
    return array

def dataMedicineName(data):
    MedicineNameRow = 0
    dlg.tableWidget.setRowCount(len(data))
    for names in MedicineName:
        dlg.tableWidget.setItem(MedicineNameRow, 0, QtWidgets.QTableWidgetItem(names))
        MedicineNameRow = MedicineNameRow  + 1
    
def dataOldprice(p2):
    OldpriceRow = 0
    for oldPrice in Oldprice:
        dlg.tableWidget.setItem(OldpriceRow, 0, QtWidgets.QTableWidgetItem(oldPrice))
        OldpriceRow = OldpriceRow  + 1
    
def dataNewPrice(p3):
    NewPriceRow = 0
    for newPrice in NewPrice:
        dlg.tableWidget.setItem(NewPriceRow, 0, QtWidgets.QTableWidgetItem(newPrice))
        NewPriceRow = NewPriceRow  + 1

def dataQuantity(p4):
    QuantityRow = 0
    for Quantity in QuantityRow:
        dlg.tableWidget.setItem(QuantityRow, 0, QtWidgets.QTableWidgetItem(Quantity))
        QuantityRow = QuantityRow  + 1

def dataStars(p5):
    StarsRow = 0
    for Stars in StarsRow:
        dlg.tableWidget.setItem(StarsRow, 0, QtWidgets.QTableWidgetItem(Stars))
        StarsRow = StarsRow  + 1

def dataRating(p6):
    RatingRow = 0
    for Rating in RatingRow:
        dlg.tableWidget.setItem(RatingRow, 0, QtWidgets.QTableWidgetItem(Rating))
        RatingRow = RatingRow  + 1

def dataDiscount(p7):
    DiscountRow = 0
    for Discount in DiscountRow:
        dlg.tableWidget.setItem(DiscountRow, 0, QtWidgets.QTableWidgetItem(Discount))
        DiscountRow = DiscountRow  + 1

def dataDescription(p8):
    DescriptionRow = 0
    for Description in DescriptionRow:
        dlg.tableWidget.setItem(DescriptionRow, 0, QtWidgets.QTableWidgetItem(Description))
        DescriptionRow = DescriptionRow  + 1

dataMedicineName(MedicineName)
dataOldprice(Oldprice)
dataNewPrice(NewPrice)
dataQuantity(Quantity)
dataStars(Stars)
dataRating(Rating)
dataDiscount(Discount)
dataDescription(Description)
dlg.Sort_pushButton.clicked.connect(applySorting)
dlg.show()
app.exec()