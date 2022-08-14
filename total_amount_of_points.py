def points(games):
    
    result = 0
    for i in games:
        x, y = i.split(':')
        
        if x > y:
            result = result + 3
        elif x < y:
            result = result + 0
        elif x == y:
            result = result + 1
    
    return result
  
