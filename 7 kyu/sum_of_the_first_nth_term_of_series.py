def series_sum(n):
    fractions = []
    for n in range(1, 3*n - 1, 3):
        fractions.append(1/n)
    return "{:.2f}".format(sum(fractions))
    
