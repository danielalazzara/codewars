geese = ["African", "Roman Tufted", "Toulouse", "Pilgrim", "Steinbacher"]
def goose_filter(birds):
    filter = []
    for b in birds:
        if b not in geese:
            filter.append(b)
    return filter
  
