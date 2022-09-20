def round_to_next5(n):
    if n % 5 == 4:
        n += 1
    elif n % 5 == 3:
        n += 2
    elif n % 5 == 2:
        n += 3
    elif n % 5 == 1:
        n += 4
    return n
  
