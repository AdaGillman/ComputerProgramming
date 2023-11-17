import random
wordlist = []
f = open("sowpods.txt", "r")
for i in f:
    wordlist.append(i) 

word = random.choice(wordlist)

letters_guessed = []

print("Welcome to the game Hangman!")

input("Are you ready to start? ")

print("Okay let's start!")

turns = 6

while turns > 0:
    def display_clue(word, letters_guessed):
        clue = ""
        for letter in word:
            if letter.lower() in letters_guessed or letter.upper() in letters_guessed:
                clue += letter + " "
            else:
                clue += "_ "
        return clue

    while True:
        print(display_clue(word, letters_guessed))
        guess = input("Guess a letter: ").upper()
        if guess in letters_guessed:
            print("Guess again, you've already guessed that letter.")
            continue
        letters_guessed.append(guess)
        if all(letter.lower() in letters_guessed or letter.upper() in letters_guessed for letter in word):
            print(f"Good job! You got the word: {word}")
            print("You are so good at this game!")
            break
        if guess not in word:
            turns -= 1
            print(f"You have {turns} guesses left. That was incorrect.")
            if turns == 0:
                print(f"The word was {word}")
                break