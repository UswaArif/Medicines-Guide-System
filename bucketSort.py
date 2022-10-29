def insertion_sort(Arr):
    for i in range(1,len(Arr),1):
        key = Arr[i]
        j = i - 1
        while (j >= 0 and key < Arr[j]):
            Arr[j + 1] = Arr[j]
            j = j - 1
            
        Arr[j + 1] = key
 
#Bucket Sort Ascending Function
def bucketSort(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description):
    largest = max(OldpriceInt)
    length = len(OldpriceInt)
    size = largest/length
 
    # Create Empty Buckets array
    buckets = [[] for i in range(length)]
    bucketsOld = [[] for i in range(length)]
    bucketsNew = [[] for i in range(length)]
    bucketsQ = [[] for i in range(length)]
    bucketsS = [[] for i in range(length)]
    bucketsR = [[] for i in range(length)]
    bucketsDis = [[] for i in range(length)]
    bucketsDescript = [[] for i in range(length)]
 
    # Bucket Sorting   
    for i in range(length):
        index = int(OldpriceInt[i]/size)
        if index != length:
            buckets[index].append(MedicineName[i])
            bucketsOld[index].append(OldpriceInt[i])
            bucketsNew[index].append(NewPriceInt[i])
            bucketsQ[index].append(Quantity[i])
            bucketsS[index].append(Stars[i])
            bucketsR[index].append(RatingInt[i])
            bucketsDis[index].append(Discount[i])
            bucketsDescript[index].append(Description[i])

        else:
            buckets[length - 1].append(MedicineName[i])
            bucketsOld[length - 1].append(OldpriceInt[i])
            bucketsNew[length - 1].append(NewPriceInt[i])
            bucketsQ[length - 1].append(Quantity[i])
            bucketsS[length - 1].append(Stars[i])
            bucketsR[length - 1].append(RatingInt[i])
            bucketsDis[length - 1].append(Discount[i])
            bucketsDescript[length - 1].append(Description[i])
  
    #Sorting Array with insertion sort
    for i in range(len(OldpriceInt)):
        insertion_sort(bucketsOld[i])
 
 
    # Concatenating the bucket Array
    result = []
    for i in range(length):
        result = result + buckets[i]
             
    return result


def bucketSortDescending(Array):
    largest = max(Array)
    length = len(Array)
    size = largest/length
 
    # Create Empty Buckets array
    buckets = [[] for i in range(length)]
 
    # Bucket Sorting   
    for i in range(length):
        index = int(Array[i]/size)
        if index != length:
            buckets[index].append(Array[i])
        else:
            buckets[length - 1].append(Array[i])
  
    #Sorting Array with insertion sort
    for i in range(len(Array)):
        insertion_sort(buckets[i])
 
 
    # Concatenating the bucket Array
    result = []
    for i in range(length):
        result = result + buckets[i]
    result.reverse()         
    return result