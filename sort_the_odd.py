def sort_array(source_array):
    odd = sorted([n for n in source_array if not n % 2 == 0])
    for n, i in enumerate(source_array):
        if i % 2 == 0:
            odd.insert(n, i)
    return odd
  
