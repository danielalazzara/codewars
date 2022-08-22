def dig_pow(n, p):
    total = 0
    for num in str(n):
        total += int(num) ** p
        p += 1
    if total % n == 0: 
        return total / n 
    else:
        return -1
      
