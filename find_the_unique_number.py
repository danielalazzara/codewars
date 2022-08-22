from collections import Counter

def find_uniq(arr):
    counter = Counter(arr)
    for value, count in counter.items():
        if count == 1:
            return value
          
