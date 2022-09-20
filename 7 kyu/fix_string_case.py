def solve(s):
    low = 0
    for c in list(s):
        if c.lower() == c:
            low += 1
    return s.lower() if low >= len(s)/2 else s.upper()
  
