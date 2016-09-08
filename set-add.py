# https://www.hackerrank.com/challenges/py-set-add
N = int(raw_input())
nation = set()
for i in range(0, N):
    nation.add(raw_input())

print len(nation)
