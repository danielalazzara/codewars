def count_sheep(n):
    total = ""
    for i in range(1, n+1):
        total = total + "{} sheep...".format(i)
    return total
    
