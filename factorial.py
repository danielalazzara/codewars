def factorial(n):
    f = 1
    if n < 0 or n > 12:
        raise ValueError
    for i in range(1, n + 1):
        f*= i
    return f
  
