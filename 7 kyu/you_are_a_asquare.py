def is_square(n):  
    if n < 0:
        return False
    if n == 0 or n == 1:
        return True
    if n > 1:
        for i in range(0, n):
            if i * i == n:
                return True
            if i * i > n:
                break
    return False
  
