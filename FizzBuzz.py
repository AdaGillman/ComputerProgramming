for i in range(1, 101):
    if i % 15 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")   
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)

num = int(input("Pick a number 1-10 "))
word = input("Now give me a number to print rather than multiples of the number you picked ")

for i in range(1, 101):
    if i % num == 0:
        print(word)
    else:
        print(i)