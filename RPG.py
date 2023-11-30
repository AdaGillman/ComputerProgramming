inventory = (" ")

import random

enemy_list = ["A vicious yeti", "A wild ice goblin", "A giant frosty spider"]

enemy = random.choice(enemy_list)

name = input("Welcome fellow taveler! What is your name? ")
print("Your adventure begins...")
print(f"During your travels, you come across a snowy, ice-cold tundra, with no end in sight. What would you like to do {name}?")
option1 = input("Press 'w' if you would like to walk, press 'p' if you would like to check your inventory. ")

if option1 in "p":
    option1 = input(f"{name}, you have 150 HP and {inventory} in your inventory. Press 'w' to walk forward. ")

while option1 == "w":
    option2 = input("{enemy} appears! would you like to attack or run away? ")