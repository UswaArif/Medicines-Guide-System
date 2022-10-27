def InsertionSort(MedicineName,OldpriceInt,NewPriceInt,Quantity,Starsfloat,RatingInt,Discount,Description):
    for i in range(0, len(MedicineName)):
        Key = MedicineName[i]
        KeyOld = OldpriceInt[i]
        KeyNew = NewPriceInt[i]
        KeyQ = Quantity[i]
        KeyS = Starsfloat[i]
        KeyR = RatingInt[i]
        KeyDis = Discount[i]
        KeyDescript = Description[i]

        j = i - 1 
        while(Key < MedicineName[j] and j  >= 0):
            MedicineName[j + 1] = MedicineName[j]
            OldpriceInt[j + 1] = OldpriceInt[j]
            NewPriceInt[j + 1] = NewPriceInt[j]
            Quantity[j + 1] = Quantity[j]
            Starsfloat[j + 1] = Starsfloat[j]
            RatingInt[j + 1] = RatingInt[j]
            Discount[j + 1] = Discount[j]
            Description[j + 1] = Description[j]
            j = j - 1
        MedicineName[j + 1] = Key 
        OldpriceInt[j + 1] = KeyOld
        NewPriceInt[j + 1] = KeyNew
        Quantity[j + 1] = KeyQ
        Starsfloat[j + 1] = KeyS
        RatingInt[j + 1] = KeyR
        Discount[j + 1] = KeyDis
        Description[j + 1] =  KeyDescript
    return MedicineName,OldpriceInt,NewPriceInt,Quantity,Starsfloat,RatingInt,Discount,Description

def InsertionSortOldprice(MedicineName,OldpriceInt,NewPriceInt,Quantity,Starsfloat,RatingInt,Discount,Description):
    for i in range(0,OldpriceInt):
        Key = MedicineName[i]
        KeyOld = OldpriceInt[i]
        KeyNew = NewPriceInt[i]
        KeyQ = Quantity[i]
        KeyS = Starsfloat[i]
        KeyR = RatingInt[i]
        KeyDis = Discount[i]
        KeyDescript = Description[i]

        j = i - 1 
        while(KeyOld < OldpriceInt[j] and j  >= 0):
            MedicineName[j + 1] = MedicineName[j]
            OldpriceInt[j + 1] = OldpriceInt[j]
            NewPriceInt[j + 1] = NewPriceInt[j]
            Quantity[j + 1] = Quantity[j]
            Starsfloat[j + 1] = Starsfloat[j]
            RatingInt[j + 1] = RatingInt[j]
            Discount[j + 1] = Discount[j]
            Description[j + 1] = Description[j]
            j = j - 1
        MedicineName[j + 1] = Key 
        OldpriceInt[j + 1] = KeyOld
        NewPriceInt[j + 1] = KeyNew
        Quantity[j + 1] = KeyQ
        Starsfloat[j + 1] = KeyS
        RatingInt[j + 1] = KeyR
        Discount[j + 1] = KeyDis
        Description[j + 1] =  KeyDescript
    return MedicineName,OldpriceInt,NewPriceInt,Quantity,Starsfloat,RatingInt,Discount,Description


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