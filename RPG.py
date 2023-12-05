inventory = (" ")
HP = 100
Enemy_HP = 100
import random

enemy_list = ["vicious yeti", "yeti", "wild ice goblin", "goblin", "giant frosty spider", "spider"]

enemy = random.choice(enemy_list)

import random

random_chance = ["a", "w", "w"]

chance = random.choice(random_chance)

name = input("Welcome fellow taveler! What is your name? ")
print("Your adventure begins...")
print(f"During your travels, you come across a snowy, ice-cold tundra, with no end in sight. What would you like to do {name}?")
option1 = input("Press 'w' if you would like to walk, press 'p' if you would like to check your inventory. ")

if option1 in "p":
    option1 = input(f"{name}, you have {HP} HP and {inventory} in your inventory. Press 'w' to walk forward. ")

while option1 == "w":
    if chance == "a":
        if enemy == "wild ice goblin":
            option2 = input(f"A wild ice goblin appears!")
            fight_input = input("Would you like to attack or run? ")
            if fight_input == "attack":
                   def attack_enemy(HP, Enemy_HP):
                    while True:
                        if HP > 0:
                            your_attack = random.randint(10,100)
                            print(f"You attacked the enemy for {your_attack} damage!")
                            Enemy_HP -= your_attack
        
                        if Enemy_HP > 0:
                            your_attack = random.randint(10,100)
                            print(f"You attacked the enemy for {your_attack} damage!")
                            Enemy_HP -= your_attack

                        if player_health <= 0:
                            print("You were able to deafeat the enemy!")
                            print("You received an item in your inventory!")
                            break
                            
        if enemy == "vicious yeti":   
