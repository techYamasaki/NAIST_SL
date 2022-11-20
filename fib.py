def fib(a, b, limit):
    a = 0
    b = 1
    while b < limit:
        a = b
        b = a+b
    return b