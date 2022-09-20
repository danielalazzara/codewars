def digitize(n):
    number = []
    for i in reversed(str(n)):
        number.append(int(i))
    return number
