from re import search
import sys
from tkinter import Widget
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5 import QtWidgets,uic,QtCore
from PyQt5 import *
from PyQt5.QtWidgets import QMainWindow,QApplication,QTableWidgetItem,QStackedWidget,QMessageBox,QDialog,QSizePolicy,QPushButton,QComboBox
import pandas as pd
from AdvancedSearch import Ui_MainWindow
import InsertionSort2
import bubbleSort
import selectionSort
import shellSort
import OddEvenSort
import mergeSort
import quickSort
import heapSort
import TimSort
import radixSort
import search

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        loadUi("MedicineGuide.UI", self)
        #print(RatingInt)
        #print(self.InsertionSort(MedicineName,OldpriceInt,NewPriceInt,Quantity,Starsfloat,RatingInt,Discount,Description))
        self.startButton.clicked.connect(self.load)
        self.sortButton.clicked.connect(self.SortingImplement)
        self.advancedButton.clicked.connect(self.show_new_window)
        self.MultiLevelSort.clicked.connect(self.MultiLevelSorting)
        self.ExcelButton.clicked.connect(self.ExportToExcel)
        
    def read(self):
        df = pd.read_csv("700Data.csv")
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
        df = pd.read_csv("700Data.csv")
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

    def SortingImplement(self):
        
        MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description=self.read()
        #QMessageBox.about(self,'error1','Order')

        column = self.ColumncomboBox.currentText()
        Order = self.AscendCombobox.currentText()
        sort = self.sortCombobox.currentText()
        #print(insertionSort.InsertionSort(MedicineName,OldpriceInt,NewPriceInt,Quantity,Starsfloat,RatingInt,Discount,Description))
        QMessageBox.about(self,'Column Name', column)

        #Insertion Sort Ascending
        if column == 'Name' and Order == 'Ascending' and sort == 'Insertion':
            MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description = InsertionSort2.InsertionSort(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description)

        elif column == 'Old Prices' and Order == 'Ascending' and sort == 'Insertion':
            MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description = InsertionSort2.InsertionSortOldprice(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description)

        elif column == 'New Prices' and Order == 'Ascending' and sort == 'Insertion':
            MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description = InsertionSort2.InsertionSortNewPrice(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description)

        elif column == 'Quantity' and Order == 'Ascending' and sort == 'Insertion':
            MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description = InsertionSort2.InsertionSortQuantity(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description)

        elif column == 'Stars' and Order == 'Ascending' and sort == 'Insertion':
            MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description = InsertionSort2.InsertionSortStars(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description)
        
        elif column == 'Orders' and Order == 'Ascending' and sort == 'Insertion':
            MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description = InsertionSort2.InsertionSortRating(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description)

        elif column == 'Discounts' and Order == 'Ascending' and sort == 'Insertion':
            MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description = InsertionSort2.InsertionSortDiscount(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description)
        
        elif column == 'Descriptions' and Order == 'Ascending' and sort == 'Insertion':
            MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description = InsertionSort2.InsertionSortDescription(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description)

        #Insertion Sort Descending
        elif column == 'Name' and Order == 'Descending' and sort == 'Insertion':
            MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description = InsertionSort2.InsertionSortDescending(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description)

        elif column == 'Old Prices' and Order == 'Descending' and sort == 'Insertion':
            MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description = InsertionSort2.InsertionSortOldpriceDescending(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description)

        elif column == 'New Prices' and Order == 'Descending' and sort == 'Insertion':
            MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description = InsertionSort2.InsertionSortNewPriceDescending(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description)

        elif column == 'Quantity' and Order == 'Descending' and sort == 'Insertion':
            MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description = InsertionSort2.InsertionSortQuantityDescending(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description)

        elif column == 'Stars' and Order == 'Descending' and sort == 'Insertion':
            MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description = InsertionSort2.InsertionSortStarsDescending(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description)
        
        elif column == 'Orders' and Order == 'Descending' and sort == 'Insertion':
            MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description = InsertionSort2.InsertionSortRatingDescending(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description)

        elif column == 'Discounts' and Order == 'Descending' and sort == 'Insertion':
            MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description = InsertionSort2.InsertionSortDiscountDescending(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description)
        
        elif column == 'Descriptions' and Order == 'Descending' and sort == 'Insertion':
            MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description = InsertionSort2.InsertionSortDescriptionDescending(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description)

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

        #Shell Sort Ascending
        elif column == 'Name' and Order == 'Ascending' and sort == 'Shell':
            MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description = shellSort.shellSortAscending(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description)

        elif column == 'Old Prices' and Order == 'Ascending' and sort == 'Shell':
            MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description = shellSort.shellSortOldpriceAscending(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description)

        elif column == 'New Prices' and Order == 'Ascending' and sort == 'Shell':
            MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description = shellSort.shellSortNewPriceAscending(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description)
        
        elif column == 'Quantity' and Order == 'Ascending' and sort == 'Shell':
            MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description = shellSort.shellSortQuantityAscending(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description)
        
        elif column == 'Stars' and Order == 'Ascending' and sort == 'Shell':
            MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description = shellSort.shellSortStarsAscending(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description)
        
        elif column == 'Orders' and Order == 'Ascending' and sort == 'Shell':
            MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description = shellSort.shellSortRatingAscending(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description)
        
        elif column == 'Discounts' and Order == 'Ascending' and sort == 'Shell':
            MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description = shellSort.shellSortDiscountAscending(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description)
        
        elif column == 'Descriptions' and Order == 'Ascending' and sort == 'Shell':
            MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description = shellSort.shellSortDescriptionAscending(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description)
        
        #Shell Sort Descending
        elif column == 'Name' and Order == 'Descending' and sort == 'Shell':
            MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description = shellSort.shellSortDescending(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description)

        elif column == 'Old Prices' and Order == 'Descending' and sort == 'Shell':
            MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description = shellSort.shellSortOldpriceDescending(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description)

        elif column == 'New Prices' and Order == 'Descending' and sort == 'Shell':
            MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description = shellSort.shellSortNewPriceDescending(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description)
        
        elif column == 'Quantity' and Order == 'Descending' and sort == 'Shell':
            MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description = shellSort.shellSortQuantityDescending(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description)
        
        elif column == 'Stars' and Order == 'Descending' and sort == 'Shell':
            MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description = shellSort.shellSortStarsDescending(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description)
        
        elif column == 'Orders' and Order == 'Descending' and sort == 'Shell':
            MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description = shellSort.shellSortRatingDescending(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description)
        
        elif column == 'Discounts' and Order == 'Descending' and sort == 'Shell':
            MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description = shellSort.shellSortDiscountDescending(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description)
        
        elif column == 'Descriptions' and Order == 'Descending' and sort == 'Shell':
            MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description = shellSort.shellSortDescriptionDescending(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description)

        #Odd/Even Sort Ascending
        elif column == 'Old Prices' and Order == 'Ascending' and sort == 'Odd/Even':
            MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description = OddEvenSort.oddEvenSortOldpriceAscending(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description)

        elif column == 'New Prices' and Order == 'Ascending' and sort == 'Odd/Even':
            MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description = OddEvenSort.oddEvenSortNewPriceAscending(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description)

        elif column == 'Orders' and Order == 'Ascending' and sort == 'Odd/Even':
            MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description = OddEvenSort.oddEvenSortRatingAscending(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description)

        #Odd/Even Sort Descending
        elif column == 'Old Prices' and Order == 'Descending' and sort == 'Odd/Even':
            MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description = OddEvenSort.oddEvenSortOldpriceDescending(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description)

        elif column == 'New Prices' and Order == 'Descending' and sort == 'Odd/Even':
            MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description = OddEvenSort.oddEvenSortNewPriceDescending(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description)

        elif column == 'Orders' and Order == 'Descending' and sort == 'Odd/Even':
            MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description = OddEvenSort.oddEvenSortRatingDescending(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description)

        #Merge Sort Ascending
        elif column == 'Name' and Order == 'Ascending' and sort == 'Merge':
            MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description = mergeSort.MergeSort(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description, 0, len(MedicineName)-1)

        elif column == 'Old Prices' and Order == 'Ascending' and sort == 'Merge':
            MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description = mergeSort.MergeSortOldprice(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description, 0, len(OldpriceInt)-1)

        elif column == 'New Prices' and Order == 'Ascending' and sort == 'Merge':
            MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description = mergeSort.MergeSortNewPrice(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description, 0, len(NewPriceInt)-1)
        
        elif column == 'Quantity' and Order == 'Ascending' and sort == 'Merge':
            MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description = mergeSort.MergeSortQuantity(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description, 0, len(Quantity)-1)
        
        elif column == 'Stars' and Order == 'Ascending' and sort == 'Merge':
            MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description = mergeSort.MergeSortStars(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description, 0, len(Stars)-1)
        
        elif column == 'Orders' and Order == 'Ascending' and sort == 'Merge':
            MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description = mergeSort.MergeSortRating(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description, 0, len(RatingInt)-1)
        
        elif column == 'Discounts' and Order == 'Ascending' and sort == 'Merge':
            MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description = mergeSort.MergeSortDiscount(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description, 0, len(Discount)-1)
        
        elif column == 'Descriptions' and Order == 'Ascending' and sort == 'Merge':
            MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description = mergeSort.MergeSortDescription(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description, 0, len(Description)-1)
        
        #Merge Sort Descending 
        elif column == 'Name' and Order == 'Descending' and sort == 'Merge':
            MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description = mergeSort.MergeSortDescending(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description, 0, len(MedicineName)-1)

        elif column == 'Old Prices' and Order == 'Descending' and sort == 'Merge':
            MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description = mergeSort.MergeSortOldpriceDescending(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description, 0, len(OldpriceInt)-1)

        elif column == 'New Prices' and Order == 'Descending' and sort == 'Merge':
            MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description = mergeSort.MergeSortNewPriceDescending(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description, 0, len(NewPriceInt)-1)
        
        elif column == 'Quantity' and Order == 'Descending' and sort == 'Merge':
            MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description = mergeSort.MergeSortQuantityDescending(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description, 0, len(Quantity)-1)
        
        elif column == 'Stars' and Order == 'Descending' and sort == 'Merge':
            MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description = mergeSort.MergeSortStarsDescending(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description, 0, len(Stars)-1)
        
        elif column == 'Orders' and Order == 'Descending' and sort == 'Merge':
            MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description = mergeSort.MergeSortRatingDescending(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description, 0, len(RatingInt)-1)
        
        elif column == 'Discounts' and Order == 'Descending' and sort == 'Merge':
            MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description = mergeSort.MergeSortDiscountDescending(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description, 0, len(Discount)-1)
        
        elif column == 'Descriptions' and Order == 'Descending' and sort == 'Merge':
            MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description = mergeSort.MergeSortDescriptionDescending(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description, 0, len(Description)-1)
        
        #Quick Sort Ascending
        elif column == 'Name' and Order == 'Ascending' and sort == 'Quick':
            MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description = quickSort.QuickSortAscending(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description, 0, len(MedicineName)-1)

        elif column == 'Old Prices' and Order == 'Ascending' and sort == 'Quick':
            MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description = quickSort.QuickSortOldpriceAscending(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description, 0, len(MedicineName)-1)
        
        elif column == 'New Prices' and Order == 'Ascending' and sort == 'Quick':
            MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description = quickSort.QuickSortNewPriceAscending(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description, 0, len(MedicineName)-1)
        
        elif column == 'Quantity' and Order == 'Ascending' and sort == 'Quick':
            MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description = quickSort.QuickSortQuantityAscending(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description, 0, len(MedicineName)-1)

        elif column == 'Stars' and Order == 'Ascending' and sort == 'Quick':
            MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description = quickSort.QuickSortStarsAscending(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description, 0, len(MedicineName)-1)
        
        elif column == 'Orders' and Order == 'Ascending' and sort == 'Quick':
            MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description = quickSort.QuickSortRatingAscending(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description, 0, len(MedicineName)-1)
        
        elif column == 'Discounts' and Order == 'Ascending' and sort == 'Quick':
            MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description = quickSort.QuickSortDiscountAscending(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description, 0, len(MedicineName)-1)
        
        elif column == 'Descriptions' and Order == 'Ascending' and sort == 'Quick':
            MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description = quickSort.QuickSortDescriptionAscending(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description, 0, len(MedicineName)-1)

        #Quick Sort Descending
        elif column == 'Name' and Order == 'Descending' and sort == 'Quick':
            MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description = quickSort.QuickSortDescending(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description, 0, len(MedicineName)-1)

        elif column == 'Old Prices' and Order == 'Descending' and sort == 'Quick':
            MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description = quickSort.QuickSortOldpriceDescending(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description, 0, len(MedicineName)-1)
        
        elif column == 'New Prices' and Order == 'Descending' and sort == 'Quick':
            MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description = quickSort.QuickSortNewPriceDescending(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description, 0, len(MedicineName)-1)
        
        elif column == 'Quantity' and Order == 'Descending' and sort == 'Quick':
            MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description = quickSort.QuickSortQuantityDescending(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description, 0, len(MedicineName)-1)

        elif column == 'Stars' and Order == 'Descending' and sort == 'Quick':
            MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description = quickSort.QuickSortStarsDescending(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description, 0, len(MedicineName)-1)
        
        elif column == 'Orders' and Order == 'Descending' and sort == 'Quick':
            MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description = quickSort.QuickSortRatingDescending(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description, 0, len(MedicineName)-1)
        
        elif column == 'Discounts' and Order == 'Descending' and sort == 'Quick':
            MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description = quickSort.QuickSortDiscountDescending(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description, 0, len(MedicineName)-1)
        
        elif column == 'Descriptions' and Order == 'Descending' and sort == 'Quick':
            MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description = quickSort.QuickSortDescriptionDescending(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description, 0, len(MedicineName)-1)
        
        #Heap Sort Ascending
        elif column == 'Name' and Order == 'Ascending' and sort == 'Heap':
            MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description = heapSort.heapSortAscending(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description)

        elif column == 'Old Prices' and Order == 'Ascending' and sort == 'Heap':
            MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description = heapSort.heapSortOldpriceAscending(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description)

        elif column == 'New Prices' and Order == 'Ascending' and sort == 'Heap':
            MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description = heapSort.heapSortNewPriceAscending(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description)
        
        elif column == 'Quantity' and Order == 'Ascending' and sort == 'Heap':
            MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description = heapSort.heapSortQuantityAscending(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description)
        
        elif column == 'Stars' and Order == 'Ascending' and sort == 'Heap':
            MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description = heapSort.heapSortStarsAscending(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description)
        
        elif column == 'Orders' and Order == 'Ascending' and sort == 'Heap':
            MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description = heapSort.heapSortRatingAscending(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description)
        
        elif column == 'Discounts' and Order == 'Ascending' and sort == 'Heap':
            MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description = heapSort.heapSortDiscountAscending(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description)
        
        elif column == 'Descriptions' and Order == 'Ascending' and sort == 'Heap':
            MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description = heapSort.heapSortDescriptionAscending(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description)

        #Heap Sort Descending
        elif column == 'Name' and Order == 'Descending' and sort == 'Heap':
            MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description = heapSort.heapSortDescending(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description)

        elif column == 'Old Prices' and Order == 'Descending' and sort == 'Heap':
            MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description = heapSort.heapSortOldpriceDescending(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description)

        elif column == 'New Prices' and Order == 'Descending' and sort == 'Heap':
            MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description = heapSort.heapSortNewPriceDescending(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description)
        
        elif column == 'Quantity' and Order == 'Descending' and sort == 'Heap':
            MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description = heapSort.heapSortQuantityDescending(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description)
        
        elif column == 'Stars' and Order == 'Descending' and sort == 'Heap':
            MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description = heapSort.heapSortStarsDescending(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description)
        
        elif column == 'Orders' and Order == 'Descending' and sort == 'Heap':
            MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description = heapSort.heapSortRatingDescending(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description)
        
        elif column == 'Discounts' and Order == 'Descending' and sort == 'Heap':
            MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description = heapSort.heapSortDiscountDescending(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description)
        
        elif column == 'Descriptions' and Order == 'Descending' and sort == 'Heap':
            MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description = heapSort.heapSortDescriptionDescending(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description)

        #Tim Sort Ascending
        elif column == 'Name' and Order == 'Ascending' and sort == 'Tim':
            MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description = TimSort.timSortAscending(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description)

        elif column == 'Old Prices' and Order == 'Ascending' and sort == 'Tim':
            MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description = TimSort.timSortOldpriceAscending(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description)

        elif column == 'New Prices' and Order == 'Ascending' and sort == 'Tim':
            MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description = TimSort.timSortNewPriceAscending(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description)
        
        elif column == 'Quantity' and Order == 'Ascending' and sort == 'Tim':
            MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description = TimSort.timSortQuantityAscending(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description)
        
        elif column == 'Stars' and Order == 'Ascending' and sort == 'Tim':
            MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description = TimSort.timSortStarsAscending(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description)
        
        elif column == 'Orders' and Order == 'Ascending' and sort == 'Tim':
            MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description = TimSort.timSortRatingAscending(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description)
        
        elif column == 'Discounts' and Order == 'Ascending' and sort == 'Tim':
            MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description = TimSort.timSortDiscountAscending(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description)
        
        elif column == 'Descriptions' and Order == 'Ascending' and sort == 'Tim':
            MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description = TimSort.timSortDescriptionAscending(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description)

        #Tim Sort Descending
        elif column == 'Name' and Order == 'Descending' and sort == 'Tim':
            MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description = TimSort.timSortDescending(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description)

        elif column == 'Old Prices' and Order == 'Descending' and sort == 'Tim':
            MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description = TimSort.timSortOldpriceDescending(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description)

        elif column == 'New Prices' and Order == 'Descending' and sort == 'Tim':
            MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description = TimSort.timSortNewPriceDescending(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description)
        
        elif column == 'Quantity' and Order == 'Descending' and sort == 'Tim':
            MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description = TimSort.timSortQuantityDescending(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description)
        
        elif column == 'Stars' and Order == 'Descending' and sort == 'Tim':
            MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description = TimSort.timSortStarsDescending(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description)
        
        elif column == 'Orders' and Order == 'Descending' and sort == 'Tim':
            MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description = TimSort.timSortRatingDescending(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description)
        
        elif column == 'Discounts' and Order == 'Descending' and sort == 'Tim':
            MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description = TimSort.timSortDiscountDescending(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description)
        
        elif column == 'Descriptions' and Order == 'Descending' and sort == 'Tim':
            MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description = TimSort.timSortDescriptionDescending(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description)

        #Radix Sort Ascending
        elif column == 'Old Prices' and Order == 'Ascending' and sort == 'Radix':
            MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description = radixSort.RadixSortAscending(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description)
        
        elif column == 'New Prices' and Order == 'Ascending' and sort == 'Radix':
            MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description = radixSort.RadixSortAscendingNewPrice(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description)

        elif column == 'Orders' and Order == 'Ascending' and sort == 'Radix':
            MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description = radixSort.RadixSortAscendingRating(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description)
        
        #Radix Sort Descending
        elif column == 'Old Prices' and Order == 'Descending' and sort == 'Radix':
            MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description = radixSort.RadixSortDescending(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description)
        
        elif column == 'New Prices' and Order == 'Descending' and sort == 'Radix':
            MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description = radixSort.RadixSortDescendingNewPrice(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description)

        elif column == 'Orders' and Order == 'Descending' and sort == 'Radix':
            MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description = radixSort.RadixSortDescendingRating(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description)

        else:
            QMessageBox.about(self,'Error','Not Avaiable')

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

    def MultiLevelSorting(self):
        
        MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description=self.read()  
        MedicineName.sort()  
        OldpriceInt.sort()
        NewPriceInt.sort()
        Quantity.sort()
        Stars.sort()
        RatingInt.sort()
        Discount.sort()
        Description.sort()

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

    def ExportToExcel(self):
        #QMessageBox.about(self,'Column Name', 'aa')
        MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description=self.read()
        
        data = pd.DataFrame({'Medicine Name': MedicineName,
                            'Old Price': OldpriceInt,
                            'New Price': NewPriceInt,
                            'Quantity': Quantity,
                            'Stars': Stars,
                            'Orders': RatingInt,
                            'Discount': Discount,
                            'Description': Description
                            })
  
        # determining the name of the file
        #file_name = 'Data.xlsx'
        
        # saving the excel
        data.to_excel('E:\ProjectMid\Data.xlsx',sheet_name='sheet1',index=False,header=True)
        QMessageBox.about(self,'Column Name', 'aa')
        print('DataFrame is written to Excel File successfully.')
            

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