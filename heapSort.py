def MaxHeapify(arr, n, i):
    l = 2 * i 
    r = 2 * i + 1
 
    if l < n and arr[l] > arr[i]:
        largest = l
    else:
        largest = i

    if r < n and arr[r] > arr[largest]:
        largest = r
 
    if largest != i:
        (arr[i], arr[largest]) = (arr[largest], arr[i]) 
        MaxHeapify(arr, n, largest)
 
def heapSort(arr):
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        MaxHeapify(arr, n, i)
 
    for i in range(n - 1, 0, -1):
        (arr[i], arr[0]) = (arr[0], arr[i]) 
        MaxHeapify(arr, i, 0)
 

Arr = [2,43,2,4,6,1,9,4,6,0]
print(heapSort(Arr))