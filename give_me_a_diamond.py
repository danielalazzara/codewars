def diamond(n):
    if n < 0 or n % 2 == 0:
        return None
    s = ''
    for i in range(n):
        ast = '*' *(i * 2 + 1) if i <= n / 2 else '*' * ((n - i) * 2 - 1)
        s += ' ' * int((n - len(ast)) / 2) + ast + '\n'
    return s
  
