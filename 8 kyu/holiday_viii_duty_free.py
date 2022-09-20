def duty_free(price, discount, holiday_cost):
    duty_free_discount = price * discount / 100
    total_bottles = holiday_cost / duty_free_discount
    return int(total_bottles)
  
