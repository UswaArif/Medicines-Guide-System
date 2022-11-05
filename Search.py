from re import search
import sys
from tkinter import Widget
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5 import QtWidgets,uic,QtCore
from PyQt5 import *
from PyQt5.QtWidgets import QMainWindow,QApplication,QTableWidgetItem,QStackedWidget,QMessageBox,QDialog,QSizePolicy,QPushButton,QComboBox
import pandas as pd


def AttributeSearchUsingOr(DataList,searchBox,FilterComboBox):
    flag1 = False
    flag2 = False
    flag3 = False
    flag4 = False
    if(FilterComboBox == "Contains"):
        for element in DataList:
            if searchBox in element:
                flag1 = True
                            
        if(flag1 == True):
            return DataList
        else:
            return "Data list does not contain this word"
    if(FilterComboBox == "Equals to"):
        for element in DataList:
            if element == searchBox:
                flag2 = True
                            
        if(flag2 == True):
            return DataList
        else:
            return "Data list does not have  a word which is equal to this specific word"
    if (FilterComboBox == "Starts with"):
        for element in DataList:
            if element.startswith(searchBox):
                flag3 = True
                            
        if(flag3 == True):
            return DataList
        else:
            return" Data list does not have a word that starts with this word"
    if (FilterComboBox == "Ends with"):
        for element in DataList:
            if element.endswith(searchBox):
                flag4 = True
                            
        if(flag4 == True):
            return DataList
        else:
            return "Data list does not have a word that ends with this word"

def AttributeSearchUsingAnd(columnComboBox,searchBox,FilterComboBox):
    outputList=[]
    if(FilterComboBox == "Contains"):
        for element in columnComboBox:
            if searchBox in element:
                outputList.append(element)                      # return the element containing     
        return outputList
    if(FilterComboBox == "Equals to"):
        for element in columnComboBox:
            if element == searchBox:
                outputList.append(element)                      # return the element equal with     
        return outputList
    if (FilterComboBox == "Starts with"):
        for element in columnComboBox:
            if element.startswith(searchBox):
                outputList.append(element) 
        print(outputList)                     # return the element equal with     
        return outputList
    if (FilterComboBox == "Ends with"):
        for element in columnComboBox:
            if element.endswith(searchBox):
                outputList.append(element)
            
                                    # return the element equal with     
        return outputList
    

def AttributeSearchUsingLinearSearch(columnComboBox,searchBox):
    outputList=[]
    for i in range(0,len(columnComboBox)):
        if(columnComboBox[i] == searchBox):
            outputList.append(columnComboBox[i])
    return outputList


def SearchingFunction_call(DataList,typecomboBox,FilterComboBox,showBox):
        res=[]
        if(typecomboBox == "OR"):
            res = AttributeSearchUsingOr(DataList,showBox,FilterComboBox)
            print(res)
        elif(typecomboBox == "AND"):
            res = AttributeSearchUsingAnd(DataList,showBox,FilterComboBox)
            print(res)
        elif(typecomboBox == "Linear"):
            res = AttributeSearchUsingLinearSearch(DataList,showBox)
            #"YouTube Boxing Cringe Moments"
            print(res)
        return res