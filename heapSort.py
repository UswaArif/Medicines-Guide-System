#Heap Sort Ascending Function
def maxHeapify(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description, n, i):
    largest = i  
    left = 2 * i   
    right = 2 * i + 1  

    if left < n and MedicineName[i] < MedicineName[left]:
        largest = left
    else:
        largest = i
 
    if right < n and MedicineName[largest] < MedicineName[right]:
        largest = right
  
    if largest != i:
        temp = MedicineName[i]
        MedicineName[i] = MedicineName[largest] 
        MedicineName[largest] = temp

        tempOld = OldpriceInt[i]
        OldpriceInt[i] = OldpriceInt[largest] 
        OldpriceInt[largest] = tempOld

        tempNew = NewPriceInt[i]
        NewPriceInt[i] = NewPriceInt[largest] 
        NewPriceInt[largest] = tempNew

        tempQ = Quantity[i]
        Quantity[i] = Quantity[largest] 
        Quantity[largest] = tempQ

        tempS = Stars[i]
        Stars[i] = Stars[largest] 
        Stars[largest] = tempS

        tempR = RatingInt[i]
        RatingInt[i] = RatingInt[largest] 
        RatingInt[largest] = tempR

        tempDis = Discount[i]
        Discount[i] = Discount[largest] 
        Discount[largest] = tempDis

        tempDescript = Description[i]
        Description[i] = Description[largest] 
        Description[largest] = tempDescript

        maxHeapify(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description, n, largest)

def buildMaxHeap(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description):
    n = len(MedicineName)
    for i in range(n // 2 - 1, -1, -1):
        maxHeapify(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description, n, i)

def heapSortAscending(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description):
    n = len(MedicineName)
    buildMaxHeap(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description)
    for i in range(n - 1, 0, -1):
        temp = MedicineName[i]
        MedicineName[i] = MedicineName[0]
        MedicineName[0] = temp 

        tempOld = OldpriceInt[i]
        OldpriceInt[i] = OldpriceInt[0]
        OldpriceInt[0] = tempOld 

        tempNew = NewPriceInt[i]
        NewPriceInt[i] = NewPriceInt[0]
        NewPriceInt[0] = tempNew 

        tempQ = Quantity[i]
        Quantity[i] = Quantity[0]
        Quantity[0] = tempQ 

        tempS = Stars[i]
        Stars[i] = Stars[0]
        Stars[0] = tempS 

        tempR = RatingInt[i]
        RatingInt[i] = RatingInt[0]
        RatingInt[0] = tempR 

        tempDis = Discount[i]
        Discount[i] = Discount[0]
        Discount[0] = tempDis 

        tempDescript = Description[i]
        Description[i] = Description[0]
        Description[0] = tempDescript 
        maxHeapify(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description, i, 0)
    return MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description

def maxHeapifyOldprice(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description, n, i):
    largest = i  
    left = 2 * i   
    right = 2 * i + 1  

    if left < n and OldpriceInt[i] < OldpriceInt[left]:
        largest = left
    else:
        largest = i
 
    if right < n and OldpriceInt[largest] < OldpriceInt[right]:
        largest = right
  
    if largest != i:
        temp = MedicineName[i]
        MedicineName[i] = MedicineName[largest] 
        MedicineName[largest] = temp

        tempOld = OldpriceInt[i]
        OldpriceInt[i] = OldpriceInt[largest] 
        OldpriceInt[largest] = tempOld

        tempNew = NewPriceInt[i]
        NewPriceInt[i] = NewPriceInt[largest] 
        NewPriceInt[largest] = tempNew

        tempQ = Quantity[i]
        Quantity[i] = Quantity[largest] 
        Quantity[largest] = tempQ

        tempS = Stars[i]
        Stars[i] = Stars[largest] 
        Stars[largest] = tempS

        tempR = RatingInt[i]
        RatingInt[i] = RatingInt[largest] 
        RatingInt[largest] = tempR

        tempDis = Discount[i]
        Discount[i] = Discount[largest] 
        Discount[largest] = tempDis

        tempDescript = Description[i]
        Description[i] = Description[largest] 
        Description[largest] = tempDescript

        maxHeapifyOldprice(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description, n, largest)

def buildMaxHeapOldprice(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description):
    n = len(OldpriceInt)
    for i in range(n // 2 - 1, -1, -1):
        maxHeapifyOldprice(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description, n, i)

def heapSortOldpriceAscending(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description):
    n = len(OldpriceInt)
    buildMaxHeapOldprice(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description)
    for i in range(n - 1, 0, -1):
        temp = MedicineName[i]
        MedicineName[i] = MedicineName[0]
        MedicineName[0] = temp 

        tempOld = OldpriceInt[i]
        OldpriceInt[i] = OldpriceInt[0]
        OldpriceInt[0] = tempOld 

        tempNew = NewPriceInt[i]
        NewPriceInt[i] = NewPriceInt[0]
        NewPriceInt[0] = tempNew 

        tempQ = Quantity[i]
        Quantity[i] = Quantity[0]
        Quantity[0] = tempQ 

        tempS = Stars[i]
        Stars[i] = Stars[0]
        Stars[0] = tempS 

        tempR = RatingInt[i]
        RatingInt[i] = RatingInt[0]
        RatingInt[0] = tempR 

        tempDis = Discount[i]
        Discount[i] = Discount[0]
        Discount[0] = tempDis 

        tempDescript = Description[i]
        Description[i] = Description[0]
        Description[0] = tempDescript 
        maxHeapifyOldprice(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description, i, 0)
    return MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description

def maxHeapifyNewPrice(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description, n, i):
    largest = i  
    left = 2 * i   
    right = 2 * i + 1  

    if left < n and NewPriceInt[i] < NewPriceInt[left]:
        largest = left
    else:
        largest = i
 
    if right < n and NewPriceInt[largest] < NewPriceInt[right]:
        largest = right
  
    if largest != i:
        temp = MedicineName[i]
        MedicineName[i] = MedicineName[largest] 
        MedicineName[largest] = temp

        tempOld = OldpriceInt[i]
        OldpriceInt[i] = OldpriceInt[largest] 
        OldpriceInt[largest] = tempOld

        tempNew = NewPriceInt[i]
        NewPriceInt[i] = NewPriceInt[largest] 
        NewPriceInt[largest] = tempNew

        tempQ = Quantity[i]
        Quantity[i] = Quantity[largest] 
        Quantity[largest] = tempQ

        tempS = Stars[i]
        Stars[i] = Stars[largest] 
        Stars[largest] = tempS

        tempR = RatingInt[i]
        RatingInt[i] = RatingInt[largest] 
        RatingInt[largest] = tempR

        tempDis = Discount[i]
        Discount[i] = Discount[largest] 
        Discount[largest] = tempDis

        tempDescript = Description[i]
        Description[i] = Description[largest] 
        Description[largest] = tempDescript

        maxHeapifyNewPrice(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description, n, largest)

def buildMaxHeapNewPrice(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description):
    n = len(NewPriceInt)
    for i in range(n // 2 - 1, -1, -1):
        maxHeapifyNewPrice(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description, n, i)

def heapSortNewPriceAscending(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description):
    n = len(NewPriceInt)
    buildMaxHeapNewPrice(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description)
    for i in range(n - 1, 0, -1):
        temp = MedicineName[i]
        MedicineName[i] = MedicineName[0]
        MedicineName[0] = temp 

        tempOld = OldpriceInt[i]
        OldpriceInt[i] = OldpriceInt[0]
        OldpriceInt[0] = tempOld 

        tempNew = NewPriceInt[i]
        NewPriceInt[i] = NewPriceInt[0]
        NewPriceInt[0] = tempNew 

        tempQ = Quantity[i]
        Quantity[i] = Quantity[0]
        Quantity[0] = tempQ 

        tempS = Stars[i]
        Stars[i] = Stars[0]
        Stars[0] = tempS 

        tempR = RatingInt[i]
        RatingInt[i] = RatingInt[0]
        RatingInt[0] = tempR 

        tempDis = Discount[i]
        Discount[i] = Discount[0]
        Discount[0] = tempDis 

        tempDescript = Description[i]
        Description[i] = Description[0]
        Description[0] = tempDescript 
        maxHeapifyNewPrice(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description, i, 0)
    return MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description

def maxHeapifyQuantity(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description, n, i):
    largest = i  
    left = 2 * i   
    right = 2 * i + 1  

    if left < n and Quantity[i] < Quantity[left]:
        largest = left
    else:
        largest = i
 
    if right < n and Quantity[largest] < Quantity[right]:
        largest = right
  
    if largest != i:
        temp = MedicineName[i]
        MedicineName[i] = MedicineName[largest] 
        MedicineName[largest] = temp

        tempOld = OldpriceInt[i]
        OldpriceInt[i] = OldpriceInt[largest] 
        OldpriceInt[largest] = tempOld

        tempNew = NewPriceInt[i]
        NewPriceInt[i] = NewPriceInt[largest] 
        NewPriceInt[largest] = tempNew

        tempQ = Quantity[i]
        Quantity[i] = Quantity[largest] 
        Quantity[largest] = tempQ

        tempS = Stars[i]
        Stars[i] = Stars[largest] 
        Stars[largest] = tempS

        tempR = RatingInt[i]
        RatingInt[i] = RatingInt[largest] 
        RatingInt[largest] = tempR

        tempDis = Discount[i]
        Discount[i] = Discount[largest] 
        Discount[largest] = tempDis

        tempDescript = Description[i]
        Description[i] = Description[largest] 
        Description[largest] = tempDescript

        maxHeapifyQuantity(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description, n, largest)

def buildMaxHeapQuantity(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description):
    n = len(Quantity)
    for i in range(n // 2 - 1, -1, -1):
        maxHeapifyQuantity(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description, n, i)

def heapSortQuantityAscending(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description):
    n = len(Quantity)
    buildMaxHeapQuantity(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description)
    for i in range(n - 1, 0, -1):
        temp = MedicineName[i]
        MedicineName[i] = MedicineName[0]
        MedicineName[0] = temp 

        tempOld = OldpriceInt[i]
        OldpriceInt[i] = OldpriceInt[0]
        OldpriceInt[0] = tempOld 

        tempNew = NewPriceInt[i]
        NewPriceInt[i] = NewPriceInt[0]
        NewPriceInt[0] = tempNew 

        tempQ = Quantity[i]
        Quantity[i] = Quantity[0]
        Quantity[0] = tempQ 

        tempS = Stars[i]
        Stars[i] = Stars[0]
        Stars[0] = tempS 

        tempR = RatingInt[i]
        RatingInt[i] = RatingInt[0]
        RatingInt[0] = tempR 

        tempDis = Discount[i]
        Discount[i] = Discount[0]
        Discount[0] = tempDis 

        tempDescript = Description[i]
        Description[i] = Description[0]
        Description[0] = tempDescript 
        maxHeapifyQuantity(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description, i, 0)
    return MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description
 
def maxHeapifyStars(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description, n, i):
    largest = i  
    left = 2 * i   
    right = 2 * i + 1  

    if left < n and Stars[i] < Stars[left]:
        largest = left
    else:
        largest = i
 
    if right < n and Stars[largest] < Stars[right]:
        largest = right
  
    if largest != i:
        temp = MedicineName[i]
        MedicineName[i] = MedicineName[largest] 
        MedicineName[largest] = temp

        tempOld = OldpriceInt[i]
        OldpriceInt[i] = OldpriceInt[largest] 
        OldpriceInt[largest] = tempOld

        tempNew = NewPriceInt[i]
        NewPriceInt[i] = NewPriceInt[largest] 
        NewPriceInt[largest] = tempNew

        tempQ = Quantity[i]
        Quantity[i] = Quantity[largest] 
        Quantity[largest] = tempQ

        tempS = Stars[i]
        Stars[i] = Stars[largest] 
        Stars[largest] = tempS

        tempR = RatingInt[i]
        RatingInt[i] = RatingInt[largest] 
        RatingInt[largest] = tempR

        tempDis = Discount[i]
        Discount[i] = Discount[largest] 
        Discount[largest] = tempDis

        tempDescript = Description[i]
        Description[i] = Description[largest] 
        Description[largest] = tempDescript

        maxHeapifyStars(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description, n, largest)

def buildMaxHeapStars(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description):
    n = len(Stars)
    for i in range(n // 2 - 1, -1, -1):
        maxHeapifyStars(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description, n, i)

def heapSortStarsAscending(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description):
    n = len(Stars)
    buildMaxHeapStars(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description)
    for i in range(n - 1, 0, -1):
        temp = MedicineName[i]
        MedicineName[i] = MedicineName[0]
        MedicineName[0] = temp 

        tempOld = OldpriceInt[i]
        OldpriceInt[i] = OldpriceInt[0]
        OldpriceInt[0] = tempOld 

        tempNew = NewPriceInt[i]
        NewPriceInt[i] = NewPriceInt[0]
        NewPriceInt[0] = tempNew 

        tempQ = Quantity[i]
        Quantity[i] = Quantity[0]
        Quantity[0] = tempQ 

        tempS = Stars[i]
        Stars[i] = Stars[0]
        Stars[0] = tempS 

        tempR = RatingInt[i]
        RatingInt[i] = RatingInt[0]
        RatingInt[0] = tempR 

        tempDis = Discount[i]
        Discount[i] = Discount[0]
        Discount[0] = tempDis 

        tempDescript = Description[i]
        Description[i] = Description[0]
        Description[0] = tempDescript 
        maxHeapifyStars(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description, i, 0)
    return MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description

def maxHeapifyRating(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description, n, i):
    largest = i  
    left = 2 * i   
    right = 2 * i + 1  

    if left < n and RatingInt[i] < RatingInt[left]:
        largest = left
    else:
        largest = i
 
    if right < n and RatingInt[largest] < RatingInt[right]:
        largest = right
  
    if largest != i:
        temp = MedicineName[i]
        MedicineName[i] = MedicineName[largest] 
        MedicineName[largest] = temp

        tempOld = OldpriceInt[i]
        OldpriceInt[i] = OldpriceInt[largest] 
        OldpriceInt[largest] = tempOld

        tempNew = NewPriceInt[i]
        NewPriceInt[i] = NewPriceInt[largest] 
        NewPriceInt[largest] = tempNew

        tempQ = Quantity[i]
        Quantity[i] = Quantity[largest] 
        Quantity[largest] = tempQ

        tempS = Stars[i]
        Stars[i] = Stars[largest] 
        Stars[largest] = tempS

        tempR = RatingInt[i]
        RatingInt[i] = RatingInt[largest] 
        RatingInt[largest] = tempR

        tempDis = Discount[i]
        Discount[i] = Discount[largest] 
        Discount[largest] = tempDis

        tempDescript = Description[i]
        Description[i] = Description[largest] 
        Description[largest] = tempDescript

        maxHeapifyRating(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description, n, largest)

def buildMaxHeapRating(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description):
    n = len(RatingInt)
    for i in range(n // 2 - 1, -1, -1):
        maxHeapifyRating(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description, n, i)

def heapSortRatingAscending(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description):
    n = len(RatingInt)
    buildMaxHeapRating(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description)
    for i in range(n - 1, 0, -1):
        temp = MedicineName[i]
        MedicineName[i] = MedicineName[0]
        MedicineName[0] = temp 

        tempOld = OldpriceInt[i]
        OldpriceInt[i] = OldpriceInt[0]
        OldpriceInt[0] = tempOld 

        tempNew = NewPriceInt[i]
        NewPriceInt[i] = NewPriceInt[0]
        NewPriceInt[0] = tempNew 

        tempQ = Quantity[i]
        Quantity[i] = Quantity[0]
        Quantity[0] = tempQ 

        tempS = Stars[i]
        Stars[i] = Stars[0]
        Stars[0] = tempS 

        tempR = RatingInt[i]
        RatingInt[i] = RatingInt[0]
        RatingInt[0] = tempR 

        tempDis = Discount[i]
        Discount[i] = Discount[0]
        Discount[0] = tempDis 

        tempDescript = Description[i]
        Description[i] = Description[0]
        Description[0] = tempDescript 
        maxHeapifyRating(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description, i, 0)
    return MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description

def maxHeapifyDiscount(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description, n, i):
    largest = i  
    left = 2 * i   
    right = 2 * i + 1  

    if left < n and Discount[i] < Discount[left]:
        largest = left
    else:
        largest = i
 
    if right < n and Discount[largest] < Discount[right]:
        largest = right
  
    if largest != i:
        temp = MedicineName[i]
        MedicineName[i] = MedicineName[largest] 
        MedicineName[largest] = temp

        tempOld = OldpriceInt[i]
        OldpriceInt[i] = OldpriceInt[largest] 
        OldpriceInt[largest] = tempOld

        tempNew = NewPriceInt[i]
        NewPriceInt[i] = NewPriceInt[largest] 
        NewPriceInt[largest] = tempNew

        tempQ = Quantity[i]
        Quantity[i] = Quantity[largest] 
        Quantity[largest] = tempQ

        tempS = Stars[i]
        Stars[i] = Stars[largest] 
        Stars[largest] = tempS

        tempR = RatingInt[i]
        RatingInt[i] = RatingInt[largest] 
        RatingInt[largest] = tempR

        tempDis = Discount[i]
        Discount[i] = Discount[largest] 
        Discount[largest] = tempDis

        tempDescript = Description[i]
        Description[i] = Description[largest] 
        Description[largest] = tempDescript

        maxHeapifyDiscount(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description, n, largest)

def buildMaxHeapDiscount(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description):
    n = len(Discount)
    for i in range(n // 2 - 1, -1, -1):
        maxHeapifyDiscount(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description, n, i)

def heapSortDiscountAscending(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description):
    n = len(Discount)
    buildMaxHeapDiscount(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description)
    for i in range(n - 1, 0, -1):
        temp = MedicineName[i]
        MedicineName[i] = MedicineName[0]
        MedicineName[0] = temp 

        tempOld = OldpriceInt[i]
        OldpriceInt[i] = OldpriceInt[0]
        OldpriceInt[0] = tempOld 

        tempNew = NewPriceInt[i]
        NewPriceInt[i] = NewPriceInt[0]
        NewPriceInt[0] = tempNew 

        tempQ = Quantity[i]
        Quantity[i] = Quantity[0]
        Quantity[0] = tempQ 

        tempS = Stars[i]
        Stars[i] = Stars[0]
        Stars[0] = tempS 

        tempR = RatingInt[i]
        RatingInt[i] = RatingInt[0]
        RatingInt[0] = tempR 

        tempDis = Discount[i]
        Discount[i] = Discount[0]
        Discount[0] = tempDis 

        tempDescript = Description[i]
        Description[i] = Description[0]
        Description[0] = tempDescript 
        maxHeapifyDiscount(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description, i, 0)
    return MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description

def maxHeapifyDescription(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description, n, i):
    largest = i  
    left = 2 * i   
    right = 2 * i + 1  

    if left < n and Description[i] < Description[left]:
        largest = left
    else:
        largest = i
 
    if right < n and Description[largest] < Description[right]:
        largest = right
  
    if largest != i:
        temp = MedicineName[i]
        MedicineName[i] = MedicineName[largest] 
        MedicineName[largest] = temp

        tempOld = OldpriceInt[i]
        OldpriceInt[i] = OldpriceInt[largest] 
        OldpriceInt[largest] = tempOld

        tempNew = NewPriceInt[i]
        NewPriceInt[i] = NewPriceInt[largest] 
        NewPriceInt[largest] = tempNew

        tempQ = Quantity[i]
        Quantity[i] = Quantity[largest] 
        Quantity[largest] = tempQ

        tempS = Stars[i]
        Stars[i] = Stars[largest] 
        Stars[largest] = tempS

        tempR = RatingInt[i]
        RatingInt[i] = RatingInt[largest] 
        RatingInt[largest] = tempR

        tempDis = Discount[i]
        Discount[i] = Discount[largest] 
        Discount[largest] = tempDis

        tempDescript = Description[i]
        Description[i] = Description[largest] 
        Description[largest] = tempDescript

        maxHeapifyDescription(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description, n, largest)

def buildMaxHeapDescription(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description):
    n = len(Description)
    for i in range(n // 2 - 1, -1, -1):
        maxHeapifyDescription(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description, n, i)

def heapSortDescriptionAscending(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description):
    n = len(Description)
    buildMaxHeapDescription(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description)
    for i in range(n - 1, 0, -1):
        temp = MedicineName[i]
        MedicineName[i] = MedicineName[0]
        MedicineName[0] = temp 

        tempOld = OldpriceInt[i]
        OldpriceInt[i] = OldpriceInt[0]
        OldpriceInt[0] = tempOld 

        tempNew = NewPriceInt[i]
        NewPriceInt[i] = NewPriceInt[0]
        NewPriceInt[0] = tempNew 

        tempQ = Quantity[i]
        Quantity[i] = Quantity[0]
        Quantity[0] = tempQ 

        tempS = Stars[i]
        Stars[i] = Stars[0]
        Stars[0] = tempS 

        tempR = RatingInt[i]
        RatingInt[i] = RatingInt[0]
        RatingInt[0] = tempR 

        tempDis = Discount[i]
        Discount[i] = Discount[0]
        Discount[0] = tempDis 

        tempDescript = Description[i]
        Description[i] = Description[0]
        Description[0] = tempDescript 
        maxHeapifyDescription(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description, i, 0)
    return MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description

#Heap Sort Descending Function
def maxHeapifyDescending(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description, n, i):
    largest = i  
    left = 2 * i   
    right = 2 * i + 1  

    if left < n and MedicineName[i] > MedicineName[left]:
        largest = left
    else:
        largest = i
 
    if right < n and MedicineName[largest] > MedicineName[right]:
        largest = right
  
    if largest != i:
        temp = MedicineName[i]
        MedicineName[i] = MedicineName[largest] 
        MedicineName[largest] = temp

        tempOld = OldpriceInt[i]
        OldpriceInt[i] = OldpriceInt[largest] 
        OldpriceInt[largest] = tempOld

        tempNew = NewPriceInt[i]
        NewPriceInt[i] = NewPriceInt[largest] 
        NewPriceInt[largest] = tempNew

        tempQ = Quantity[i]
        Quantity[i] = Quantity[largest] 
        Quantity[largest] = tempQ

        tempS = Stars[i]
        Stars[i] = Stars[largest] 
        Stars[largest] = tempS

        tempR = RatingInt[i]
        RatingInt[i] = RatingInt[largest] 
        RatingInt[largest] = tempR

        tempDis = Discount[i]
        Discount[i] = Discount[largest] 
        Discount[largest] = tempDis

        tempDescript = Description[i]
        Description[i] = Description[largest] 
        Description[largest] = tempDescript

        maxHeapifyDescending(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description, n, largest)

def buildMaxHeapDescending(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description):
    n = len(MedicineName)
    for i in range(n // 2 - 1, -1, -1):
        maxHeapifyDescending(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description, n, i)

def heapSortDescending(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description):
    n = len(MedicineName)
    buildMaxHeapDescending(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description)
    for i in range(n - 1, 0, -1):
        temp = MedicineName[i]
        MedicineName[i] = MedicineName[0]
        MedicineName[0] = temp 

        tempOld = OldpriceInt[i]
        OldpriceInt[i] = OldpriceInt[0]
        OldpriceInt[0] = tempOld 

        tempNew = NewPriceInt[i]
        NewPriceInt[i] = NewPriceInt[0]
        NewPriceInt[0] = tempNew 

        tempQ = Quantity[i]
        Quantity[i] = Quantity[0]
        Quantity[0] = tempQ 

        tempS = Stars[i]
        Stars[i] = Stars[0]
        Stars[0] = tempS 

        tempR = RatingInt[i]
        RatingInt[i] = RatingInt[0]
        RatingInt[0] = tempR 

        tempDis = Discount[i]
        Discount[i] = Discount[0]
        Discount[0] = tempDis 

        tempDescript = Description[i]
        Description[i] = Description[0]
        Description[0] = tempDescript 
        maxHeapifyDescending(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description, i, 0)
    return MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description

def maxHeapifyOldpriceDescending(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description, n, i):
    largest = i  
    left = 2 * i   
    right = 2 * i + 1  

    if left < n and OldpriceInt[i] > OldpriceInt[left]:
        largest = left
    else:
        largest = i
 
    if right < n and OldpriceInt[largest] > OldpriceInt[right]:
        largest = right
  
    if largest != i:
        temp = MedicineName[i]
        MedicineName[i] = MedicineName[largest] 
        MedicineName[largest] = temp

        tempOld = OldpriceInt[i]
        OldpriceInt[i] = OldpriceInt[largest] 
        OldpriceInt[largest] = tempOld

        tempNew = NewPriceInt[i]
        NewPriceInt[i] = NewPriceInt[largest] 
        NewPriceInt[largest] = tempNew

        tempQ = Quantity[i]
        Quantity[i] = Quantity[largest] 
        Quantity[largest] = tempQ

        tempS = Stars[i]
        Stars[i] = Stars[largest] 
        Stars[largest] = tempS

        tempR = RatingInt[i]
        RatingInt[i] = RatingInt[largest] 
        RatingInt[largest] = tempR

        tempDis = Discount[i]
        Discount[i] = Discount[largest] 
        Discount[largest] = tempDis

        tempDescript = Description[i]
        Description[i] = Description[largest] 
        Description[largest] = tempDescript

        maxHeapifyOldpriceDescending(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description, n, largest)

def buildMaxHeapOldpriceDescending(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description):
    n = len(OldpriceInt)
    for i in range(n // 2 - 1, -1, -1):
        maxHeapifyOldpriceDescending(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description, n, i)

def heapSortOldpriceDescending(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description):
    n = len(OldpriceInt)
    buildMaxHeapOldpriceDescending(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description)
    for i in range(n - 1, 0, -1):
        temp = MedicineName[i]
        MedicineName[i] = MedicineName[0]
        MedicineName[0] = temp 

        tempOld = OldpriceInt[i]
        OldpriceInt[i] = OldpriceInt[0]
        OldpriceInt[0] = tempOld 

        tempNew = NewPriceInt[i]
        NewPriceInt[i] = NewPriceInt[0]
        NewPriceInt[0] = tempNew 

        tempQ = Quantity[i]
        Quantity[i] = Quantity[0]
        Quantity[0] = tempQ 

        tempS = Stars[i]
        Stars[i] = Stars[0]
        Stars[0] = tempS 

        tempR = RatingInt[i]
        RatingInt[i] = RatingInt[0]
        RatingInt[0] = tempR 

        tempDis = Discount[i]
        Discount[i] = Discount[0]
        Discount[0] = tempDis 

        tempDescript = Description[i]
        Description[i] = Description[0]
        Description[0] = tempDescript 
        maxHeapifyOldpriceDescending(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description, i, 0)
    return MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description

def maxHeapifyNewPriceDescending(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description, n, i):
    largest = i  
    left = 2 * i   
    right = 2 * i + 1  

    if left < n and NewPriceInt[i] > NewPriceInt[left]:
        largest = left
    else:
        largest = i
 
    if right < n and NewPriceInt[largest] > NewPriceInt[right]:
        largest = right
  
    if largest != i:
        temp = MedicineName[i]
        MedicineName[i] = MedicineName[largest] 
        MedicineName[largest] = temp

        tempOld = OldpriceInt[i]
        OldpriceInt[i] = OldpriceInt[largest] 
        OldpriceInt[largest] = tempOld

        tempNew = NewPriceInt[i]
        NewPriceInt[i] = NewPriceInt[largest] 
        NewPriceInt[largest] = tempNew

        tempQ = Quantity[i]
        Quantity[i] = Quantity[largest] 
        Quantity[largest] = tempQ

        tempS = Stars[i]
        Stars[i] = Stars[largest] 
        Stars[largest] = tempS

        tempR = RatingInt[i]
        RatingInt[i] = RatingInt[largest] 
        RatingInt[largest] = tempR

        tempDis = Discount[i]
        Discount[i] = Discount[largest] 
        Discount[largest] = tempDis

        tempDescript = Description[i]
        Description[i] = Description[largest] 
        Description[largest] = tempDescript

        maxHeapifyNewPriceDescending(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description, n, largest)

def buildMaxHeapNewPriceDescending(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description):
    n = len(NewPriceInt)
    for i in range(n // 2 - 1, -1, -1):
        maxHeapifyNewPriceDescending(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description, n, i)

def heapSortNewPriceDescending(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description):
    n = len(NewPriceInt)
    buildMaxHeapNewPriceDescending(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description)
    for i in range(n - 1, 0, -1):
        temp = MedicineName[i]
        MedicineName[i] = MedicineName[0]
        MedicineName[0] = temp 

        tempOld = OldpriceInt[i]
        OldpriceInt[i] = OldpriceInt[0]
        OldpriceInt[0] = tempOld 

        tempNew = NewPriceInt[i]
        NewPriceInt[i] = NewPriceInt[0]
        NewPriceInt[0] = tempNew 

        tempQ = Quantity[i]
        Quantity[i] = Quantity[0]
        Quantity[0] = tempQ 

        tempS = Stars[i]
        Stars[i] = Stars[0]
        Stars[0] = tempS 

        tempR = RatingInt[i]
        RatingInt[i] = RatingInt[0]
        RatingInt[0] = tempR 

        tempDis = Discount[i]
        Discount[i] = Discount[0]
        Discount[0] = tempDis 

        tempDescript = Description[i]
        Description[i] = Description[0]
        Description[0] = tempDescript 
        maxHeapifyNewPriceDescending(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description, i, 0)
    return MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description

def maxHeapifyQuantityDescending(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description, n, i):
    largest = i  
    left = 2 * i   
    right = 2 * i + 1  

    if left < n and Quantity[i] > Quantity[left]:
        largest = left
    else:
        largest = i
 
    if right < n and Quantity[largest] > Quantity[right]:
        largest = right
  
    if largest != i:
        temp = MedicineName[i]
        MedicineName[i] = MedicineName[largest] 
        MedicineName[largest] = temp

        tempOld = OldpriceInt[i]
        OldpriceInt[i] = OldpriceInt[largest] 
        OldpriceInt[largest] = tempOld

        tempNew = NewPriceInt[i]
        NewPriceInt[i] = NewPriceInt[largest] 
        NewPriceInt[largest] = tempNew

        tempQ = Quantity[i]
        Quantity[i] = Quantity[largest] 
        Quantity[largest] = tempQ

        tempS = Stars[i]
        Stars[i] = Stars[largest] 
        Stars[largest] = tempS

        tempR = RatingInt[i]
        RatingInt[i] = RatingInt[largest] 
        RatingInt[largest] = tempR

        tempDis = Discount[i]
        Discount[i] = Discount[largest] 
        Discount[largest] = tempDis

        tempDescript = Description[i]
        Description[i] = Description[largest] 
        Description[largest] = tempDescript

        maxHeapifyQuantityDescending(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description, n, largest)

def buildMaxHeapQuantityDescending(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description):
    n = len(Quantity)
    for i in range(n // 2 - 1, -1, -1):
        maxHeapifyQuantityDescending(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description, n, i)

def heapSortQuantityDescending(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description):
    n = len(Quantity)
    buildMaxHeapQuantityDescending(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description)
    for i in range(n - 1, 0, -1):
        temp = MedicineName[i]
        MedicineName[i] = MedicineName[0]
        MedicineName[0] = temp 

        tempOld = OldpriceInt[i]
        OldpriceInt[i] = OldpriceInt[0]
        OldpriceInt[0] = tempOld 

        tempNew = NewPriceInt[i]
        NewPriceInt[i] = NewPriceInt[0]
        NewPriceInt[0] = tempNew 

        tempQ = Quantity[i]
        Quantity[i] = Quantity[0]
        Quantity[0] = tempQ 

        tempS = Stars[i]
        Stars[i] = Stars[0]
        Stars[0] = tempS 

        tempR = RatingInt[i]
        RatingInt[i] = RatingInt[0]
        RatingInt[0] = tempR 

        tempDis = Discount[i]
        Discount[i] = Discount[0]
        Discount[0] = tempDis 

        tempDescript = Description[i]
        Description[i] = Description[0]
        Description[0] = tempDescript 
        maxHeapifyQuantityDescending(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description, i, 0)
    return MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description
 
def maxHeapifyStarsDescending(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description, n, i):
    largest = i  
    left = 2 * i   
    right = 2 * i + 1  

    if left < n and Stars[i] > Stars[left]:
        largest = left
    else:
        largest = i
 
    if right < n and Stars[largest] > Stars[right]:
        largest = right
  
    if largest != i:
        temp = MedicineName[i]
        MedicineName[i] = MedicineName[largest] 
        MedicineName[largest] = temp

        tempOld = OldpriceInt[i]
        OldpriceInt[i] = OldpriceInt[largest] 
        OldpriceInt[largest] = tempOld

        tempNew = NewPriceInt[i]
        NewPriceInt[i] = NewPriceInt[largest] 
        NewPriceInt[largest] = tempNew

        tempQ = Quantity[i]
        Quantity[i] = Quantity[largest] 
        Quantity[largest] = tempQ

        tempS = Stars[i]
        Stars[i] = Stars[largest] 
        Stars[largest] = tempS

        tempR = RatingInt[i]
        RatingInt[i] = RatingInt[largest] 
        RatingInt[largest] = tempR

        tempDis = Discount[i]
        Discount[i] = Discount[largest] 
        Discount[largest] = tempDis

        tempDescript = Description[i]
        Description[i] = Description[largest] 
        Description[largest] = tempDescript

        maxHeapifyStarsDescending(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description, n, largest)

def buildMaxHeapStarsDescending(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description):
    n = len(Stars)
    for i in range(n // 2 - 1, -1, -1):
        maxHeapifyStarsDescending(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description, n, i)

def heapSortStarsDescending(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description):
    n = len(Stars)
    buildMaxHeapStarsDescending(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description)
    for i in range(n - 1, 0, -1):
        temp = MedicineName[i]
        MedicineName[i] = MedicineName[0]
        MedicineName[0] = temp 

        tempOld = OldpriceInt[i]
        OldpriceInt[i] = OldpriceInt[0]
        OldpriceInt[0] = tempOld 

        tempNew = NewPriceInt[i]
        NewPriceInt[i] = NewPriceInt[0]
        NewPriceInt[0] = tempNew 

        tempQ = Quantity[i]
        Quantity[i] = Quantity[0]
        Quantity[0] = tempQ 

        tempS = Stars[i]
        Stars[i] = Stars[0]
        Stars[0] = tempS 

        tempR = RatingInt[i]
        RatingInt[i] = RatingInt[0]
        RatingInt[0] = tempR 

        tempDis = Discount[i]
        Discount[i] = Discount[0]
        Discount[0] = tempDis 

        tempDescript = Description[i]
        Description[i] = Description[0]
        Description[0] = tempDescript 
        maxHeapifyStarsDescending(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description, i, 0)
    return MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description

def maxHeapifyRatingDescending(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description, n, i):
    largest = i  
    left = 2 * i   
    right = 2 * i + 1  

    if left < n and RatingInt[i] > RatingInt[left]:
        largest = left
    else:
        largest = i
 
    if right < n and RatingInt[largest] > RatingInt[right]:
        largest = right
  
    if largest != i:
        temp = MedicineName[i]
        MedicineName[i] = MedicineName[largest] 
        MedicineName[largest] = temp

        tempOld = OldpriceInt[i]
        OldpriceInt[i] = OldpriceInt[largest] 
        OldpriceInt[largest] = tempOld

        tempNew = NewPriceInt[i]
        NewPriceInt[i] = NewPriceInt[largest] 
        NewPriceInt[largest] = tempNew

        tempQ = Quantity[i]
        Quantity[i] = Quantity[largest] 
        Quantity[largest] = tempQ

        tempS = Stars[i]
        Stars[i] = Stars[largest] 
        Stars[largest] = tempS

        tempR = RatingInt[i]
        RatingInt[i] = RatingInt[largest] 
        RatingInt[largest] = tempR

        tempDis = Discount[i]
        Discount[i] = Discount[largest] 
        Discount[largest] = tempDis

        tempDescript = Description[i]
        Description[i] = Description[largest] 
        Description[largest] = tempDescript

        maxHeapifyRatingDescending(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description, n, largest)

def buildMaxHeapRatingDescending(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description):
    n = len(RatingInt)
    for i in range(n // 2 - 1, -1, -1):
        maxHeapifyRatingDescending(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description, n, i)

def heapSortRatingDescending(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description):
    n = len(RatingInt)
    buildMaxHeapRatingDescending(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description)
    for i in range(n - 1, 0, -1):
        temp = MedicineName[i]
        MedicineName[i] = MedicineName[0]
        MedicineName[0] = temp 

        tempOld = OldpriceInt[i]
        OldpriceInt[i] = OldpriceInt[0]
        OldpriceInt[0] = tempOld 

        tempNew = NewPriceInt[i]
        NewPriceInt[i] = NewPriceInt[0]
        NewPriceInt[0] = tempNew 

        tempQ = Quantity[i]
        Quantity[i] = Quantity[0]
        Quantity[0] = tempQ 

        tempS = Stars[i]
        Stars[i] = Stars[0]
        Stars[0] = tempS 

        tempR = RatingInt[i]
        RatingInt[i] = RatingInt[0]
        RatingInt[0] = tempR 

        tempDis = Discount[i]
        Discount[i] = Discount[0]
        Discount[0] = tempDis 

        tempDescript = Description[i]
        Description[i] = Description[0]
        Description[0] = tempDescript 
        maxHeapifyRatingDescending(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description, i, 0)
    return MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description

def maxHeapifyDiscountDescending(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description, n, i):
    largest = i  
    left = 2 * i   
    right = 2 * i + 1  

    if left < n and Discount[i] > Discount[left]:
        largest = left
    else:
        largest = i
 
    if right < n and Discount[largest] > Discount[right]:
        largest = right
  
    if largest != i:
        temp = MedicineName[i]
        MedicineName[i] = MedicineName[largest] 
        MedicineName[largest] = temp

        tempOld = OldpriceInt[i]
        OldpriceInt[i] = OldpriceInt[largest] 
        OldpriceInt[largest] = tempOld

        tempNew = NewPriceInt[i]
        NewPriceInt[i] = NewPriceInt[largest] 
        NewPriceInt[largest] = tempNew

        tempQ = Quantity[i]
        Quantity[i] = Quantity[largest] 
        Quantity[largest] = tempQ

        tempS = Stars[i]
        Stars[i] = Stars[largest] 
        Stars[largest] = tempS

        tempR = RatingInt[i]
        RatingInt[i] = RatingInt[largest] 
        RatingInt[largest] = tempR

        tempDis = Discount[i]
        Discount[i] = Discount[largest] 
        Discount[largest] = tempDis

        tempDescript = Description[i]
        Description[i] = Description[largest] 
        Description[largest] = tempDescript

        maxHeapifyDiscountDescending(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description, n, largest)

def buildMaxHeapDiscountDescending(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description):
    n = len(Discount)
    for i in range(n // 2 - 1, -1, -1):
        maxHeapifyDiscountDescending(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description, n, i)

def heapSortDiscountDescending(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description):
    n = len(Discount)
    buildMaxHeapDiscountDescending(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description)
    for i in range(n - 1, 0, -1):
        temp = MedicineName[i]
        MedicineName[i] = MedicineName[0]
        MedicineName[0] = temp 

        tempOld = OldpriceInt[i]
        OldpriceInt[i] = OldpriceInt[0]
        OldpriceInt[0] = tempOld 

        tempNew = NewPriceInt[i]
        NewPriceInt[i] = NewPriceInt[0]
        NewPriceInt[0] = tempNew 

        tempQ = Quantity[i]
        Quantity[i] = Quantity[0]
        Quantity[0] = tempQ 

        tempS = Stars[i]
        Stars[i] = Stars[0]
        Stars[0] = tempS 

        tempR = RatingInt[i]
        RatingInt[i] = RatingInt[0]
        RatingInt[0] = tempR 

        tempDis = Discount[i]
        Discount[i] = Discount[0]
        Discount[0] = tempDis 

        tempDescript = Description[i]
        Description[i] = Description[0]
        Description[0] = tempDescript 
        maxHeapifyDiscountDescending(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description, i, 0)
    return MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description

def maxHeapifyDescriptionDescending(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description, n, i):
    largest = i  
    left = 2 * i   
    right = 2 * i + 1  

    if left < n and Description[i] > Description[left]:
        largest = left
    else:
        largest = i
 
    if right < n and Description[largest] > Description[right]:
        largest = right
  
    if largest != i:
        temp = MedicineName[i]
        MedicineName[i] = MedicineName[largest] 
        MedicineName[largest] = temp

        tempOld = OldpriceInt[i]
        OldpriceInt[i] = OldpriceInt[largest] 
        OldpriceInt[largest] = tempOld

        tempNew = NewPriceInt[i]
        NewPriceInt[i] = NewPriceInt[largest] 
        NewPriceInt[largest] = tempNew

        tempQ = Quantity[i]
        Quantity[i] = Quantity[largest] 
        Quantity[largest] = tempQ

        tempS = Stars[i]
        Stars[i] = Stars[largest] 
        Stars[largest] = tempS

        tempR = RatingInt[i]
        RatingInt[i] = RatingInt[largest] 
        RatingInt[largest] = tempR

        tempDis = Discount[i]
        Discount[i] = Discount[largest] 
        Discount[largest] = tempDis

        tempDescript = Description[i]
        Description[i] = Description[largest] 
        Description[largest] = tempDescript

        maxHeapifyDescriptionDescending(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description, n, largest)

def buildMaxHeapDescriptionDescending(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description):
    n = len(Description)
    for i in range(n // 2 - 1, -1, -1):
        maxHeapifyDescriptionDescending(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description, n, i)

def heapSortDescriptionDescending(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description):
    n = len(Description)
    buildMaxHeapDescriptionDescending(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description)
    for i in range(n - 1, 0, -1):
        temp = MedicineName[i]
        MedicineName[i] = MedicineName[0]
        MedicineName[0] = temp 

        tempOld = OldpriceInt[i]
        OldpriceInt[i] = OldpriceInt[0]
        OldpriceInt[0] = tempOld 

        tempNew = NewPriceInt[i]
        NewPriceInt[i] = NewPriceInt[0]
        NewPriceInt[0] = tempNew 

        tempQ = Quantity[i]
        Quantity[i] = Quantity[0]
        Quantity[0] = tempQ 

        tempS = Stars[i]
        Stars[i] = Stars[0]
        Stars[0] = tempS 

        tempR = RatingInt[i]
        RatingInt[i] = RatingInt[0]
        RatingInt[0] = tempR 

        tempDis = Discount[i]
        Discount[i] = Discount[0]
        Discount[0] = tempDis 

        tempDescript = Description[i]
        Description[i] = Description[0]
        Description[0] = tempDescript 
        maxHeapifyDescriptionDescending(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description, i, 0)
    return MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description

def heapSortDescending(array):
    n = len(array)
    buildMaxHeap(array)
    for i in range(n - 1, 0, -1):
        (array[i], array[0]) = (array[0], array[i])  
        maxHeapify(array, i, 0)
    array.reverse()
    return array