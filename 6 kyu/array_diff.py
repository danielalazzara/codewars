def array_diff(a, b):
    for i in b:
        for n in range(a.count(i)):
            a.remove(i)
    return a  
  
