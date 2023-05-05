def last(s):
    arr = s.split(" ")
    arr.sort(key= lambda s:s[-1])
    return arr
    
