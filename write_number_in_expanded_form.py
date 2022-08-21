def expanded_form(num):
    digits = len(str(num)) - 1
    output = []
    for n in str(num):
        if not n == '0':
            output.append(n + '0' * digits)
        digits -= 1
    return ' + '.join(output)
  
