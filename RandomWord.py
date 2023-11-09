#with open('sowpods.txt', 'r') as f:
  #line = f.readline()
  #while line:
    # do something to the line, for example
    # saving it to disk
import random
wordlist = []
f = open("sowpods.txt", "r")
for i in f:
    wordlist.append(i)
print(random.choice(wordlist)) 