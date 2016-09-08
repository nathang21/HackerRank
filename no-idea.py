# https://www.hackerrank.com/challenges/no-idea
n, m = map(int, raw_input().split())
array = map(int, raw_input().split())
A = set(map(int, raw_input().split()))
B = set(map(int, raw_input().split()))

# Compare and Calculate
happiness = 0
for i in array:
    if i in A:
        happiness += 1
    elif i in B:
        happiness -= 1
    else:
        pass

print happiness
