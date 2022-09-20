def multi_table(number):
    result = ''
    for n in range(1, 11):
        result += (str(n) + ' * ' + str(number) + ' = ' + str(n * number) + '\n')
    return result.strip()
    
