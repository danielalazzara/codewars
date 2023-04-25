def kebabize(st):
    result = ''
    for i in st:
        if i.isalpha():
            if i.isupper():
                result += '-' + i.lower()
            else:
                result += i
    if len(result) > 0:
        return result if result[0] != '-' else result[1:]
    else:
        return ''
      
