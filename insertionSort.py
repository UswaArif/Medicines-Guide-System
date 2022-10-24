def InsertionSort(array):                    # sort in ascending
    for i in range(1, len(array)):
        key = array[i]
        j = i - 1
        while key < array[j] and j >= 0:
            array[j + 1] = array[j]
            j = j - 1
        array[j + 1] = key    
    return array


def InsertionSortDescending(array):         # sort in descending
    for i in range(1, len(array)):
        key = array[i]
        j = i - 1
        while key < array[j] and j >= 0:
            array[j + 1] = array[j]
            j = j - 1
        array[j + 1] = key    
    array.reverse()
    return array