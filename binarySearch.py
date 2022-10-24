# -*- coding: utf-8 -*-
"""
Created on Mon Oct 24 00:35:55 2022

@author: HP
"""

def binarySearch(arr,x):
    low = 0
    high = len(arr) - 1
 
    while high - low > 1:
        mid = (high + low) // 2
        if arr[mid] < x:
            low = mid + 1
        else:
            high = mid
 
    if arr[low] == x:
        return low
    elif arr[high] == x:
        return high
    else:
        return -1
 
 
arr = [1, 3, 4, 5, 6]
 
x = 4
print(binarySearch(arr,x))
 
