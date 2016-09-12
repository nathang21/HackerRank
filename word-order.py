# https://www.tutorialspoint.com//python/python_continue_statement.htm
from collections import Counter
n = int(raw_input())
words = [raw_input().strip() for i in range(n)]
counts = Counter(words)

print len(counts)
for word in words:
    temp = counts.pop(word, None)
    if temp:
        print temp,
