def countingSort(A):
    maxNum = max(A)
    arrayLen = maxNum + 1
    array = [0 for x in range(arrayLen)]
    result = [0 for x in range(len(A))]
    for i in A: 
        array[i] = array[i] + 1
    for i in range(1, maxNum + 1):
        array[i] = array[i] + array[i-1] 
    i = len(A) - 1
    while i >= 0:
        result[array[A[i]]-1] = A[i]
        array[A[i]] = array[A[i]]-1
        i = i - 1
    return result


def countingSortDescending(A):
    maxNum = max(A)
    arrayLen = maxNum + 1
    array = [0 for x in range(arrayLen)]
    result = [0 for x in range(len(A))]
    for i in A: 
        array[i] = array[i] + 1
    for i in range(1, maxNum + 1):
        array[i] = array[i] + array[i-1] 
    i = len(A) - 1
    while i >= 0:
        result[array[A[i]]-1] = A[i]
        array[A[i]] = array[A[i]]-1
        i = i - 1
    result.reverse()
    return result