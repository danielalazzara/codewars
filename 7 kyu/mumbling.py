def accum(s):
    final = ""
    for i in range(0, len(s)):
        final += s[i].upper()
        final += s[i].lower() * i
        if i != len(s) - 1:
            final += "-"
    return final
  
