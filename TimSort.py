#Tim Sort Ascending Function
import mergeSort
def calcMinRun(n):
    MIN_MERGE = 10000000
    r = 0
    while n >= MIN_MERGE:
        r |= n & 1
        n >= 1
    return n + r
 
def insertionSort(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description, left, right):
    for i in range(left + 1, right + 1):
        j = i
        while j > left and MedicineName[j] < MedicineName[j - 1]:
            temp = MedicineName[j]
            MedicineName[j] = MedicineName[j-1]
            MedicineName[j-1] = temp

            tempOld = OldpriceInt[j]
            OldpriceInt[j] = OldpriceInt[j-1]
            OldpriceInt[j-1] = tempOld

            tempNew = NewPriceInt[j]
            NewPriceInt[j] = NewPriceInt[j-1]
            NewPriceInt[j-1] = tempNew

            tempQ = Quantity[j]
            Quantity[j] = Quantity[j-1]
            Quantity[j-1] = tempQ

            tempS = Stars[j]
            Stars[j] = Stars[j-1]
            Stars[j-1] = tempS

            tempR = RatingInt[j]
            RatingInt[j] = RatingInt[j-1]
            RatingInt[j-1] = tempR

            tempDis = Discount[j]
            Discount[j] = Discount[j-1]
            Discount[j-1] = tempDis

            tempDescript = Description[j]
            Description[j] = Description[j-1]
            Description[j-1] = tempDescript

            j =j - 1
 
def merge(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description, l, m, r):
    len1 = m - l + 1
    len2 =  r - m
    L = []
    R = []
    LOld = []
    ROld = []
    LNew = []
    RNew = []
    LQ = []
    RQ = []
    LS = []
    RS = []
    LR = []
    RR = []
    LDis = []
    RDis = []
    LDescript = []
    RDescript = []

    for i in range(0, len1):
        L.append(MedicineName[l + i])
        LOld.append(OldpriceInt[l + i])
        LNew.append(NewPriceInt[l + i])
        LQ.append(Quantity[l + i])
        LS.append(Stars[l + i])
        LR.append(RatingInt[l + i])
        LDis.append(Discount[l + i])
        LDescript.append(Description[l + i])

    for i in range(0, len2):
        R.append(MedicineName[m + 1 + j])
        ROld.append(OldpriceInt[m + 1 + j])
        RNew.append(NewPriceInt[m + 1 + j])
        RQ.append(Quantity[m + 1 + j])
        RS.append(Stars[m + 1 + j])
        RR.append(RatingInt[m + 1 + j])
        RDis.append(Discount[m + 1 + j])
        RDescript.append(Description[m + 1 + j])
 
    i = 0
    j = 0
    k = l
 
    while i < len1 and j < len2:
        if L[i] <= R[j]:
            MedicineName[k] = L[i]
            OldpriceInt[k] = LOld[i]
            NewPriceInt[k] = LNew[i]
            Quantity[k] = LQ[i]
            Stars[k] = LS[i]
            RatingInt[k] = LR[i]
            Discount[k] = LDis[i]
            Description[k] = LDescript[i]
            i =i + 1
 
        else:
            MedicineName[k] = R[j]
            OldpriceInt[k] = ROld[j]
            NewPriceInt[k] = RNew[j]
            Quantity[k] = RQ[j]
            Stars[k] = RS[j]
            RatingInt[k] = RR[j]
            Discount[k] = RDis[j]
            Description[k] = RDescript[j]
            j =j + 1
 
        k = k + 1
 
    while i < len1:
        MedicineName[k] = L[i]
        OldpriceInt[k] = LOld[i]
        NewPriceInt[k] = LNew[i]
        Quantity[k] = LQ[i]
        Stars[k] = LS[i]
        RatingInt[k] = LR[i]
        Discount[k] = LDis[i]
        Description[k] = LDescript[i]
        k = k + 1
        i = i + 1
 
    while j < len2:
        MedicineName[k] = R[j]
        OldpriceInt[k] = ROld[j]
        NewPriceInt[k] = RNew[j]
        Quantity[k] = RQ[j]
        Stars[k] = RS[j]
        RatingInt[k] = RR[j]
        Discount[k] = RDis[j]
        Description[k] = RDescript[j]
        k = k + 1
        j = j + 1
 
 
def timSortAscending(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description):
    n = len(MedicineName)
    minRun = calcMinRun(n)

    for start in range(0, n, minRun):
        end = min(start + minRun - 1, n - 1)
        insertionSort(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description, start, end)
 
    size = minRun
    while size < n:
        for left in range(0, n, 2 * size):
            mid = min(n - 1, left + size - 1)
            right = min((left + 2 * size - 1), (n - 1))
 
            if mid < right:
                merge(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description, left, mid, right)
 
        size = 2 * size
    return MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description
 
def insertionSortOldprice(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description, left, right):
    for i in range(left + 1, right + 1):
        j = i
        while j > left and OldpriceInt[j] < OldpriceInt[j - 1]:
            temp = MedicineName[j]
            MedicineName[j] = MedicineName[j-1]
            MedicineName[j-1] = temp

            tempOld = OldpriceInt[j]
            OldpriceInt[j] = OldpriceInt[j-1]
            OldpriceInt[j-1] = tempOld

            tempNew = NewPriceInt[j]
            NewPriceInt[j] = NewPriceInt[j-1]
            NewPriceInt[j-1] = tempNew

            tempQ = Quantity[j]
            Quantity[j] = Quantity[j-1]
            Quantity[j-1] = tempQ

            tempS = Stars[j]
            Stars[j] = Stars[j-1]
            Stars[j-1] = tempS

            tempR = RatingInt[j]
            RatingInt[j] = RatingInt[j-1]
            RatingInt[j-1] = tempR

            tempDis = Discount[j]
            Discount[j] = Discount[j-1]
            Discount[j-1] = tempDis

            tempDescript = Description[j]
            Description[j] = Description[j-1]
            Description[j-1] = tempDescript

            j =j - 1
 
def timSortOldpriceAscending(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description):
    n = len(OldpriceInt)
    minRun = calcMinRun(n)

    for start in range(0, n, minRun):
        end = min(start + minRun - 1, n - 1)
        insertionSortOldprice(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description, start, end)
 
    size = minRun
    while size < n:
        for left in range(0, n, 2 * size):
            mid = min(n - 1, left + size - 1)
            right = min((left + 2 * size - 1), (n - 1))
 
            if mid < right:
                mergeSort.MergeOldpricemerge(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description, left, mid, right)
 
        size = 2 * size
    return MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description

def insertionSortNewPrice(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description, left, right):
    for i in range(left + 1, right + 1):
        j = i
        while j > left and NewPriceInt[j] < NewPriceInt[j - 1]:
            temp = MedicineName[j]
            MedicineName[j] = MedicineName[j-1]
            MedicineName[j-1] = temp

            tempOld = OldpriceInt[j]
            OldpriceInt[j] = OldpriceInt[j-1]
            OldpriceInt[j-1] = tempOld

            tempNew = NewPriceInt[j]
            NewPriceInt[j] = NewPriceInt[j-1]
            NewPriceInt[j-1] = tempNew

            tempQ = Quantity[j]
            Quantity[j] = Quantity[j-1]
            Quantity[j-1] = tempQ

            tempS = Stars[j]
            Stars[j] = Stars[j-1]
            Stars[j-1] = tempS

            tempR = RatingInt[j]
            RatingInt[j] = RatingInt[j-1]
            RatingInt[j-1] = tempR

            tempDis = Discount[j]
            Discount[j] = Discount[j-1]
            Discount[j-1] = tempDis

            tempDescript = Description[j]
            Description[j] = Description[j-1]
            Description[j-1] = tempDescript

            j =j - 1
 
def timSortNewPriceAscending(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description):
    n = len(NewPriceInt)
    minRun = calcMinRun(n)

    for start in range(0, n, minRun):
        end = min(start + minRun - 1, n - 1)
        insertionSortNewPrice(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description, start, end)
 
    size = minRun
    while size < n:
        for left in range(0, n, 2 * size):
            mid = min(n - 1, left + size - 1)
            right = min((left + 2 * size - 1), (n - 1))
 
            if mid < right:
                mergeSort.MergeSortNewPrice(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description, left, mid, right)
 
        size = 2 * size
    return MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description

def insertionSortQuantity(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description, left, right):
    for i in range(left + 1, right + 1):
        j = i
        while j > left and Quantity[j] < Quantity[j - 1]:
            temp = MedicineName[j]
            MedicineName[j] = MedicineName[j-1]
            MedicineName[j-1] = temp

            tempOld = OldpriceInt[j]
            OldpriceInt[j] = OldpriceInt[j-1]
            OldpriceInt[j-1] = tempOld

            tempNew = NewPriceInt[j]
            NewPriceInt[j] = NewPriceInt[j-1]
            NewPriceInt[j-1] = tempNew

            tempQ = Quantity[j]
            Quantity[j] = Quantity[j-1]
            Quantity[j-1] = tempQ

            tempS = Stars[j]
            Stars[j] = Stars[j-1]
            Stars[j-1] = tempS

            tempR = RatingInt[j]
            RatingInt[j] = RatingInt[j-1]
            RatingInt[j-1] = tempR

            tempDis = Discount[j]
            Discount[j] = Discount[j-1]
            Discount[j-1] = tempDis

            tempDescript = Description[j]
            Description[j] = Description[j-1]
            Description[j-1] = tempDescript

            j =j - 1
 
def timSortQuantityAscending(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description):
    n = len(Quantity)
    minRun = calcMinRun(n)

    for start in range(0, n, minRun):
        end = min(start + minRun - 1, n - 1)
        insertionSortQuantity(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description, start, end)
 
    size = minRun
    while size < n:
        for left in range(0, n, 2 * size):
            mid = min(n - 1, left + size - 1)
            right = min((left + 2 * size - 1), (n - 1))
 
            if mid < right:
                mergeSort.MergeQuantity(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description, left, mid, right)
 
        size = 2 * size
    return MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description

def insertionSortStars(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description, left, right):
    for i in range(left + 1, right + 1):
        j = i
        while j > left and Stars[j] < Stars[j - 1]:
            temp = MedicineName[j]
            MedicineName[j] = MedicineName[j-1]
            MedicineName[j-1] = temp

            tempOld = OldpriceInt[j]
            OldpriceInt[j] = OldpriceInt[j-1]
            OldpriceInt[j-1] = tempOld

            tempNew = NewPriceInt[j]
            NewPriceInt[j] = NewPriceInt[j-1]
            NewPriceInt[j-1] = tempNew

            tempQ = Quantity[j]
            Quantity[j] = Quantity[j-1]
            Quantity[j-1] = tempQ

            tempS = Stars[j]
            Stars[j] = Stars[j-1]
            Stars[j-1] = tempS

            tempR = RatingInt[j]
            RatingInt[j] = RatingInt[j-1]
            RatingInt[j-1] = tempR

            tempDis = Discount[j]
            Discount[j] = Discount[j-1]
            Discount[j-1] = tempDis

            tempDescript = Description[j]
            Description[j] = Description[j-1]
            Description[j-1] = tempDescript

            j =j - 1
 
def timSortStarsAscending(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description):
    n = len(Stars)
    minRun = calcMinRun(n)

    for start in range(0, n, minRun):
        end = min(start + minRun - 1, n - 1)
        insertionSortStars(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description, start, end)
 
    size = minRun
    while size < n:
        for left in range(0, n, 2 * size):
            mid = min(n - 1, left + size - 1)
            right = min((left + 2 * size - 1), (n - 1))
 
            if mid < right:
                mergeSort.MergeSortStars(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description, left, mid, right)
 
        size = 2 * size
    return MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description

def insertionSortRating(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description, left, right):
    for i in range(left + 1, right + 1):
        j = i
        while j > left and RatingInt[j] < RatingInt[j - 1]:
            temp = MedicineName[j]
            MedicineName[j] = MedicineName[j-1]
            MedicineName[j-1] = temp

            tempOld = OldpriceInt[j]
            OldpriceInt[j] = OldpriceInt[j-1]
            OldpriceInt[j-1] = tempOld

            tempNew = NewPriceInt[j]
            NewPriceInt[j] = NewPriceInt[j-1]
            NewPriceInt[j-1] = tempNew

            tempQ = Quantity[j]
            Quantity[j] = Quantity[j-1]
            Quantity[j-1] = tempQ

            tempS = Stars[j]
            Stars[j] = Stars[j-1]
            Stars[j-1] = tempS

            tempR = RatingInt[j]
            RatingInt[j] = RatingInt[j-1]
            RatingInt[j-1] = tempR

            tempDis = Discount[j]
            Discount[j] = Discount[j-1]
            Discount[j-1] = tempDis

            tempDescript = Description[j]
            Description[j] = Description[j-1]
            Description[j-1] = tempDescript

            j =j - 1
 
def timSortRatingAscending(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description):
    n = len(RatingInt)
    minRun = calcMinRun(n)

    for start in range(0, n, minRun):
        end = min(start + minRun - 1, n - 1)
        insertionSortRating(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description, start, end)
 
    size = minRun
    while size < n:
        for left in range(0, n, 2 * size):
            mid = min(n - 1, left + size - 1)
            right = min((left + 2 * size - 1), (n - 1))
 
            if mid < right:
                mergeSort.MergeRating(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description, left, mid, right)
 
        size = 2 * size
    return MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description

def insertionSortDiscount(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description, left, right):
    for i in range(left + 1, right + 1):
        j = i
        while j > left and Discount[j] < Discount[j - 1]:
            temp = MedicineName[j]
            MedicineName[j] = MedicineName[j-1]
            MedicineName[j-1] = temp

            tempOld = OldpriceInt[j]
            OldpriceInt[j] = OldpriceInt[j-1]
            OldpriceInt[j-1] = tempOld

            tempNew = NewPriceInt[j]
            NewPriceInt[j] = NewPriceInt[j-1]
            NewPriceInt[j-1] = tempNew

            tempQ = Quantity[j]
            Quantity[j] = Quantity[j-1]
            Quantity[j-1] = tempQ

            tempS = Stars[j]
            Stars[j] = Stars[j-1]
            Stars[j-1] = tempS

            tempR = RatingInt[j]
            RatingInt[j] = RatingInt[j-1]
            RatingInt[j-1] = tempR

            tempDis = Discount[j]
            Discount[j] = Discount[j-1]
            Discount[j-1] = tempDis

            tempDescript = Description[j]
            Description[j] = Description[j-1]
            Description[j-1] = tempDescript

            j =j - 1
 
def timSortDiscountAscending(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description):
    n = len(Discount)
    minRun = calcMinRun(n)

    for start in range(0, n, minRun):
        end = min(start + minRun - 1, n - 1)
        insertionSortDiscount(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description, start, end)
 
    size = minRun
    while size < n:
        for left in range(0, n, 2 * size):
            mid = min(n - 1, left + size - 1)
            right = min((left + 2 * size - 1), (n - 1))
 
            if mid < right:
                mergeSort.MergeDiscount(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description, left, mid, right)
 
        size = 2 * size
    return MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description

def insertionSortDescription(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description, left, right):
    for i in range(left + 1, right + 1):
        j = i
        while j > left and Description[j] < Description[j - 1]:
            temp = MedicineName[j]
            MedicineName[j] = MedicineName[j-1]
            MedicineName[j-1] = temp

            tempOld = OldpriceInt[j]
            OldpriceInt[j] = OldpriceInt[j-1]
            OldpriceInt[j-1] = tempOld

            tempNew = NewPriceInt[j]
            NewPriceInt[j] = NewPriceInt[j-1]
            NewPriceInt[j-1] = tempNew

            tempQ = Quantity[j]
            Quantity[j] = Quantity[j-1]
            Quantity[j-1] = tempQ

            tempS = Stars[j]
            Stars[j] = Stars[j-1]
            Stars[j-1] = tempS

            tempR = RatingInt[j]
            RatingInt[j] = RatingInt[j-1]
            RatingInt[j-1] = tempR

            tempDis = Discount[j]
            Discount[j] = Discount[j-1]
            Discount[j-1] = tempDis

            tempDescript = Description[j]
            Description[j] = Description[j-1]
            Description[j-1] = tempDescript

            j =j - 1
 
def timSortDescriptionAscending(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description):
    n = len(Description)
    minRun = calcMinRun(n)

    for start in range(0, n, minRun):
        end = min(start + minRun - 1, n - 1)
        insertionSortDescription(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description, start, end)
 
    size = minRun
    while size < n:
        for left in range(0, n, 2 * size):
            mid = min(n - 1, left + size - 1)
            right = min((left + 2 * size - 1), (n - 1))
 
            if mid < right:
                mergeSort.MergeDescription(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description, left, mid, right)
 
        size = 2 * size
    return MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description

#Tim Sort Descending Function
 
def insertionSortDescending(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description, left, right):
    for i in range(left + 1, right + 1):
        j = i
        while j > left and MedicineName[j] > MedicineName[j - 1]:
            temp = MedicineName[j]
            MedicineName[j] = MedicineName[j-1]
            MedicineName[j-1] = temp

            tempOld = OldpriceInt[j]
            OldpriceInt[j] = OldpriceInt[j-1]
            OldpriceInt[j-1] = tempOld

            tempNew = NewPriceInt[j]
            NewPriceInt[j] = NewPriceInt[j-1]
            NewPriceInt[j-1] = tempNew

            tempQ = Quantity[j]
            Quantity[j] = Quantity[j-1]
            Quantity[j-1] = tempQ

            tempS = Stars[j]
            Stars[j] = Stars[j-1]
            Stars[j-1] = tempS

            tempR = RatingInt[j]
            RatingInt[j] = RatingInt[j-1]
            RatingInt[j-1] = tempR

            tempDis = Discount[j]
            Discount[j] = Discount[j-1]
            Discount[j-1] = tempDis

            tempDescript = Description[j]
            Description[j] = Description[j-1]
            Description[j-1] = tempDescript

            j =j - 1 
 
def timSortDescending(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description):
    n = len(MedicineName)
    minRun = calcMinRun(n)

    for start in range(0, n, minRun):
        end = min(start + minRun - 1, n - 1)
        insertionSortDescending(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description, start, end)
 
    size = minRun
    while size < n:
        for left in range(0, n, 2 * size):
            mid = min(n - 1, left + size - 1)
            right = min((left + 2 * size - 1), (n - 1))
 
            if mid < right:
                mergeSort.MergeDescending(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description, left, mid, right)
 
        size = 2 * size
    return MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description
 
def insertionSortOldpriceDescending(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description, left, right):
    for i in range(left + 1, right + 1):
        j = i
        while j > left and OldpriceInt[j] > OldpriceInt[j - 1]:
            temp = MedicineName[j]
            MedicineName[j] = MedicineName[j-1]
            MedicineName[j-1] = temp

            tempOld = OldpriceInt[j]
            OldpriceInt[j] = OldpriceInt[j-1]
            OldpriceInt[j-1] = tempOld

            tempNew = NewPriceInt[j]
            NewPriceInt[j] = NewPriceInt[j-1]
            NewPriceInt[j-1] = tempNew

            tempQ = Quantity[j]
            Quantity[j] = Quantity[j-1]
            Quantity[j-1] = tempQ

            tempS = Stars[j]
            Stars[j] = Stars[j-1]
            Stars[j-1] = tempS

            tempR = RatingInt[j]
            RatingInt[j] = RatingInt[j-1]
            RatingInt[j-1] = tempR

            tempDis = Discount[j]
            Discount[j] = Discount[j-1]
            Discount[j-1] = tempDis

            tempDescript = Description[j]
            Description[j] = Description[j-1]
            Description[j-1] = tempDescript

            j =j - 1
 
def timSortOldpriceDescending(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description):
    n = len(OldpriceInt)
    minRun = calcMinRun(n)

    for start in range(0, n, minRun):
        end = min(start + minRun - 1, n - 1)
        insertionSortOldpriceDescending(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description, start, end)
 
    size = minRun
    while size < n:
        for left in range(0, n, 2 * size):
            mid = min(n - 1, left + size - 1)
            right = min((left + 2 * size - 1), (n - 1))
 
            if mid < right:
                mergeSort.MergeOldpriceDescending(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description, left, mid, right)
 
        size = 2 * size
    return MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description

def insertionSortNewPriceDescending(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description, left, right):
    for i in range(left + 1, right + 1):
        j = i
        while j > left and NewPriceInt[j] > NewPriceInt[j - 1]:
            temp = MedicineName[j]
            MedicineName[j] = MedicineName[j-1]
            MedicineName[j-1] = temp

            tempOld = OldpriceInt[j]
            OldpriceInt[j] = OldpriceInt[j-1]
            OldpriceInt[j-1] = tempOld

            tempNew = NewPriceInt[j]
            NewPriceInt[j] = NewPriceInt[j-1]
            NewPriceInt[j-1] = tempNew

            tempQ = Quantity[j]
            Quantity[j] = Quantity[j-1]
            Quantity[j-1] = tempQ

            tempS = Stars[j]
            Stars[j] = Stars[j-1]
            Stars[j-1] = tempS

            tempR = RatingInt[j]
            RatingInt[j] = RatingInt[j-1]
            RatingInt[j-1] = tempR

            tempDis = Discount[j]
            Discount[j] = Discount[j-1]
            Discount[j-1] = tempDis

            tempDescript = Description[j]
            Description[j] = Description[j-1]
            Description[j-1] = tempDescript

            j =j - 1
 
def timSortNewPriceDescending(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description):
    n = len(NewPriceInt)
    minRun = calcMinRun(n)

    for start in range(0, n, minRun):
        end = min(start + minRun - 1, n - 1)
        insertionSortNewPriceDescending(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description, start, end)
 
    size = minRun
    while size < n:
        for left in range(0, n, 2 * size):
            mid = min(n - 1, left + size - 1)
            right = min((left + 2 * size - 1), (n - 1))
 
            if mid < right:
                mergeSort.MergeNewPriceDescending(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description, left, mid, right)
 
        size = 2 * size
    return MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description

def insertionSortQuantityDescending(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description, left, right):
    for i in range(left + 1, right + 1):
        j = i
        while j > left and Quantity[j] > Quantity[j - 1]:
            temp = MedicineName[j]
            MedicineName[j] = MedicineName[j-1]
            MedicineName[j-1] = temp

            tempOld = OldpriceInt[j]
            OldpriceInt[j] = OldpriceInt[j-1]
            OldpriceInt[j-1] = tempOld

            tempNew = NewPriceInt[j]
            NewPriceInt[j] = NewPriceInt[j-1]
            NewPriceInt[j-1] = tempNew

            tempQ = Quantity[j]
            Quantity[j] = Quantity[j-1]
            Quantity[j-1] = tempQ

            tempS = Stars[j]
            Stars[j] = Stars[j-1]
            Stars[j-1] = tempS

            tempR = RatingInt[j]
            RatingInt[j] = RatingInt[j-1]
            RatingInt[j-1] = tempR

            tempDis = Discount[j]
            Discount[j] = Discount[j-1]
            Discount[j-1] = tempDis

            tempDescript = Description[j]
            Description[j] = Description[j-1]
            Description[j-1] = tempDescript

            j =j - 1
 
def timSortQuantityDescending(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description):
    n = len(Quantity)
    minRun = calcMinRun(n)

    for start in range(0, n, minRun):
        end = min(start + minRun - 1, n - 1)
        insertionSortQuantityDescending(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description, start, end)
 
    size = minRun
    while size < n:
        for left in range(0, n, 2 * size):
            mid = min(n - 1, left + size - 1)
            right = min((left + 2 * size - 1), (n - 1))
 
            if mid < right:
                mergeSort.MergeQuantityDescending(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description, left, mid, right)
 
        size = 2 * size
    return MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description

def insertionSortStarsDescending(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description, left, right):
    for i in range(left + 1, right + 1):
        j = i
        while j > left and Stars[j] > Stars[j - 1]:
            temp = MedicineName[j]
            MedicineName[j] = MedicineName[j-1]
            MedicineName[j-1] = temp

            tempOld = OldpriceInt[j]
            OldpriceInt[j] = OldpriceInt[j-1]
            OldpriceInt[j-1] = tempOld

            tempNew = NewPriceInt[j]
            NewPriceInt[j] = NewPriceInt[j-1]
            NewPriceInt[j-1] = tempNew

            tempQ = Quantity[j]
            Quantity[j] = Quantity[j-1]
            Quantity[j-1] = tempQ

            tempS = Stars[j]
            Stars[j] = Stars[j-1]
            Stars[j-1] = tempS

            tempR = RatingInt[j]
            RatingInt[j] = RatingInt[j-1]
            RatingInt[j-1] = tempR

            tempDis = Discount[j]
            Discount[j] = Discount[j-1]
            Discount[j-1] = tempDis

            tempDescript = Description[j]
            Description[j] = Description[j-1]
            Description[j-1] = tempDescript

            j =j - 1
 
def timSortStarsDescending(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description):
    n = len(Stars)
    minRun = calcMinRun(n)

    for start in range(0, n, minRun):
        end = min(start + minRun - 1, n - 1)
        insertionSortStarsDescending(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description, start, end)
 
    size = minRun
    while size < n:
        for left in range(0, n, 2 * size):
            mid = min(n - 1, left + size - 1)
            right = min((left + 2 * size - 1), (n - 1))
 
            if mid < right:
                mergeSort.MergeStarsDescending(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description, left, mid, right)
 
        size = 2 * size
    return MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description

def insertionSortRatingDescending(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description, left, right):
    for i in range(left + 1, right + 1):
        j = i
        while j > left and RatingInt[j] > RatingInt[j - 1]:
            temp = MedicineName[j]
            MedicineName[j] = MedicineName[j-1]
            MedicineName[j-1] = temp

            tempOld = OldpriceInt[j]
            OldpriceInt[j] = OldpriceInt[j-1]
            OldpriceInt[j-1] = tempOld

            tempNew = NewPriceInt[j]
            NewPriceInt[j] = NewPriceInt[j-1]
            NewPriceInt[j-1] = tempNew

            tempQ = Quantity[j]
            Quantity[j] = Quantity[j-1]
            Quantity[j-1] = tempQ

            tempS = Stars[j]
            Stars[j] = Stars[j-1]
            Stars[j-1] = tempS

            tempR = RatingInt[j]
            RatingInt[j] = RatingInt[j-1]
            RatingInt[j-1] = tempR

            tempDis = Discount[j]
            Discount[j] = Discount[j-1]
            Discount[j-1] = tempDis

            tempDescript = Description[j]
            Description[j] = Description[j-1]
            Description[j-1] = tempDescript

            j =j - 1
 
def timSortRatingDescending(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description):
    n = len(RatingInt)
    minRun = calcMinRun(n)

    for start in range(0, n, minRun):
        end = min(start + minRun - 1, n - 1)
        insertionSortRatingDescending(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description, start, end)
 
    size = minRun
    while size < n:
        for left in range(0, n, 2 * size):
            mid = min(n - 1, left + size - 1)
            right = min((left + 2 * size - 1), (n - 1))
 
            if mid < right:
                mergeSort.MergeSortRatingDescending(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description, left, mid, right)
 
        size = 2 * size
    return MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description

def insertionSortDiscountDescending(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description, left, right):
    for i in range(left + 1, right + 1):
        j = i
        while j > left and Discount[j] > Discount[j - 1]:
            temp = MedicineName[j]
            MedicineName[j] = MedicineName[j-1]
            MedicineName[j-1] = temp

            tempOld = OldpriceInt[j]
            OldpriceInt[j] = OldpriceInt[j-1]
            OldpriceInt[j-1] = tempOld

            tempNew = NewPriceInt[j]
            NewPriceInt[j] = NewPriceInt[j-1]
            NewPriceInt[j-1] = tempNew

            tempQ = Quantity[j]
            Quantity[j] = Quantity[j-1]
            Quantity[j-1] = tempQ

            tempS = Stars[j]
            Stars[j] = Stars[j-1]
            Stars[j-1] = tempS

            tempR = RatingInt[j]
            RatingInt[j] = RatingInt[j-1]
            RatingInt[j-1] = tempR

            tempDis = Discount[j]
            Discount[j] = Discount[j-1]
            Discount[j-1] = tempDis

            tempDescript = Description[j]
            Description[j] = Description[j-1]
            Description[j-1] = tempDescript

            j =j - 1
 
def timSortDiscountDescending(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description):
    n = len(Discount)
    minRun = calcMinRun(n)

    for start in range(0, n, minRun):
        end = min(start + minRun - 1, n - 1)
        insertionSortDiscountDescending(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description, start, end)
 
    size = minRun
    while size < n:
        for left in range(0, n, 2 * size):
            mid = min(n - 1, left + size - 1)
            right = min((left + 2 * size - 1), (n - 1))
 
            if mid < right:
                mergeSort.MergeDiscountDescending(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description, left, mid, right)
 
        size = 2 * size
    return MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description

def insertionSortDescriptionDescending(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description, left, right):
    for i in range(left + 1, right + 1):
        j = i
        while j > left and Description[j] > Description[j - 1]:
            temp = MedicineName[j]
            MedicineName[j] = MedicineName[j-1]
            MedicineName[j-1] = temp

            tempOld = OldpriceInt[j]
            OldpriceInt[j] = OldpriceInt[j-1]
            OldpriceInt[j-1] = tempOld

            tempNew = NewPriceInt[j]
            NewPriceInt[j] = NewPriceInt[j-1]
            NewPriceInt[j-1] = tempNew

            tempQ = Quantity[j]
            Quantity[j] = Quantity[j-1]
            Quantity[j-1] = tempQ

            tempS = Stars[j]
            Stars[j] = Stars[j-1]
            Stars[j-1] = tempS

            tempR = RatingInt[j]
            RatingInt[j] = RatingInt[j-1]
            RatingInt[j-1] = tempR

            tempDis = Discount[j]
            Discount[j] = Discount[j-1]
            Discount[j-1] = tempDis

            tempDescript = Description[j]
            Description[j] = Description[j-1]
            Description[j-1] = tempDescript

            j =j - 1
 
def timSortDescriptionDescending(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description):
    n = len(Description)
    minRun = calcMinRun(n)

    for start in range(0, n, minRun):
        end = min(start + minRun - 1, n - 1)
        insertionSortDescriptionDescending(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description, start, end)
 
    size = minRun
    while size < n:
        for left in range(0, n, 2 * size):
            mid = min(n - 1, left + size - 1)
            right = min((left + 2 * size - 1), (n - 1))
 
            if mid < right:
                mergeSort.MergeDescriptionDescending(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description, left, mid, right)
 
        size = 2 * size
    return MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description