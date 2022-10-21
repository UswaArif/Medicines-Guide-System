def MergeSort(array, start, end):
    if start < end:
        q = (start + end) // 2
        MergeSort(array, start, q)
        MergeSort(array, q + 1, end)
        Merge(array, start, q, end)
        return array

def Merge(array, p, q, r):
    n1 = q - p + 1
    n2 = r - q
    L = []
    R = []
    for i in range(0, n1):
        L.append(array[p + i])
    for j in range(0, n2):
        R.append(array[q + 1 + j])
    i = 0
    j = 0
    k = p
    while i < n1 and j < n2:
        if(L[i] <= R[j]):
            array[k] = L[i]
            i += 1
        else:
            array[k] = R[j]
            j += 1
        k += 1
    if i == len(L):
        while j < n2:
            array[k] = R[j]
            j += 1
            k += 1
    else:
        while i < len(L):
            array[k] = L[i]
            i += 1
            k += 1


A = [2,1,4,67,45,5,7]
print(MergeSort(A,0,len(A)-1))