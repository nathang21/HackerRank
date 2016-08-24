# https://www.hackerrank.com/challenges/the-minion-game
vowels = ['A', 'E', 'I', 'O', 'U']

class Player(object):
    def __init__(self, name):
        self.name = name
        self.score = 0

    def incScore(self):
        self.score += 1

stuart = Player("Stuart")
kevin = Player("Kevin")
word2 = list(raw_input())

# Logic for Stuart
totalCount = 0
# Loop through each character of the string
for i in word2:
    totalCount += 1 # Extend length of substring check

    # Loop through whole sting by index
    for index, j in enumerate(word2):

        # Skip Vowels
        if j in vowels:
            pass
        else:
            count = 0

            # Loop through spartial tring (start through totalCount)
            for k in word2[index:index+totalCount]:
                count += 1

            # Make sure not to double count words
            if count >= totalCount:
                stuart.incScore() # Count substring


# Logic for Kevin
totalCount = 0
# Loop through each character of the string
for i in word2:
    totalCount += 1 # Extend length of substring check

    # Loop through whole sting by index
    for index, j in enumerate(word2):

        # Skip Vowels
        if j not in vowels:
            pass
        else:
            count = 0

            # Loop through spartial tring (start through totalCount)
            for k in word2[index:index+totalCount]:
                count += 1

            # Make sure not to double count words
            if count >= totalCount:
                kevin.incScore() # Count substring


# Determine Winner
if stuart.score > kevin.score:
    print stuart.name, stuart.score
elif stuart.score < kevin.score:
    print kevin.name, kevin.score
else:
    print "Draw"
