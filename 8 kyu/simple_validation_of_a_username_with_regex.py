import re
def validate_usr(username):
    user = re.match(r"^[a-z0-9_]{4,16}$", username)
    return bool(user)
  
