def max_sequence(arr):
    max_sum = 0
    for i in range(len(arr)):
        for j in range(i, len(arr)):
            t_sum = sum(arr[i:j + 1])
            if t_sum > max_sum:
                max_sum = t_sum
    return max_sum
  
