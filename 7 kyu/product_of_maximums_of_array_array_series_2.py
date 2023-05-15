def max_product(lst, n_largest_elements):
    ordered_list = sorted(lst, reverse=True)[:n_largest_elements]
    res = 1
    for i in ordered_list:
        res *= i
    return res
  
