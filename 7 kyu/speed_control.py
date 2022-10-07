def gps(s, x):
    if len(x) <= 1:
        return 0
    average_speed = max(x[i] - x[i-1] for i in range(1, len(x))) 
    return average_speed * 3600.0 / s
  
