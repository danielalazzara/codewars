def find_it(seq):
    return [n for n in seq if not seq.count(n) % 2 == 0][0]
    
