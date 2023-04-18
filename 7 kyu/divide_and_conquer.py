def div_con(x):
    sum_int = sum([i for i in x if type(i) == int])
    sum_str = sum([int(i) for i in x if type(i) == str])
    return sum_int - sum_str
  
