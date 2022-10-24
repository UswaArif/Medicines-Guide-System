# -*- coding: utf-8 -*-
"""
Created on Mon Oct 24 00:29:12 2022

@author: HP
"""

def LinearSearch(arr,x):
    n = len(arr)
 
    for i in range(0, n):
        if (arr[i] == x):
            return i
    return -1


arr = [-2, 7, 15, -14, 0, 0, 7, -7, -4, -133, 5, 8, -14, 12]
x = 12
print(LinearSearch(arr, x))