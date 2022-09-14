def nb_dig(n, d):
    values_list = list(range(0, n+1))
    squared_list = list(map(lambda x: str(x**2), values_list))
    str_squared_list = ''.join(squared_list)
    return str_squared_list.count(str(d))
  
