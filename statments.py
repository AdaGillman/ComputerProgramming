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

if num1 == num2:
    print("The numbers are equal")
    
age1 = int(input("Give me the age of someone "))
age2 = int(input("Give me the age of another person "))
age3 = int(input("Now give me the age of one last person "))

if age1 > age2 and age1 > age3:
    print("The first person is the oldest:")
    print(age1)

if age2 > age1 and age2 > age3:
    print("The second person is the oldest:")
    print(age2)

if age3 > age1 and age3 > age2:
    print("The third person in the oldest:")
    print(age3)

if age1 == age2 and age1 == age3:
    print("All three people are the same age")

if age1 < age2 and age1 < age3:
    print("The first person is the youngest:")
    print(age1)

if age2 < age1 and age2 < age3:
    print("The second person is the youngest:")
    print(age2)

if age3 < age1 and age3 < age2:
    print("The third person is the youngest:")
    print(age3)

class1 = int(input("How many classes were held? "))
class2 = int(input("How many classes did you attend? "))

if class2 > class1:
    print("It doesn't work like that")

class3 = (class2 / class1)
class4 = (class3 * 100)

print("You attended")
print(class4)
print("percent of the classes held")

if class4 > 75 and class4 <= 100:
    print("You are able to particapate in the test")

if class4 < 75:
    print("You cannot particapate in this test")

if class4 > 100:
    print("That doesn't really work")
