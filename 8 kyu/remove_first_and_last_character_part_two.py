def array(string):
    string = string.split(",")
    string = string[1:-1]
    if len(string) == 0:
        return None
    return " ".join(string)
  
