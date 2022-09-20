def string_clean(s):
    """
    Function will return the cleaned string
    """
    return ''.join('' if c.isdigit() else c for c in s)
  
