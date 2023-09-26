message1 = int(input("What is your salary? "))
message2 = int(input("What is your year of service? "))

if message2 >= 5:
    print("You have a bonus of")
    print(message1 * 0.05)
else:
    print("You get no bonus")



length = input("What is the lenth? ")
width = input("What is the width? ")

if length == width:
    print("Your shape is a square")
else:
    print("Your shape isn't a square")



num1 = int(input("Give me any number "))
num2 = int(input("Now give me any other number "))

if num1 > num2:
    print(num1)
    print("is the higher number")

if num1 < num2:
    print(num2)
    print("is the higher number")
    
age1 = int(input("Give me the age of someone"))
age2 = int(input("Give me the age of another person"))
age3 = int(input("Now give me the age of one last person"))
