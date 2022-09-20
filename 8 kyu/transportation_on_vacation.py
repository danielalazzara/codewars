def rental_car_cost(d):
    if d == 1 or d == 2:
        return 40 * d
    elif d >= 3 and d < 7:
        return (d * 40) - 20
    else:
        return (d * 40) - 50
      
