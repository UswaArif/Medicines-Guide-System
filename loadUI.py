from re import search
import sys
from tkinter import Widget
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow,QApplication,QTableWidgetItem,QStackedWidget,QMessageBox
import pandas as pd
from Search import Ui_MainWindow
import insertionSort
import bubbleSort
import selectionSort

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

        NewPriceInt = []
        OldpriceInt = []
        RatingInt = []
        
        for i in NewPrice:
            NewPriceInt.append(int(i))
        #print(NewPriceInt)

        for i in Oldprice:
            OldpriceInt.append(int(i))
        #print(OldpriceInt)

        for i in Rating:
            RatingInt.append(int(i))

        return MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description

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

    def InsertionSortImplement(self):
        
        MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description=self.read()
        #QMessageBox.about(self,'error1','Order')

        column = self.ColumncomboBox.currentText()
        Order = self.AscendCombobox.currentText()
        sort = self.sortCombobox.currentText()
        #print(insertionSort.InsertionSort(MedicineName,OldpriceInt,NewPriceInt,Quantity,Starsfloat,RatingInt,Discount,Description))
        QMessageBox.about(self,'error1', column)

        #Insertion Sort Ascending
        if column == 'Name' and Order == 'Ascending' and sort == 'Insertion':
            MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description = insertionSort.InsertionSort(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description)

        elif column == 'Old Prices' and Order == 'Ascending' and sort == 'Insertion':
            MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description = insertionSort.InsertionSortOldprice(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description)

        elif column == 'New Prices' and Order == 'Ascending' and sort == 'Insertion':
            MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description = insertionSort.InsertionSortNewPrice(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description)

        elif column == 'Quantity' and Order == 'Ascending' and sort == 'Insertion':
            MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description = insertionSort.InsertionSortQuantity(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description)

        elif column == 'Stars' and Order == 'Ascending' and sort == 'Insertion':
            MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description = insertionSort.InsertionSortStars(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description)
        
        elif column == 'Orders' and Order == 'Ascending' and sort == 'Insertion':
            MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description = insertionSort.InsertionSortRating(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description)

        elif column == 'Discounts' and Order == 'Ascending' and sort == 'Insertion':
            MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description = insertionSort.InsertionSortDiscount(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description)
        
        elif column == 'Descriptions' and Order == 'Ascending' and sort == 'Insertion':
            MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description = insertionSort.InsertionSortDescription(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description)

        #Insertion Sort Descending
        elif column == 'Name' and Order == 'Descending' and sort == 'Insertion':
            MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description = insertionSort.InsertionSortDescending(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description)

        elif column == 'Old Prices' and Order == 'Descending' and sort == 'Insertion':
            MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description = insertionSort.InsertionSortOldpriceDescending(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description)

        elif column == 'New Prices' and Order == 'Descending' and sort == 'Insertion':
            MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description = insertionSort.InsertionSortNewPriceDescending(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description)

        elif column == 'Quantity' and Order == 'Descending' and sort == 'Insertion':
            MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description = insertionSort.InsertionSortQuantityDescending(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description)

        elif column == 'Stars' and Order == 'Descending' and sort == 'Insertion':
            MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description = insertionSort.InsertionSortStarsDescending(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description)
        
        elif column == 'Orders' and Order == 'Descending' and sort == 'Insertion':
            MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description = insertionSort.InsertionSortRatingDescending(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description)

        elif column == 'Discounts' and Order == 'Descending' and sort == 'Insertion':
            MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description = insertionSort.InsertionSortDiscountDescending(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description)
        
        elif column == 'Descriptions' and Order == 'Descending' and sort == 'Insertion':
            MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description = insertionSort.InsertionSortDescriptionDescending(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description)

        #Bubble Sort Ascending
        elif column == 'Name' and Order == 'Ascending' and sort == 'Bubble':
            MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description = bubbleSort.BubbleSortAscending(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description)

        elif column == 'Old Prices' and Order == 'Ascending' and sort == 'Bubble':
            MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description = bubbleSort.BubbleSortOldpriceAscending(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description)

        elif column == 'New Prices' and Order == 'Ascending' and sort == 'Bubble':
            MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description = bubbleSort.BubbleSortNewPriceAscending(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description)

        elif column == 'Quantity' and Order == 'Ascending' and sort == 'Bubble':
            MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description = bubbleSort.BubbleSortQuantityAscending(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description)

        elif column == 'Stars' and Order == 'Ascending' and sort == 'Bubble':
            MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description = bubbleSort.BubbleSortStarsAscending(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description)

        elif column == 'Orders' and Order == 'Ascending' and sort == 'Bubble':
            MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description = bubbleSort.BubbleSortRatingAscending(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description)
        
        elif column == 'Discounts' and Order == 'Ascending' and sort == 'Bubble':
            MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description = bubbleSort.BubbleSortDiscountAscending(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description)
        
        elif column == 'Descriptions' and Order == 'Ascending' and sort == 'Bubble':
            MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description = bubbleSort.BubbleSortDescriptionAscending(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description)

        #Bubble Sort Descending
        elif column == 'Name' and Order == 'Descending' and sort == 'Bubble':
            MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description = bubbleSort.BubbleSortDescending(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description)

        elif column == 'Old Prices' and Order == 'Descending' and sort == 'Bubble':
            MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description = bubbleSort.BubbleSortOldpriceDescending(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description)

        elif column == 'New Prices' and Order == 'Descending' and sort == 'Bubble':
            MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description = bubbleSort.BubbleSortNewPriceDescending(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description)

        elif column == 'Quantity' and Order == 'Descending' and sort == 'Bubble':
            MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description = bubbleSort.BubbleSortQuantityDescending(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description)

        elif column == 'Stars' and Order == 'Descending' and sort == 'Bubble':
            MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description = bubbleSort.BubbleSortStarsDescending(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description)

        elif column == 'Orders' and Order == 'Descending' and sort == 'Bubble':
            MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description = bubbleSort.BubbleSortRatingDescending(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description)
        
        elif column == 'Discounts' and Order == 'Descending' and sort == 'Bubble':
            MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description = bubbleSort.BubbleSortDiscountDescending(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description)
        
        elif column == 'Descriptions' and Order == 'Descending' and sort == 'Bubble':
            MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description = bubbleSort.BubbleSortDescriptionDescending(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description)

        #Selection Sort Ascending
        elif column == 'Name' and Order == 'Ascending' and sort == 'Selection':
            MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description = selectionSort.SelectionSortAscending(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description)

        elif column == 'Old Prices' and Order == 'Ascending' and sort == 'Selection':
            MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description = selectionSort.SelectionSortOldpriceAscending(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description)

        elif column == 'New Prices' and Order == 'Ascending' and sort == 'Selection':
            MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description = selectionSort.SelectionSortNewPriceAscending(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description)

        elif column == 'Quantity' and Order == 'Ascending' and sort == 'Selection':
            MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description = selectionSort.SelectionSortQuantityAscending(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description)

        elif column == 'Stars' and Order == 'Ascending' and sort == 'Selection':
            MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description = selectionSort.SelectionSortStarsAscending(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description)

        elif column == 'Orders' and Order == 'Ascending' and sort == 'Selection':
            MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description = selectionSort.SelectionSortRatingAscending(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description)

        elif column == 'Discounts' and Order == 'Ascending' and sort == 'Selection':
            MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description = selectionSort.SelectionSortDiscountAscending(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description)

        elif column == 'Descriptions' and Order == 'Ascending' and sort == 'Selection':
            MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description = selectionSort.SelectionSortDescriptionAscending(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description)

        #Selection Sort Descending
        elif column == 'Name' and Order == 'Descending' and sort == 'Selection':
            MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description = selectionSort.SelectionSortDescending(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description)

        elif column == 'Old Prices' and Order == 'Descending' and sort == 'Selection':
            MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description = selectionSort.SelectionSortOldpriceDescending(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description)

        elif column == 'New Prices' and Order == 'Descending' and sort == 'Selection':
            MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description = selectionSort.SelectionSortNewPriceDescending(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description)

        elif column == 'Quantity' and Order == 'Descending' and sort == 'Selection':
            MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description = selectionSort.SelectionSortQuantityDescending(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description)

        elif column == 'Stars' and Order == 'Descending' and sort == 'Selection':
            MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description = selectionSort.SelectionSortStarsDescending(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description)

        elif column == 'Orders' and Order == 'Descending' and sort == 'Selection':
            MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description = selectionSort.SelectionSortRatingDescending(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description)

        elif column == 'Discounts' and Order == 'Descending' and sort == 'Selection':
            MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description = selectionSort.SelectionSortDiscountDescending(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description)

        elif column == 'Descriptions' and Order == 'Descending' and sort == 'Selection':
            MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description = selectionSort.SelectionSortDescriptionDescending(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description)

        MedicineNameRow = 0
        for names in MedicineName:
            self.tableWidget.setItem(MedicineNameRow, 0, QtWidgets.QTableWidgetItem(names))
            MedicineNameRow = MedicineNameRow  + 1

        OldpriceRow = 0
        for oldPrice in OldpriceInt:
            self.tableWidget.setItem(OldpriceRow, 1, QtWidgets.QTableWidgetItem(str(oldPrice)))
            OldpriceRow = OldpriceRow  + 1

        NewPriceRow = 0
        for newPrice in NewPriceInt:
            self.tableWidget.setItem(NewPriceRow, 2, QtWidgets.QTableWidgetItem(str(newPrice)))
            NewPriceRow = NewPriceRow  + 1
        
        QuantityRow = 0
        for quantity in Quantity:
            self.tableWidget.setItem(QuantityRow, 3, QtWidgets.QTableWidgetItem(quantity))
            QuantityRow = QuantityRow  + 1

        StarsRow = 0
        for star in Stars:
            self.tableWidget.setItem(StarsRow, 4, QtWidgets.QTableWidgetItem(str(star)))
            StarsRow = StarsRow  + 1

        RatingRow = 0
        for rating in RatingInt:
            self.tableWidget.setItem(RatingRow, 5, QtWidgets.QTableWidgetItem(str(rating)))
            RatingRow = RatingRow  + 1

        DiscountRow = 0
        for discount in Discount:
            self.tableWidget.setItem(DiscountRow, 6, QtWidgets.QTableWidgetItem(discount))
            DiscountRow = DiscountRow  + 1

        DescriptionRow = 0
        for description in Description:
            self.tableWidget.setItem(DescriptionRow, 7, QtWidgets.QTableWidgetItem(description))
            DescriptionRow = DescriptionRow  + 1
            
        
        
        
        
    

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