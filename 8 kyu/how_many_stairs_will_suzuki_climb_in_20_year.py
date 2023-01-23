def stairs_in_20(stairs):
    for stair in stairs:
        return sum(s for stair in stairs for s in stair) * 20
      
