def data_reverse(data):
    reverse = []
    for i in range(len(data), -1, -8):
        reverse.extend(data[i:i+8])
    return reverse
  
