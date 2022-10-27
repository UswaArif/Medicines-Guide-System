#Bubble Sort Ascending Functions
def BubbleSortAscending(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description):
    for i in range(0, len(MedicineName)):
        for j in range(i + 1, len(MedicineName)):
            if MedicineName[i] > MedicineName[j]:
                temp = MedicineName[i]
                MedicineName[i] = MedicineName[j]
                MedicineName[j] = temp

                tempOld = OldpriceInt[i]
                OldpriceInt[i] = OldpriceInt[j]
                OldpriceInt[j] = tempOld

                tempNew = NewPriceInt[i]
                NewPriceInt[i] = NewPriceInt[j]
                NewPriceInt[j] = tempNew

                tempQ = Quantity[i]
                Quantity[i] = Quantity[j]
                Quantity[j] = tempQ

                tempS = Stars[i]
                Stars[i] = Stars[j]
                Stars[j] = tempS

                tempR = RatingInt[i]
                RatingInt[i] = RatingInt[j]
                RatingInt[j] = tempR

                tempDis = Discount[i]
                Discount[i] = Discount[j]
                Discount[j] = tempDis

                tempDescript = Description[i]
                Description[i] = Description[j]
                Description[j] = tempDescript
    return MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description

def BubbleSortOldpriceAscending(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description):
    for i in range(0, len(OldpriceInt)):
        for j in range(i + 1, len(OldpriceInt)):
            if OldpriceInt[i] > OldpriceInt[j]:
                temp = MedicineName[i]
                MedicineName[i] = MedicineName[j]
                MedicineName[j] = temp

                tempOld = OldpriceInt[i]
                OldpriceInt[i] = OldpriceInt[j]
                OldpriceInt[j] = tempOld

                tempNew = NewPriceInt[i]
                NewPriceInt[i] = NewPriceInt[j]
                NewPriceInt[j] = tempNew

                tempQ = Quantity[i]
                Quantity[i] = Quantity[j]
                Quantity[j] = tempQ

                tempS = Stars[i]
                Stars[i] = Stars[j]
                Stars[j] = tempS

                tempR = RatingInt[i]
                RatingInt[i] = RatingInt[j]
                RatingInt[j] = tempR

                tempDis = Discount[i]
                Discount[i] = Discount[j]
                Discount[j] = tempDis

                tempDescript = Description[i]
                Description[i] = Description[j]
                Description[j] = tempDescript
    return MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description

def BubbleSortNewPriceAscending(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description):
    for i in range(0, len(NewPriceInt)):
        for j in range(i + 1, len(NewPriceInt)):
            if NewPriceInt[i] > NewPriceInt[j]:
                temp = MedicineName[i]
                MedicineName[i] = MedicineName[j]
                MedicineName[j] = temp

                tempOld = OldpriceInt[i]
                OldpriceInt[i] = OldpriceInt[j]
                OldpriceInt[j] = tempOld

                tempNew = NewPriceInt[i]
                NewPriceInt[i] = NewPriceInt[j]
                NewPriceInt[j] = tempNew

                tempQ = Quantity[i]
                Quantity[i] = Quantity[j]
                Quantity[j] = tempQ

                tempS = Stars[i]
                Stars[i] = Stars[j]
                Stars[j] = tempS

                tempR = RatingInt[i]
                RatingInt[i] = RatingInt[j]
                RatingInt[j] = tempR

                tempDis = Discount[i]
                Discount[i] = Discount[j]
                Discount[j] = tempDis

                tempDescript = Description[i]
                Description[i] = Description[j]
                Description[j] = tempDescript
    return MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description

def BubbleSortQuantityAscending(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description):
    for i in range(0, len(Quantity)):
        for j in range(i + 1, len(Quantity)):
            if Quantity[i] > Quantity[j]:
                temp = MedicineName[i]
                MedicineName[i] = MedicineName[j]
                MedicineName[j] = temp

                tempOld = OldpriceInt[i]
                OldpriceInt[i] = OldpriceInt[j]
                OldpriceInt[j] = tempOld

                tempNew = NewPriceInt[i]
                NewPriceInt[i] = NewPriceInt[j]
                NewPriceInt[j] = tempNew

                tempQ = Quantity[i]
                Quantity[i] = Quantity[j]
                Quantity[j] = tempQ

                tempS = Stars[i]
                Stars[i] = Stars[j]
                Stars[j] = tempS

                tempR = RatingInt[i]
                RatingInt[i] = RatingInt[j]
                RatingInt[j] = tempR

                tempDis = Discount[i]
                Discount[i] = Discount[j]
                Discount[j] = tempDis

                tempDescript = Description[i]
                Description[i] = Description[j]
                Description[j] = tempDescript
    return MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description

def BubbleSortStarsAscending(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description):
    for i in range(0, len(Stars)):
        for j in range(i + 1, len(Stars)):
            if Stars[i] > Stars[j]:
                temp = MedicineName[i]
                MedicineName[i] = MedicineName[j]
                MedicineName[j] = temp

                tempOld = OldpriceInt[i]
                OldpriceInt[i] = OldpriceInt[j]
                OldpriceInt[j] = tempOld

                tempNew = NewPriceInt[i]
                NewPriceInt[i] = NewPriceInt[j]
                NewPriceInt[j] = tempNew

                tempQ = Quantity[i]
                Quantity[i] = Quantity[j]
                Quantity[j] = tempQ

                tempS = Stars[i]
                Stars[i] = Stars[j]
                Stars[j] = tempS

                tempR = RatingInt[i]
                RatingInt[i] = RatingInt[j]
                RatingInt[j] = tempR

                tempDis = Discount[i]
                Discount[i] = Discount[j]
                Discount[j] = tempDis

                tempDescript = Description[i]
                Description[i] = Description[j]
                Description[j] = tempDescript
    return MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description

def BubbleSortRatingAscending(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description):
    for i in range(0, len(RatingInt)):
        for j in range(i + 1, len(RatingInt)):
            if RatingInt[i] > RatingInt[j]:
                temp = MedicineName[i]
                MedicineName[i] = MedicineName[j]
                MedicineName[j] = temp

                tempOld = OldpriceInt[i]
                OldpriceInt[i] = OldpriceInt[j]
                OldpriceInt[j] = tempOld

                tempNew = NewPriceInt[i]
                NewPriceInt[i] = NewPriceInt[j]
                NewPriceInt[j] = tempNew

                tempQ = Quantity[i]
                Quantity[i] = Quantity[j]
                Quantity[j] = tempQ

                tempS = Stars[i]
                Stars[i] = Stars[j]
                Stars[j] = tempS

                tempR = RatingInt[i]
                RatingInt[i] = RatingInt[j]
                RatingInt[j] = tempR

                tempDis = Discount[i]
                Discount[i] = Discount[j]
                Discount[j] = tempDis

                tempDescript = Description[i]
                Description[i] = Description[j]
                Description[j] = tempDescript
    return MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description

def BubbleSortDiscountAscending(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description):
    for i in range(0, len(Discount)):
        for j in range(i + 1, len(Discount)):
            if Discount[i] > Discount[j]:
                temp = MedicineName[i]
                MedicineName[i] = MedicineName[j]
                MedicineName[j] = temp

                tempOld = OldpriceInt[i]
                OldpriceInt[i] = OldpriceInt[j]
                OldpriceInt[j] = tempOld

                tempNew = NewPriceInt[i]
                NewPriceInt[i] = NewPriceInt[j]
                NewPriceInt[j] = tempNew

                tempQ = Quantity[i]
                Quantity[i] = Quantity[j]
                Quantity[j] = tempQ

                tempS = Stars[i]
                Stars[i] = Stars[j]
                Stars[j] = tempS

                tempR = RatingInt[i]
                RatingInt[i] = RatingInt[j]
                RatingInt[j] = tempR

                tempDis = Discount[i]
                Discount[i] = Discount[j]
                Discount[j] = tempDis

                tempDescript = Description[i]
                Description[i] = Description[j]
                Description[j] = tempDescript
    return MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description

def BubbleSortDescriptionAscending(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description):
    for i in range(0, len(Description)):
        for j in range(i + 1, len(Description)):
            if Description[i] > Description[j]:
                temp = MedicineName[i]
                MedicineName[i] = MedicineName[j]
                MedicineName[j] = temp

                tempOld = OldpriceInt[i]
                OldpriceInt[i] = OldpriceInt[j]
                OldpriceInt[j] = tempOld

                tempNew = NewPriceInt[i]
                NewPriceInt[i] = NewPriceInt[j]
                NewPriceInt[j] = tempNew

                tempQ = Quantity[i]
                Quantity[i] = Quantity[j]
                Quantity[j] = tempQ

                tempS = Stars[i]
                Stars[i] = Stars[j]
                Stars[j] = tempS

                tempR = RatingInt[i]
                RatingInt[i] = RatingInt[j]
                RatingInt[j] = tempR

                tempDis = Discount[i]
                Discount[i] = Discount[j]
                Discount[j] = tempDis

                tempDescript = Description[i]
                Description[i] = Description[j]
                Description[j] = tempDescript
    return MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description

#Bubble Sort Descending Functions

def BubbleSortDescending(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description):
    for i in range(0, len(MedicineName)):
        for j in range(i + 1, len(MedicineName)):
            if MedicineName[i] > MedicineName[j]:
                temp = MedicineName[i]
                MedicineName[i] = MedicineName[j]
                MedicineName[j] = temp

                tempOld = OldpriceInt[i]
                OldpriceInt[i] = OldpriceInt[j]
                OldpriceInt[j] = tempOld

                tempNew = NewPriceInt[i]
                NewPriceInt[i] = NewPriceInt[j]
                NewPriceInt[j] = tempNew

                tempQ = Quantity[i]
                Quantity[i] = Quantity[j]
                Quantity[j] = tempQ

                tempS = Stars[i]
                Stars[i] = Stars[j]
                Stars[j] = tempS

                tempR = RatingInt[i]
                RatingInt[i] = RatingInt[j]
                RatingInt[j] = tempR

                tempDis = Discount[i]
                Discount[i] = Discount[j]
                Discount[j] = tempDis

                tempDescript = Description[i]
                Description[i] = Description[j]
                Description[j] = tempDescript

    MedicineName.reverse()
    OldpriceInt.reverse()
    NewPriceInt.reverse()
    Quantity.reverse()
    Stars.reverse()
    RatingInt.reverse()
    Discount.reverse()
    Description.reverse()
    return MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description

def BubbleSortOldpriceDescending(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description):
    for i in range(0, len(OldpriceInt)):
        for j in range(i + 1, len(OldpriceInt)):
            if OldpriceInt[i] > OldpriceInt[j]:
                temp = MedicineName[i]
                MedicineName[i] = MedicineName[j]
                MedicineName[j] = temp

                tempOld = OldpriceInt[i]
                OldpriceInt[i] = OldpriceInt[j]
                OldpriceInt[j] = tempOld

                tempNew = NewPriceInt[i]
                NewPriceInt[i] = NewPriceInt[j]
                NewPriceInt[j] = tempNew

                tempQ = Quantity[i]
                Quantity[i] = Quantity[j]
                Quantity[j] = tempQ

                tempS = Stars[i]
                Stars[i] = Stars[j]
                Stars[j] = tempS

                tempR = RatingInt[i]
                RatingInt[i] = RatingInt[j]
                RatingInt[j] = tempR

                tempDis = Discount[i]
                Discount[i] = Discount[j]
                Discount[j] = tempDis

                tempDescript = Description[i]
                Description[i] = Description[j]
                Description[j] = tempDescript

    MedicineName.reverse()
    OldpriceInt.reverse()
    NewPriceInt.reverse()
    Quantity.reverse()
    Stars.reverse()
    RatingInt.reverse()
    Discount.reverse()
    Description.reverse()
    return MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description

def BubbleSortNewPriceDescending(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description):
    for i in range(0, len(NewPriceInt)):
        for j in range(i + 1, len(NewPriceInt)):
            if NewPriceInt[i] > NewPriceInt[j]:
                temp = MedicineName[i]
                MedicineName[i] = MedicineName[j]
                MedicineName[j] = temp

                tempOld = OldpriceInt[i]
                OldpriceInt[i] = OldpriceInt[j]
                OldpriceInt[j] = tempOld

                tempNew = NewPriceInt[i]
                NewPriceInt[i] = NewPriceInt[j]
                NewPriceInt[j] = tempNew

                tempQ = Quantity[i]
                Quantity[i] = Quantity[j]
                Quantity[j] = tempQ

                tempS = Stars[i]
                Stars[i] = Stars[j]
                Stars[j] = tempS

                tempR = RatingInt[i]
                RatingInt[i] = RatingInt[j]
                RatingInt[j] = tempR

                tempDis = Discount[i]
                Discount[i] = Discount[j]
                Discount[j] = tempDis

                tempDescript = Description[i]
                Description[i] = Description[j]
                Description[j] = tempDescript

    MedicineName.reverse()
    OldpriceInt.reverse()
    NewPriceInt.reverse()
    Quantity.reverse()
    Stars.reverse()
    RatingInt.reverse()
    Discount.reverse()
    Description.reverse()
    return MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description

def BubbleSortQuantityDescending(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description):
    for i in range(0, len(Quantity)):
        for j in range(i + 1, len(Quantity)):
            if Quantity[i] > Quantity[j]:
                temp = MedicineName[i]
                MedicineName[i] = MedicineName[j]
                MedicineName[j] = temp

                tempOld = OldpriceInt[i]
                OldpriceInt[i] = OldpriceInt[j]
                OldpriceInt[j] = tempOld

                tempNew = NewPriceInt[i]
                NewPriceInt[i] = NewPriceInt[j]
                NewPriceInt[j] = tempNew

                tempQ = Quantity[i]
                Quantity[i] = Quantity[j]
                Quantity[j] = tempQ

                tempS = Stars[i]
                Stars[i] = Stars[j]
                Stars[j] = tempS

                tempR = RatingInt[i]
                RatingInt[i] = RatingInt[j]
                RatingInt[j] = tempR

                tempDis = Discount[i]
                Discount[i] = Discount[j]
                Discount[j] = tempDis

                tempDescript = Description[i]
                Description[i] = Description[j]
                Description[j] = tempDescript

    MedicineName.reverse()
    OldpriceInt.reverse()
    NewPriceInt.reverse()
    Quantity.reverse()
    Stars.reverse()
    RatingInt.reverse()
    Discount.reverse()
    Description.reverse()
    return MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description

def BubbleSortStarsDescending(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description):
    for i in range(0, len(Stars)):
        for j in range(i + 1, len(Stars)):
            if Stars[i] > Stars[j]:
                temp = MedicineName[i]
                MedicineName[i] = MedicineName[j]
                MedicineName[j] = temp

                tempOld = OldpriceInt[i]
                OldpriceInt[i] = OldpriceInt[j]
                OldpriceInt[j] = tempOld

                tempNew = NewPriceInt[i]
                NewPriceInt[i] = NewPriceInt[j]
                NewPriceInt[j] = tempNew

                tempQ = Quantity[i]
                Quantity[i] = Quantity[j]
                Quantity[j] = tempQ

                tempS = Stars[i]
                Stars[i] = Stars[j]
                Stars[j] = tempS

                tempR = RatingInt[i]
                RatingInt[i] = RatingInt[j]
                RatingInt[j] = tempR

                tempDis = Discount[i]
                Discount[i] = Discount[j]
                Discount[j] = tempDis

                tempDescript = Description[i]
                Description[i] = Description[j]
                Description[j] = tempDescript

    MedicineName.reverse()
    OldpriceInt.reverse()
    NewPriceInt.reverse()
    Quantity.reverse()
    Stars.reverse()
    RatingInt.reverse()
    Discount.reverse()
    Description.reverse()
    return MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description

def BubbleSortRatingDescending(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description):
    for i in range(0, len(RatingInt)):
        for j in range(i + 1, len(RatingInt)):
            if RatingInt[i] > RatingInt[j]:
                temp = MedicineName[i]
                MedicineName[i] = MedicineName[j]
                MedicineName[j] = temp

                tempOld = OldpriceInt[i]
                OldpriceInt[i] = OldpriceInt[j]
                OldpriceInt[j] = tempOld

                tempNew = NewPriceInt[i]
                NewPriceInt[i] = NewPriceInt[j]
                NewPriceInt[j] = tempNew

                tempQ = Quantity[i]
                Quantity[i] = Quantity[j]
                Quantity[j] = tempQ

                tempS = Stars[i]
                Stars[i] = Stars[j]
                Stars[j] = tempS

                tempR = RatingInt[i]
                RatingInt[i] = RatingInt[j]
                RatingInt[j] = tempR

                tempDis = Discount[i]
                Discount[i] = Discount[j]
                Discount[j] = tempDis

                tempDescript = Description[i]
                Description[i] = Description[j]
                Description[j] = tempDescript
            
    MedicineName.reverse()
    OldpriceInt.reverse()
    NewPriceInt.reverse()
    Quantity.reverse()
    Stars.reverse()
    RatingInt.reverse()
    Discount.reverse()
    Description.reverse()
    return MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description

def BubbleSortDiscountDescending(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description):
    for i in range(0, len(Discount)):
        for j in range(i + 1, len(Discount)):
            if Discount[i] > Discount[j]:
                temp = MedicineName[i]
                MedicineName[i] = MedicineName[j]
                MedicineName[j] = temp

                tempOld = OldpriceInt[i]
                OldpriceInt[i] = OldpriceInt[j]
                OldpriceInt[j] = tempOld

                tempNew = NewPriceInt[i]
                NewPriceInt[i] = NewPriceInt[j]
                NewPriceInt[j] = tempNew

                tempQ = Quantity[i]
                Quantity[i] = Quantity[j]
                Quantity[j] = tempQ

                tempS = Stars[i]
                Stars[i] = Stars[j]
                Stars[j] = tempS

                tempR = RatingInt[i]
                RatingInt[i] = RatingInt[j]
                RatingInt[j] = tempR

                tempDis = Discount[i]
                Discount[i] = Discount[j]
                Discount[j] = tempDis

                tempDescript = Description[i]
                Description[i] = Description[j]
                Description[j] = tempDescript

    MedicineName.reverse()
    OldpriceInt.reverse()
    NewPriceInt.reverse()
    Quantity.reverse()
    Stars.reverse()
    RatingInt.reverse()
    Discount.reverse()
    Description.reverse()
    return MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description

def BubbleSortDescriptionDescending(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description):
    for i in range(0, len(Description)):
        for j in range(i + 1, len(Description)):
            if Description[i] > Description[j]:
                temp = MedicineName[i]
                MedicineName[i] = MedicineName[j]
                MedicineName[j] = temp

                tempOld = OldpriceInt[i]
                OldpriceInt[i] = OldpriceInt[j]
                OldpriceInt[j] = tempOld

                tempNew = NewPriceInt[i]
                NewPriceInt[i] = NewPriceInt[j]
                NewPriceInt[j] = tempNew

                tempQ = Quantity[i]
                Quantity[i] = Quantity[j]
                Quantity[j] = tempQ

                tempS = Stars[i]
                Stars[i] = Stars[j]
                Stars[j] = tempS

                tempR = RatingInt[i]
                RatingInt[i] = RatingInt[j]
                RatingInt[j] = tempR

                tempDis = Discount[i]
                Discount[i] = Discount[j]
                Discount[j] = tempDis

                tempDescript = Description[i]
                Description[i] = Description[j]
                Description[j] = tempDescript

    MedicineName.reverse()
    OldpriceInt.reverse()
    NewPriceInt.reverse()
    Quantity.reverse()
    Stars.reverse()
    RatingInt.reverse()
    Discount.reverse()
    Description.reverse()
    return MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description

