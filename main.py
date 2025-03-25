# PYLIFE 2
pylife_version = "2.0.0-0"
# Text
print("Initializing PyLife...")

print("Step 1: Imports")
import os
import time
import random
import shutil

print("Step 2: Import Basic Variables")
# CONSOLE VARIABLES
terminal_width, terminal_height = shutil.get_terminal_size((50,50))
# PLAYER VARIABLES
death = 0
gender = ""
name = "John Doe"
age = -1
athletics = 0
plays_soccer = True
plays_cricket = False
plays_hockey = False
plays_tennis = False
plays_volleyball = False
plays_tabletennis = False
plays_basketball = False

print(" Step 3: Initialize Data")
# SOCCER
soccer_injury= 0.05
soccer_injury_messages = ["You broke your left arm whilst defending!", "You broke your right arm whilst offending!", "You broke your leg after colliding with a player!"]
soccer_athletics_bonus = 10
soccer_start_messages = "You joined your town soccer team!"

soccer_academy_chance = (athletics-40)/20
soccer_academy_athletics_bonus = 20
soccer_academy_messages = "You joined the Soccer Academy Program!"

# CRICKET
cricket_injury= 0.10
cricket_injury_messages = ["You broke your left arm whilst defending!", "You broke your right arm whilst offending!", "You broke your leg after slipping on the field!"]
cricket_athletics_bonus = 10
cricket_start_messages = "You joined your town cricket team!"

cricket_academy_chance = (athletics-30)/20
cricket_academy_athletics_bonus = 15
cricket_academy_messages = "You joined the Cricket Academy Program!"

# HOCKEY
hockey_injury= 0.10
hockey_injury_messages = ["You broke your left arm whilst defending!", "You broke your right arm whilst offending!", "You broke you leg after slipping on the ice!"]
hockey_athletics_bonus = 10
hockey_start_messages = "You joined your town hockey team!"

hockey_academy_chance = (athletics-50)/20
hockey_academy_athletics_bonus = 30
# SPORT CHANCES

tennis_injury = 0.05
volleyball_injury = 0.07
tabletennis_injury = 0.05


print("Step 3: PyLife Functions")

def clear():
    clears = lambda: os.system('cls')
    clears()


def cycle():
    clear()
    global age
    age += 1
    global athletics

    # Header
    print("PyLife " + pylife_version)
    print("=" * terminal_width)
    print(name + "(" + gender + ")")
    print("Age: " + str(age))
    print("=" * terminal_width)
    print("Age " + str(age))
    if age == 0:
        print(name + " is born!")

    if plays_soccer == True:
        athletics += (soccer_athletics_bonus + random.randint(-5,2))
        if random.random() <= soccer_injury:
            print("INJURY: " + random.choice(soccer_injury_messages))
            print("INJURY: You were not able to play for a season.")

    if plays_cricket == True:
        athletics += (cricket_athletics_bonus + random.randint(-5,2))
        if random.random() <= cricket_injury:
            print("INJURY: " + random.choice(cricket_injury_messages))
            print("INJURY: You were not able to play for a season.")
    play()
def play():
    print("=" * terminal_width)
    print("Stats:")
    print("Athletics: " + str(athletics) + "/" + "200")
    print("-" * terminal_width)
    print("Select an option:")
    print("0: Age 1 Year")
    
    play_selection = input(">>> ")
    if play_selection == "0":
        cycle()


def sports_menu():
    global age
    if age >= 6:
        print("SPORTS")
        print("1. Soccer")
        print("2. Rugby")
cycle()
print(random.random())
print("asdfasdf")
