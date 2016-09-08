# https://www.hackerrank.com/challenges/exceptions
t = int(raw_input())
i = 0
while i < t:
    values = raw_input().split()
    try:
        values = map(int, values)
        print values[0] / values[1]
    except ZeroDivisionError as e:
        print "Error Code:",e
    except ValueError as e:
        print "Error Code:",e

    i += 1
