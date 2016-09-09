# https://www.hackerrank.com/challenges/iterables-and-iterators
from __future__ import division
from itertools import combinations
from itertools import ifilter

N = int(raw_input())
letters = raw_input().split()
K = int(raw_input())
combs = []
count = 0

# Get all possibile tuples  of size K
combs = list(combinations(letters, K))

# Count tuples comtaining leter 'a'
for item in ifilter(lambda x: 'a' in x, combs):
    count += 1

print round(count / len(combs), 3)
