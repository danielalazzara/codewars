def pillars(num_pill, dist, width):
    dist = dist * 100
    if num_pill > 1:
        return (dist *  (num_pill - 1)) + (width * (num_pill - 2))
    else:
        return 0
      
