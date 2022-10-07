def is_lock_ness_monster(string):
    if 'three fifty' in string:
        return True
    elif 'tree fiddy' in string:
        return True
    elif '3.50' in string:
        return True
    else:
        return False
      
