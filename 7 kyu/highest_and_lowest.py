def high_and_low(numbers):
    number = [int(n) for n in numbers.split()]
    return " ".join([str(max(number)), str(min(number))])
  
