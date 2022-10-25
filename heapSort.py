def maxHeapify(array, n, i):
    largest = i  
    left = 2 * i   
    right = 2 * i + 1  

    if left < n and array[i] < array[left]:
        largest = left
    else:
        largest = i
 
    if right < n and array[largest] < array[right]:
        largest = right
  
    if largest != i:
        (array[i], array[largest]) = (array[largest], array[i]) 

        maxHeapify(array, n, largest)

def buildMaxHeap(array):
    n = len(array)
    for i in range(n // 2 - 1, -1, -1):
        maxHeapify(array, n, i)

def heapSort(array):
    n = len(array)
    buildMaxHeap(array)
    for i in range(n - 1, 0, -1):
        (array[i], array[0]) = (array[0], array[i])  
        maxHeapify(array, i, 0)
    return array
 

def heapSortDescending(array):
    n = len(array)
    buildMaxHeap(array)
    for i in range(n - 1, 0, -1):
        (array[i], array[0]) = (array[0], array[i])  
        maxHeapify(array, i, 0)
    array.reverse()
    return array