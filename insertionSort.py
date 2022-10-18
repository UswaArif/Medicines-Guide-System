def InsertionSort(array, start, end):
    Arr = []
    for i in range(start, end):
        key = array[i]
        j = i - 1
        while key < array[j] and j >= 0:
            array[j + 1] = array[j]
            j = j - 1
        array[j + 1] = key    
    for i in range(start, end):
        Arr.append(array[i])
    return Arr




