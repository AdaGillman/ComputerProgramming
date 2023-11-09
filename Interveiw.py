name = input("Welcome to this interveiw. What is your name? ")

question1 = input(f"Nice to meet you {name}. What position are you interested in? The current positions avaliable are junior developer and analyst. ")

if question1 in "junior developer" or question1 in "analyst":
   print("Very interesting.")
else:
    print("We are not currently offering that position here")
    question = input("Are you looking to become one of our junior developers or an analyst? ")
    if question in "analyst" or question in "junior developer":
        print("Good to know...")
    else:
        print("That is not a job we are offering. This interveiw is over thank you for coming.")
        exit()

question2 = input("What languages do you know? We typically use python here aswell as a few others. ")
print("Those languages are pretty useful thank you for answering.")

question3 = int(input("How many years of experience do you have with programming? (Please answer in a number) "))

if question3 < 3:
    print("I'm sorry but in order to get this job you need atleast 3 years of experience. This interveiw is over thank you for coming.")
    exit()

question4 =  input("Do you have experience working in a team of developers or as an independent worker? ")

question5 = input("Would you be comfortable working with our team? ")

question6 = input("Why would we want you to be a part of our company? ")

question7 = (input("How often would you say you go on vacation? "))
print("That sounds reasonable.")

question8 = int(input("What salary do you desire? "))

if question8 <= 20000:
    print("That is way to low and we can't accept you to have a salary of that amount.")

if question8 >= 100000:
    print("That might be a little too big of a salary for starting out but maybe we could work up towards that.")


question9 = int(input("How many days of the week are you able to work? (Please answer in a number) "))

if question9 < 4:
    print("If you want this job you would need to commit more time. Thank you for coming but this job isn't for you. ")
    exit()

question10 = input("Why do you want this job? ")

print(f"Thank you for attending this interveiw {name}. I want to recap what we went over. Does this sound right?")
reveiw = input(f"The position you are interested in, is {question1}, the languages you know are {question2}, you have {question3} years of experience in computer programming, you have worked as a(n) {question4} worker, you want to be a part of our company because {question6}, you go on vacation {question7}, your desired salary is {question8}, you are able to work {question9} days of the week, and lastly you want this job because {question10}. ")

print("Thank you for coming to this interveiw, have a nice day.")