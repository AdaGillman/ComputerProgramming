word = "ceiling"

letters_guessed = []

print("Welcome to Hangman!")

input("Are you ready to start? ")

print("Okay let's start!")

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