def zero(x = None): return 0 if x is None else int(x(0))
def one(x = None): return 1 if x is None else int(x(1))
def two(x = None): return 2 if x is None else int(x(2))
def three(x = None): return 3 if x is None else int(x(3))
def four(x = None): return 4 if x is None else int(x(4))
def five(x = None): return 5 if x is None else int(x(5))
def six(x = None): return 6 if x is None else int(x(6))
def seven(x = None): return 7 if x is None else int(x(7))
def eight(x = None): return 8 if x is None else int(x(8))
def nine(x = None): return 9 if x is None else int(x(9))

def plus(y): return lambda x: x + y
def minus(y): return lambda x: x - y
def times(y): return lambda x: x * y
def divided_by(y): return lambda x: x / y
