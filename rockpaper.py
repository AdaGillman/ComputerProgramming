Player1 = input("First player, do you choose rock, paper, or scissors? ")
Player2 = input("Alright seccond player, do you choose rock, paper or scissors? ")

if Player1 == "rock" and Player2 == "paper":
    print("Paper defeats rock")
    print("Player two wins, good job!")

if Player1 == "rock" and Player2 == "scissors":
    print("Rock defeats scissors")
    print("Player one wins, good job!")


if Player1 == "paper" and Player2 == "rock":
    print("Paper defeats rock")
    print("Player one wins, good job!")

if Player1 == "paper" and Player2 == "scissors":
    print("Scissors defeats paper")
    print("Player two wins, good job!")

if Player1 == "scissors" and Player2 == "rock":
    print("Rock defeats scissors")
    print("Player two wins, good job!")

if Player1 == "scissors" and Player2 == "paper":
    print("Scissors defeats paper")
    print("Player one wins, good job!")

if Player1 == Player2:
    print("That's a tie!")

print("Would you like to start a new game? If so, then restart!")