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

def RadixCountingSortNewPrice(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description,n):
        maxNum = max(NewPriceInt)
        arrayLen = maxNum + 1
        
        arrayNew = [0 for x in range(arrayLen)] 

        result = [0 for x in range(len(MedicineName))] 
        resultOld = [0 for x in range(len(OldpriceInt))] 
        resultNew = [0 for x in range(len(NewPriceInt))] 
        resultQ = [0 for x in range(len(Quantity))] 
        resultS = [0 for x in range(len(Stars))] 
        resultR = [0 for x in range(len(RatingInt))] 
        resultDis = [0 for x in range(len(Discount))] 
        resultDescript = [0 for x in range(len(Description))] 

        for i in NewPriceInt: 
            temp = i // n
            arrayNew[temp % 10] += 1
        for i in range(1, maxNum + 1):
            arrayNew[i] = arrayNew[i] + arrayNew[i-1] 
        i = len(NewPriceInt) - 1
        while i >= 0:
            temp = NewPriceInt[i] // n
            resultOld[arrayNew[temp % 10]-1] = OldpriceInt[i]
            result[arrayNew[temp % 10]-1] = MedicineName[i]
            resultNew[arrayNew[temp % 10]-1] = NewPriceInt[i]
            resultQ[arrayNew[temp % 10]-1] = Quantity[i]
            resultS[arrayNew[temp % 10]-1] = Stars[i]
            resultR[arrayNew[temp % 10]-1] = RatingInt[i]
            resultDis[arrayNew[temp % 10]-1] = Discount[i]
            resultDescript[arrayNew[temp % 10]-1] = Description[i]
            arrayNew[temp % 10] -= 1
            i -= 1
        return result,resultOld,resultNew,resultQ,resultS,resultR,resultDis,resultDescript

         
def RadixSortAscendingNewPrice(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description):
    MaxNum = max(NewPriceInt)
    d = 1
    while int(MaxNum / d) > 0:
        MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description = RadixCountingSortNewPrice(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description,d)
        d = d * 10
    return MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description

def RadixCountingSortRating(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description,n):
        maxNum = max(RatingInt)
        arrayLen = maxNum + 1
        
        arrayR = [0 for x in range(arrayLen)] 

        result = [0 for x in range(len(MedicineName))] 
        resultOld = [0 for x in range(len(OldpriceInt))] 
        resultNew = [0 for x in range(len(NewPriceInt))] 
        resultQ = [0 for x in range(len(Quantity))] 
        resultS = [0 for x in range(len(Stars))] 
        resultR = [0 for x in range(len(RatingInt))] 
        resultDis = [0 for x in range(len(Discount))] 
        resultDescript = [0 for x in range(len(Description))] 

        for i in RatingInt: 
            temp = i // n
            arrayR[temp % 10] += 1
        for i in range(1, maxNum + 1):
            arrayR[i] = arrayR[i] + arrayR[i-1] 
        i = len(RatingInt) - 1
        while i >= 0:
            temp = RatingInt[i] // n
            resultOld[arrayR[temp % 10]-1] = OldpriceInt[i]
            result[arrayR[temp % 10]-1] = MedicineName[i]
            resultNew[arrayR[temp % 10]-1] = NewPriceInt[i]
            resultQ[arrayR[temp % 10]-1] = Quantity[i]
            resultS[arrayR[temp % 10]-1] = Stars[i]
            resultR[arrayR[temp % 10]-1] = RatingInt[i]
            resultDis[arrayR[temp % 10]-1] = Discount[i]
            resultDescript[arrayR[temp % 10]-1] = Description[i]
            arrayR[temp % 10] -= 1
            i -= 1
        return result,resultOld,resultNew,resultQ,resultS,resultR,resultDis,resultDescript

         
def RadixSortAscendingRating(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description):
    MaxNum = max(RatingInt)
    d = 1
    while int(MaxNum / d) > 0:
        MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description = RadixCountingSortRating(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description,d)
        d = d * 10
    return MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description

#Radix Sorting Descending Function
def RadixCountingSortDescending(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description,n):
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

         
def RadixSortDescending(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description):
    MaxNum = max(OldpriceInt)
    d = 1
    while int(MaxNum / d) > 0:
        MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description = RadixCountingSortDescending(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description,d)
        d = d * 10
    MedicineName.reverse()
    OldpriceInt.reverse()
    NewPriceInt.reverse()
    Quantity.reverse()
    Stars.reverse()
    RatingInt.reverse()
    Discount.reverse()
    Description.reverse()
    return MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description

def RadixCountingSortNewPriceDescending(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description,n):
        maxNum = max(NewPriceInt)
        arrayLen = maxNum + 1
        
        arrayNew = [0 for x in range(arrayLen)] 

        result = [0 for x in range(len(MedicineName))] 
        resultOld = [0 for x in range(len(OldpriceInt))] 
        resultNew = [0 for x in range(len(NewPriceInt))] 
        resultQ = [0 for x in range(len(Quantity))] 
        resultS = [0 for x in range(len(Stars))] 
        resultR = [0 for x in range(len(RatingInt))] 
        resultDis = [0 for x in range(len(Discount))] 
        resultDescript = [0 for x in range(len(Description))] 

        for i in NewPriceInt: 
            temp = i // n
            arrayNew[temp % 10] += 1
        for i in range(1, maxNum + 1):
            arrayNew[i] = arrayNew[i] + arrayNew[i-1] 
        i = len(NewPriceInt) - 1
        while i >= 0:
            temp = NewPriceInt[i] // n
            resultOld[arrayNew[temp % 10]-1] = OldpriceInt[i]
            result[arrayNew[temp % 10]-1] = MedicineName[i]
            resultNew[arrayNew[temp % 10]-1] = NewPriceInt[i]
            resultQ[arrayNew[temp % 10]-1] = Quantity[i]
            resultS[arrayNew[temp % 10]-1] = Stars[i]
            resultR[arrayNew[temp % 10]-1] = RatingInt[i]
            resultDis[arrayNew[temp % 10]-1] = Discount[i]
            resultDescript[arrayNew[temp % 10]-1] = Description[i]
            arrayNew[temp % 10] -= 1
            i -= 1
        return result,resultOld,resultNew,resultQ,resultS,resultR,resultDis,resultDescript

         
def RadixSortDescendingNewPrice(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description):
    MaxNum = max(NewPriceInt)
    d = 1
    while int(MaxNum / d) > 0:
        MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description = RadixCountingSortNewPriceDescending(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description,d)
        d = d * 10
    MedicineName.reverse()
    OldpriceInt.reverse()
    NewPriceInt.reverse()
    Quantity.reverse()
    Stars.reverse()
    RatingInt.reverse()
    Discount.reverse()
    Description.reverse()
    return MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description

def RadixCountingSortRatingDescending(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description,n):
        maxNum = max(RatingInt)
        arrayLen = maxNum + 1
        
        arrayR = [0 for x in range(arrayLen)] 

        result = [0 for x in range(len(MedicineName))] 
        resultOld = [0 for x in range(len(OldpriceInt))] 
        resultNew = [0 for x in range(len(NewPriceInt))] 
        resultQ = [0 for x in range(len(Quantity))] 
        resultS = [0 for x in range(len(Stars))] 
        resultR = [0 for x in range(len(RatingInt))] 
        resultDis = [0 for x in range(len(Discount))] 
        resultDescript = [0 for x in range(len(Description))] 

        for i in RatingInt: 
            temp = i // n
            arrayR[temp % 10] += 1
        for i in range(1, maxNum + 1):
            arrayR[i] = arrayR[i] + arrayR[i-1] 
        i = len(RatingInt) - 1
        while i >= 0:
            temp = RatingInt[i] // n
            resultOld[arrayR[temp % 10]-1] = OldpriceInt[i]
            result[arrayR[temp % 10]-1] = MedicineName[i]
            resultNew[arrayR[temp % 10]-1] = NewPriceInt[i]
            resultQ[arrayR[temp % 10]-1] = Quantity[i]
            resultS[arrayR[temp % 10]-1] = Stars[i]
            resultR[arrayR[temp % 10]-1] = RatingInt[i]
            resultDis[arrayR[temp % 10]-1] = Discount[i]
            resultDescript[arrayR[temp % 10]-1] = Description[i]
            arrayR[temp % 10] -= 1
            i -= 1
        return result,resultOld,resultNew,resultQ,resultS,resultR,resultDis,resultDescript

         
def RadixSortDescendingRating(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description):
    MaxNum = max(RatingInt)
    d = 1
    while int(MaxNum / d) > 0:
        MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description = RadixCountingSortRatingDescending(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description,d)
        d = d * 10
    MedicineName.reverse()
    OldpriceInt.reverse()
    NewPriceInt.reverse()
    Quantity.reverse()
    Stars.reverse()
    RatingInt.reverse()
    Discount.reverse()
    Description.reverse()
    return MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description


