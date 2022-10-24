def shellSort(Arr):
    n = len(Arr)
    # Rearrange elements at each n/2, n/4, n/8, ... intervals
    interval = n // 2
    while interval > 0:
        for i in range(interval,n,1):
            temp = Arr[i]
            j = i
            while j >= interval and Arr[j - interval] > temp:
                Arr[j] = Arr[j - interval]
                j = j - interval
            Arr[j] = temp
        interval = interval // 2
    return Arr


def shellSortDescending(Arr):
    n = len(Arr)
    # Rearrange elements at each n/2, n/4, n/8, ... intervals
    interval = n // 2
    while interval > 0:
        for i in range(interval,n,1):
            temp = Arr[i]
            j = i
            while j >= interval and Arr[j - interval] > temp:
                Arr[j] = Arr[j - interval]
                j = j - interval
            Arr[j] = temp
        interval = interval // 2
    Arr.reverse()
    return Arr