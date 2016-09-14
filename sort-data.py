# https://www.hackerrank.com/challenges/python-sort-sort
N, M = map(int, raw_input().split())
table = []
for i in range(N):
    table.append(map(int, raw_input().split()))

K = int(raw_input())

# Sort list by sublist[K]
table.sort(key = lambda x: int(x[K]))

for l in table:
    for n in l:
        print n,
    print
