from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setStyleSheet("")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.mainLabel = QtWidgets.QLabel(self.frame)
        self.mainLabel.setObjectName("mainLabel")
        self.gridLayout_2.addWidget(self.mainLabel, 0, 0, 1, 3)
        self.advancedButton = QtWidgets.QPushButton(self.frame)
        self.advancedButton.setObjectName("advancedButton")
        self.gridLayout_2.addWidget(self.advancedButton, 1, 0, 1, 3)
        self.tableWidget = QtWidgets.QTableWidget(self.frame)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(8)
        self.tableWidget.setRowCount(16)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(10, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(11, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(12, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(13, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(14, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(15, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(7, item)
        self.gridLayout_2.addWidget(self.tableWidget, 3, 0, 1, 11)
        self.ScrappingLabel = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.ScrappingLabel.setFont(font)
        self.ScrappingLabel.setObjectName("ScrappingLabel")
        self.gridLayout_2.addWidget(self.ScrappingLabel, 4, 0, 1, 2)
        self.csvButton = QtWidgets.QPushButton(self.frame)
        self.csvButton.setObjectName("csvButton")
        self.gridLayout_2.addWidget(self.csvButton, 4, 8, 1, 2)
        self.excelButton = QtWidgets.QPushButton(self.frame)
        self.excelButton.setObjectName("excelButton")
        self.gridLayout_2.addWidget(self.excelButton, 4, 10, 1, 1)
        self.urlLabel = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.urlLabel.setFont(font)
        self.urlLabel.setObjectName("urlLabel")
        self.gridLayout_2.addWidget(self.urlLabel, 5, 0, 1, 1)
        self.stopButton = QtWidgets.QPushButton(self.frame)
        self.stopButton.setObjectName("stopButton")
        self.gridLayout_2.addWidget(self.stopButton, 5, 7, 1, 1)
        self.progressBar = QtWidgets.QProgressBar(self.frame)
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.gridLayout_2.addWidget(self.progressBar, 6, 1, 1, 9)
        self.urlTextbox = QtWidgets.QPlainTextEdit(self.frame)
        self.urlTextbox.setObjectName("urlTextbox")
        self.gridLayout_2.addWidget(self.urlTextbox, 5, 1, 1, 4)
        self.startButton = QtWidgets.QPushButton(self.frame)
        self.startButton.setObjectName("startButton")
        self.gridLayout_2.addWidget(self.startButton, 5, 6, 1, 1)
        self.searchCombobox = QtWidgets.QComboBox(self.frame)
        self.searchCombobox.setObjectName("searchCombobox")
        self.gridLayout_2.addWidget(self.searchCombobox, 2, 0, 1, 2)
        self.searchButton = QtWidgets.QPushButton(self.frame)
        self.searchButton.setObjectName("searchButton")
        self.gridLayout_2.addWidget(self.searchButton, 2, 2, 1, 1)
        self.sortButton = QtWidgets.QPushButton(self.frame)
        self.sortButton.setObjectName("sortButton")
        self.gridLayout_2.addWidget(self.sortButton, 2, 10, 1, 1)
        self.sortCombobox = QtWidgets.QComboBox(self.frame)
        self.sortCombobox.setObjectName("sortCombobox")
        self.sortCombobox.addItem("Insertion Sort")
        self.sortCombobox.addItem("Merge Sort")
        self.sortCombobox.addItem("Bubble Sort")
        self.sortCombobox.addItem("Selection Sort")
        self.sortCombobox.addItem("Heap Sort")
        self.sortCombobox.addItem("Quick Sort")
        self.sortCombobox.addItem("PigeonHole Sort")
        self.sortCombobox.addItem("Shell Sort")
        self.sortCombobox.addItem("Tim Sort")
        self.sortCombobox.addItem("Counting Sort")
        self.sortCombobox.addItem("Radix Sort")
        self.sortCombobox.addItem("Bracket Sort")
        self.sortCombobox.addItem("odd-even Sort")
        self.gridLayout_2.addWidget(self.sortCombobox, 2, 8, 1, 2)
        self.comboBox = QtWidgets.QComboBox(self.frame)
        self.comboBox.setObjectName("comboBox")
        self.gridLayout_2.addWidget(self.comboBox, 2, 6, 1, 2)
        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.mainLabel.setText(_translate("MainWindow", "Find medicines you need:"))
        self.advancedButton.setText(_translate("MainWindow", "Advanced Search"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Names"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Old Price"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "New Price"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Quantity"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Stars"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Order"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "Discount"))
        item = self.tableWidget.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "Description"))
        self.ScrappingLabel.setText(_translate("MainWindow", "Scrapping"))
        self.csvButton.setText(_translate("MainWindow", "Export to csv"))
        self.excelButton.setText(_translate("MainWindow", "Export to excel"))
        self.urlLabel.setText(_translate("MainWindow", "Enter URL:"))
        self.stopButton.setText(_translate("MainWindow", "Stop"))
        self.startButton.setText(_translate("MainWindow", "Start"))
        self.searchButton.setText(_translate("MainWindow", "Search"))
        self.sortButton.setText(_translate("MainWindow", "Sort"))
        self.sortCombobox.setItemText(0, _translate("MainWindow", "Insertion Sort"))
        self.sortCombobox.setItemText(1, _translate("MainWindow", "Merge Sort"))

    def InsertionSort(array):                    # sort in ascending
        for i in range(1, len(array)):
            key = array[i]
            j = i - 1
            while key < array[j] and j >= 0:
                array[j + 1] = array[j]
                j = j - 1
            array[j + 1] = key    
        return array

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())