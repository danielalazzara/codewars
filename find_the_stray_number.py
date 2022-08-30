from collections import Counter


def stray(arr):
    counter = Counter(arr)
    for value, count in counter.items():
        if count == 1:
            return value
          
