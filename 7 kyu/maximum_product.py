def adjacent_element_product(array):
    a = list(map(int, list(array)))
    return max(i * j for i, j in zip(a, a[1:]))
  
