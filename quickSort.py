#Quick Sort Ascending Functions
def Partition(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description, left, right):
    i = left
    j = right-1 
    pivot = MedicineName[right]
    while i < j:
        while i < right and MedicineName[i] < pivot:  
            i += 1
        while j > left and MedicineName[j] >= pivot:  
            j -= 1
        if i < j:
            temp = MedicineName[i]
            MedicineName[i] = MedicineName[j]
            MedicineName[j] = temp

            temp = OldpriceInt[i]
            OldpriceInt[i] = OldpriceInt[j]
            OldpriceInt[j] = temp

            temp = NewPriceInt[i]
            NewPriceInt[i] = NewPriceInt[j]
            NewPriceInt[j] = temp

            temp = Quantity[i]
            Quantity[i] = Quantity[j]
            Quantity[j] = temp

            temp = Stars[i]
            Stars[i] = Stars[j]
            Stars[j] = temp

            temp = RatingInt[i]
            RatingInt[i] = RatingInt[j]
            RatingInt[j] = temp

            temp = Discount[i]
            Discount[i] = Discount[j]
            Discount[j] = temp

            temp = Description[i]
            Description[i] = Description[j]
            Description[j] = temp

    if MedicineName[i] > pivot:
        temp = MedicineName[i]
        MedicineName[i] = MedicineName[right]
        MedicineName[right] = temp

        temp = OldpriceInt[i]
        OldpriceInt[i] = OldpriceInt[right]
        OldpriceInt[right] = temp

        temp = NewPriceInt[i]
        NewPriceInt[i] = NewPriceInt[right]
        NewPriceInt[right] = temp

        temp = Quantity[i]
        Quantity[i] = Quantity[right]
        Quantity[right] = temp

        temp = Stars[i]
        Stars[i] = Stars[right]
        Stars[right] = temp

        temp = RatingInt[i]
        RatingInt[i] = RatingInt[right]
        RatingInt[right] = temp

        temp = Discount[i]
        Discount[i] = Discount[right]
        Discount[right] = temp

        temp = Description[i]
        Description[i] = Description[right]
        Description[right] = temp
    
    return i

def QuickSortAscending(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description, left, right):
    if left < right:
        part = Partition(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description, left, right)
        QuickSortAscending(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description, left, part - 1)
        QuickSortAscending(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description, part + 1, right)
        return MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description

def PartitionOldprice(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description, left, right):
    i = left
    j = right-1 
    pivot = OldpriceInt[right]
    while i < j:
        while i < right and OldpriceInt[i] < pivot:  
            i += 1
        while j > left and OldpriceInt[j] >= pivot:  
            j -= 1
        if i < j:
            temp = MedicineName[i]
            MedicineName[i] = MedicineName[j]
            MedicineName[j] = temp

            temp = OldpriceInt[i]
            OldpriceInt[i] = OldpriceInt[j]
            OldpriceInt[j] = temp

            temp = NewPriceInt[i]
            NewPriceInt[i] = NewPriceInt[j]
            NewPriceInt[j] = temp

            temp = Quantity[i]
            Quantity[i] = Quantity[j]
            Quantity[j] = temp

            temp = Stars[i]
            Stars[i] = Stars[j]
            Stars[j] = temp

            temp = RatingInt[i]
            RatingInt[i] = RatingInt[j]
            RatingInt[j] = temp

            temp = Discount[i]
            Discount[i] = Discount[j]
            Discount[j] = temp

            temp = Description[i]
            Description[i] = Description[j]
            Description[j] = temp

    if OldpriceInt[i] > pivot:
        temp = MedicineName[i]
        MedicineName[i] = MedicineName[right]
        MedicineName[right] = temp

        temp = OldpriceInt[i]
        OldpriceInt[i] = OldpriceInt[right]
        OldpriceInt[right] = temp

        temp = NewPriceInt[i]
        NewPriceInt[i] = NewPriceInt[right]
        NewPriceInt[right] = temp

        temp = Quantity[i]
        Quantity[i] = Quantity[right]
        Quantity[right] = temp

        temp = Stars[i]
        Stars[i] = Stars[right]
        Stars[right] = temp

        temp = RatingInt[i]
        RatingInt[i] = RatingInt[right]
        RatingInt[right] = temp

        temp = Discount[i]
        Discount[i] = Discount[right]
        Discount[right] = temp

        temp = Description[i]
        Description[i] = Description[right]
        Description[right] = temp
    
    return i

def QuickSortOldpriceAscending(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description, left, right):
    if left < right:
        part = PartitionOldprice(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description, left, right)
        QuickSortOldpriceAscending(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description, left, part - 1)
        QuickSortOldpriceAscending(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description, part + 1, right)
        return MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description

def PartitionNewPrice(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description, left, right):
    i = left
    j = right-1 
    pivot = NewPriceInt[right]
    while i < j:
        while i < right and NewPriceInt[i] < pivot:  
            i += 1
        while j > left and NewPriceInt[j] >= pivot:  
            j -= 1
        if i < j:
            temp = MedicineName[i]
            MedicineName[i] = MedicineName[j]
            MedicineName[j] = temp

            temp = OldpriceInt[i]
            OldpriceInt[i] = OldpriceInt[j]
            OldpriceInt[j] = temp

            temp = NewPriceInt[i]
            NewPriceInt[i] = NewPriceInt[j]
            NewPriceInt[j] = temp

            temp = Quantity[i]
            Quantity[i] = Quantity[j]
            Quantity[j] = temp

            temp = Stars[i]
            Stars[i] = Stars[j]
            Stars[j] = temp

            temp = RatingInt[i]
            RatingInt[i] = RatingInt[j]
            RatingInt[j] = temp

            temp = Discount[i]
            Discount[i] = Discount[j]
            Discount[j] = temp

            temp = Description[i]
            Description[i] = Description[j]
            Description[j] = temp

    if NewPriceInt[i] > pivot:
        temp = MedicineName[i]
        MedicineName[i] = MedicineName[right]
        MedicineName[right] = temp

        temp = OldpriceInt[i]
        OldpriceInt[i] = OldpriceInt[right]
        OldpriceInt[right] = temp

        temp = NewPriceInt[i]
        NewPriceInt[i] = NewPriceInt[right]
        NewPriceInt[right] = temp

        temp = Quantity[i]
        Quantity[i] = Quantity[right]
        Quantity[right] = temp

        temp = Stars[i]
        Stars[i] = Stars[right]
        Stars[right] = temp

        temp = RatingInt[i]
        RatingInt[i] = RatingInt[right]
        RatingInt[right] = temp

        temp = Discount[i]
        Discount[i] = Discount[right]
        Discount[right] = temp

        temp = Description[i]
        Description[i] = Description[right]
        Description[right] = temp
    
    return i

def QuickSortNewPriceAscending(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description, left, right):
    if left < right:
        part = PartitionNewPrice(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description, left, right)
        QuickSortNewPriceAscending(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description, left, part - 1)
        QuickSortNewPriceAscending(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description, part + 1, right)
        return MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description


def PartitionQuantity(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description, left, right):
    i = left
    j = right-1 
    pivot = Quantity[right]
    while i < j:
        while i < right and Quantity[i] < pivot:  
            i += 1
        while j > left and Quantity[j] >= pivot:  
            j -= 1
        if i < j:
            temp = MedicineName[i]
            MedicineName[i] = MedicineName[j]
            MedicineName[j] = temp

            temp = OldpriceInt[i]
            OldpriceInt[i] = OldpriceInt[j]
            OldpriceInt[j] = temp

            temp = NewPriceInt[i]
            NewPriceInt[i] = NewPriceInt[j]
            NewPriceInt[j] = temp

            temp = Quantity[i]
            Quantity[i] = Quantity[j]
            Quantity[j] = temp

            temp = Stars[i]
            Stars[i] = Stars[j]
            Stars[j] = temp

            temp = RatingInt[i]
            RatingInt[i] = RatingInt[j]
            RatingInt[j] = temp

            temp = Discount[i]
            Discount[i] = Discount[j]
            Discount[j] = temp

            temp = Description[i]
            Description[i] = Description[j]
            Description[j] = temp

    if Quantity[i] > pivot:
        temp = MedicineName[i]
        MedicineName[i] = MedicineName[right]
        MedicineName[right] = temp

        temp = OldpriceInt[i]
        OldpriceInt[i] = OldpriceInt[right]
        OldpriceInt[right] = temp

        temp = NewPriceInt[i]
        NewPriceInt[i] = NewPriceInt[right]
        NewPriceInt[right] = temp

        temp = Quantity[i]
        Quantity[i] = Quantity[right]
        Quantity[right] = temp

        temp = Stars[i]
        Stars[i] = Stars[right]
        Stars[right] = temp

        temp = RatingInt[i]
        RatingInt[i] = RatingInt[right]
        RatingInt[right] = temp

        temp = Discount[i]
        Discount[i] = Discount[right]
        Discount[right] = temp

        temp = Description[i]
        Description[i] = Description[right]
        Description[right] = temp
    
    return i

def QuickSortQuantityAscending(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description, left, right):
    if left < right:
        part = PartitionQuantity(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description, left, right)
        QuickSortQuantityAscending(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description, left, part - 1)
        QuickSortQuantityAscending(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description, part + 1, right)
        return MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description

def PartitionStars(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description, left, right):
    i = left
    j = right-1 
    pivot = Stars[right]
    while i < j:
        while i < right and Stars[i] < pivot:  
            i += 1
        while j > left and Stars[j] >= pivot:  
            j -= 1
        if i < j:
            temp = MedicineName[i]
            MedicineName[i] = MedicineName[j]
            MedicineName[j] = temp

            temp = OldpriceInt[i]
            OldpriceInt[i] = OldpriceInt[j]
            OldpriceInt[j] = temp

            temp = NewPriceInt[i]
            NewPriceInt[i] = NewPriceInt[j]
            NewPriceInt[j] = temp

            temp = Quantity[i]
            Quantity[i] = Quantity[j]
            Quantity[j] = temp

            temp = Stars[i]
            Stars[i] = Stars[j]
            Stars[j] = temp

            temp = RatingInt[i]
            RatingInt[i] = RatingInt[j]
            RatingInt[j] = temp

            temp = Discount[i]
            Discount[i] = Discount[j]
            Discount[j] = temp

            temp = Description[i]
            Description[i] = Description[j]
            Description[j] = temp

    if Stars[i] > pivot:
        temp = MedicineName[i]
        MedicineName[i] = MedicineName[right]
        MedicineName[right] = temp

        temp = OldpriceInt[i]
        OldpriceInt[i] = OldpriceInt[right]
        OldpriceInt[right] = temp

        temp = NewPriceInt[i]
        NewPriceInt[i] = NewPriceInt[right]
        NewPriceInt[right] = temp

        temp = Quantity[i]
        Quantity[i] = Quantity[right]
        Quantity[right] = temp

        temp = Stars[i]
        Stars[i] = Stars[right]
        Stars[right] = temp

        temp = RatingInt[i]
        RatingInt[i] = RatingInt[right]
        RatingInt[right] = temp

        temp = Discount[i]
        Discount[i] = Discount[right]
        Discount[right] = temp

        temp = Description[i]
        Description[i] = Description[right]
        Description[right] = temp
    
    return i

def QuickSortStarsAscending(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description, left, right):
    if left < right:
        part = PartitionStars(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description, left, right)
        QuickSortStarsAscending(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description, left, part - 1)
        QuickSortStarsAscending(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description, part + 1, right)
        return MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description

def PartitionRating(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description, left, right):
    i = left
    j = right-1 
    pivot = RatingInt[right]
    while i < j:
        while i < right and RatingInt[i] < pivot:  
            i += 1
        while j > left and RatingInt[j] >= pivot:  
            j -= 1
        if i < j:
            temp = MedicineName[i]
            MedicineName[i] = MedicineName[j]
            MedicineName[j] = temp

            temp = OldpriceInt[i]
            OldpriceInt[i] = OldpriceInt[j]
            OldpriceInt[j] = temp

            temp = NewPriceInt[i]
            NewPriceInt[i] = NewPriceInt[j]
            NewPriceInt[j] = temp

            temp = Quantity[i]
            Quantity[i] = Quantity[j]
            Quantity[j] = temp

            temp = Stars[i]
            Stars[i] = Stars[j]
            Stars[j] = temp

            temp = RatingInt[i]
            RatingInt[i] = RatingInt[j]
            RatingInt[j] = temp

            temp = Discount[i]
            Discount[i] = Discount[j]
            Discount[j] = temp

            temp = Description[i]
            Description[i] = Description[j]
            Description[j] = temp

    if RatingInt[i] > pivot:
        temp = MedicineName[i]
        MedicineName[i] = MedicineName[right]
        MedicineName[right] = temp

        temp = OldpriceInt[i]
        OldpriceInt[i] = OldpriceInt[right]
        OldpriceInt[right] = temp

        temp = NewPriceInt[i]
        NewPriceInt[i] = NewPriceInt[right]
        NewPriceInt[right] = temp

        temp = Quantity[i]
        Quantity[i] = Quantity[right]
        Quantity[right] = temp

        temp = Stars[i]
        Stars[i] = Stars[right]
        Stars[right] = temp

        temp = RatingInt[i]
        RatingInt[i] = RatingInt[right]
        RatingInt[right] = temp

        temp = Discount[i]
        Discount[i] = Discount[right]
        Discount[right] = temp

        temp = Description[i]
        Description[i] = Description[right]
        Description[right] = temp
    
    return i

def QuickSortRatingAscending(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description, left, right):
    if left < right:
        part = PartitionRating(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description, left, right)
        QuickSortRatingAscending(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description, left, part - 1)
        QuickSortRatingAscending(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description, part + 1, right)
        return MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description

def PartitionDiscount(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description, left, right):
    i = left
    j = right-1 
    pivot = Discount[right]
    while i < j:
        while i < right and Discount[i] < pivot:  
            i += 1
        while j > left and Discount[j] >= pivot:  
            j -= 1
        if i < j:
            temp = MedicineName[i]
            MedicineName[i] = MedicineName[j]
            MedicineName[j] = temp

            temp = OldpriceInt[i]
            OldpriceInt[i] = OldpriceInt[j]
            OldpriceInt[j] = temp

            temp = NewPriceInt[i]
            NewPriceInt[i] = NewPriceInt[j]
            NewPriceInt[j] = temp

            temp = Quantity[i]
            Quantity[i] = Quantity[j]
            Quantity[j] = temp

            temp = Stars[i]
            Stars[i] = Stars[j]
            Stars[j] = temp

            temp = RatingInt[i]
            RatingInt[i] = RatingInt[j]
            RatingInt[j] = temp

            temp = Discount[i]
            Discount[i] = Discount[j]
            Discount[j] = temp

            temp = Description[i]
            Description[i] = Description[j]
            Description[j] = temp

    if Discount[i] > pivot:
        temp = MedicineName[i]
        MedicineName[i] = MedicineName[right]
        MedicineName[right] = temp

        temp = OldpriceInt[i]
        OldpriceInt[i] = OldpriceInt[right]
        OldpriceInt[right] = temp

        temp = NewPriceInt[i]
        NewPriceInt[i] = NewPriceInt[right]
        NewPriceInt[right] = temp

        temp = Quantity[i]
        Quantity[i] = Quantity[right]
        Quantity[right] = temp

        temp = Stars[i]
        Stars[i] = Stars[right]
        Stars[right] = temp

        temp = RatingInt[i]
        RatingInt[i] = RatingInt[right]
        RatingInt[right] = temp

        temp = Discount[i]
        Discount[i] = Discount[right]
        Discount[right] = temp

        temp = Description[i]
        Description[i] = Description[right]
        Description[right] = temp
    
    return i

def QuickSortDiscountAscending(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description, left, right):
    if left < right:
        part = PartitionDiscount(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description, left, right)
        QuickSortDiscountAscending(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description, left, part - 1)
        QuickSortDiscountAscending(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description, part + 1, right)
        return MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description

def PartitionDescription(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description, left, right):
    i = left
    j = right-1 
    pivot = Description[right]
    while i < j:
        while i < right and Description[i] < pivot:  
            i += 1
        while j > left and Description[j] >= pivot:  
            j -= 1
        if i < j:
            temp = MedicineName[i]
            MedicineName[i] = MedicineName[j]
            MedicineName[j] = temp

            temp = OldpriceInt[i]
            OldpriceInt[i] = OldpriceInt[j]
            OldpriceInt[j] = temp

            temp = NewPriceInt[i]
            NewPriceInt[i] = NewPriceInt[j]
            NewPriceInt[j] = temp

            temp = Quantity[i]
            Quantity[i] = Quantity[j]
            Quantity[j] = temp

            temp = Stars[i]
            Stars[i] = Stars[j]
            Stars[j] = temp

            temp = RatingInt[i]
            RatingInt[i] = RatingInt[j]
            RatingInt[j] = temp

            temp = Discount[i]
            Discount[i] = Discount[j]
            Discount[j] = temp

            temp = Description[i]
            Description[i] = Description[j]
            Description[j] = temp

    if Description[i] > pivot:
        temp = MedicineName[i]
        MedicineName[i] = MedicineName[right]
        MedicineName[right] = temp

        temp = OldpriceInt[i]
        OldpriceInt[i] = OldpriceInt[right]
        OldpriceInt[right] = temp

        temp = NewPriceInt[i]
        NewPriceInt[i] = NewPriceInt[right]
        NewPriceInt[right] = temp

        temp = Quantity[i]
        Quantity[i] = Quantity[right]
        Quantity[right] = temp

        temp = Stars[i]
        Stars[i] = Stars[right]
        Stars[right] = temp

        temp = RatingInt[i]
        RatingInt[i] = RatingInt[right]
        RatingInt[right] = temp

        temp = Discount[i]
        Discount[i] = Discount[right]
        Discount[right] = temp

        temp = Description[i]
        Description[i] = Description[right]
        Description[right] = temp
    
    return i

def QuickSortDescriptionAscending(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description, left, right):
    if left < right:
        part = PartitionDescription(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description, left, right)
        QuickSortDescriptionAscending(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description, left, part - 1)
        QuickSortDescriptionAscending(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description, part + 1, right)
        return MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description


#Quick Sort Descending Functions
def PartitionDescending(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description, left, right):
    i = left
    j = right-1 
    pivot = MedicineName[right]
    while i < j:
        while i < right and MedicineName[i] > pivot:  
            i += 1
        while j > left and MedicineName[j] <= pivot:  
            j -= 1
        if i < j:
            temp = MedicineName[i]
            MedicineName[i] = MedicineName[j]
            MedicineName[j] = temp

            temp = OldpriceInt[i]
            OldpriceInt[i] = OldpriceInt[j]
            OldpriceInt[j] = temp

            temp = NewPriceInt[i]
            NewPriceInt[i] = NewPriceInt[j]
            NewPriceInt[j] = temp

            temp = Quantity[i]
            Quantity[i] = Quantity[j]
            Quantity[j] = temp

            temp = Stars[i]
            Stars[i] = Stars[j]
            Stars[j] = temp

            temp = RatingInt[i]
            RatingInt[i] = RatingInt[j]
            RatingInt[j] = temp

            temp = Discount[i]
            Discount[i] = Discount[j]
            Discount[j] = temp

            temp = Description[i]
            Description[i] = Description[j]
            Description[j] = temp

    if MedicineName[i] < pivot:
        temp = MedicineName[i]
        MedicineName[i] = MedicineName[right]
        MedicineName[right] = temp

        temp = OldpriceInt[i]
        OldpriceInt[i] = OldpriceInt[right]
        OldpriceInt[right] = temp

        temp = NewPriceInt[i]
        NewPriceInt[i] = NewPriceInt[right]
        NewPriceInt[right] = temp

        temp = Quantity[i]
        Quantity[i] = Quantity[right]
        Quantity[right] = temp

        temp = Stars[i]
        Stars[i] = Stars[right]
        Stars[right] = temp

        temp = RatingInt[i]
        RatingInt[i] = RatingInt[right]
        RatingInt[right] = temp

        temp = Discount[i]
        Discount[i] = Discount[right]
        Discount[right] = temp

        temp = Description[i]
        Description[i] = Description[right]
        Description[right] = temp
    
    return i

def QuickSortDescending(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description, left, right):
    if left < right:
        part = PartitionDescending(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description, left, right)
        QuickSortDescending(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description, left, part - 1)
        QuickSortDescending(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description, part + 1, right)
        return MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description

def PartitionOldpriceDescending(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description, left, right):
    i = left
    j = right-1 
    pivot = OldpriceInt[right]
    while i < j:
        while i < right and OldpriceInt[i] > pivot:  
            i += 1
        while j > left and OldpriceInt[j] <= pivot:  
            j -= 1
        if i < j:
            temp = MedicineName[i]
            MedicineName[i] = MedicineName[j]
            MedicineName[j] = temp

            temp = OldpriceInt[i]
            OldpriceInt[i] = OldpriceInt[j]
            OldpriceInt[j] = temp

            temp = NewPriceInt[i]
            NewPriceInt[i] = NewPriceInt[j]
            NewPriceInt[j] = temp

            temp = Quantity[i]
            Quantity[i] = Quantity[j]
            Quantity[j] = temp

            temp = Stars[i]
            Stars[i] = Stars[j]
            Stars[j] = temp

            temp = RatingInt[i]
            RatingInt[i] = RatingInt[j]
            RatingInt[j] = temp

            temp = Discount[i]
            Discount[i] = Discount[j]
            Discount[j] = temp

            temp = Description[i]
            Description[i] = Description[j]
            Description[j] = temp

    if OldpriceInt[i] < pivot:
        temp = MedicineName[i]
        MedicineName[i] = MedicineName[right]
        MedicineName[right] = temp

        temp = OldpriceInt[i]
        OldpriceInt[i] = OldpriceInt[right]
        OldpriceInt[right] = temp

        temp = NewPriceInt[i]
        NewPriceInt[i] = NewPriceInt[right]
        NewPriceInt[right] = temp

        temp = Quantity[i]
        Quantity[i] = Quantity[right]
        Quantity[right] = temp

        temp = Stars[i]
        Stars[i] = Stars[right]
        Stars[right] = temp

        temp = RatingInt[i]
        RatingInt[i] = RatingInt[right]
        RatingInt[right] = temp

        temp = Discount[i]
        Discount[i] = Discount[right]
        Discount[right] = temp

        temp = Description[i]
        Description[i] = Description[right]
        Description[right] = temp
    
    return i

def QuickSortOldpriceDescending(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description, left, right):
    if left < right:
        part = PartitionOldpriceDescending(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description, left, right)
        QuickSortOldpriceDescending(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description, left, part - 1)
        QuickSortOldpriceDescending(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description, part + 1, right)
        return MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description

def PartitionNewPriceDescending(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description, left, right):
    i = left
    j = right-1 
    pivot = NewPriceInt[right]
    while i < j:
        while i < right and NewPriceInt[i] > pivot:  
            i += 1
        while j > left and NewPriceInt[j] <= pivot:  
            j -= 1
        if i < j:
            temp = MedicineName[i]
            MedicineName[i] = MedicineName[j]
            MedicineName[j] = temp

            temp = OldpriceInt[i]
            OldpriceInt[i] = OldpriceInt[j]
            OldpriceInt[j] = temp

            temp = NewPriceInt[i]
            NewPriceInt[i] = NewPriceInt[j]
            NewPriceInt[j] = temp

            temp = Quantity[i]
            Quantity[i] = Quantity[j]
            Quantity[j] = temp

            temp = Stars[i]
            Stars[i] = Stars[j]
            Stars[j] = temp

            temp = RatingInt[i]
            RatingInt[i] = RatingInt[j]
            RatingInt[j] = temp

            temp = Discount[i]
            Discount[i] = Discount[j]
            Discount[j] = temp

            temp = Description[i]
            Description[i] = Description[j]
            Description[j] = temp

    if NewPriceInt[i] < pivot:
        temp = MedicineName[i]
        MedicineName[i] = MedicineName[right]
        MedicineName[right] = temp

        temp = OldpriceInt[i]
        OldpriceInt[i] = OldpriceInt[right]
        OldpriceInt[right] = temp

        temp = NewPriceInt[i]
        NewPriceInt[i] = NewPriceInt[right]
        NewPriceInt[right] = temp

        temp = Quantity[i]
        Quantity[i] = Quantity[right]
        Quantity[right] = temp

        temp = Stars[i]
        Stars[i] = Stars[right]
        Stars[right] = temp

        temp = RatingInt[i]
        RatingInt[i] = RatingInt[right]
        RatingInt[right] = temp

        temp = Discount[i]
        Discount[i] = Discount[right]
        Discount[right] = temp

        temp = Description[i]
        Description[i] = Description[right]
        Description[right] = temp
    
    return i

def QuickSortNewPriceDescending(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description, left, right):
    if left < right:
        part = PartitionNewPriceDescending(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description, left, right)
        QuickSortNewPriceDescending(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description, left, part - 1)
        QuickSortNewPriceDescending(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description, part + 1, right)
        return MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description


def PartitionQuantityDescending(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description, left, right):
    i = left
    j = right-1 
    pivot = Quantity[right]
    while i < j:
        while i < right and Quantity[i] > pivot:  
            i += 1
        while j > left and Quantity[j] <= pivot:  
            j -= 1
        if i < j:
            temp = MedicineName[i]
            MedicineName[i] = MedicineName[j]
            MedicineName[j] = temp

            temp = OldpriceInt[i]
            OldpriceInt[i] = OldpriceInt[j]
            OldpriceInt[j] = temp

            temp = NewPriceInt[i]
            NewPriceInt[i] = NewPriceInt[j]
            NewPriceInt[j] = temp

            temp = Quantity[i]
            Quantity[i] = Quantity[j]
            Quantity[j] = temp

            temp = Stars[i]
            Stars[i] = Stars[j]
            Stars[j] = temp

            temp = RatingInt[i]
            RatingInt[i] = RatingInt[j]
            RatingInt[j] = temp

            temp = Discount[i]
            Discount[i] = Discount[j]
            Discount[j] = temp

            temp = Description[i]
            Description[i] = Description[j]
            Description[j] = temp

    if Quantity[i] < pivot:
        temp = MedicineName[i]
        MedicineName[i] = MedicineName[right]
        MedicineName[right] = temp

        temp = OldpriceInt[i]
        OldpriceInt[i] = OldpriceInt[right]
        OldpriceInt[right] = temp

        temp = NewPriceInt[i]
        NewPriceInt[i] = NewPriceInt[right]
        NewPriceInt[right] = temp

        temp = Quantity[i]
        Quantity[i] = Quantity[right]
        Quantity[right] = temp

        temp = Stars[i]
        Stars[i] = Stars[right]
        Stars[right] = temp

        temp = RatingInt[i]
        RatingInt[i] = RatingInt[right]
        RatingInt[right] = temp

        temp = Discount[i]
        Discount[i] = Discount[right]
        Discount[right] = temp

        temp = Description[i]
        Description[i] = Description[right]
        Description[right] = temp
    
    return i

def QuickSortQuantityDescending(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description, left, right):
    if left < right:
        part = PartitionQuantityDescending(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description, left, right)
        QuickSortQuantityDescending(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description, left, part - 1)
        QuickSortQuantityDescending(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description, part + 1, right)
        return MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description

def PartitionStarsDescending(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description, left, right):
    i = left
    j = right-1 
    pivot = Stars[right]
    while i < j:
        while i < right and Stars[i] > pivot:  
            i += 1
        while j > left and Stars[j] <= pivot:  
            j -= 1
        if i < j:
            temp = MedicineName[i]
            MedicineName[i] = MedicineName[j]
            MedicineName[j] = temp

            temp = OldpriceInt[i]
            OldpriceInt[i] = OldpriceInt[j]
            OldpriceInt[j] = temp

            temp = NewPriceInt[i]
            NewPriceInt[i] = NewPriceInt[j]
            NewPriceInt[j] = temp

            temp = Quantity[i]
            Quantity[i] = Quantity[j]
            Quantity[j] = temp

            temp = Stars[i]
            Stars[i] = Stars[j]
            Stars[j] = temp

            temp = RatingInt[i]
            RatingInt[i] = RatingInt[j]
            RatingInt[j] = temp

            temp = Discount[i]
            Discount[i] = Discount[j]
            Discount[j] = temp

            temp = Description[i]
            Description[i] = Description[j]
            Description[j] = temp

    if Stars[i] < pivot:
        temp = MedicineName[i]
        MedicineName[i] = MedicineName[right]
        MedicineName[right] = temp

        temp = OldpriceInt[i]
        OldpriceInt[i] = OldpriceInt[right]
        OldpriceInt[right] = temp

        temp = NewPriceInt[i]
        NewPriceInt[i] = NewPriceInt[right]
        NewPriceInt[right] = temp

        temp = Quantity[i]
        Quantity[i] = Quantity[right]
        Quantity[right] = temp

        temp = Stars[i]
        Stars[i] = Stars[right]
        Stars[right] = temp

        temp = RatingInt[i]
        RatingInt[i] = RatingInt[right]
        RatingInt[right] = temp

        temp = Discount[i]
        Discount[i] = Discount[right]
        Discount[right] = temp

        temp = Description[i]
        Description[i] = Description[right]
        Description[right] = temp
    
    return i

def QuickSortStarsDescending(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description, left, right):
    if left < right:
        part = PartitionStarsDescending(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description, left, right)
        QuickSortStarsDescending(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description, left, part - 1)
        QuickSortStarsDescending(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description, part + 1, right)
        return MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description

def PartitionRatingDescending(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description, left, right):
    i = left
    j = right-1 
    pivot = RatingInt[right]
    while i < j:
        while i < right and RatingInt[i] > pivot:  
            i += 1
        while j > left and RatingInt[j] <= pivot:  
            j -= 1
        if i < j:
            temp = MedicineName[i]
            MedicineName[i] = MedicineName[j]
            MedicineName[j] = temp

            temp = OldpriceInt[i]
            OldpriceInt[i] = OldpriceInt[j]
            OldpriceInt[j] = temp

            temp = NewPriceInt[i]
            NewPriceInt[i] = NewPriceInt[j]
            NewPriceInt[j] = temp

            temp = Quantity[i]
            Quantity[i] = Quantity[j]
            Quantity[j] = temp

            temp = Stars[i]
            Stars[i] = Stars[j]
            Stars[j] = temp

            temp = RatingInt[i]
            RatingInt[i] = RatingInt[j]
            RatingInt[j] = temp

            temp = Discount[i]
            Discount[i] = Discount[j]
            Discount[j] = temp

            temp = Description[i]
            Description[i] = Description[j]
            Description[j] = temp

    if RatingInt[i] < pivot:
        temp = MedicineName[i]
        MedicineName[i] = MedicineName[right]
        MedicineName[right] = temp

        temp = OldpriceInt[i]
        OldpriceInt[i] = OldpriceInt[right]
        OldpriceInt[right] = temp

        temp = NewPriceInt[i]
        NewPriceInt[i] = NewPriceInt[right]
        NewPriceInt[right] = temp

        temp = Quantity[i]
        Quantity[i] = Quantity[right]
        Quantity[right] = temp

        temp = Stars[i]
        Stars[i] = Stars[right]
        Stars[right] = temp

        temp = RatingInt[i]
        RatingInt[i] = RatingInt[right]
        RatingInt[right] = temp

        temp = Discount[i]
        Discount[i] = Discount[right]
        Discount[right] = temp

        temp = Description[i]
        Description[i] = Description[right]
        Description[right] = temp
    
    return i

def QuickSortRatingDescending(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description, left, right):
    if left < right:
        part = PartitionRatingDescending(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description, left, right)
        QuickSortRatingDescending(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description, left, part - 1)
        QuickSortRatingDescending(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description, part + 1, right)
        return MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description

def PartitionDiscountDescending(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description, left, right):
    i = left
    j = right-1 
    pivot = Discount[right]
    while i < j:
        while i < right and Discount[i] > pivot:  
            i += 1
        while j > left and Discount[j] <= pivot:  
            j -= 1
        if i < j:
            temp = MedicineName[i]
            MedicineName[i] = MedicineName[j]
            MedicineName[j] = temp

            temp = OldpriceInt[i]
            OldpriceInt[i] = OldpriceInt[j]
            OldpriceInt[j] = temp

            temp = NewPriceInt[i]
            NewPriceInt[i] = NewPriceInt[j]
            NewPriceInt[j] = temp

            temp = Quantity[i]
            Quantity[i] = Quantity[j]
            Quantity[j] = temp

            temp = Stars[i]
            Stars[i] = Stars[j]
            Stars[j] = temp

            temp = RatingInt[i]
            RatingInt[i] = RatingInt[j]
            RatingInt[j] = temp

            temp = Discount[i]
            Discount[i] = Discount[j]
            Discount[j] = temp

            temp = Description[i]
            Description[i] = Description[j]
            Description[j] = temp

    if Discount[i] < pivot:
        temp = MedicineName[i]
        MedicineName[i] = MedicineName[right]
        MedicineName[right] = temp

        temp = OldpriceInt[i]
        OldpriceInt[i] = OldpriceInt[right]
        OldpriceInt[right] = temp

        temp = NewPriceInt[i]
        NewPriceInt[i] = NewPriceInt[right]
        NewPriceInt[right] = temp

        temp = Quantity[i]
        Quantity[i] = Quantity[right]
        Quantity[right] = temp

        temp = Stars[i]
        Stars[i] = Stars[right]
        Stars[right] = temp

        temp = RatingInt[i]
        RatingInt[i] = RatingInt[right]
        RatingInt[right] = temp

        temp = Discount[i]
        Discount[i] = Discount[right]
        Discount[right] = temp

        temp = Description[i]
        Description[i] = Description[right]
        Description[right] = temp
    
    return i

def QuickSortDiscountDescending(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description, left, right):
    if left < right:
        part = PartitionDiscountDescending(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description, left, right)
        QuickSortDiscountDescending(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description, left, part - 1)
        QuickSortDiscountDescending(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description, part + 1, right)
        return MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description

def PartitionDescriptionDescending(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description, left, right):
    i = left
    j = right-1 
    pivot = Description[right]
    while i < j:
        while i < right and Description[i] > pivot:  
            i += 1
        while j > left and Description[j] <= pivot:  
            j -= 1
        if i < j:
            temp = MedicineName[i]
            MedicineName[i] = MedicineName[j]
            MedicineName[j] = temp

            temp = OldpriceInt[i]
            OldpriceInt[i] = OldpriceInt[j]
            OldpriceInt[j] = temp

            temp = NewPriceInt[i]
            NewPriceInt[i] = NewPriceInt[j]
            NewPriceInt[j] = temp

            temp = Quantity[i]
            Quantity[i] = Quantity[j]
            Quantity[j] = temp

            temp = Stars[i]
            Stars[i] = Stars[j]
            Stars[j] = temp

            temp = RatingInt[i]
            RatingInt[i] = RatingInt[j]
            RatingInt[j] = temp

            temp = Discount[i]
            Discount[i] = Discount[j]
            Discount[j] = temp

            temp = Description[i]
            Description[i] = Description[j]
            Description[j] = temp

    if Description[i] < pivot:
        temp = MedicineName[i]
        MedicineName[i] = MedicineName[right]
        MedicineName[right] = temp

        temp = OldpriceInt[i]
        OldpriceInt[i] = OldpriceInt[right]
        OldpriceInt[right] = temp

        temp = NewPriceInt[i]
        NewPriceInt[i] = NewPriceInt[right]
        NewPriceInt[right] = temp

        temp = Quantity[i]
        Quantity[i] = Quantity[right]
        Quantity[right] = temp

        temp = Stars[i]
        Stars[i] = Stars[right]
        Stars[right] = temp

        temp = RatingInt[i]
        RatingInt[i] = RatingInt[right]
        RatingInt[right] = temp

        temp = Discount[i]
        Discount[i] = Discount[right]
        Discount[right] = temp

        temp = Description[i]
        Description[i] = Description[right]
        Description[right] = temp
    
    return i

def QuickSortDescriptionDescending(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description, left, right):
    if left < right:
        part = PartitionDescriptionDescending(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description, left, right)
        QuickSortDescriptionDescending(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description, left, part - 1)
        QuickSortDescriptionDescending(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description, part + 1, right)
        return MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description