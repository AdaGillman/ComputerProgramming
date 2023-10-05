message1 = int(input("How many numbers of the fibonacci sequence would you like? "))


n1, n2 = 0, 1
count = 0


if message1 <= 0:
   print("Enter a postitive integer")

elif message1 == 1:
   print("Fibonacci numbers upto",message1,":")
   print(n1)

else:
   print("Fibonacci sequence:")
   while count < message1:
       print(n1)
       nth = n1 + n2
       
       n1 = n2
       n2 = nth
       count += 1

