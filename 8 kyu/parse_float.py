def parse_float(string):
    if type(string) == list:
        return None
    try:
        return float(string)
    except ValueError:
        return None
      
