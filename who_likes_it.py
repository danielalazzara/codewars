def likes(names):
    if len(names) == 0:
        return 'no one likes this'
    elif len(names) == 1:
        return (str(names[0]) + ' likes this')
    elif len(names) == 2:
        return str(names[0]) + ' and ' + str(names[1]) + ' like this'
    elif len(names) > 2 and len(names) < 4:
        return str(names[0]) + ', ' + str(names[1]) + ' and ' + str(names[2]) + ' like this'
    else:
        return str(names[0]) + ', ' + str(names[1]) + ' and ' + str(len(names)-2) + ' others like this'
      
