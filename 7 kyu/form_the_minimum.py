def min_value(digits):
    return int(''.join(list(sorted(set(str(n) for n in digits)))))
  
