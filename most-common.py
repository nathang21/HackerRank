# https://www.hackerrank.com/challenges/most-commons
from collections import Counter
from collections import OrderedDict
s = str(raw_input())
c = Counter(s)
c = OrderedDict(sorted(c.items(), key = lambda x: (-x[1], x[0])))
t = 0

for k, v in c.iteritems():
    if t < 3:
        print k, v
        t += 1
