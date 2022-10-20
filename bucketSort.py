# -*- coding: utf-8 -*-
"""
Created on Thu Oct 20 14:11:16 2022

@author: HP
"""
def insertion_sort(Arr):
    for i in range(1,len(Arr),1):
        key = Arr[i]
        j = i - 1
        while (j >= 0 and key < Arr[j]):
            Arr[j + 1] = Arr[j]
            j = j - 1
            
        Arr[j + 1] = key
 

def bucketSort(Array):
    largest = max(Array)
    length = len(Array)
    size = largest/length
 
    # Create Empty Buckets array
    buckets = [[] for i in range(length)]
 
    # Bucket Sorting   
    for i in range(length):
        index = int(Array[i]/size)
        if index != length:
            buckets[index].append(Array[i])
        else:
            buckets[length - 1].append(Array[i])
  
    #Sorting Array with insertion sort
    for i in range(len(Array)):
        insertion_sort(buckets[i])
 
 
    # Concatenating the bucket Array
    result = []
    for i in range(length):
        result = result + buckets[i]
             
    return result
 
 
Arr = [5, 0, 2, 7, 8, 55, -2, 111, 4, 5, 1, 2]
print(bucketSort(Arr))
