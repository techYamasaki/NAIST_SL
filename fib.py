def fib(a, b):
    a = 0
    b = 1
    while b < 100:
        a = b
        b = a+b
    return b