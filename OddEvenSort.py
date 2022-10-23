# -*- coding: utf-8 -*-
"""
Created on Thu Oct 20 13:31:12 2022

@author: HP
"""

def oddEvenSort(Arr):
   n = len(Arr)
   isSorted = 0 #isSorted is used as flag
   
   while isSorted == 0:
      isSorted = 1
      temp = 0
      #For Odd Numbers
      for i in range(1, n-1, 2):
         if Arr[i] > Arr[i+1]:
            temp = Arr[i]
            Arr[i] = Arr[i+1]
            Arr[i+1] = temp
            isSorted = 0
       
      #For Even Numbers      
      for i in range(0, n-1, 2):
         if Arr[i] > Arr[i+1]:
            temp = Arr[i]
            Arr[i] = Arr[i+1]
            Arr[i+1] = temp
            isSorted = 0
   return Arr

Arr = [9,0,2,-3,26,-1,8,7]

print(oddEvenSort(Arr))
