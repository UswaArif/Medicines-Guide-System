#Radix Sorting Ascending Function
def RadixCountingSort(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description,n):
        maxNum = max(OldpriceInt)
        arrayLen = maxNum + 1
        
        arrayOld = [0 for x in range(arrayLen)] 

        result = [0 for x in range(len(MedicineName))] 
        resultOld = [0 for x in range(len(OldpriceInt))] 
        resultNew = [0 for x in range(len(NewPriceInt))] 
        resultQ = [0 for x in range(len(Quantity))] 
        resultS = [0 for x in range(len(Stars))] 
        resultR = [0 for x in range(len(RatingInt))] 
        resultDis = [0 for x in range(len(Discount))] 
        resultDescript = [0 for x in range(len(Description))] 

        for i in OldpriceInt: 
            temp = i // n
            arrayOld[temp % 10] += 1
        for i in range(1, maxNum + 1):
            arrayOld[i] = arrayOld[i] + arrayOld[i-1] 
        i = len(OldpriceInt) - 1
        while i >= 0:
            temp = OldpriceInt[i] // n
            resultOld[arrayOld[temp % 10]-1] = OldpriceInt[i]
            result[arrayOld[temp % 10]-1] = MedicineName[i]
            resultNew[arrayOld[temp % 10]-1] = NewPriceInt[i]
            resultQ[arrayOld[temp % 10]-1] = Quantity[i]
            resultS[arrayOld[temp % 10]-1] = Stars[i]
            resultR[arrayOld[temp % 10]-1] = RatingInt[i]
            resultDis[arrayOld[temp % 10]-1] = Discount[i]
            resultDescript[arrayOld[temp % 10]-1] = Description[i]
            arrayOld[temp % 10] -= 1
            i -= 1
        return result,resultOld,resultNew,resultQ,resultS,resultR,resultDis,resultDescript

         
def RadixSortAscending(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description):
    MaxNum = max(OldpriceInt)
    d = 1
    while int(MaxNum / d) > 0:
        MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description = RadixCountingSort(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description,d)
        d = d * 10
    return MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description





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