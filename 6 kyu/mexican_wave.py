def wave(people):
    people = people.lower()
    new=[]
    for i, val in enumerate(people):
        if val == ' ':
            continue
        else:
            new.append(people[:i] + people[i].upper() + people[i+1:]) 
    return new
  
