#Shell Sort Ascending Functions

def shellSortAscending(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description):
    n = len(MedicineName)
    # Rearrange elements at each n/2, n/4, n/8, ... intervals
    interval = n // 2
    while interval > 0:
        for i in range(interval,n,1):
            temp = MedicineName[i]
            tempOld = OldpriceInt[i]
            tempNew = NewPriceInt[i]
            tempQ = Quantity[i]
            tempS = Stars[i]
            tempR = RatingInt[i]
            tempDis = Discount[i]
            tempDescript = Description[i]
            j = i
            while j >= interval and MedicineName[j - interval] > temp:
                MedicineName[j] = MedicineName[j - interval]
                OldpriceInt[j] = OldpriceInt[j - interval]
                NewPriceInt[j] = NewPriceInt[j - interval]
                Quantity[j] = Quantity[j - interval]
                Stars[j] = Stars[j - interval]
                RatingInt[j] = RatingInt[j - interval]
                Discount[j] = Discount[j - interval]
                Description[j] = Description[j - interval]

                j = j - interval
            MedicineName[j] = temp
            OldpriceInt[j] = tempOld
            NewPriceInt[j] = tempNew
            Quantity[j] = tempQ
            Stars[j] = tempS
            RatingInt[j] = tempR
            Discount[j] = tempDis
            Description[j] = tempDescript
        interval = interval // 2

    return MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description

def shellSortOldpriceAscending(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description):
    n = len(OldpriceInt)
    # Rearrange elements at each n/2, n/4, n/8, ... intervals
    interval = n // 2
    while interval > 0:
        for i in range(interval,n,1):
            temp = MedicineName[i]
            tempOld = OldpriceInt[i]
            tempNew = NewPriceInt[i]
            tempQ = Quantity[i]
            tempS = Stars[i]
            tempR = RatingInt[i]
            tempDis = Discount[i]
            tempDescript = Description[i]
            j = i
            while j >= interval and OldpriceInt[j - interval] > tempOld:
                MedicineName[j] = MedicineName[j - interval]
                OldpriceInt[j] = OldpriceInt[j - interval]
                NewPriceInt[j] = NewPriceInt[j - interval]
                Quantity[j] = Quantity[j - interval]
                Stars[j] = Stars[j - interval]
                RatingInt[j] = RatingInt[j - interval]
                Discount[j] = Discount[j - interval]
                Description[j] = Description[j - interval]

                j = j - interval
            MedicineName[j] = temp
            OldpriceInt[j] = tempOld
            NewPriceInt[j] = tempNew
            Quantity[j] = tempQ
            Stars[j] = tempS
            RatingInt[j] = tempR
            Discount[j] = tempDis
            Description[j] = tempDescript
        interval = interval // 2

    return MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description

def shellSortNewPriceAscending(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description):
    n = len(NewPriceInt)
    # Rearrange elements at each n/2, n/4, n/8, ... intervals
    interval = n // 2
    while interval > 0:
        for i in range(interval,n,1):
            temp = MedicineName[i]
            tempOld = OldpriceInt[i]
            tempNew = NewPriceInt[i]
            tempQ = Quantity[i]
            tempS = Stars[i]
            tempR = RatingInt[i]
            tempDis = Discount[i]
            tempDescript = Description[i]
            j = i
            while j >= interval and NewPriceInt[j - interval] > tempNew:
                MedicineName[j] = MedicineName[j - interval]
                OldpriceInt[j] = OldpriceInt[j - interval]
                NewPriceInt[j] = NewPriceInt[j - interval]
                Quantity[j] = Quantity[j - interval]
                Stars[j] = Stars[j - interval]
                RatingInt[j] = RatingInt[j - interval]
                Discount[j] = Discount[j - interval]
                Description[j] = Description[j - interval]

                j = j - interval
            MedicineName[j] = temp
            OldpriceInt[j] = tempOld
            NewPriceInt[j] = tempNew
            Quantity[j] = tempQ
            Stars[j] = tempS
            RatingInt[j] = tempR
            Discount[j] = tempDis
            Description[j] = tempDescript
        interval = interval // 2

    return MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description

def shellSortQuantityAscending(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description):
    n = len(Quantity)
    # Rearrange elements at each n/2, n/4, n/8, ... intervals
    interval = n // 2
    while interval > 0:
        for i in range(interval,n,1):
            temp = MedicineName[i]
            tempOld = OldpriceInt[i]
            tempNew = NewPriceInt[i]
            tempQ = Quantity[i]
            tempS = Stars[i]
            tempR = RatingInt[i]
            tempDis = Discount[i]
            tempDescript = Description[i]
            j = i
            while j >= interval and Quantity[j - interval] > tempQ:
                MedicineName[j] = MedicineName[j - interval]
                OldpriceInt[j] = OldpriceInt[j - interval]
                NewPriceInt[j] = NewPriceInt[j - interval]
                Quantity[j] = Quantity[j - interval]
                Stars[j] = Stars[j - interval]
                RatingInt[j] = RatingInt[j - interval]
                Discount[j] = Discount[j - interval]
                Description[j] = Description[j - interval]

                j = j - interval
            MedicineName[j] = temp
            OldpriceInt[j] = tempOld
            NewPriceInt[j] = tempNew
            Quantity[j] = tempQ
            Stars[j] = tempS
            RatingInt[j] = tempR
            Discount[j] = tempDis
            Description[j] = tempDescript
        interval = interval // 2

    return MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description

def shellSortStarsAscending(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description):
    n = len(Stars)
    # Rearrange elements at each n/2, n/4, n/8, ... intervals
    interval = n // 2
    while interval > 0:
        for i in range(interval,n,1):
            temp = MedicineName[i]
            tempOld = OldpriceInt[i]
            tempNew = NewPriceInt[i]
            tempQ = Quantity[i]
            tempS = Stars[i]
            tempR = RatingInt[i]
            tempDis = Discount[i]
            tempDescript = Description[i]
            j = i
            while j >= interval and Stars[j - interval] > tempS:
                MedicineName[j] = MedicineName[j - interval]
                OldpriceInt[j] = OldpriceInt[j - interval]
                NewPriceInt[j] = NewPriceInt[j - interval]
                Quantity[j] = Quantity[j - interval]
                Stars[j] = Stars[j - interval]
                RatingInt[j] = RatingInt[j - interval]
                Discount[j] = Discount[j - interval]
                Description[j] = Description[j - interval]

                j = j - interval
            MedicineName[j] = temp
            OldpriceInt[j] = tempOld
            NewPriceInt[j] = tempNew
            Quantity[j] = tempQ
            Stars[j] = tempS
            RatingInt[j] = tempR
            Discount[j] = tempDis
            Description[j] = tempDescript
        interval = interval // 2

    return MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description

def shellSortRatingAscending(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description):
    n = len(RatingInt)
    # Rearrange elements at each n/2, n/4, n/8, ... intervals
    interval = n // 2
    while interval > 0:
        for i in range(interval,n,1):
            temp = MedicineName[i]
            tempOld = OldpriceInt[i]
            tempNew = NewPriceInt[i]
            tempQ = Quantity[i]
            tempS = Stars[i]
            tempR = RatingInt[i]
            tempDis = Discount[i]
            tempDescript = Description[i]
            j = i
            while j >= interval and RatingInt[j - interval] > tempR:
                MedicineName[j] = MedicineName[j - interval]
                OldpriceInt[j] = OldpriceInt[j - interval]
                NewPriceInt[j] = NewPriceInt[j - interval]
                Quantity[j] = Quantity[j - interval]
                Stars[j] = Stars[j - interval]
                RatingInt[j] = RatingInt[j - interval]
                Discount[j] = Discount[j - interval]
                Description[j] = Description[j - interval]

                j = j - interval
            MedicineName[j] = temp
            OldpriceInt[j] = tempOld
            NewPriceInt[j] = tempNew
            Quantity[j] = tempQ
            Stars[j] = tempS
            RatingInt[j] = tempR
            Discount[j] = tempDis
            Description[j] = tempDescript
        interval = interval // 2

    return MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description

def shellSortDiscountAscending(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description):
    n = len(Discount)
    # Rearrange elements at each n/2, n/4, n/8, ... intervals
    interval = n // 2
    while interval > 0:
        for i in range(interval,n,1):
            temp = MedicineName[i]
            tempOld = OldpriceInt[i]
            tempNew = NewPriceInt[i]
            tempQ = Quantity[i]
            tempS = Stars[i]
            tempR = RatingInt[i]
            tempDis = Discount[i]
            tempDescript = Description[i]
            j = i
            while j >= interval and Discount[j - interval] > tempDis:
                MedicineName[j] = MedicineName[j - interval]
                OldpriceInt[j] = OldpriceInt[j - interval]
                NewPriceInt[j] = NewPriceInt[j - interval]
                Quantity[j] = Quantity[j - interval]
                Stars[j] = Stars[j - interval]
                RatingInt[j] = RatingInt[j - interval]
                Discount[j] = Discount[j - interval]
                Description[j] = Description[j - interval]

                j = j - interval
            MedicineName[j] = temp
            OldpriceInt[j] = tempOld
            NewPriceInt[j] = tempNew
            Quantity[j] = tempQ
            Stars[j] = tempS
            RatingInt[j] = tempR
            Discount[j] = tempDis
            Description[j] = tempDescript
        interval = interval // 2

    return MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description

def shellSortDescriptionAscending(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description):
    n = len(Description)
    # Rearrange elements at each n/2, n/4, n/8, ... intervals
    interval = n // 2
    while interval > 0:
        for i in range(interval,n,1):
            temp = MedicineName[i]
            tempOld = OldpriceInt[i]
            tempNew = NewPriceInt[i]
            tempQ = Quantity[i]
            tempS = Stars[i]
            tempR = RatingInt[i]
            tempDis = Discount[i]
            tempDescript = Description[i]
            j = i
            while j >= interval and Description[j - interval] > tempDescript:
                MedicineName[j] = MedicineName[j - interval]
                OldpriceInt[j] = OldpriceInt[j - interval]
                NewPriceInt[j] = NewPriceInt[j - interval]
                Quantity[j] = Quantity[j - interval]
                Stars[j] = Stars[j - interval]
                RatingInt[j] = RatingInt[j - interval]
                Discount[j] = Discount[j - interval]
                Description[j] = Description[j - interval]

                j = j - interval
            MedicineName[j] = temp
            OldpriceInt[j] = tempOld
            NewPriceInt[j] = tempNew
            Quantity[j] = tempQ
            Stars[j] = tempS
            RatingInt[j] = tempR
            Discount[j] = tempDis
            Description[j] = tempDescript
        interval = interval // 2

    return MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description

#Shell Sort Descending Functions
def shellSortDescending(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description):
    n = len(MedicineName)
    # Rearrange elements at each n/2, n/4, n/8, ... intervals
    interval = n // 2
    while interval > 0:
        for i in range(interval,n,1):
            temp = MedicineName[i]
            tempOld = OldpriceInt[i]
            tempNew = NewPriceInt[i]
            tempQ = Quantity[i]
            tempS = Stars[i]
            tempR = RatingInt[i]
            tempDis = Discount[i]
            tempDescript = Description[i]
            j = i
            while j >= interval and MedicineName[j - interval] > temp:
                MedicineName[j] = MedicineName[j - interval]
                OldpriceInt[j] = OldpriceInt[j - interval]
                NewPriceInt[j] = NewPriceInt[j - interval]
                Quantity[j] = Quantity[j - interval]
                Stars[j] = Stars[j - interval]
                RatingInt[j] = RatingInt[j - interval]
                Discount[j] = Discount[j - interval]
                Description[j] = Description[j - interval]

                j = j - interval
            MedicineName[j] = temp
            OldpriceInt[j] = tempOld
            NewPriceInt[j] = tempNew
            Quantity[j] = tempQ
            Stars[j] = tempS
            RatingInt[j] = tempR
            Discount[j] = tempDis
            Description[j] = tempDescript
        interval = interval // 2
    MedicineName.reverse()
    OldpriceInt.reverse()
    NewPriceInt.reverse()
    Quantity.reverse()
    Stars.reverse()
    RatingInt.reverse()
    Discount.reverse()
    Description.reverse()

    return MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description

def shellSortOldpriceDescending(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description):
    n = len(OldpriceInt)
    # Rearrange elements at each n/2, n/4, n/8, ... intervals
    interval = n // 2
    while interval > 0:
        for i in range(interval,n,1):
            temp = MedicineName[i]
            tempOld = OldpriceInt[i]
            tempNew = NewPriceInt[i]
            tempQ = Quantity[i]
            tempS = Stars[i]
            tempR = RatingInt[i]
            tempDis = Discount[i]
            tempDescript = Description[i]
            j = i
            while j >= interval and OldpriceInt[j - interval] > tempOld:
                MedicineName[j] = MedicineName[j - interval]
                OldpriceInt[j] = OldpriceInt[j - interval]
                NewPriceInt[j] = NewPriceInt[j - interval]
                Quantity[j] = Quantity[j - interval]
                Stars[j] = Stars[j - interval]
                RatingInt[j] = RatingInt[j - interval]
                Discount[j] = Discount[j - interval]
                Description[j] = Description[j - interval]

                j = j - interval
            MedicineName[j] = temp
            OldpriceInt[j] = tempOld
            NewPriceInt[j] = tempNew
            Quantity[j] = tempQ
            Stars[j] = tempS
            RatingInt[j] = tempR
            Discount[j] = tempDis
            Description[j] = tempDescript
        interval = interval // 2
    
    MedicineName.reverse()
    OldpriceInt.reverse()
    NewPriceInt.reverse()
    Quantity.reverse()
    Stars.reverse()
    RatingInt.reverse()
    Discount.reverse()
    Description.reverse()

    return MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description

def shellSortNewPriceDescending(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description):
    n = len(NewPriceInt)
    # Rearrange elements at each n/2, n/4, n/8, ... intervals
    interval = n // 2
    while interval > 0:
        for i in range(interval,n,1):
            temp = MedicineName[i]
            tempOld = OldpriceInt[i]
            tempNew = NewPriceInt[i]
            tempQ = Quantity[i]
            tempS = Stars[i]
            tempR = RatingInt[i]
            tempDis = Discount[i]
            tempDescript = Description[i]
            j = i
            while j >= interval and NewPriceInt[j - interval] > tempNew:
                MedicineName[j] = MedicineName[j - interval]
                OldpriceInt[j] = OldpriceInt[j - interval]
                NewPriceInt[j] = NewPriceInt[j - interval]
                Quantity[j] = Quantity[j - interval]
                Stars[j] = Stars[j - interval]
                RatingInt[j] = RatingInt[j - interval]
                Discount[j] = Discount[j - interval]
                Description[j] = Description[j - interval]

                j = j - interval
            MedicineName[j] = temp
            OldpriceInt[j] = tempOld
            NewPriceInt[j] = tempNew
            Quantity[j] = tempQ
            Stars[j] = tempS
            RatingInt[j] = tempR
            Discount[j] = tempDis
            Description[j] = tempDescript
        interval = interval // 2
    
    MedicineName.reverse()
    OldpriceInt.reverse()
    NewPriceInt.reverse()
    Quantity.reverse()
    Stars.reverse()
    RatingInt.reverse()
    Discount.reverse()
    Description.reverse()

    return MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description

def shellSortQuantityDescending(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description):
    n = len(Quantity)
    # Rearrange elements at each n/2, n/4, n/8, ... intervals
    interval = n // 2
    while interval > 0:
        for i in range(interval,n,1):
            temp = MedicineName[i]
            tempOld = OldpriceInt[i]
            tempNew = NewPriceInt[i]
            tempQ = Quantity[i]
            tempS = Stars[i]
            tempR = RatingInt[i]
            tempDis = Discount[i]
            tempDescript = Description[i]
            j = i
            while j >= interval and Quantity[j - interval] > tempQ:
                MedicineName[j] = MedicineName[j - interval]
                OldpriceInt[j] = OldpriceInt[j - interval]
                NewPriceInt[j] = NewPriceInt[j - interval]
                Quantity[j] = Quantity[j - interval]
                Stars[j] = Stars[j - interval]
                RatingInt[j] = RatingInt[j - interval]
                Discount[j] = Discount[j - interval]
                Description[j] = Description[j - interval]

                j = j - interval
            MedicineName[j] = temp
            OldpriceInt[j] = tempOld
            NewPriceInt[j] = tempNew
            Quantity[j] = tempQ
            Stars[j] = tempS
            RatingInt[j] = tempR
            Discount[j] = tempDis
            Description[j] = tempDescript
        interval = interval // 2
    
    MedicineName.reverse()
    OldpriceInt.reverse()
    NewPriceInt.reverse()
    Quantity.reverse()
    Stars.reverse()
    RatingInt.reverse()
    Discount.reverse()
    Description.reverse()

    return MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description

def shellSortStarsDescending(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description):
    n = len(Stars)
    # Rearrange elements at each n/2, n/4, n/8, ... intervals
    interval = n // 2
    while interval > 0:
        for i in range(interval,n,1):
            temp = MedicineName[i]
            tempOld = OldpriceInt[i]
            tempNew = NewPriceInt[i]
            tempQ = Quantity[i]
            tempS = Stars[i]
            tempR = RatingInt[i]
            tempDis = Discount[i]
            tempDescript = Description[i]
            j = i
            while j >= interval and Stars[j - interval] > tempS:
                MedicineName[j] = MedicineName[j - interval]
                OldpriceInt[j] = OldpriceInt[j - interval]
                NewPriceInt[j] = NewPriceInt[j - interval]
                Quantity[j] = Quantity[j - interval]
                Stars[j] = Stars[j - interval]
                RatingInt[j] = RatingInt[j - interval]
                Discount[j] = Discount[j - interval]
                Description[j] = Description[j - interval]

                j = j - interval
            MedicineName[j] = temp
            OldpriceInt[j] = tempOld
            NewPriceInt[j] = tempNew
            Quantity[j] = tempQ
            Stars[j] = tempS
            RatingInt[j] = tempR
            Discount[j] = tempDis
            Description[j] = tempDescript
        interval = interval // 2
    
    MedicineName.reverse()
    OldpriceInt.reverse()
    NewPriceInt.reverse()
    Quantity.reverse()
    Stars.reverse()
    RatingInt.reverse()
    Discount.reverse()
    Description.reverse()

    return MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description

def shellSortRatingDescending(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description):
    n = len(RatingInt)
    # Rearrange elements at each n/2, n/4, n/8, ... intervals
    interval = n // 2
    while interval > 0:
        for i in range(interval,n,1):
            temp = MedicineName[i]
            tempOld = OldpriceInt[i]
            tempNew = NewPriceInt[i]
            tempQ = Quantity[i]
            tempS = Stars[i]
            tempR = RatingInt[i]
            tempDis = Discount[i]
            tempDescript = Description[i]
            j = i
            while j >= interval and RatingInt[j - interval] > tempR:
                MedicineName[j] = MedicineName[j - interval]
                OldpriceInt[j] = OldpriceInt[j - interval]
                NewPriceInt[j] = NewPriceInt[j - interval]
                Quantity[j] = Quantity[j - interval]
                Stars[j] = Stars[j - interval]
                RatingInt[j] = RatingInt[j - interval]
                Discount[j] = Discount[j - interval]
                Description[j] = Description[j - interval]

                j = j - interval
            MedicineName[j] = temp
            OldpriceInt[j] = tempOld
            NewPriceInt[j] = tempNew
            Quantity[j] = tempQ
            Stars[j] = tempS
            RatingInt[j] = tempR
            Discount[j] = tempDis
            Description[j] = tempDescript
        interval = interval // 2
    
    MedicineName.reverse()
    OldpriceInt.reverse()
    NewPriceInt.reverse()
    Quantity.reverse()
    Stars.reverse()
    RatingInt.reverse()
    Discount.reverse()
    Description.reverse()

    return MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description

def shellSortDiscountDescending(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description):
    n = len(Discount)
    # Rearrange elements at each n/2, n/4, n/8, ... intervals
    interval = n // 2
    while interval > 0:
        for i in range(interval,n,1):
            temp = MedicineName[i]
            tempOld = OldpriceInt[i]
            tempNew = NewPriceInt[i]
            tempQ = Quantity[i]
            tempS = Stars[i]
            tempR = RatingInt[i]
            tempDis = Discount[i]
            tempDescript = Description[i]
            j = i
            while j >= interval and Discount[j - interval] > tempDis:
                MedicineName[j] = MedicineName[j - interval]
                OldpriceInt[j] = OldpriceInt[j - interval]
                NewPriceInt[j] = NewPriceInt[j - interval]
                Quantity[j] = Quantity[j - interval]
                Stars[j] = Stars[j - interval]
                RatingInt[j] = RatingInt[j - interval]
                Discount[j] = Discount[j - interval]
                Description[j] = Description[j - interval]

                j = j - interval
            MedicineName[j] = temp
            OldpriceInt[j] = tempOld
            NewPriceInt[j] = tempNew
            Quantity[j] = tempQ
            Stars[j] = tempS
            RatingInt[j] = tempR
            Discount[j] = tempDis
            Description[j] = tempDescript
        interval = interval // 2
    
    MedicineName.reverse()
    OldpriceInt.reverse()
    NewPriceInt.reverse()
    Quantity.reverse()
    Stars.reverse()
    RatingInt.reverse()
    Discount.reverse()
    Description.reverse()

    return MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description

def shellSortDescriptionDescending(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description):
    n = len(Description)
    # Rearrange elements at each n/2, n/4, n/8, ... intervals
    interval = n // 2
    while interval > 0:
        for i in range(interval,n,1):
            temp = MedicineName[i]
            tempOld = OldpriceInt[i]
            tempNew = NewPriceInt[i]
            tempQ = Quantity[i]
            tempS = Stars[i]
            tempR = RatingInt[i]
            tempDis = Discount[i]
            tempDescript = Description[i]
            j = i
            while j >= interval and Description[j - interval] > tempDescript:
                MedicineName[j] = MedicineName[j - interval]
                OldpriceInt[j] = OldpriceInt[j - interval]
                NewPriceInt[j] = NewPriceInt[j - interval]
                Quantity[j] = Quantity[j - interval]
                Stars[j] = Stars[j - interval]
                RatingInt[j] = RatingInt[j - interval]
                Discount[j] = Discount[j - interval]
                Description[j] = Description[j - interval]

                j = j - interval
            MedicineName[j] = temp
            OldpriceInt[j] = tempOld
            NewPriceInt[j] = tempNew
            Quantity[j] = tempQ
            Stars[j] = tempS
            RatingInt[j] = tempR
            Discount[j] = tempDis
            Description[j] = tempDescript
        interval = interval // 2
    
    MedicineName.reverse()
    OldpriceInt.reverse()
    NewPriceInt.reverse()
    Quantity.reverse()
    Stars.reverse()
    RatingInt.reverse()
    Discount.reverse()
    Description.reverse()

    return MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description




