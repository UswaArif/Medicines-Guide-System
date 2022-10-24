def PigeonHoleSort(array):              
    minNum = min(array)
    maxNum = max(array)
    size = maxNum - minNum + 1
    holes = [0 for x in range(size)]
    for x in array:
        holes[x - minNum] += 1
  
    i = 0
    for count in range(size):               
        while holes[count] > 0:
            holes[count] -= 1
            array[i] = count + minNum
            i += 1
    return array


def PigeonHoleSortDescending(array):              
    minNum = min(array)
    maxNum = max(array)
    size = maxNum - minNum + 1
    holes = [0 for x in range(size)]
    for x in array:
        holes[x - minNum] += 1
  
    i = 0
    for count in range(size):               
        while holes[count] > 0:
            holes[count] -= 1
            array[i] = count + minNum
            i += 1
    array.reverse()
    return array