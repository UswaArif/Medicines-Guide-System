def Partition(array,left,right):
    i,j=left,right-1 #i moves to the left #j moves to the right 
    pivot=array[right]
    while(i<j):
        while i<right and array[i]<pivot:   #i ne find karna largest ko
            i=i+1
        while j>left and array[j]>= pivot:  #j ne find karna smallest ko
            j=j-1
        if i<j:
            array[i],array[j]=array[j],array[i]
    if(array[i]>pivot):
        array[i],array[right]=array[right],array[i]
    return i

def QuickSort(array,left,right):
    #left=0==start,right=len(array)=end
    if(left<right):
        partition_positon=Partition(array,left,right)
        QuickSort(array,left,partition_positon-1)
        QuickSort(array,partition_positon+1,right)


A = [22,1,3,9,6,0,3,5,8]
print(QuickSort(A, 4,7))