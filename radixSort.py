def RadixCountingSort(A,n):
        maxNum = max(A)
        arrayLen = maxNum + 1
        array = [0 for x in range(arrayLen)] 
        result = [0 for x in range(len(A))] 
        for i in A: 
            temp = i // n
            array[temp % 10] += 1
        for i in range(1, maxNum + 1):
            array[i] = array[i] + array[i-1] 
        i = len(A) - 1
        while i >= 0:
            temp = A[i] // n
            result[array[temp % 10]-1] = A[i]
            array[temp % 10] -= 1
            i -= 1
        return result

         
def RadixSort(A):
    MaxNum = max(A)
    d = 1
    while int(MaxNum / d) > 0:
        A = RadixCountingSort(A,d)
        d = d * 10
    return A


def RadixSortDescending(A):
    MaxNum = max(A)
    d = 1
    while int(MaxNum / d) > 0:
        A = RadixCountingSort(A,d)
        d = d * 10
    A.reverse()
    return A