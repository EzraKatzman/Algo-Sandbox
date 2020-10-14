from random import shuffle
from collections import Counter
import pprint

def bogosortstat(arr):
    ctr = Counter()
    while arr != sorted(arr):
        shuffle(arr)
        ctr[str(arr)] += 1
    return ctr,"Shuffled array: " + str(arr), "Total shuffles: " + str(len(ctr)) + " for an array of size " + str(len(arr))

pprint.pprint(bogosortstat([4,3,1,6,5,8]))