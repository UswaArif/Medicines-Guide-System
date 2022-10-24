def BubbleSort(array):
    for i in range(0, len(array)):
        for j in range(i + 1, len(array)):
            if array[i] > array[j]:
                temp = array[i]
                array[i] = array[j]
                array[j] = temp
    return array


def BubbleSortDescending(array):
    for i in range(0, len(array)):
        for j in range(i + 1, len(array)):
            if array[i] > array[j]:
                temp = array[i]
                array[i] = array[j]
                array[j] = temp
    array.reverse()
    return array