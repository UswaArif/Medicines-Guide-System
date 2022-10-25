def Partition(array, left, right):
    i = left
    j = right-1 
    pivot = array[right]
    while i < j:
        while i < right and array[i] < pivot:  
            i += 1
        while j > left and array[j] >= pivot:  
            j -= 1
        if i < j:
            [array[i],array[j]] = [array[j],array[i]]
    if array[i] > pivot:
        [array[i],array[right]] = [array[right],array[i]]
    return i

def QuickSort(array, left, right):
    if left < right:
        part = Partition(array, left, right)
        QuickSort(array, left, part - 1)
        QuickSort(array, part + 1, right)
        return array



def QuickSortDescending(array, left, right):
    if left < right:
        part = Partition(array, left, right)
        QuickSort(array, left, part - 1)
        QuickSort(array, part + 1, right)
    array.reverse()
    return array