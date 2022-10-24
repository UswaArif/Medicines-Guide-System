def pigeonhole_sort(a):
    my_min = min(a)
    my_max = max(a)
    size = my_max - my_min + 1
  
    holes = [0] * size   #   holes=[0 for x in range(numberOfHoles)]
  
    for x in a:
       # assert type(x) is int, "integers only please"
    
        holes[x - my_min] += 1
  
    i = 0
    for count in range(size):               
        while holes[count] > 0:
            holes[count] -= 1
            a[i] = count + my_min
            i += 1
    return a
              
#  sortedArray=[]
#    for count in range(numberOfHoles):
 #       while holes[count]>0:
  #          holes[count] -=1
   #         sortedArray.append(count+smallestlestInteger)
   
A = [22,1,3,9,6,0,3,5,8]
print(pigeonhole_sort(A))