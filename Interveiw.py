name = input("Welcome to this interveiw. What is your name? ")

question1 = input(f"Nice to meet you {name}. What position are you interested in? The current positions avaliable are junior developer and analyst. ")

if question1 in "junior developer" or question1 in "analyst":
   print("Very interesting.")
else:
    print("We are not currently offering that position here")
    question = input("Are you looking to become one of our junior developers or an analyst? ")
    if question in "analyst" or question in "junior developer":
        print("Good to know...")

        

question2 = input("What languages do you know? We typically use python here aswell as a few others. ")

question3 = int(input("How many years of experience do you have with programming? "))

while question3 < 3:
    print("You need atleast 3 years of experience to get this job")
    question3 = int(input("How many years of experience do you have with programming? "))

question4 = input()



# print(f"Thank you for attending this interveiw {name}. I want to recap what we went over. Does this sound correct?")