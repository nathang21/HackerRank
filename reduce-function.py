# https://www.hackerrank.com/challenges/reduce-function
from __future__ import print_function
from fractions import Fraction

def product(fracs):
    t = reduce(lambda num, den: num * den, fracs)
    return t.numerator, t.denominator
    
if __name__ == '__main__':
    fracs = []
    for _ in range(input()):
        fracs.append(Fraction(*map(int, raw_input().split())))
    result = product(fracs)
    print(*result)