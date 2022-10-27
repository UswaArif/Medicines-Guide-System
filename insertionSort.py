def InsertionSort(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description):
    for i in range(0, len(MedicineName)):
        Key = MedicineName[i]
        KeyOld = OldpriceInt[i]
        KeyNew = NewPriceInt[i]
        KeyQ = Quantity[i]
        KeyS = Stars[i]
        KeyR = RatingInt[i]
        KeyDis = Discount[i]
        KeyDescript = Description[i]

        j = i - 1 
        while(Key < MedicineName[j] and j  >= 0):
            MedicineName[j + 1] = MedicineName[j]
            OldpriceInt[j + 1] = OldpriceInt[j]
            NewPriceInt[j + 1] = NewPriceInt[j]
            Quantity[j + 1] = Quantity[j]
            Stars[j + 1] = Stars[j]
            RatingInt[j + 1] = RatingInt[j]
            Discount[j + 1] = Discount[j]
            Description[j + 1] = Description[j]
            j = j - 1
        MedicineName[j + 1] = Key 
        OldpriceInt[j + 1] = KeyOld
        NewPriceInt[j + 1] = KeyNew
        Quantity[j + 1] = KeyQ
        Stars[j + 1] = KeyS
        RatingInt[j + 1] = KeyR
        Discount[j + 1] = KeyDis
        Description[j + 1] =  KeyDescript

    return MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description

def InsertionSortOldprice(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description):
    for i in range(0,len(OldpriceInt)):
        Key = MedicineName[i]
        KeyOld = OldpriceInt[i]
        KeyNew = NewPriceInt[i]
        KeyQ = Quantity[i]
        KeyS = Stars[i]
        KeyR = RatingInt[i]
        KeyDis = Discount[i]
        KeyDescript = Description[i]

        j = i - 1 
        while(KeyOld < OldpriceInt[j] and j  >= 0):
            MedicineName[j + 1] = MedicineName[j]
            OldpriceInt[j + 1] = OldpriceInt[j]
            NewPriceInt[j + 1] = NewPriceInt[j]
            Quantity[j + 1] = Quantity[j]
            Stars[j + 1] = Stars[j]
            RatingInt[j + 1] = RatingInt[j]
            Discount[j + 1] = Discount[j]
            Description[j + 1] = Description[j]
            j = j - 1
        MedicineName[j + 1] = Key 
        OldpriceInt[j + 1] = KeyOld
        NewPriceInt[j + 1] = KeyNew
        Quantity[j + 1] = KeyQ
        Stars[j + 1] = KeyS
        RatingInt[j + 1] = KeyR
        Discount[j + 1] = KeyDis
        Description[j + 1] =  KeyDescript
    return MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description

def InsertionSortNewPrice(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description):
    for i in range(0,len(NewPriceInt)):
        Key = MedicineName[i]
        KeyOld = OldpriceInt[i]
        KeyNew = NewPriceInt[i]
        KeyQ = Quantity[i]
        KeyS = Stars[i]
        KeyR = RatingInt[i]
        KeyDis = Discount[i]
        KeyDescript = Description[i]

        j = i - 1 
        while(KeyNew < NewPriceInt[j] and j  >= 0):
            MedicineName[j + 1] = MedicineName[j]
            OldpriceInt[j + 1] = OldpriceInt[j]
            NewPriceInt[j + 1] = NewPriceInt[j]
            Quantity[j + 1] = Quantity[j]
            Stars[j + 1] = Stars[j]
            RatingInt[j + 1] = RatingInt[j]
            Discount[j + 1] = Discount[j]
            Description[j + 1] = Description[j]
            j = j - 1
        MedicineName[j + 1] = Key 
        OldpriceInt[j + 1] = KeyOld
        NewPriceInt[j + 1] = KeyNew
        Quantity[j + 1] = KeyQ
        Stars[j + 1] = KeyS
        RatingInt[j + 1] = KeyR
        Discount[j + 1] = KeyDis
        Description[j + 1] =  KeyDescript
    return MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description

def InsertionSortQuantity(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description):
    for i in range(0,len(Quantity)):
        Key = MedicineName[i]
        KeyOld = OldpriceInt[i]
        KeyNew = NewPriceInt[i]
        KeyQ = Quantity[i]
        KeyS = Stars[i]
        KeyR = RatingInt[i]
        KeyDis = Discount[i]
        KeyDescript = Description[i]

        j = i - 1 
        while(KeyQ < Quantity[j] and j  >= 0):
            MedicineName[j + 1] = MedicineName[j]
            OldpriceInt[j + 1] = OldpriceInt[j]
            NewPriceInt[j + 1] = NewPriceInt[j]
            Quantity[j + 1] = Quantity[j]
            Stars[j + 1] = Stars[j]
            RatingInt[j + 1] = RatingInt[j]
            Discount[j + 1] = Discount[j]
            Description[j + 1] = Description[j]
            j = j - 1
        MedicineName[j + 1] = Key 
        OldpriceInt[j + 1] = KeyOld
        NewPriceInt[j + 1] = KeyNew
        Quantity[j + 1] = KeyQ
        Stars[j + 1] = KeyS
        RatingInt[j + 1] = KeyR
        Discount[j + 1] = KeyDis
        Description[j + 1] =  KeyDescript
    return MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description

def InsertionSortStars(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description):
    for i in range(0,len(Stars)):
        Key = MedicineName[i]
        KeyOld = OldpriceInt[i]
        KeyNew = NewPriceInt[i]
        KeyQ = Quantity[i]
        KeyS = Stars[i]
        KeyR = RatingInt[i]
        KeyDis = Discount[i]
        KeyDescript = Description[i]

        j = i - 1 
        while(KeyS < Stars[j] and j  >= 0):
            MedicineName[j + 1] = MedicineName[j]
            OldpriceInt[j + 1] = OldpriceInt[j]
            NewPriceInt[j + 1] = NewPriceInt[j]
            Quantity[j + 1] = Quantity[j]
            Stars[j + 1] = Stars[j]
            RatingInt[j + 1] = RatingInt[j]
            Discount[j + 1] = Discount[j]
            Description[j + 1] = Description[j]
            j = j - 1
        MedicineName[j + 1] = Key 
        OldpriceInt[j + 1] = KeyOld
        NewPriceInt[j + 1] = KeyNew
        Quantity[j + 1] = KeyQ
        Stars[j + 1] = KeyS
        RatingInt[j + 1] = KeyR
        Discount[j + 1] = KeyDis
        Description[j + 1] =  KeyDescript
    return MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description

def InsertionSortRating(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description):
    for i in range(0,len(RatingInt)):
        Key = MedicineName[i]
        KeyOld = OldpriceInt[i]
        KeyNew = NewPriceInt[i]
        KeyQ = Quantity[i]
        KeyS = Stars[i]
        KeyR = RatingInt[i]
        KeyDis = Discount[i]
        KeyDescript = Description[i]

        j = i - 1 
        while(KeyR < RatingInt[j] and j  >= 0):
            MedicineName[j + 1] = MedicineName[j]
            OldpriceInt[j + 1] = OldpriceInt[j]
            NewPriceInt[j + 1] = NewPriceInt[j]
            Quantity[j + 1] = Quantity[j]
            Stars[j + 1] = Stars[j]
            RatingInt[j + 1] = RatingInt[j]
            Discount[j + 1] = Discount[j]
            Description[j + 1] = Description[j]
            j = j - 1
        MedicineName[j + 1] = Key 
        OldpriceInt[j + 1] = KeyOld
        NewPriceInt[j + 1] = KeyNew
        Quantity[j + 1] = KeyQ
        Stars[j + 1] = KeyS
        RatingInt[j + 1] = KeyR
        Discount[j + 1] = KeyDis
        Description[j + 1] =  KeyDescript
    return MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description

def InsertionSortDiscount(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description):
    for i in range(0,len(Discount)):
        Key = MedicineName[i]
        KeyOld = OldpriceInt[i]
        KeyNew = NewPriceInt[i]
        KeyQ = Quantity[i]
        KeyS = Stars[i]
        KeyR = RatingInt[i]
        KeyDis = Discount[i]
        KeyDescript = Description[i]

        j = i - 1 
        while(KeyDis < Discount[j] and j  >= 0):
            MedicineName[j + 1] = MedicineName[j]
            OldpriceInt[j + 1] = OldpriceInt[j]
            NewPriceInt[j + 1] = NewPriceInt[j]
            Quantity[j + 1] = Quantity[j]
            Stars[j + 1] = Stars[j]
            RatingInt[j + 1] = RatingInt[j]
            Discount[j + 1] = Discount[j]
            Description[j + 1] = Description[j]
            j = j - 1
        MedicineName[j + 1] = Key 
        OldpriceInt[j + 1] = KeyOld
        NewPriceInt[j + 1] = KeyNew
        Quantity[j + 1] = KeyQ
        Stars[j + 1] = KeyS
        RatingInt[j + 1] = KeyR
        Discount[j + 1] = KeyDis
        Description[j + 1] =  KeyDescript
    return MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description

def InsertionSortDescription(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description):
    for i in range(0,len(Description)):
        Key = MedicineName[i]
        KeyOld = OldpriceInt[i]
        KeyNew = NewPriceInt[i]
        KeyQ = Quantity[i]
        KeyS = Stars[i]
        KeyR = RatingInt[i]
        KeyDis = Discount[i]
        KeyDescript = Description[i]

        j = i - 1 
        while(KeyDescript < Description[j] and j  >= 0):
            MedicineName[j + 1] = MedicineName[j]
            OldpriceInt[j + 1] = OldpriceInt[j]
            NewPriceInt[j + 1] = NewPriceInt[j]
            Quantity[j + 1] = Quantity[j]
            Stars[j + 1] = Stars[j]
            RatingInt[j + 1] = RatingInt[j]
            Discount[j + 1] = Discount[j]
            Description[j + 1] = Description[j]
            j = j - 1
        MedicineName[j + 1] = Key 
        OldpriceInt[j + 1] = KeyOld
        NewPriceInt[j + 1] = KeyNew
        Quantity[j + 1] = KeyQ
        Stars[j + 1] = KeyS
        RatingInt[j + 1] = KeyR
        Discount[j + 1] = KeyDis
        Description[j + 1] =  KeyDescript
    return MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description

#Descending

def InsertionSortDescending(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description):
    for i in range(0, len(MedicineName)):
        Key = MedicineName[i]
        KeyOld = OldpriceInt[i]
        KeyNew = NewPriceInt[i]
        KeyQ = Quantity[i]
        KeyS = Stars[i]
        KeyR = RatingInt[i]
        KeyDis = Discount[i]
        KeyDescript = Description[i]

        j = i - 1 
        while(Key < MedicineName[j] and j  >= 0):
            MedicineName[j + 1] = MedicineName[j]
            OldpriceInt[j + 1] = OldpriceInt[j]
            NewPriceInt[j + 1] = NewPriceInt[j]
            Quantity[j + 1] = Quantity[j]
            Stars[j + 1] = Stars[j]
            RatingInt[j + 1] = RatingInt[j]
            Discount[j + 1] = Discount[j]
            Description[j + 1] = Description[j]
            j = j - 1
        MedicineName[j + 1] = Key 
        OldpriceInt[j + 1] = KeyOld
        NewPriceInt[j + 1] = KeyNew
        Quantity[j + 1] = KeyQ
        Stars[j + 1] = KeyS
        RatingInt[j + 1] = KeyR
        Discount[j + 1] = KeyDis
        Description[j + 1] =  KeyDescript

    MedicineName.reverse()
    OldpriceInt.reverse()
    NewPriceInt.reverse()
    Quantity.reverse()
    Stars.reverse()
    RatingInt.reverse()
    Discount.reverse()
    Description.reverse()
    return MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description


def InsertionSortOldpriceDescending(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description):
    for i in range(0,len(OldpriceInt)):
        Key = MedicineName[i]
        KeyOld = OldpriceInt[i]
        KeyNew = NewPriceInt[i]
        KeyQ = Quantity[i]
        KeyS = Stars[i]
        KeyR = RatingInt[i]
        KeyDis = Discount[i]
        KeyDescript = Description[i]

        j = i - 1 
        while(KeyOld < OldpriceInt[j] and j  >= 0):
            MedicineName[j + 1] = MedicineName[j]
            OldpriceInt[j + 1] = OldpriceInt[j]
            NewPriceInt[j + 1] = NewPriceInt[j]
            Quantity[j + 1] = Quantity[j]
            Stars[j + 1] = Stars[j]
            RatingInt[j + 1] = RatingInt[j]
            Discount[j + 1] = Discount[j]
            Description[j + 1] = Description[j]
            j = j - 1
        MedicineName[j + 1] = Key 
        OldpriceInt[j + 1] = KeyOld
        NewPriceInt[j + 1] = KeyNew
        Quantity[j + 1] = KeyQ
        Stars[j + 1] = KeyS
        RatingInt[j + 1] = KeyR
        Discount[j + 1] = KeyDis
        Description[j + 1] =  KeyDescript

    MedicineName.reverse()
    OldpriceInt.reverse()
    NewPriceInt.reverse()
    Quantity.reverse()
    Stars.reverse()
    RatingInt.reverse()
    Discount.reverse()
    Description.reverse()
    return MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description

def InsertionSortNewPriceDescending(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description):
    for i in range(0,len(NewPriceInt)):
        Key = MedicineName[i]
        KeyOld = OldpriceInt[i]
        KeyNew = NewPriceInt[i]
        KeyQ = Quantity[i]
        KeyS = Stars[i]
        KeyR = RatingInt[i]
        KeyDis = Discount[i]
        KeyDescript = Description[i]

        j = i - 1 
        while(KeyNew < NewPriceInt[j] and j  >= 0):
            MedicineName[j + 1] = MedicineName[j]
            OldpriceInt[j + 1] = OldpriceInt[j]
            NewPriceInt[j + 1] = NewPriceInt[j]
            Quantity[j + 1] = Quantity[j]
            Stars[j + 1] = Stars[j]
            RatingInt[j + 1] = RatingInt[j]
            Discount[j + 1] = Discount[j]
            Description[j + 1] = Description[j]
            j = j - 1
        MedicineName[j + 1] = Key 
        OldpriceInt[j + 1] = KeyOld
        NewPriceInt[j + 1] = KeyNew
        Quantity[j + 1] = KeyQ
        Stars[j + 1] = KeyS
        RatingInt[j + 1] = KeyR
        Discount[j + 1] = KeyDis
        Description[j + 1] =  KeyDescript

    MedicineName.reverse()
    OldpriceInt.reverse()
    NewPriceInt.reverse()
    Quantity.reverse()
    Stars.reverse()
    RatingInt.reverse()
    Discount.reverse()
    Description.reverse()
    return MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description

def InsertionSortQuantityDescending(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description):
    for i in range(0,len(Quantity)):
        Key = MedicineName[i]
        KeyOld = OldpriceInt[i]
        KeyNew = NewPriceInt[i]
        KeyQ = Quantity[i]
        KeyS = Stars[i]
        KeyR = RatingInt[i]
        KeyDis = Discount[i]
        KeyDescript = Description[i]

        j = i - 1 
        while(KeyQ < Quantity[j] and j  >= 0):
            MedicineName[j + 1] = MedicineName[j]
            OldpriceInt[j + 1] = OldpriceInt[j]
            NewPriceInt[j + 1] = NewPriceInt[j]
            Quantity[j + 1] = Quantity[j]
            Stars[j + 1] = Stars[j]
            RatingInt[j + 1] = RatingInt[j]
            Discount[j + 1] = Discount[j]
            Description[j + 1] = Description[j]
            j = j - 1
        MedicineName[j + 1] = Key 
        OldpriceInt[j + 1] = KeyOld
        NewPriceInt[j + 1] = KeyNew
        Quantity[j + 1] = KeyQ
        Stars[j + 1] = KeyS
        RatingInt[j + 1] = KeyR
        Discount[j + 1] = KeyDis
        Description[j + 1] =  KeyDescript
    
    MedicineName.reverse()
    OldpriceInt.reverse()
    NewPriceInt.reverse()
    Quantity.reverse()
    Stars.reverse()
    RatingInt.reverse()
    Discount.reverse()
    Description.reverse()
    return MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description

def InsertionSortStarsDescending(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description):
    for i in range(0,len(Stars)):
        Key = MedicineName[i]
        KeyOld = OldpriceInt[i]
        KeyNew = NewPriceInt[i]
        KeyQ = Quantity[i]
        KeyS = Stars[i]
        KeyR = RatingInt[i]
        KeyDis = Discount[i]
        KeyDescript = Description[i]

        j = i - 1 
        while(KeyS < Stars[j] and j  >= 0):
            MedicineName[j + 1] = MedicineName[j]
            OldpriceInt[j + 1] = OldpriceInt[j]
            NewPriceInt[j + 1] = NewPriceInt[j]
            Quantity[j + 1] = Quantity[j]
            Stars[j + 1] = Stars[j]
            RatingInt[j + 1] = RatingInt[j]
            Discount[j + 1] = Discount[j]
            Description[j + 1] = Description[j]
            j = j - 1
        MedicineName[j + 1] = Key 
        OldpriceInt[j + 1] = KeyOld
        NewPriceInt[j + 1] = KeyNew
        Quantity[j + 1] = KeyQ
        Stars[j + 1] = KeyS
        RatingInt[j + 1] = KeyR
        Discount[j + 1] = KeyDis
        Description[j + 1] =  KeyDescript
    
    MedicineName.reverse()
    OldpriceInt.reverse()
    NewPriceInt.reverse()
    Quantity.reverse()
    Stars.reverse()
    RatingInt.reverse()
    Discount.reverse()
    Description.reverse()
    return MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description

def InsertionSortRatingDescending(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description):
    for i in range(0,len(RatingInt)):
        Key = MedicineName[i]
        KeyOld = OldpriceInt[i]
        KeyNew = NewPriceInt[i]
        KeyQ = Quantity[i]
        KeyS = Stars[i]
        KeyR = RatingInt[i]
        KeyDis = Discount[i]
        KeyDescript = Description[i]

        j = i - 1 
        while(KeyR < RatingInt[j] and j  >= 0):
            MedicineName[j + 1] = MedicineName[j]
            OldpriceInt[j + 1] = OldpriceInt[j]
            NewPriceInt[j + 1] = NewPriceInt[j]
            Quantity[j + 1] = Quantity[j]
            Stars[j + 1] = Stars[j]
            RatingInt[j + 1] = RatingInt[j]
            Discount[j + 1] = Discount[j]
            Description[j + 1] = Description[j]
            j = j - 1
        MedicineName[j + 1] = Key 
        OldpriceInt[j + 1] = KeyOld
        NewPriceInt[j + 1] = KeyNew
        Quantity[j + 1] = KeyQ
        Stars[j + 1] = KeyS
        RatingInt[j + 1] = KeyR
        Discount[j + 1] = KeyDis
        Description[j + 1] =  KeyDescript

    MedicineName.reverse()
    OldpriceInt.reverse()
    NewPriceInt.reverse()
    Quantity.reverse()
    Stars.reverse()
    RatingInt.reverse()
    Discount.reverse()
    Description.reverse()
    return MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description

def InsertionSortDiscountDescending(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description):
    for i in range(0,len(Discount)):
        Key = MedicineName[i]
        KeyOld = OldpriceInt[i]
        KeyNew = NewPriceInt[i]
        KeyQ = Quantity[i]
        KeyS = Stars[i]
        KeyR = RatingInt[i]
        KeyDis = Discount[i]
        KeyDescript = Description[i]

        j = i - 1 
        while(KeyDis < Discount[j] and j  >= 0):
            MedicineName[j + 1] = MedicineName[j]
            OldpriceInt[j + 1] = OldpriceInt[j]
            NewPriceInt[j + 1] = NewPriceInt[j]
            Quantity[j + 1] = Quantity[j]
            Stars[j + 1] = Stars[j]
            RatingInt[j + 1] = RatingInt[j]
            Discount[j + 1] = Discount[j]
            Description[j + 1] = Description[j]
            j = j - 1
        MedicineName[j + 1] = Key 
        OldpriceInt[j + 1] = KeyOld
        NewPriceInt[j + 1] = KeyNew
        Quantity[j + 1] = KeyQ
        Stars[j + 1] = KeyS
        RatingInt[j + 1] = KeyR
        Discount[j + 1] = KeyDis
        Description[j + 1] =  KeyDescript

    MedicineName.reverse()
    OldpriceInt.reverse()
    NewPriceInt.reverse()
    Quantity.reverse()
    Stars.reverse()
    RatingInt.reverse()
    Discount.reverse()
    Description.reverse()
    return MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description

def InsertionSortDescriptionDescending(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description):
    for i in range(0,len(Description)):
        Key = MedicineName[i]
        KeyOld = OldpriceInt[i]
        KeyNew = NewPriceInt[i]
        KeyQ = Quantity[i]
        KeyS = Stars[i]
        KeyR = RatingInt[i]
        KeyDis = Discount[i]
        KeyDescript = Description[i]

        j = i - 1 
        while(KeyDescript < Description[j] and j  >= 0):
            MedicineName[j + 1] = MedicineName[j]
            OldpriceInt[j + 1] = OldpriceInt[j]
            NewPriceInt[j + 1] = NewPriceInt[j]
            Quantity[j + 1] = Quantity[j]
            Stars[j + 1] = Stars[j]
            RatingInt[j + 1] = RatingInt[j]
            Discount[j + 1] = Discount[j]
            Description[j + 1] = Description[j]
            j = j - 1
        MedicineName[j + 1] = Key 
        OldpriceInt[j + 1] = KeyOld
        NewPriceInt[j + 1] = KeyNew
        Quantity[j + 1] = KeyQ
        Stars[j + 1] = KeyS
        RatingInt[j + 1] = KeyR
        Discount[j + 1] = KeyDis
        Description[j + 1] =  KeyDescript

    MedicineName.reverse()
    OldpriceInt.reverse()
    NewPriceInt.reverse()
    Quantity.reverse()
    Stars.reverse()
    RatingInt.reverse()
    Discount.reverse()
    Description.reverse()
    return MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description


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