greeting1 = int(input("What is the first number? "))

greeting2 = int(input("What is the second number? "))

greeting3 = input("Would you like to add, subtract, multiply, or divide? ")

if greeting3 in ["add"]:
    print("Your answer is") 
    print(greeting1 + greeting2)

if greeting3 in ["subtract"]:
    print("Your answer is")
    print(greeting1 - greeting2)

if greeting3 in ["multiply"]:
    print("Your answer is")
    print(greeting1 * greeting2)

if greeting3 in ["divide"]:
    print("Your answer is")
    print(greeting1 / greeting2)
    