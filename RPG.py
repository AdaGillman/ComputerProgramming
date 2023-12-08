inventory = []
HP = 100
Enemy_HP = 100

import random
enemy_list = ["vicious yeti", "wild ice goblin", "giant frosty spider"]
enemy = random.choice(enemy_list)

run = ["1", "2"]
chance = random.choice(run)

walk = ["1", "2", "3"]
walk_chance = random.choice(walk)

item = ["rope", "golden necklace", "picture of a dog"]
name = input("Welcome fellow taveler! What is your name? ")
print("Your adventure begins...")
print(f"During your travels, you come across a snowy, ice-cold tundra, with no end in sight. What would you like to do {name}?")
option1 = input("Press 'w' if you would like to walk, press 'p' if you would like to check your inventory. ")

while option1 in "p":
    option1 = input(f"{name}, you have {HP} HP and {inventory} in your inventory. Press 'w' to walk forward. ")

def attack_enemy(HP, Enemy_HP):
    while True:
        if HP > 0:
            your_attack = random.randint(10,100)
            print(f"You attacked the enemy for {your_attack} damage!")
            Enemy_HP -= your_attack

        if Enemy_HP > 0:
            enemy_attack = random.randint(10,130)
            print(f"The enemy attacked you for {enemy_attack} damage!")
            HP -= enemy_attack

        if Enemy_HP <= 0:
            print("You were able to deafeat the enemy!")
            print("You received an item in your inventory!")
            option1 = input("Press 'w' if you would like to walk, press 'p' if you would like to check your inventory. ")
            inventory = [f"{item}"]
            break

        if HP <= 0:
            print("You lived a great adventurous life, but sadly you died. May you forever be remembered.")
            exit()

def enemy_attacks_you(HP, Enemy_HP):
    while True:
        if Enemy_HP > 0:
            enemy_attack = random.randint(10,100)
            print(f"The enemy attacked you for {enemy_attack} damage!")
            HP -= enemy_attack
        
        if HP > 0:
            your_attack = random.randint(10,100)
            print(f"You attacked the enemy for {your_attack} damage!")
            Enemy_HP -= your_attack

        if Enemy_HP <= 0:
            print("You were able to deafeat the enemy!")
            print("You received an item in your inventory!")
            option1 = input("Press 'w' if you would like to walk, press 'p' if you would like to check your inventory. ")
            break

        if HP <= 0:
            print("You lived a great adventurous life, but sadly you died. May you forever be remembered.")
            exit()

while option1 == "w":
        for enemy in enemy_list:
            walk = ["1", "2", "3"]
            walk_chance = random.choice(walk)
            if walk_chance == "2":
                print(f"A {enemy} appears!")
                fight_input = input("Would you like to attack or run? ")
                if fight_input == "attack":
                    attack_enemy(HP, Enemy_HP)
                if fight_input == "run":
                    if run == "1":
                        print("It looks like you didn't escape.")
                        enemy_attacks_you(HP, Enemy_HP)
                    else:
                            print("You got away!")
                            option1 = input("Press 'w' if you would like to walk, press 'p' if you would like to check your inventory. ")
                            break