def mxdiflg(a1, a2):
    if a1 == [] or a2 == []:
        return -1
    
    x = len(min(a1, key=len))
    y = len(max(a2, key=len))
    res1 = abs(x-y)
    x = len(max(a1, key=len))
    y = len(min(a2, key=len))
    res2 = abs(y-x)
    
    return res1 if res1 >= res2 else res2
  
