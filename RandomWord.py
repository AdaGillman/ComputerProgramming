import random
wordlist = []
f = open("sowpods.txt", "r")
for i in f:
    wordlist.append(i)
print(random.choice(wordlist)) 