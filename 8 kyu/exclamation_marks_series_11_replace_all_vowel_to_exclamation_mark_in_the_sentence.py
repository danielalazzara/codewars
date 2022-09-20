def replace_exclamation(s):
    return "".join(["!" if v in "aeiouAEIOU" else v for v in s])
  
