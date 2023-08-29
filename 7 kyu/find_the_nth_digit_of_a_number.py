def find_digit(num, nth):
    num = abs(num)
    if nth <= 0:
        return -1
    
    return int(str(num)[-nth]) if 0 < nth <= len(str(num)) else 0
  
