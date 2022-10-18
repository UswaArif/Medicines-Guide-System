def SelectionSort(array, start, end):
    for i in range(start, end):
        min = i
        for j in range(i + 1, end):
            if array[min] > array[j]:
                min = j
        temp = array[i]
        array[i] = array[min]
        array[min] = temp
    Arr = []
    for i in range(start, end):
        Arr.append(array[i])
    return Arr