def sum_dig_pow(a, b): # range(a, b + 1) will be studied by the function
    total = []
    for i in range(a, b + 1):
        result = 0
        for x, v in enumerate(str(i), 1):
            result += pow(int(v), int(x))
        if i == result:
            total.append(i)
    return total
  
