# https://www.hackerrank.com/challenges/merge-the-tools
# Input & Initialization
s = list(raw_input())
k = int(raw_input())
d = len(s) / k

# Put string into list of characters
# Seperate into sub-lists by k
l1 = [s[i:i+k] for i in range(0, len(s), k)]
l2 = []

# Loop full list (0, len)
for ele in l1:
    # Loop sub list (i, i+k)
    for char in ele:
        # Check if repeated letter
        if char not in l2:
            l2.append(char)
    # Output & Cleanup
    print (''.join(l2))
    del l2[:]
