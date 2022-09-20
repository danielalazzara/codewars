def odd_or_even(arr):
    if sum(arr) % 2 == 0:
        return 'even'
    if sum(arr) % 2 != 0 or sum(arr) == 0:
        return 'odd'
      
