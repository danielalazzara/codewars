def evaporator(content, evap_per_day, threshold):
    days = 0
    limit = threshold * content / 100
    while content >= limit:
        content -= evap_per_day * content / 100
        days += 1
    return days
  
