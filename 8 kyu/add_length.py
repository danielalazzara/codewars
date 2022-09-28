def add_length(str_):
    words = []
    for w in str_.split():
        words.append(w + ' ' + str(len(w)))
    return words
  
