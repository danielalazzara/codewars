def is_palindrome(s):
    s = list(s.lower())
    s_reverse = s[::-1]
    if s == s_reverse:
        return True
    return False
  
