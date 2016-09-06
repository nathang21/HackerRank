import sys

# Input & Initialization
s = list(raw_input())
k = int(raw_input())
d = len(s) / k
i = 0
buff = []
out = []

# Loop through list of characters
for e in s:
    # Resetfor next sub-string
    if i >= d:
        i = 0
        out.append('\n')
        del buff[:]

    # Add only unique characters
    if e not in buff:
        out.append(e)

    # Keep track of previous characters & count
    buff.append(e)
    i += 1

# Output
out.append('\n')
for item in out:
    sys.stdout.write(item)
