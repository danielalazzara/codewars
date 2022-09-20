def persistence(n):
    counter = 0
    while n >= 10:
        counter += 1
        str_num = str(n)
        total = 1
        for i in str_num:
            total = total * int(i)
        n = total
    return counter
  
