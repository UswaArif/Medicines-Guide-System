#Selection Sort Ascending Function

def SelectionSortAscending(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description):
    for i in range(0, len(MedicineName)):
        min = i
        for j in range(i + 1, len(MedicineName)):
            if MedicineName[min] > MedicineName[j]:
                min = j

        temp = MedicineName[i]
        MedicineName[i] = MedicineName[min]
        MedicineName[min] = temp

        tempOld = OldpriceInt[i]
        OldpriceInt[i] = OldpriceInt[min]
        OldpriceInt[min] = tempOld

        tempNew = NewPriceInt[i]
        NewPriceInt[i] = NewPriceInt[min]
        NewPriceInt[min] = tempNew

        tempQ = Quantity[i]
        Quantity[i] = Quantity[min]
        Quantity[min] = tempQ

        tempS = Stars[i]
        Stars[i] = Stars[min]
        Stars[min] = tempS

        tempR = RatingInt[i]
        RatingInt[i] = RatingInt[min]
        RatingInt[min] = tempR

        tempDis = Discount[i]
        Discount[i] = Discount[min]
        Discount[min] = tempDis

        tempDescript = Description[i]
        Description[i] = Description[min]
        Description[min] = tempDescript

    return MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description

def SelectionSortOldpriceAscending(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description):
    for i in range(0, len(OldpriceInt)):
        min = i
        for j in range(i + 1, len(OldpriceInt)):
            if OldpriceInt[min] > OldpriceInt[j]:
                min = j

        temp = MedicineName[i]
        MedicineName[i] = MedicineName[min]
        MedicineName[min] = temp

        tempOld = OldpriceInt[i]
        OldpriceInt[i] = OldpriceInt[min]
        OldpriceInt[min] = tempOld

        tempNew = NewPriceInt[i]
        NewPriceInt[i] = NewPriceInt[min]
        NewPriceInt[min] = tempNew

        tempQ = Quantity[i]
        Quantity[i] = Quantity[min]
        Quantity[min] = tempQ

        tempS = Stars[i]
        Stars[i] = Stars[min]
        Stars[min] = tempS

        tempR = RatingInt[i]
        RatingInt[i] = RatingInt[min]
        RatingInt[min] = tempR

        tempDis = Discount[i]
        Discount[i] = Discount[min]
        Discount[min] = tempDis

        tempDescript = Description[i]
        Description[i] = Description[min]
        Description[min] = tempDescript

    return MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description

def SelectionSortNewPriceAscending(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description):
    for i in range(0, len(NewPriceInt)):
        min = i
        for j in range(i + 1, len(NewPriceInt)):
            if NewPriceInt[min] > NewPriceInt[j]:
                min = j

        temp = MedicineName[i]
        MedicineName[i] = MedicineName[min]
        MedicineName[min] = temp

        tempOld = OldpriceInt[i]
        OldpriceInt[i] = OldpriceInt[min]
        OldpriceInt[min] = tempOld

        tempNew = NewPriceInt[i]
        NewPriceInt[i] = NewPriceInt[min]
        NewPriceInt[min] = tempNew

        tempQ = Quantity[i]
        Quantity[i] = Quantity[min]
        Quantity[min] = tempQ

        tempS = Stars[i]
        Stars[i] = Stars[min]
        Stars[min] = tempS

        tempR = RatingInt[i]
        RatingInt[i] = RatingInt[min]
        RatingInt[min] = tempR

        tempDis = Discount[i]
        Discount[i] = Discount[min]
        Discount[min] = tempDis

        tempDescript = Description[i]
        Description[i] = Description[min]
        Description[min] = tempDescript

    return MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description

def SelectionSortQuantityAscending(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description):
    for i in range(0, len(Quantity)):
        min = i
        for j in range(i + 1, len(Quantity)):
            if Quantity[min] > Quantity[j]:
                min = j

        temp = MedicineName[i]
        MedicineName[i] = MedicineName[min]
        MedicineName[min] = temp

        tempOld = OldpriceInt[i]
        OldpriceInt[i] = OldpriceInt[min]
        OldpriceInt[min] = tempOld

        tempNew = NewPriceInt[i]
        NewPriceInt[i] = NewPriceInt[min]
        NewPriceInt[min] = tempNew

        tempQ = Quantity[i]
        Quantity[i] = Quantity[min]
        Quantity[min] = tempQ

        tempS = Stars[i]
        Stars[i] = Stars[min]
        Stars[min] = tempS

        tempR = RatingInt[i]
        RatingInt[i] = RatingInt[min]
        RatingInt[min] = tempR

        tempDis = Discount[i]
        Discount[i] = Discount[min]
        Discount[min] = tempDis

        tempDescript = Description[i]
        Description[i] = Description[min]
        Description[min] = tempDescript

    return MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description

def SelectionSortStarsAscending(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description):
    for i in range(0, len(Stars)):
        min = i
        for j in range(i + 1, len(Stars)):
            if Stars[min] > Stars[j]:
                min = j

        temp = MedicineName[i]
        MedicineName[i] = MedicineName[min]
        MedicineName[min] = temp

        tempOld = OldpriceInt[i]
        OldpriceInt[i] = OldpriceInt[min]
        OldpriceInt[min] = tempOld

        tempNew = NewPriceInt[i]
        NewPriceInt[i] = NewPriceInt[min]
        NewPriceInt[min] = tempNew

        tempQ = Quantity[i]
        Quantity[i] = Quantity[min]
        Quantity[min] = tempQ

        tempS = Stars[i]
        Stars[i] = Stars[min]
        Stars[min] = tempS

        tempR = RatingInt[i]
        RatingInt[i] = RatingInt[min]
        RatingInt[min] = tempR

        tempDis = Discount[i]
        Discount[i] = Discount[min]
        Discount[min] = tempDis

        tempDescript = Description[i]
        Description[i] = Description[min]
        Description[min] = tempDescript

    return MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description

def SelectionSortRatingAscending(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description):
    for i in range(0, len(RatingInt)):
        min = i
        for j in range(i + 1, len(RatingInt)):
            if RatingInt[min] > RatingInt[j]:
                min = j

        temp = MedicineName[i]
        MedicineName[i] = MedicineName[min]
        MedicineName[min] = temp

        tempOld = OldpriceInt[i]
        OldpriceInt[i] = OldpriceInt[min]
        OldpriceInt[min] = tempOld

        tempNew = NewPriceInt[i]
        NewPriceInt[i] = NewPriceInt[min]
        NewPriceInt[min] = tempNew

        tempQ = Quantity[i]
        Quantity[i] = Quantity[min]
        Quantity[min] = tempQ

        tempS = Stars[i]
        Stars[i] = Stars[min]
        Stars[min] = tempS

        tempR = RatingInt[i]
        RatingInt[i] = RatingInt[min]
        RatingInt[min] = tempR

        tempDis = Discount[i]
        Discount[i] = Discount[min]
        Discount[min] = tempDis

        tempDescript = Description[i]
        Description[i] = Description[min]
        Description[min] = tempDescript

    return MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description

def SelectionSortDiscountAscending(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description):
    for i in range(0, len(Discount)):
        min = i
        for j in range(i + 1, len(Discount)):
            if Discount[min] > Discount[j]:
                min = j

        temp = MedicineName[i]
        MedicineName[i] = MedicineName[min]
        MedicineName[min] = temp

        tempOld = OldpriceInt[i]
        OldpriceInt[i] = OldpriceInt[min]
        OldpriceInt[min] = tempOld

        tempNew = NewPriceInt[i]
        NewPriceInt[i] = NewPriceInt[min]
        NewPriceInt[min] = tempNew

        tempQ = Quantity[i]
        Quantity[i] = Quantity[min]
        Quantity[min] = tempQ

        tempS = Stars[i]
        Stars[i] = Stars[min]
        Stars[min] = tempS

        tempR = RatingInt[i]
        RatingInt[i] = RatingInt[min]
        RatingInt[min] = tempR

        tempDis = Discount[i]
        Discount[i] = Discount[min]
        Discount[min] = tempDis

        tempDescript = Description[i]
        Description[i] = Description[min]
        Description[min] = tempDescript

    return MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description

def SelectionSortDescriptionAscending(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description):
    for i in range(0, len(Description)):
        min = i
        for j in range(i + 1, len(Description)):
            if Description[min] > Description[j]:
                min = j

        temp = MedicineName[i]
        MedicineName[i] = MedicineName[min]
        MedicineName[min] = temp

        tempOld = OldpriceInt[i]
        OldpriceInt[i] = OldpriceInt[min]
        OldpriceInt[min] = tempOld

        tempNew = NewPriceInt[i]
        NewPriceInt[i] = NewPriceInt[min]
        NewPriceInt[min] = tempNew

        tempQ = Quantity[i]
        Quantity[i] = Quantity[min]
        Quantity[min] = tempQ

        tempS = Stars[i]
        Stars[i] = Stars[min]
        Stars[min] = tempS

        tempR = RatingInt[i]
        RatingInt[i] = RatingInt[min]
        RatingInt[min] = tempR

        tempDis = Discount[i]
        Discount[i] = Discount[min]
        Discount[min] = tempDis

        tempDescript = Description[i]
        Description[i] = Description[min]
        Description[min] = tempDescript

    return MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description


#Selection Sort Descending Functions

def SelectionSortDescending(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description):
    for i in range(0, len(MedicineName)):
        min = i
        for j in range(i + 1, len(MedicineName)):
            if MedicineName[min] > MedicineName[j]:
                min = j

        temp = MedicineName[i]
        MedicineName[i] = MedicineName[min]
        MedicineName[min] = temp

        tempOld = OldpriceInt[i]
        OldpriceInt[i] = OldpriceInt[min]
        OldpriceInt[min] = tempOld

        tempNew = NewPriceInt[i]
        NewPriceInt[i] = NewPriceInt[min]
        NewPriceInt[min] = tempNew

        tempQ = Quantity[i]
        Quantity[i] = Quantity[min]
        Quantity[min] = tempQ

        tempS = Stars[i]
        Stars[i] = Stars[min]
        Stars[min] = tempS

        tempR = RatingInt[i]
        RatingInt[i] = RatingInt[min]
        RatingInt[min] = tempR

        tempDis = Discount[i]
        Discount[i] = Discount[min]
        Discount[min] = tempDis

        tempDescript = Description[i]
        Description[i] = Description[min]
        Description[min] = tempDescript

    MedicineName.reverse()
    OldpriceInt.reverse()
    NewPriceInt.reverse()
    Quantity.reverse()
    Stars.reverse()
    RatingInt.reverse()
    Discount.reverse()
    Description.reverse()

    return MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description

def SelectionSortOldpriceDescending(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description):
    for i in range(0, len(OldpriceInt)):
        min = i
        for j in range(i + 1, len(OldpriceInt)):
            if OldpriceInt[min] > OldpriceInt[j]:
                min = j

        temp = MedicineName[i]
        MedicineName[i] = MedicineName[min]
        MedicineName[min] = temp

        tempOld = OldpriceInt[i]
        OldpriceInt[i] = OldpriceInt[min]
        OldpriceInt[min] = tempOld

        tempNew = NewPriceInt[i]
        NewPriceInt[i] = NewPriceInt[min]
        NewPriceInt[min] = tempNew

        tempQ = Quantity[i]
        Quantity[i] = Quantity[min]
        Quantity[min] = tempQ

        tempS = Stars[i]
        Stars[i] = Stars[min]
        Stars[min] = tempS

        tempR = RatingInt[i]
        RatingInt[i] = RatingInt[min]
        RatingInt[min] = tempR

        tempDis = Discount[i]
        Discount[i] = Discount[min]
        Discount[min] = tempDis

        tempDescript = Description[i]
        Description[i] = Description[min]
        Description[min] = tempDescript

    MedicineName.reverse()
    OldpriceInt.reverse()
    NewPriceInt.reverse()
    Quantity.reverse()
    Stars.reverse()
    RatingInt.reverse()
    Discount.reverse()
    Description.reverse()
    return MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description

def SelectionSortNewPriceDescending(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description):
    for i in range(0, len(NewPriceInt)):
        min = i
        for j in range(i + 1, len(NewPriceInt)):
            if NewPriceInt[min] > NewPriceInt[j]:
                min = j

        temp = MedicineName[i]
        MedicineName[i] = MedicineName[min]
        MedicineName[min] = temp

        tempOld = OldpriceInt[i]
        OldpriceInt[i] = OldpriceInt[min]
        OldpriceInt[min] = tempOld

        tempNew = NewPriceInt[i]
        NewPriceInt[i] = NewPriceInt[min]
        NewPriceInt[min] = tempNew

        tempQ = Quantity[i]
        Quantity[i] = Quantity[min]
        Quantity[min] = tempQ

        tempS = Stars[i]
        Stars[i] = Stars[min]
        Stars[min] = tempS

        tempR = RatingInt[i]
        RatingInt[i] = RatingInt[min]
        RatingInt[min] = tempR

        tempDis = Discount[i]
        Discount[i] = Discount[min]
        Discount[min] = tempDis

        tempDescript = Description[i]
        Description[i] = Description[min]
        Description[min] = tempDescript
    MedicineName.reverse()
    OldpriceInt.reverse()
    NewPriceInt.reverse()
    Quantity.reverse()
    Stars.reverse()
    RatingInt.reverse()
    Discount.reverse()
    Description.reverse()
    return MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description

def SelectionSortQuantityDescending(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description):
    for i in range(0, len(Quantity)):
        min = i
        for j in range(i + 1, len(Quantity)):
            if Quantity[min] > Quantity[j]:
                min = j

        temp = MedicineName[i]
        MedicineName[i] = MedicineName[min]
        MedicineName[min] = temp

        tempOld = OldpriceInt[i]
        OldpriceInt[i] = OldpriceInt[min]
        OldpriceInt[min] = tempOld

        tempNew = NewPriceInt[i]
        NewPriceInt[i] = NewPriceInt[min]
        NewPriceInt[min] = tempNew

        tempQ = Quantity[i]
        Quantity[i] = Quantity[min]
        Quantity[min] = tempQ

        tempS = Stars[i]
        Stars[i] = Stars[min]
        Stars[min] = tempS

        tempR = RatingInt[i]
        RatingInt[i] = RatingInt[min]
        RatingInt[min] = tempR

        tempDis = Discount[i]
        Discount[i] = Discount[min]
        Discount[min] = tempDis

        tempDescript = Description[i]
        Description[i] = Description[min]
        Description[min] = tempDescript

    MedicineName.reverse()
    OldpriceInt.reverse()
    NewPriceInt.reverse()
    Quantity.reverse()
    Stars.reverse()
    RatingInt.reverse()
    Discount.reverse()
    Description.reverse()
    return MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description

def SelectionSortStarsDescending(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description):
    for i in range(0, len(Stars)):
        min = i
        for j in range(i + 1, len(Stars)):
            if Stars[min] > Stars[j]:
                min = j

        temp = MedicineName[i]
        MedicineName[i] = MedicineName[min]
        MedicineName[min] = temp

        tempOld = OldpriceInt[i]
        OldpriceInt[i] = OldpriceInt[min]
        OldpriceInt[min] = tempOld

        tempNew = NewPriceInt[i]
        NewPriceInt[i] = NewPriceInt[min]
        NewPriceInt[min] = tempNew

        tempQ = Quantity[i]
        Quantity[i] = Quantity[min]
        Quantity[min] = tempQ

        tempS = Stars[i]
        Stars[i] = Stars[min]
        Stars[min] = tempS

        tempR = RatingInt[i]
        RatingInt[i] = RatingInt[min]
        RatingInt[min] = tempR

        tempDis = Discount[i]
        Discount[i] = Discount[min]
        Discount[min] = tempDis

        tempDescript = Description[i]
        Description[i] = Description[min]
        Description[min] = tempDescript

    MedicineName.reverse()
    OldpriceInt.reverse()
    NewPriceInt.reverse()
    Quantity.reverse()
    Stars.reverse()
    RatingInt.reverse()
    Discount.reverse()
    Description.reverse()
    return MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description

def SelectionSortRatingDescending(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description):
    for i in range(0, len(RatingInt)):
        min = i
        for j in range(i + 1, len(RatingInt)):
            if RatingInt[min] > RatingInt[j]:
                min = j

        temp = MedicineName[i]
        MedicineName[i] = MedicineName[min]
        MedicineName[min] = temp

        tempOld = OldpriceInt[i]
        OldpriceInt[i] = OldpriceInt[min]
        OldpriceInt[min] = tempOld

        tempNew = NewPriceInt[i]
        NewPriceInt[i] = NewPriceInt[min]
        NewPriceInt[min] = tempNew

        tempQ = Quantity[i]
        Quantity[i] = Quantity[min]
        Quantity[min] = tempQ

        tempS = Stars[i]
        Stars[i] = Stars[min]
        Stars[min] = tempS

        tempR = RatingInt[i]
        RatingInt[i] = RatingInt[min]
        RatingInt[min] = tempR

        tempDis = Discount[i]
        Discount[i] = Discount[min]
        Discount[min] = tempDis

        tempDescript = Description[i]
        Description[i] = Description[min]
        Description[min] = tempDescript

    MedicineName.reverse()
    OldpriceInt.reverse()
    NewPriceInt.reverse()
    Quantity.reverse()
    Stars.reverse()
    RatingInt.reverse()
    Discount.reverse()
    Description.reverse()
    return MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description

def SelectionSortDiscountDescending(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description):
    for i in range(0, len(Discount)):
        min = i
        for j in range(i + 1, len(Discount)):
            if Discount[min] > Discount[j]:
                min = j

        temp = MedicineName[i]
        MedicineName[i] = MedicineName[min]
        MedicineName[min] = temp

        tempOld = OldpriceInt[i]
        OldpriceInt[i] = OldpriceInt[min]
        OldpriceInt[min] = tempOld

        tempNew = NewPriceInt[i]
        NewPriceInt[i] = NewPriceInt[min]
        NewPriceInt[min] = tempNew

        tempQ = Quantity[i]
        Quantity[i] = Quantity[min]
        Quantity[min] = tempQ

        tempS = Stars[i]
        Stars[i] = Stars[min]
        Stars[min] = tempS

        tempR = RatingInt[i]
        RatingInt[i] = RatingInt[min]
        RatingInt[min] = tempR

        tempDis = Discount[i]
        Discount[i] = Discount[min]
        Discount[min] = tempDis

        tempDescript = Description[i]
        Description[i] = Description[min]
        Description[min] = tempDescript

    MedicineName.reverse()
    OldpriceInt.reverse()
    NewPriceInt.reverse()
    Quantity.reverse()
    Stars.reverse()
    RatingInt.reverse()
    Discount.reverse()
    Description.reverse()
    return MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description

def SelectionSortDescriptionDescending(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description):
    for i in range(0, len(Description)):
        min = i
        for j in range(i + 1, len(Description)):
            if Description[min] > Description[j]:
                min = j

        temp = MedicineName[i]
        MedicineName[i] = MedicineName[min]
        MedicineName[min] = temp

        tempOld = OldpriceInt[i]
        OldpriceInt[i] = OldpriceInt[min]
        OldpriceInt[min] = tempOld

        tempNew = NewPriceInt[i]
        NewPriceInt[i] = NewPriceInt[min]
        NewPriceInt[min] = tempNew

        tempQ = Quantity[i]
        Quantity[i] = Quantity[min]
        Quantity[min] = tempQ

        tempS = Stars[i]
        Stars[i] = Stars[min]
        Stars[min] = tempS

        tempR = RatingInt[i]
        RatingInt[i] = RatingInt[min]
        RatingInt[min] = tempR

        tempDis = Discount[i]
        Discount[i] = Discount[min]
        Discount[min] = tempDis

        tempDescript = Description[i]
        Description[i] = Description[min]
        Description[min] = tempDescript

    MedicineName.reverse()
    OldpriceInt.reverse()
    NewPriceInt.reverse()
    Quantity.reverse()
    Stars.reverse()
    RatingInt.reverse()
    Discount.reverse()
    Description.reverse()
    return MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description









def SelectionSortDescending(array):
    for i in range(0, len(array)):
        min = i
        for j in range(i + 1, len(array)):
            if array[min] > array[j]:
                min = j
        temp = array[i]
        array[i] = array[min]
        array[min] = temp
    array.reverse()
    return array