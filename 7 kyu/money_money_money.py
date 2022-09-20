def calculate_years(principal, interest, tax, desired):
    result = principal * interest * (1 - tax) + principal
    if principal >= desired:
        return 0
    if result >= desired:
        return 1
    return 1 + calculate_years(result, interest, tax, desired)
  
