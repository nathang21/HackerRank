# https://www.hackerrank.com/challenges/python-sort-sort
N, M = map(int, raw_input().split())
table = [raw_input() for i in range(N)]
K = int(raw_input())

# Sort and print list by sublist[K]
for row in sorted(table, key=lambda row: int(row.split()[K])):
    print row
