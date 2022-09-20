def is_isogram(string):
    string_list = []
    for i in string.upper():
        if i in string_list:
            return False
        string_list.append(i)
    return True
  
