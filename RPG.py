import random
HP = 100
Enemy_HP = 100
inventory = []

enemy_list = ["vicious yeti", "wild ice goblin", "giant frosty spider"]
enemy = random.choice(enemy_list)

run = ["1", "2"]
chance = random.choice(run)

walk = ["1", "2", "3"]
walk_chance = random.choice(walk)

item = ["rope", "golden necklace", "picture of a dog"]

def attack_enemy(HP, Enemy_HP):
    if HP > 0:
        your_attack = random.randint(10,100)
        print(f"You attacked the enemy for {your_attack} damage!")
        Enemy_HP -= your_attack
    return Enemy_HP

def enemy_attacks_you(HP, Enemy_HP):
    if Enemy_HP > 0:
        enemy_attack = random.randint(10,100)
        print(f"The enemy attacked you for {enemy_attack} damage!")
        HP -= enemy_attack
    return HP

name = input("Welcome taveler! What is your name? ")
print("Your adventure begins...")
print(f"During your travels, you come across a snowy, ice-cold tundra, with no end in sight. What would you like to do {name}?")

while True:
    option1 = input("Press 'w' if you would like to walk, press 'p' if you would like to check your inventory. ")
    
    if option1 == "p":
        print(f"{name}, you have {HP} HP and {inventory} in your inventory.")

    if option1 == "w":
        walk_chance = random.choice(walk)
        if walk_chance == "2":
            enemy = random.choice(enemy_list)
            print(f"A {enemy} appears!")
            Enemy_HP = 100
            while True:
                fight_input = input("Would you like to attack or run? ")
                if fight_input == "attack":
                    Enemy_HP = attack_enemy(HP, Enemy_HP)
                    if Enemy_HP <= 0:
                        healing = random.randint(5,80)
                        random_item = random.choice(item)
                        print("You were able to deafeat the enemy!")
                        print(f"You received {healing} health and a {random_item} in your inventory!")
                        inventory.append(random_item)
                        HP = min(100, HP + healing) 
                        break

                if fight_input == "run":
                    chance = random.choice(run)
                    if chance == "1":
                        print("It looks like you didn't escape.")

                    else:
                        print("You got away!")
                        break

                HP = enemy_attacks_you(HP, Enemy_HP)
                if HP <= 0:
                    print("You lived a great adventurous life, but sadly you died. May you forever be remembered.")
                    exit()
        else:
            print("You walked forward.")
