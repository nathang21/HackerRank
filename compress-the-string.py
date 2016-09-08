# https://www.hackerrank.com/challenges/compress-the-string
from itertools import groupby
S = map(int, raw_input())

for key, group in groupby(S):
    print (len(list(group)), key),
