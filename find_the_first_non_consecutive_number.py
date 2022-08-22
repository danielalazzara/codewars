def first_non_consecutive(arr):
    prev = arr[0]
    first = None
    for n in arr[1:]:
        if not prev + 1 == n:
            first = n
            break
        prev += 1
    return first
  
