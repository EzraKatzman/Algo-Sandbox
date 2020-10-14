import random

def bogosort(arr):
    while (is_sorted(arr) == False):
        random.shuffle(arr)
    return(arr)

def is_sorted(arr): 
    n = len(arr) 
    for i in range(0, n-1): 
        if (arr[i] > arr[i+1] ): 
            return False
    return True

print(bogosort([4,3,1,6,5]))