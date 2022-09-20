def remove_smallest(numbers):
    if len(numbers) < 1:
        return numbers
    else:
        number = numbers.copy()
        number.remove(min(numbers))
        return number
      
