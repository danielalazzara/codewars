import re
def printer_error(s):
    matches = re.findall(r"[a-m]", s)
    return str(len(s) - len(matches)) + "/" + str(len(s))
  
