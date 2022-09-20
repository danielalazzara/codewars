import re

def validate_pin(pin):
    if len(pin) == 4 or len(pin) == 6:
        if re.search('[^\d]', pin) == None:
            return True
    
    return False
  
