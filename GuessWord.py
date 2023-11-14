word = "ceiling"

message = len(word)*"_"

correctletters = ("c" and "e" and "i" and "l" and "n" and "g")

print("Welcome to Guess a Word!")

input("Are you ready to start? ")

print("Okay let's start!")
letter = input(f"Guess a letter: {message}. ")

while len(letter) > 1:
    print("I'm sorry but you can only guess one letter")
    letter = input(f"Guess a letter: {message}. ")

while letter == "a" or "b" or "d" or "f" or "h" or "j" or "k" or "m" or "o" or "p" or "q" or "r" or "s" or "t" or "u" or "v" or "w" or "x" or "y" or "z":
    print("Guess another letter, that ones not in the word.")
    letter = input(f"Guess a letter: {message}. ")

for i in range(len(word)):
    if word[i] in correctletters:
        print(letter, end='')
        print()