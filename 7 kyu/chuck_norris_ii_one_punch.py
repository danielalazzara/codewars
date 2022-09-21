def one_punch(item): 
    return ' '.join(([i.replace("a","").replace("A","").replace("e","").replace("E","") for i in sorted(item.split(' '))])) if type(item)==str and item != '' else "Broken!"
