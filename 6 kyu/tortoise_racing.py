def race(v1, v2, g):
    if v1 >= v2:
        return None
    time_req = (g / (v2 - v1)) * 3600
    hour = int(time_req / 3600)
    min = int((time_req - hour * 3600)/60)
    sec = int((time_req - hour * 3600 - min * 60))
    return [hour, min, sec]
    
