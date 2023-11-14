import random
wordlist = []
f = open("sowpods.txt", "r")
for i in f:
    wordlist.append(i) 

message = len(random.choice(wordlist))
# idk what here but it has the length of the thing rn so yeah
print("Welcome to the game Hangman!")

input("Are you ready to start? ")

print("Okay let's start!")
question1 = input(f"Guess a letter: {}. ")
