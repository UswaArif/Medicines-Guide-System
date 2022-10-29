#Merge Sorting Ascending Function
def MergeSort(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description, start, end):
    if start < end:
        q = (start + end) // 2
        MergeSort(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description, start, q)
        MergeSort(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description, q + 1, end)
        Merge(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description, start, q, end)
    return MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description

def Merge(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description, p, q, r):
    n1 = q - p + 1
    n2 = r - q
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

    for i in range(0, n1):
        L.append(MedicineName[p + i])
        LOld.append(OldpriceInt[p + i])
        LNew.append(NewPriceInt[p + i])
        LQ.append(Quantity[p + i])
        LS.append(Stars[p + i])
        LR.append(RatingInt[p + i])
        LDis.append(Discount[p + i])
        LDescript.append(Description[p + i])

    for j in range(0, n2):
        R.append(MedicineName[q + 1 + j])
        ROld.append(OldpriceInt[q + 1 + j])
        RNew.append(NewPriceInt[q + 1 + j])
        RQ.append(Quantity[q + 1 + j])
        RS.append(Stars[q + 1 + j])
        RR.append(RatingInt[q + 1 + j])
        RDis.append(Discount[q + 1 + j])
        RDescript.append(Description[q + 1 + j])
    i = 0
    j = 0
    k = p
    while i < n1 and j < n2:
        if(L[i] <= R[j]):
            MedicineName[k] = L[i]
            OldpriceInt[k] = LOld[i]
            NewPriceInt[k] = LNew[i]
            Quantity[k] = LQ[i]
            Stars[k] = LS[i]
            RatingInt[k] = LR[i]
            Discount[k] = LDis[i]
            Description[k] = LDescript[i]
            i += 1
        else:
            MedicineName[k] = R[j]
            OldpriceInt[k] = ROld[j]
            NewPriceInt[k] = RNew[j]
            Quantity[k] = RQ[j]
            Stars[k] = RS[j]
            RatingInt[k] = RR[j]
            Discount[k] = RDis[j]
            Description[k] = RDescript[j]
            j += 1
        k += 1
    if i == len(L):
        while j < n2:
            MedicineName[k] = R[j]
            OldpriceInt[k] = ROld[j]
            NewPriceInt[k] = RNew[j]
            Quantity[k] = RQ[j]
            Stars[k] = RS[j]
            RatingInt[k] = RR[j]
            Discount[k] = RDis[j]
            Description[k] = RDescript[j]
            j += 1
            k += 1
    else:
        while i < len(L):
            MedicineName[k] = L[i]
            OldpriceInt[k] = LOld[i]
            NewPriceInt[k] = LNew[i]
            Quantity[k] = LQ[i]
            Stars[k] = LS[i]
            RatingInt[k] = LR[i]
            Discount[k] = LDis[i]
            Description[k] = LDescript[i]
            i += 1
            k += 1
    return MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description

def MergeSortOldprice(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description, start, end):
    if start < end:
        q = (start + end) // 2
        MergeSortOldprice(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description, start, q)
        MergeSortOldprice(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description, q + 1, end)
        MergeOldprice(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description, start, q, end)
    return MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description

def MergeOldprice(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description, p, q, r):
    n1 = q - p + 1
    n2 = r - q
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

    for i in range(0, n1):
        L.append(MedicineName[p + i])
        LOld.append(OldpriceInt[p + i])
        LNew.append(NewPriceInt[p + i])
        LQ.append(Quantity[p + i])
        LS.append(Stars[p + i])
        LR.append(RatingInt[p + i])
        LDis.append(Discount[p + i])
        LDescript.append(Description[p + i])

    for j in range(0, n2):
        R.append(MedicineName[q + 1 + j])
        ROld.append(OldpriceInt[q + 1 + j])
        RNew.append(NewPriceInt[q + 1 + j])
        RQ.append(Quantity[q + 1 + j])
        RS.append(Stars[q + 1 + j])
        RR.append(RatingInt[q + 1 + j])
        RDis.append(Discount[q + 1 + j])
        RDescript.append(Description[q + 1 + j])
    i = 0
    j = 0
    k = p
    while i < n1 and j < n2:
        if(LOld[i] <= ROld[j]):
            MedicineName[k] = L[i]
            OldpriceInt[k] = LOld[i]
            NewPriceInt[k] = LNew[i]
            Quantity[k] = LQ[i]
            Stars[k] = LS[i]
            RatingInt[k] = LR[i]
            Discount[k] = LDis[i]
            Description[k] = LDescript[i]
            i += 1
        else:
            MedicineName[k] = R[j]
            OldpriceInt[k] = ROld[j]
            NewPriceInt[k] = RNew[j]
            Quantity[k] = RQ[j]
            Stars[k] = RS[j]
            RatingInt[k] = RR[j]
            Discount[k] = RDis[j]
            Description[k] = RDescript[j]
            j += 1
        k += 1
    if i == len(LOld):
        while j < n2:
            MedicineName[k] = R[j]
            OldpriceInt[k] = ROld[j]
            NewPriceInt[k] = RNew[j]
            Quantity[k] = RQ[j]
            Stars[k] = RS[j]
            RatingInt[k] = RR[j]
            Discount[k] = RDis[j]
            Description[k] = RDescript[j]
            j += 1
            k += 1
    else:
        while i < len(LOld):
            MedicineName[k] = L[i]
            OldpriceInt[k] = LOld[i]
            NewPriceInt[k] = LNew[i]
            Quantity[k] = LQ[i]
            Stars[k] = LS[i]
            RatingInt[k] = LR[i]
            Discount[k] = LDis[i]
            Description[k] = LDescript[i]
            i += 1
            k += 1
    return MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description

def MergeSortNewPrice(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description, start, end):
    if start < end:
        q = (start + end) // 2
        MergeSortNewPrice(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description, start, q)
        MergeSortNewPrice(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description, q + 1, end)
        MergeNewPrice(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description, start, q, end)
    return MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description

def MergeNewPrice(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description, p, q, r):
    n1 = q - p + 1
    n2 = r - q
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

    for i in range(0, n1):
        L.append(MedicineName[p + i])
        LOld.append(OldpriceInt[p + i])
        LNew.append(NewPriceInt[p + i])
        LQ.append(Quantity[p + i])
        LS.append(Stars[p + i])
        LR.append(RatingInt[p + i])
        LDis.append(Discount[p + i])
        LDescript.append(Description[p + i])

    for j in range(0, n2):
        R.append(MedicineName[q + 1 + j])
        ROld.append(OldpriceInt[q + 1 + j])
        RNew.append(NewPriceInt[q + 1 + j])
        RQ.append(Quantity[q + 1 + j])
        RS.append(Stars[q + 1 + j])
        RR.append(RatingInt[q + 1 + j])
        RDis.append(Discount[q + 1 + j])
        RDescript.append(Description[q + 1 + j])
    i = 0
    j = 0
    k = p
    while i < n1 and j < n2:
        if(LNew[i] <= RNew[j]):
            MedicineName[k] = L[i]
            OldpriceInt[k] = LOld[i]
            NewPriceInt[k] = LNew[i]
            Quantity[k] = LQ[i]
            Stars[k] = LS[i]
            RatingInt[k] = LR[i]
            Discount[k] = LDis[i]
            Description[k] = LDescript[i]
            i += 1
        else:
            MedicineName[k] = R[j]
            OldpriceInt[k] = ROld[j]
            NewPriceInt[k] = RNew[j]
            Quantity[k] = RQ[j]
            Stars[k] = RS[j]
            RatingInt[k] = RR[j]
            Discount[k] = RDis[j]
            Description[k] = RDescript[j]
            j += 1
        k += 1
    if i == len(LNew):
        while j < n2:
            MedicineName[k] = R[j]
            OldpriceInt[k] = ROld[j]
            NewPriceInt[k] = RNew[j]
            Quantity[k] = RQ[j]
            Stars[k] = RS[j]
            RatingInt[k] = RR[j]
            Discount[k] = RDis[j]
            Description[k] = RDescript[j]
            j += 1
            k += 1
    else:
        while i < len(LNew):
            MedicineName[k] = L[i]
            OldpriceInt[k] = LOld[i]
            NewPriceInt[k] = LNew[i]
            Quantity[k] = LQ[i]
            Stars[k] = LS[i]
            RatingInt[k] = LR[i]
            Discount[k] = LDis[i]
            Description[k] = LDescript[i]
            i += 1
            k += 1
    return MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description

def MergeSortQuantity(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description, start, end):
    if start < end:
        q = (start + end) // 2
        MergeSortQuantity(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description, start, q)
        MergeSortQuantity(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description, q + 1, end)
        MergeQuantity(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description, start, q, end)
    return MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description

def MergeQuantity(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description, p, q, r):
    n1 = q - p + 1
    n2 = r - q
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

    for i in range(0, n1):
        L.append(MedicineName[p + i])
        LOld.append(OldpriceInt[p + i])
        LNew.append(NewPriceInt[p + i])
        LQ.append(Quantity[p + i])
        LS.append(Stars[p + i])
        LR.append(RatingInt[p + i])
        LDis.append(Discount[p + i])
        LDescript.append(Description[p + i])

    for j in range(0, n2):
        R.append(MedicineName[q + 1 + j])
        ROld.append(OldpriceInt[q + 1 + j])
        RNew.append(NewPriceInt[q + 1 + j])
        RQ.append(Quantity[q + 1 + j])
        RS.append(Stars[q + 1 + j])
        RR.append(RatingInt[q + 1 + j])
        RDis.append(Discount[q + 1 + j])
        RDescript.append(Description[q + 1 + j])
    i = 0
    j = 0
    k = p
    while i < n1 and j < n2:
        if(LQ[i] <= RQ[j]):
            MedicineName[k] = L[i]
            OldpriceInt[k] = LOld[i]
            NewPriceInt[k] = LNew[i]
            Quantity[k] = LQ[i]
            Stars[k] = LS[i]
            RatingInt[k] = LR[i]
            Discount[k] = LDis[i]
            Description[k] = LDescript[i]
            i += 1
        else:
            MedicineName[k] = R[j]
            OldpriceInt[k] = ROld[j]
            NewPriceInt[k] = RNew[j]
            Quantity[k] = RQ[j]
            Stars[k] = RS[j]
            RatingInt[k] = RR[j]
            Discount[k] = RDis[j]
            Description[k] = RDescript[j]
            j += 1
        k += 1
    if i == len(LQ):
        while j < n2:
            MedicineName[k] = R[j]
            OldpriceInt[k] = ROld[j]
            NewPriceInt[k] = RNew[j]
            Quantity[k] = RQ[j]
            Stars[k] = RS[j]
            RatingInt[k] = RR[j]
            Discount[k] = RDis[j]
            Description[k] = RDescript[j]
            j += 1
            k += 1
    else:
        while i < len(LQ):
            MedicineName[k] = L[i]
            OldpriceInt[k] = LOld[i]
            NewPriceInt[k] = LNew[i]
            Quantity[k] = LQ[i]
            Stars[k] = LS[i]
            RatingInt[k] = LR[i]
            Discount[k] = LDis[i]
            Description[k] = LDescript[i]
            i += 1
            k += 1
    return MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description

def MergeSortStars(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description, start, end):
    if start < end:
        q = (start + end) // 2
        MergeSortStars(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description, start, q)
        MergeSortStars(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description, q + 1, end)
        MergeStars(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description, start, q, end)
    return MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description

def MergeStars(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description, p, q, r):
    n1 = q - p + 1
    n2 = r - q
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

    for i in range(0, n1):
        L.append(MedicineName[p + i])
        LOld.append(OldpriceInt[p + i])
        LNew.append(NewPriceInt[p + i])
        LQ.append(Quantity[p + i])
        LS.append(Stars[p + i])
        LR.append(RatingInt[p + i])
        LDis.append(Discount[p + i])
        LDescript.append(Description[p + i])

    for j in range(0, n2):
        R.append(MedicineName[q + 1 + j])
        ROld.append(OldpriceInt[q + 1 + j])
        RNew.append(NewPriceInt[q + 1 + j])
        RQ.append(Quantity[q + 1 + j])
        RS.append(Stars[q + 1 + j])
        RR.append(RatingInt[q + 1 + j])
        RDis.append(Discount[q + 1 + j])
        RDescript.append(Description[q + 1 + j])
    i = 0
    j = 0
    k = p
    while i < n1 and j < n2:
        if(LS[i] <= RS[j]):
            MedicineName[k] = L[i]
            OldpriceInt[k] = LOld[i]
            NewPriceInt[k] = LNew[i]
            Quantity[k] = LQ[i]
            Stars[k] = LS[i]
            RatingInt[k] = LR[i]
            Discount[k] = LDis[i]
            Description[k] = LDescript[i]
            i += 1
        else:
            MedicineName[k] = R[j]
            OldpriceInt[k] = ROld[j]
            NewPriceInt[k] = RNew[j]
            Quantity[k] = RQ[j]
            Stars[k] = RS[j]
            RatingInt[k] = RR[j]
            Discount[k] = RDis[j]
            Description[k] = RDescript[j]
            j += 1
        k += 1
    if i == len(LS):
        while j < n2:
            MedicineName[k] = R[j]
            OldpriceInt[k] = ROld[j]
            NewPriceInt[k] = RNew[j]
            Quantity[k] = RQ[j]
            Stars[k] = RS[j]
            RatingInt[k] = RR[j]
            Discount[k] = RDis[j]
            Description[k] = RDescript[j]
            j += 1
            k += 1
    else:
        while i < len(LS):
            MedicineName[k] = L[i]
            OldpriceInt[k] = LOld[i]
            NewPriceInt[k] = LNew[i]
            Quantity[k] = LQ[i]
            Stars[k] = LS[i]
            RatingInt[k] = LR[i]
            Discount[k] = LDis[i]
            Description[k] = LDescript[i]
            i += 1
            k += 1
    return MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description

def MergeSortRating(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description, start, end):
    if start < end:
        q = (start + end) // 2
        MergeSortRating(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description, start, q)
        MergeSortRating(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description, q + 1, end)
        MergeRating(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description, start, q, end)
    return MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description

def MergeRating(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description, p, q, r):
    n1 = q - p + 1
    n2 = r - q
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

    for i in range(0, n1):
        L.append(MedicineName[p + i])
        LOld.append(OldpriceInt[p + i])
        LNew.append(NewPriceInt[p + i])
        LQ.append(Quantity[p + i])
        LS.append(Stars[p + i])
        LR.append(RatingInt[p + i])
        LDis.append(Discount[p + i])
        LDescript.append(Description[p + i])

    for j in range(0, n2):
        R.append(MedicineName[q + 1 + j])
        ROld.append(OldpriceInt[q + 1 + j])
        RNew.append(NewPriceInt[q + 1 + j])
        RQ.append(Quantity[q + 1 + j])
        RS.append(Stars[q + 1 + j])
        RR.append(RatingInt[q + 1 + j])
        RDis.append(Discount[q + 1 + j])
        RDescript.append(Description[q + 1 + j])
    i = 0
    j = 0
    k = p
    while i < n1 and j < n2:
        if(LR[i] <= RR[j]):
            MedicineName[k] = L[i]
            OldpriceInt[k] = LOld[i]
            NewPriceInt[k] = LNew[i]
            Quantity[k] = LQ[i]
            Stars[k] = LS[i]
            RatingInt[k] = LR[i]
            Discount[k] = LDis[i]
            Description[k] = LDescript[i]
            i += 1
        else:
            MedicineName[k] = R[j]
            OldpriceInt[k] = ROld[j]
            NewPriceInt[k] = RNew[j]
            Quantity[k] = RQ[j]
            Stars[k] = RS[j]
            RatingInt[k] = RR[j]
            Discount[k] = RDis[j]
            Description[k] = RDescript[j]
            j += 1
        k += 1
    if i == len(LR):
        while j < n2:
            MedicineName[k] = R[j]
            OldpriceInt[k] = ROld[j]
            NewPriceInt[k] = RNew[j]
            Quantity[k] = RQ[j]
            Stars[k] = RS[j]
            RatingInt[k] = RR[j]
            Discount[k] = RDis[j]
            Description[k] = RDescript[j]
            j += 1
            k += 1
    else:
        while i < len(LR):
            MedicineName[k] = L[i]
            OldpriceInt[k] = LOld[i]
            NewPriceInt[k] = LNew[i]
            Quantity[k] = LQ[i]
            Stars[k] = LS[i]
            RatingInt[k] = LR[i]
            Discount[k] = LDis[i]
            Description[k] = LDescript[i]
            i += 1
            k += 1
    return MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description

def MergeSortDiscount(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description, start, end):
    if start < end:
        q = (start + end) // 2
        MergeSortDiscount(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description, start, q)
        MergeSortDiscount(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description, q + 1, end)
        MergeDiscount(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description, start, q, end)
    return MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description

def MergeDiscount(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description, p, q, r):
    n1 = q - p + 1
    n2 = r - q
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

    for i in range(0, n1):
        L.append(MedicineName[p + i])
        LOld.append(OldpriceInt[p + i])
        LNew.append(NewPriceInt[p + i])
        LQ.append(Quantity[p + i])
        LS.append(Stars[p + i])
        LR.append(RatingInt[p + i])
        LDis.append(Discount[p + i])
        LDescript.append(Description[p + i])

    for j in range(0, n2):
        R.append(MedicineName[q + 1 + j])
        ROld.append(OldpriceInt[q + 1 + j])
        RNew.append(NewPriceInt[q + 1 + j])
        RQ.append(Quantity[q + 1 + j])
        RS.append(Stars[q + 1 + j])
        RR.append(RatingInt[q + 1 + j])
        RDis.append(Discount[q + 1 + j])
        RDescript.append(Description[q + 1 + j])
    i = 0
    j = 0
    k = p
    while i < n1 and j < n2:
        if(LDis[i] <= RDis[j]):
            MedicineName[k] = L[i]
            OldpriceInt[k] = LOld[i]
            NewPriceInt[k] = LNew[i]
            Quantity[k] = LQ[i]
            Stars[k] = LS[i]
            RatingInt[k] = LR[i]
            Discount[k] = LDis[i]
            Description[k] = LDescript[i]
            i += 1
        else:
            MedicineName[k] = R[j]
            OldpriceInt[k] = ROld[j]
            NewPriceInt[k] = RNew[j]
            Quantity[k] = RQ[j]
            Stars[k] = RS[j]
            RatingInt[k] = RR[j]
            Discount[k] = RDis[j]
            Description[k] = RDescript[j]
            j += 1
        k += 1
    if i == len(LDis):
        while j < n2:
            MedicineName[k] = R[j]
            OldpriceInt[k] = ROld[j]
            NewPriceInt[k] = RNew[j]
            Quantity[k] = RQ[j]
            Stars[k] = RS[j]
            RatingInt[k] = RR[j]
            Discount[k] = RDis[j]
            Description[k] = RDescript[j]
            j += 1
            k += 1
    else:
        while i < len(LDis):
            MedicineName[k] = L[i]
            OldpriceInt[k] = LOld[i]
            NewPriceInt[k] = LNew[i]
            Quantity[k] = LQ[i]
            Stars[k] = LS[i]
            RatingInt[k] = LR[i]
            Discount[k] = LDis[i]
            Description[k] = LDescript[i]
            i += 1
            k += 1
    return MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description

def MergeSortDescription(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description, start, end):
    if start < end:
        q = (start + end) // 2
        MergeSortDescription(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description, start, q)
        MergeSortDescription(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description, q + 1, end)
        MergeDescription(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description, start, q, end)
    return MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description

def MergeDescription(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description, p, q, r):
    n1 = q - p + 1
    n2 = r - q
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

    for i in range(0, n1):
        L.append(MedicineName[p + i])
        LOld.append(OldpriceInt[p + i])
        LNew.append(NewPriceInt[p + i])
        LQ.append(Quantity[p + i])
        LS.append(Stars[p + i])
        LR.append(RatingInt[p + i])
        LDis.append(Discount[p + i])
        LDescript.append(Description[p + i])

    for j in range(0, n2):
        R.append(MedicineName[q + 1 + j])
        ROld.append(OldpriceInt[q + 1 + j])
        RNew.append(NewPriceInt[q + 1 + j])
        RQ.append(Quantity[q + 1 + j])
        RS.append(Stars[q + 1 + j])
        RR.append(RatingInt[q + 1 + j])
        RDis.append(Discount[q + 1 + j])
        RDescript.append(Description[q + 1 + j])
    i = 0
    j = 0
    k = p
    while i < n1 and j < n2:
        if(LDescript[i] <= RDescript[j]):
            MedicineName[k] = L[i]
            OldpriceInt[k] = LOld[i]
            NewPriceInt[k] = LNew[i]
            Quantity[k] = LQ[i]
            Stars[k] = LS[i]
            RatingInt[k] = LR[i]
            Discount[k] = LDis[i]
            Description[k] = LDescript[i]
            i += 1
        else:
            MedicineName[k] = R[j]
            OldpriceInt[k] = ROld[j]
            NewPriceInt[k] = RNew[j]
            Quantity[k] = RQ[j]
            Stars[k] = RS[j]
            RatingInt[k] = RR[j]
            Discount[k] = RDis[j]
            Description[k] = RDescript[j]
            j += 1
        k += 1
    if i == len(LDescript):
        while j < n2:
            MedicineName[k] = R[j]
            OldpriceInt[k] = ROld[j]
            NewPriceInt[k] = RNew[j]
            Quantity[k] = RQ[j]
            Stars[k] = RS[j]
            RatingInt[k] = RR[j]
            Discount[k] = RDis[j]
            Description[k] = RDescript[j]
            j += 1
            k += 1
    else:
        while i < len(LDescript):
            MedicineName[k] = L[i]
            OldpriceInt[k] = LOld[i]
            NewPriceInt[k] = LNew[i]
            Quantity[k] = LQ[i]
            Stars[k] = LS[i]
            RatingInt[k] = LR[i]
            Discount[k] = LDis[i]
            Description[k] = LDescript[i]
            i += 1
            k += 1
    return MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description

#Merge Sorting Descending Function
def MergeSortDescending(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description, start, end):
    if start < end:
        q = (start + end) // 2
        MergeSortDescending(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description, start, q)
        MergeSortDescending(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description, q + 1, end)
        MergeDescending(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description, start, q, end)
    return MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description

def MergeDescending(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description, p, q, r):
    n1 = q - p + 1
    n2 = r - q
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

    for i in range(0, n1):
        L.append(MedicineName[p + i])
        LOld.append(OldpriceInt[p + i])
        LNew.append(NewPriceInt[p + i])
        LQ.append(Quantity[p + i])
        LS.append(Stars[p + i])
        LR.append(RatingInt[p + i])
        LDis.append(Discount[p + i])
        LDescript.append(Description[p + i])

    for j in range(0, n2):
        R.append(MedicineName[q + 1 + j])
        ROld.append(OldpriceInt[q + 1 + j])
        RNew.append(NewPriceInt[q + 1 + j])
        RQ.append(Quantity[q + 1 + j])
        RS.append(Stars[q + 1 + j])
        RR.append(RatingInt[q + 1 + j])
        RDis.append(Discount[q + 1 + j])
        RDescript.append(Description[q + 1 + j])
    i = 0
    j = 0
    k = p
    while i < n1 and j < n2:
        if(L[i] >= R[j]):
            MedicineName[k] = L[i]
            OldpriceInt[k] = LOld[i]
            NewPriceInt[k] = LNew[i]
            Quantity[k] = LQ[i]
            Stars[k] = LS[i]
            RatingInt[k] = LR[i]
            Discount[k] = LDis[i]
            Description[k] = LDescript[i]
            i += 1
        else:
            MedicineName[k] = R[j]
            OldpriceInt[k] = ROld[j]
            NewPriceInt[k] = RNew[j]
            Quantity[k] = RQ[j]
            Stars[k] = RS[j]
            RatingInt[k] = RR[j]
            Discount[k] = RDis[j]
            Description[k] = RDescript[j]
            j += 1
        k += 1
    if i == len(L):
        while j < n2:
            MedicineName[k] = R[j]
            OldpriceInt[k] = ROld[j]
            NewPriceInt[k] = RNew[j]
            Quantity[k] = RQ[j]
            Stars[k] = RS[j]
            RatingInt[k] = RR[j]
            Discount[k] = RDis[j]
            Description[k] = RDescript[j]
            j += 1
            k += 1
    else:
        while i < len(L):
            MedicineName[k] = L[i]
            OldpriceInt[k] = LOld[i]
            NewPriceInt[k] = LNew[i]
            Quantity[k] = LQ[i]
            Stars[k] = LS[i]
            RatingInt[k] = LR[i]
            Discount[k] = LDis[i]
            Description[k] = LDescript[i]
            i += 1
            k += 1
    return MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description

def MergeSortOldpriceDescending(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description, start, end):
    if start < end:
        q = (start + end) // 2
        MergeSortOldpriceDescending(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description, start, q)
        MergeSortOldpriceDescending(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description, q + 1, end)
        MergeOldpriceDescending(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description, start, q, end)
    return MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description

def MergeOldpriceDescending(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description, p, q, r):
    n1 = q - p + 1
    n2 = r - q
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

    for i in range(0, n1):
        L.append(MedicineName[p + i])
        LOld.append(OldpriceInt[p + i])
        LNew.append(NewPriceInt[p + i])
        LQ.append(Quantity[p + i])
        LS.append(Stars[p + i])
        LR.append(RatingInt[p + i])
        LDis.append(Discount[p + i])
        LDescript.append(Description[p + i])

    for j in range(0, n2):
        R.append(MedicineName[q + 1 + j])
        ROld.append(OldpriceInt[q + 1 + j])
        RNew.append(NewPriceInt[q + 1 + j])
        RQ.append(Quantity[q + 1 + j])
        RS.append(Stars[q + 1 + j])
        RR.append(RatingInt[q + 1 + j])
        RDis.append(Discount[q + 1 + j])
        RDescript.append(Description[q + 1 + j])
    i = 0
    j = 0
    k = p
    while i < n1 and j < n2:
        if(LOld[i] >= ROld[j]):
            MedicineName[k] = L[i]
            OldpriceInt[k] = LOld[i]
            NewPriceInt[k] = LNew[i]
            Quantity[k] = LQ[i]
            Stars[k] = LS[i]
            RatingInt[k] = LR[i]
            Discount[k] = LDis[i]
            Description[k] = LDescript[i]
            i += 1
        else:
            MedicineName[k] = R[j]
            OldpriceInt[k] = ROld[j]
            NewPriceInt[k] = RNew[j]
            Quantity[k] = RQ[j]
            Stars[k] = RS[j]
            RatingInt[k] = RR[j]
            Discount[k] = RDis[j]
            Description[k] = RDescript[j]
            j += 1
        k += 1
    if i == len(LOld):
        while j < n2:
            MedicineName[k] = R[j]
            OldpriceInt[k] = ROld[j]
            NewPriceInt[k] = RNew[j]
            Quantity[k] = RQ[j]
            Stars[k] = RS[j]
            RatingInt[k] = RR[j]
            Discount[k] = RDis[j]
            Description[k] = RDescript[j]
            j += 1
            k += 1
    else:
        while i < len(LOld):
            MedicineName[k] = L[i]
            OldpriceInt[k] = LOld[i]
            NewPriceInt[k] = LNew[i]
            Quantity[k] = LQ[i]
            Stars[k] = LS[i]
            RatingInt[k] = LR[i]
            Discount[k] = LDis[i]
            Description[k] = LDescript[i]
            i += 1
            k += 1
    return MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description

def MergeSortNewPriceDescending(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description, start, end):
    if start < end:
        q = (start + end) // 2
        MergeSortNewPriceDescending(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description, start, q)
        MergeSortNewPriceDescending(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description, q + 1, end)
        MergeNewPriceDescending(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description, start, q, end)
    return MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description

def MergeNewPriceDescending(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description, p, q, r):
    n1 = q - p + 1
    n2 = r - q
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

    for i in range(0, n1):
        L.append(MedicineName[p + i])
        LOld.append(OldpriceInt[p + i])
        LNew.append(NewPriceInt[p + i])
        LQ.append(Quantity[p + i])
        LS.append(Stars[p + i])
        LR.append(RatingInt[p + i])
        LDis.append(Discount[p + i])
        LDescript.append(Description[p + i])

    for j in range(0, n2):
        R.append(MedicineName[q + 1 + j])
        ROld.append(OldpriceInt[q + 1 + j])
        RNew.append(NewPriceInt[q + 1 + j])
        RQ.append(Quantity[q + 1 + j])
        RS.append(Stars[q + 1 + j])
        RR.append(RatingInt[q + 1 + j])
        RDis.append(Discount[q + 1 + j])
        RDescript.append(Description[q + 1 + j])
    i = 0
    j = 0
    k = p
    while i < n1 and j < n2:
        if(LNew[i] >= RNew[j]):
            MedicineName[k] = L[i]
            OldpriceInt[k] = LOld[i]
            NewPriceInt[k] = LNew[i]
            Quantity[k] = LQ[i]
            Stars[k] = LS[i]
            RatingInt[k] = LR[i]
            Discount[k] = LDis[i]
            Description[k] = LDescript[i]
            i += 1
        else:
            MedicineName[k] = R[j]
            OldpriceInt[k] = ROld[j]
            NewPriceInt[k] = RNew[j]
            Quantity[k] = RQ[j]
            Stars[k] = RS[j]
            RatingInt[k] = RR[j]
            Discount[k] = RDis[j]
            Description[k] = RDescript[j]
            j += 1
        k += 1
    if i == len(LNew):
        while j < n2:
            MedicineName[k] = R[j]
            OldpriceInt[k] = ROld[j]
            NewPriceInt[k] = RNew[j]
            Quantity[k] = RQ[j]
            Stars[k] = RS[j]
            RatingInt[k] = RR[j]
            Discount[k] = RDis[j]
            Description[k] = RDescript[j]
            j += 1
            k += 1
    else:
        while i < len(LNew):
            MedicineName[k] = L[i]
            OldpriceInt[k] = LOld[i]
            NewPriceInt[k] = LNew[i]
            Quantity[k] = LQ[i]
            Stars[k] = LS[i]
            RatingInt[k] = LR[i]
            Discount[k] = LDis[i]
            Description[k] = LDescript[i]
            i += 1
            k += 1
    return MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description

def MergeSortQuantityDescending(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description, start, end):
    if start < end:
        q = (start + end) // 2
        MergeSortQuantityDescending(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description, start, q)
        MergeSortQuantityDescending(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description, q + 1, end)
        MergeQuantityDescending(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description, start, q, end)
    return MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description

def MergeQuantityDescending(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description, p, q, r):
    n1 = q - p + 1
    n2 = r - q
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

    for i in range(0, n1):
        L.append(MedicineName[p + i])
        LOld.append(OldpriceInt[p + i])
        LNew.append(NewPriceInt[p + i])
        LQ.append(Quantity[p + i])
        LS.append(Stars[p + i])
        LR.append(RatingInt[p + i])
        LDis.append(Discount[p + i])
        LDescript.append(Description[p + i])

    for j in range(0, n2):
        R.append(MedicineName[q + 1 + j])
        ROld.append(OldpriceInt[q + 1 + j])
        RNew.append(NewPriceInt[q + 1 + j])
        RQ.append(Quantity[q + 1 + j])
        RS.append(Stars[q + 1 + j])
        RR.append(RatingInt[q + 1 + j])
        RDis.append(Discount[q + 1 + j])
        RDescript.append(Description[q + 1 + j])
    i = 0
    j = 0
    k = p
    while i < n1 and j < n2:
        if(LQ[i] >= RQ[j]):
            MedicineName[k] = L[i]
            OldpriceInt[k] = LOld[i]
            NewPriceInt[k] = LNew[i]
            Quantity[k] = LQ[i]
            Stars[k] = LS[i]
            RatingInt[k] = LR[i]
            Discount[k] = LDis[i]
            Description[k] = LDescript[i]
            i += 1
        else:
            MedicineName[k] = R[j]
            OldpriceInt[k] = ROld[j]
            NewPriceInt[k] = RNew[j]
            Quantity[k] = RQ[j]
            Stars[k] = RS[j]
            RatingInt[k] = RR[j]
            Discount[k] = RDis[j]
            Description[k] = RDescript[j]
            j += 1
        k += 1
    if i == len(LQ):
        while j < n2:
            MedicineName[k] = R[j]
            OldpriceInt[k] = ROld[j]
            NewPriceInt[k] = RNew[j]
            Quantity[k] = RQ[j]
            Stars[k] = RS[j]
            RatingInt[k] = RR[j]
            Discount[k] = RDis[j]
            Description[k] = RDescript[j]
            j += 1
            k += 1
    else:
        while i < len(LQ):
            MedicineName[k] = L[i]
            OldpriceInt[k] = LOld[i]
            NewPriceInt[k] = LNew[i]
            Quantity[k] = LQ[i]
            Stars[k] = LS[i]
            RatingInt[k] = LR[i]
            Discount[k] = LDis[i]
            Description[k] = LDescript[i]
            i += 1
            k += 1
    return MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description

def MergeSortStarsDescending(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description, start, end):
    if start < end:
        q = (start + end) // 2
        MergeSortStarsDescending(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description, start, q)
        MergeSortStarsDescending(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description, q + 1, end)
        MergeStarsDescending(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description, start, q, end)
    return MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description

def MergeStarsDescending(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description, p, q, r):
    n1 = q - p + 1
    n2 = r - q
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

    for i in range(0, n1):
        L.append(MedicineName[p + i])
        LOld.append(OldpriceInt[p + i])
        LNew.append(NewPriceInt[p + i])
        LQ.append(Quantity[p + i])
        LS.append(Stars[p + i])
        LR.append(RatingInt[p + i])
        LDis.append(Discount[p + i])
        LDescript.append(Description[p + i])

    for j in range(0, n2):
        R.append(MedicineName[q + 1 + j])
        ROld.append(OldpriceInt[q + 1 + j])
        RNew.append(NewPriceInt[q + 1 + j])
        RQ.append(Quantity[q + 1 + j])
        RS.append(Stars[q + 1 + j])
        RR.append(RatingInt[q + 1 + j])
        RDis.append(Discount[q + 1 + j])
        RDescript.append(Description[q + 1 + j])
    i = 0
    j = 0
    k = p
    while i < n1 and j < n2:
        if(LS[i] >= RS[j]):
            MedicineName[k] = L[i]
            OldpriceInt[k] = LOld[i]
            NewPriceInt[k] = LNew[i]
            Quantity[k] = LQ[i]
            Stars[k] = LS[i]
            RatingInt[k] = LR[i]
            Discount[k] = LDis[i]
            Description[k] = LDescript[i]
            i += 1
        else:
            MedicineName[k] = R[j]
            OldpriceInt[k] = ROld[j]
            NewPriceInt[k] = RNew[j]
            Quantity[k] = RQ[j]
            Stars[k] = RS[j]
            RatingInt[k] = RR[j]
            Discount[k] = RDis[j]
            Description[k] = RDescript[j]
            j += 1
        k += 1
    if i == len(LS):
        while j < n2:
            MedicineName[k] = R[j]
            OldpriceInt[k] = ROld[j]
            NewPriceInt[k] = RNew[j]
            Quantity[k] = RQ[j]
            Stars[k] = RS[j]
            RatingInt[k] = RR[j]
            Discount[k] = RDis[j]
            Description[k] = RDescript[j]
            j += 1
            k += 1
    else:
        while i < len(LS):
            MedicineName[k] = L[i]
            OldpriceInt[k] = LOld[i]
            NewPriceInt[k] = LNew[i]
            Quantity[k] = LQ[i]
            Stars[k] = LS[i]
            RatingInt[k] = LR[i]
            Discount[k] = LDis[i]
            Description[k] = LDescript[i]
            i += 1
            k += 1
    return MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description

def MergeSortRatingDescending(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description, start, end):
    if start < end:
        q = (start + end) // 2
        MergeSortRatingDescending(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description, start, q)
        MergeSortRatingDescending(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description, q + 1, end)
        MergeRatingDescending(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description, start, q, end)
    return MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description

def MergeRatingDescending(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description, p, q, r):
    n1 = q - p + 1
    n2 = r - q
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

    for i in range(0, n1):
        L.append(MedicineName[p + i])
        LOld.append(OldpriceInt[p + i])
        LNew.append(NewPriceInt[p + i])
        LQ.append(Quantity[p + i])
        LS.append(Stars[p + i])
        LR.append(RatingInt[p + i])
        LDis.append(Discount[p + i])
        LDescript.append(Description[p + i])

    for j in range(0, n2):
        R.append(MedicineName[q + 1 + j])
        ROld.append(OldpriceInt[q + 1 + j])
        RNew.append(NewPriceInt[q + 1 + j])
        RQ.append(Quantity[q + 1 + j])
        RS.append(Stars[q + 1 + j])
        RR.append(RatingInt[q + 1 + j])
        RDis.append(Discount[q + 1 + j])
        RDescript.append(Description[q + 1 + j])
    i = 0
    j = 0
    k = p
    while i < n1 and j < n2:
        if(LR[i] >= RR[j]):
            MedicineName[k] = L[i]
            OldpriceInt[k] = LOld[i]
            NewPriceInt[k] = LNew[i]
            Quantity[k] = LQ[i]
            Stars[k] = LS[i]
            RatingInt[k] = LR[i]
            Discount[k] = LDis[i]
            Description[k] = LDescript[i]
            i += 1
        else:
            MedicineName[k] = R[j]
            OldpriceInt[k] = ROld[j]
            NewPriceInt[k] = RNew[j]
            Quantity[k] = RQ[j]
            Stars[k] = RS[j]
            RatingInt[k] = RR[j]
            Discount[k] = RDis[j]
            Description[k] = RDescript[j]
            j += 1
        k += 1
    if i == len(LR):
        while j < n2:
            MedicineName[k] = R[j]
            OldpriceInt[k] = ROld[j]
            NewPriceInt[k] = RNew[j]
            Quantity[k] = RQ[j]
            Stars[k] = RS[j]
            RatingInt[k] = RR[j]
            Discount[k] = RDis[j]
            Description[k] = RDescript[j]
            j += 1
            k += 1
    else:
        while i < len(LR):
            MedicineName[k] = L[i]
            OldpriceInt[k] = LOld[i]
            NewPriceInt[k] = LNew[i]
            Quantity[k] = LQ[i]
            Stars[k] = LS[i]
            RatingInt[k] = LR[i]
            Discount[k] = LDis[i]
            Description[k] = LDescript[i]
            i += 1
            k += 1
    return MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description

def MergeSortDiscountDescending(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description, start, end):
    if start < end:
        q = (start + end) // 2
        MergeSortDiscountDescending(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description, start, q)
        MergeSortDiscountDescending(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description, q + 1, end)
        MergeDiscountDescending(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description, start, q, end)
    return MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description

def MergeDiscountDescending(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description, p, q, r):
    n1 = q - p + 1
    n2 = r - q
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

    for i in range(0, n1):
        L.append(MedicineName[p + i])
        LOld.append(OldpriceInt[p + i])
        LNew.append(NewPriceInt[p + i])
        LQ.append(Quantity[p + i])
        LS.append(Stars[p + i])
        LR.append(RatingInt[p + i])
        LDis.append(Discount[p + i])
        LDescript.append(Description[p + i])

    for j in range(0, n2):
        R.append(MedicineName[q + 1 + j])
        ROld.append(OldpriceInt[q + 1 + j])
        RNew.append(NewPriceInt[q + 1 + j])
        RQ.append(Quantity[q + 1 + j])
        RS.append(Stars[q + 1 + j])
        RR.append(RatingInt[q + 1 + j])
        RDis.append(Discount[q + 1 + j])
        RDescript.append(Description[q + 1 + j])
    i = 0
    j = 0
    k = p
    while i < n1 and j < n2:
        if(LDis[i] >= RDis[j]):
            MedicineName[k] = L[i]
            OldpriceInt[k] = LOld[i]
            NewPriceInt[k] = LNew[i]
            Quantity[k] = LQ[i]
            Stars[k] = LS[i]
            RatingInt[k] = LR[i]
            Discount[k] = LDis[i]
            Description[k] = LDescript[i]
            i += 1
        else:
            MedicineName[k] = R[j]
            OldpriceInt[k] = ROld[j]
            NewPriceInt[k] = RNew[j]
            Quantity[k] = RQ[j]
            Stars[k] = RS[j]
            RatingInt[k] = RR[j]
            Discount[k] = RDis[j]
            Description[k] = RDescript[j]
            j += 1
        k += 1
    if i == len(LDis):
        while j < n2:
            MedicineName[k] = R[j]
            OldpriceInt[k] = ROld[j]
            NewPriceInt[k] = RNew[j]
            Quantity[k] = RQ[j]
            Stars[k] = RS[j]
            RatingInt[k] = RR[j]
            Discount[k] = RDis[j]
            Description[k] = RDescript[j]
            j += 1
            k += 1
    else:
        while i < len(LDis):
            MedicineName[k] = L[i]
            OldpriceInt[k] = LOld[i]
            NewPriceInt[k] = LNew[i]
            Quantity[k] = LQ[i]
            Stars[k] = LS[i]
            RatingInt[k] = LR[i]
            Discount[k] = LDis[i]
            Description[k] = LDescript[i]
            i += 1
            k += 1
    return MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description

def MergeSortDescriptionDescending(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description, start, end):
    if start < end:
        q = (start + end) // 2
        MergeSortDescriptionDescending(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description, start, q)
        MergeSortDescriptionDescending(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description, q + 1, end)
        MergeDescriptionDescending(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description, start, q, end)
    return MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description

def MergeDescriptionDescending(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description, p, q, r):
    n1 = q - p + 1
    n2 = r - q
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

    for i in range(0, n1):
        L.append(MedicineName[p + i])
        LOld.append(OldpriceInt[p + i])
        LNew.append(NewPriceInt[p + i])
        LQ.append(Quantity[p + i])
        LS.append(Stars[p + i])
        LR.append(RatingInt[p + i])
        LDis.append(Discount[p + i])
        LDescript.append(Description[p + i])

    for j in range(0, n2):
        R.append(MedicineName[q + 1 + j])
        ROld.append(OldpriceInt[q + 1 + j])
        RNew.append(NewPriceInt[q + 1 + j])
        RQ.append(Quantity[q + 1 + j])
        RS.append(Stars[q + 1 + j])
        RR.append(RatingInt[q + 1 + j])
        RDis.append(Discount[q + 1 + j])
        RDescript.append(Description[q + 1 + j])
    i = 0
    j = 0
    k = p
    while i < n1 and j < n2:
        if(LDescript[i] >= RDescript[j]):
            MedicineName[k] = L[i]
            OldpriceInt[k] = LOld[i]
            NewPriceInt[k] = LNew[i]
            Quantity[k] = LQ[i]
            Stars[k] = LS[i]
            RatingInt[k] = LR[i]
            Discount[k] = LDis[i]
            Description[k] = LDescript[i]
            i += 1
        else:
            MedicineName[k] = R[j]
            OldpriceInt[k] = ROld[j]
            NewPriceInt[k] = RNew[j]
            Quantity[k] = RQ[j]
            Stars[k] = RS[j]
            RatingInt[k] = RR[j]
            Discount[k] = RDis[j]
            Description[k] = RDescript[j]
            j += 1
        k += 1
    if i == len(LDescript):
        while j < n2:
            MedicineName[k] = R[j]
            OldpriceInt[k] = ROld[j]
            NewPriceInt[k] = RNew[j]
            Quantity[k] = RQ[j]
            Stars[k] = RS[j]
            RatingInt[k] = RR[j]
            Discount[k] = RDis[j]
            Description[k] = RDescript[j]
            j += 1
            k += 1
    else:
        while i < len(LDescript):
            MedicineName[k] = L[i]
            OldpriceInt[k] = LOld[i]
            NewPriceInt[k] = LNew[i]
            Quantity[k] = LQ[i]
            Stars[k] = LS[i]
            RatingInt[k] = LR[i]
            Discount[k] = LDis[i]
            Description[k] = LDescript[i]
            i += 1
            k += 1
    return MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description