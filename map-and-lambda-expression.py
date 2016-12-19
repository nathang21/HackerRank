# https://www.hackerrank.com/challenges/map-and-lambda-expression
cube = lambda x: x**3

def fibonacci(n):
    fib = []
    for i in range(0, n):
        if i < 2:
            fib.append(i)
        else: 
            next = fib[i - 1] + fib[i - 2]
            fib.append(next) 
    return fib


# Pre-set main
if __name__ == '__main__':
    n = int(raw_input())
    print map(cube, fibonacci(n))
