def show_sequence(n):
    if n < 0:
        return f"{n}<0"
    elif n == 0:
        return '0=0'
    else:
        sequence = ''
        for i in range(n + 1):
            sequence += str(i) + '+'
        return f"{sequence[:-1]} = {sum(i for i in range(n + 1))}"
        
