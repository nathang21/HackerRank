# https://www.hackerrank.com/challenges/the-minion-game
s = raw_input()

vowels = 'AEIOU'
sScore = 0
kScore = 0

# Sort subStrings between players & add score
for i in range(len(s)):
    if s[i] in vowels:
        kScore += (len(s) - i)
    else:
        sScore += (len(s) - i)

# Determine Winner
if sScore > kScore:
    print "Stuart", sScore
elif sScore < kScore:
    print "Kevin", kScore
else:
    print "Draw"
