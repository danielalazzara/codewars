def comp(array1, array2):    
    array1.sort()
    array2.sort()
    
    if isinstance(array1, list) and isinstance(array2, list):
        for i in range(len(array1)):
            a1 = array1[i]
            a2 = array2[i]
            if a2 != a1 ** 2:
                return False
    return True
  
