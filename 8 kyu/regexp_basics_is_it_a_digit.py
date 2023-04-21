import re

def is_digit(n):
    if len(n) > 1:
        return False
    return bool(re.match(r'^\d+$', n))
  
