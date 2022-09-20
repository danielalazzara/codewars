def distinct(seq):
    duplicate = []
    for n in seq:
        if n not in duplicate:
            duplicate.append(n)
    return duplicate
  
