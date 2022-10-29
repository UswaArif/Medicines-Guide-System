#Counting Sort Ascending Function

def countingSortOldpriceAscending(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description):
    maxNum = max(OldpriceInt)
    
    arrayLen = maxNum + 1

    array = [0 for x in range(arrayLen)]
    arrayOld = [0 for x in range(arrayLen)]
    arrayNew = [0 for x in range(arrayLen)]
    arrayQ = [0 for x in range(arrayLen)]
    arrayS = [0 for x in range(arrayLen)]
    arrayR = [0 for x in range(arrayLen)]
    arrayDis = [0 for x in range(arrayLen)]
    arrayDescript = [0 for x in range(arrayLen)]
    
    result = [0 for x in range(len(MedicineName))]
    resultOld = [0 for x in range(len(OldpriceInt))]
    resultNew = [0 for x in range(len(NewPriceInt))]
    resultQ = [0 for x in range(len(Quantity))]
    resultS = [0 for x in range(len(Stars))]
    resultR = [0 for x in range(len(RatingInt))]
    resultDis = [0 for x in range(len(Discount))]
    resultDescript = [0 for x in range(len(Description))]
 
    for i in MedicineName: 
        array[i] = array[i] + 1
    for i in OldpriceInt: 
        arrayOld[i] = arrayOld[i] + 1
    for i in NewPriceInt: 
        arrayNew[i] = arrayNew[i] + 1
    for i in Quantity: 
        arrayQ[i] = arrayQ[i] + 1
    for i in Stars: 
        arrayS[i] = arrayS[i] + 1
    for i in RatingInt: 
        arrayR[i] = arrayR[i] + 1
    for i in Discount: 
        arrayDis[i] = arrayDis[i] + 1
    for i in Description: 
        arrayDescript[i] = arrayDescript[i] + 1

    for i in range(1, maxNum + 1):
        array[i] = array[i] + array[i-1] 
        arrayOld[i] = arrayOld[i] + 1
        arrayNew[i] = arrayNew[i] + 1
        arrayQ[i] = arrayQ[i] + 1
        arrayS[i] = arrayS[i] + 1
        arrayR[i] = arrayR[i] + 1
        arrayDis[i] = arrayDis[i] + 1
        arrayDescript[i] = arrayDescript[i] + 1
    i = len(OldpriceInt) - 1
    while i >= 0:
        result[array[MedicineName[i]]-1] = MedicineName[i]
        array[MedicineName[i]] = array[MedicineName[i]]-1

        resultOld[arrayOld[OldpriceInt[i]]-1] = OldpriceInt[i]
        arrayOld[OldpriceInt[i]] = arrayOld[OldpriceInt[i]]-1

        resultNew[arrayNew[NewPriceInt[i]]-1] = NewPriceInt[i]
        arrayNew[NewPriceInt[i]] = arrayNew[NewPriceInt[i]]-1

        resultQ[arrayQ[Quantity[i]]-1] = Quantity[i]
        arrayQ[Quantity[i]] = arrayQ[Quantity[i]]-1

        resultS[arrayS[Stars[i]]-1] = Stars[i]
        arrayS[Stars[i]] = arrayS[Stars[i]]-1

        resultR[arrayR[RatingInt[i]]-1] = RatingInt[i]
        arrayR[RatingInt[i]] = arrayR[RatingInt[i]]-1

        resultDis[arrayDis[Discount[i]]-1] = Discount[i]
        arrayDis[Discount[i]] = arrayDis[Discount[i]]-1

        resultDescript[arrayDescript[Description[i]]-1] = Description[i]
        arrayDescript[Description[i]] = arrayDescript[Description[i]]-1
        i = i - 1

    return result,resultOld,resultNew,resultQ,resultS,resultR,resultDis,resultDescript

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