# https://www.hackerrank.com/challenges/map-and-lambda-expression
cube = lambda x: x**3

def fibonacci(n):
    # return a list of fibonacci numbers
    if n == 0:
        return []
    if n == 1:
        return [0]
    fib = [0, 1]
    last = fib[0]
    now = fib[1]
    for i in range(n - 2):
        fib.append(last + now)
        temp = last + now
        last = now
        now = temp 
    return fib
