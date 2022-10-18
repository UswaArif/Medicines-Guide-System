def BubbleSort(array, start, end):
    for i in range(start, end):
        for j in range(i + 1, end):
            if array[i] > array[j]:
                temp = array[i]
                array[i] = array[j]
                array[j] = temp
    Arr = []
    for i in range(start, end):
        Arr.append(array[i])
    return Arr
