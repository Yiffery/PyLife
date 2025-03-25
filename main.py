# PYLIFE 2
# PYLIFE is best edited in PyCharm
pylife_version = "0.0.1-0"
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
intelligence = 0
happiness = 0
plays_soccer = True
plays_cricket = False
plays_hockey = False
plays_tennis = False
plays_volleyball = False
plays_tabletennis = False
plays_basketball = False
# SPORTS KEY: Soccer, Cricket, Hockey, Tennis, Volleyball, Tabletennis, Basketball
sportss = [1, 0, 0, 0, 0, 0, 0]
sportskey = ["Soccer", "Cricket", "Hockey", "Tennis", "Volleyball", "Table Tennis", "Basketball"]

sports = [
    # SOCCER
    {"name": "Soccer",
     "level": 1,
    "injury": 0.05,
    "injury_messages": ["You broke your left arm whilst defending!", "You broke your right arm whilst offending!", "You broke your leg after colliding with a player!"],
    "athletics_bonus": 10,
    "start_messages": ["You have joined your town soccer team!"],

    "academy_name": "Soccer Academy Program",
    "academy_athletics_bonus": 20,
    "academy_messages": "You joined the Soccer Academy Program"},

    # CRICKET
    {"name": "Cricket",
     "level": 0,
     "injury": 0.10,
     "injury_messages": ["You broke your left arm whilst defending!", "You broke your right arm whilst offending!", "You broke your leg after slipping on the field!"],
     "athletics_bonus": 10,
     "start_messages": ["You have joined your town cricket team!"],

     "academy_name": "Cricket Academy Program",
     "academy_athletics_bonus": 15,
     "academy_messages": "You joined the Cricket Academy Program"},

]
print(" Step 3: Initialize Data")

soccer_academy_chance = (athletics-40)/20

# CRICKET
cricket_academy_chance = (athletics-30)/20

# HOCKEY
hockey_injury= 0.10
hockey_injury_messages = ["You broke your left arm whilst defending!", "You broke your right arm whilst offending!", "You broke you leg after slipping on the ice!"]
hockey_athletics_bonus = 10
hockey_start_messages = "You joined your town hockey team!"

hockey_academy_chance = (athletics-50)/20
hockey_academy_athletics_bonus = 30
hockey_academy_messages = "You joined the Hockey Academy Program!"

tennis_injury= 0.05
tennis_injury_messages = ["You broke your left arm after tripping on a ball!", "You broke your right arm whilst serving!", "You broke you leg after slipping on the court!"]
tennis_athletics_bonus = 10
tennis_start_messages = "You started playing tennis at your local community center!"

tennis_academy_chance = (athletics-50)/20
tennis_academy_athletics_bonus = 30
tennis_academy_messages = "You joined a Tennis Academy Program!"

# VOLLEYBALL
volleyball_injury= 0.07
volleyball_injury_messages = ["You broke your left arm whilst serving!", "You broke your right arm whilst hitting the ball!", "You broke you leg after slipping on the court!"]
volleyball_athletics_bonus = 7
volleyball_start_messages = "You joined your town volleyball team!"

volleyball_academy_chance = (athletics-30)/20
volleyball_academy_athletics_bonus = 30
volleyball_academy_messages = "You joined the Volleyball Academy Program!"
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
    print("=" * terminal_width)
    print("Age " + str(age))
    if age == 0:
        print(name + " is born!")
    # SPORT CYCLE
    for sport in sports:
        if sport['level'] >= 1:
            athletics += (sport['athletics_bonus'] + random.randint(-5,2))
            if random.random() <= sport['injury']:
                print("INJURY: " + random.choice(sport["injury_messages"]))
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

    # PLAN

    # Sports
    # 1. Start new sport
    # 2. Manage current sports

    global age
    global plays_soccer
    global plays_cricket
    global plays_hockey
    print("SPORTS")
    print("1. Start a new sport")
    print("2. Manage current sports")

    sport_selection = input(">>> ")
    if sport_selection == "1":
        if age >= 6:
            # Age 6 Sports
            print("SPORTS")
            print("1. Soccer")
            if age >= 8:
                # Age 8 Sports
                print("2. Cricket")

            print("Select a sport")
            sport_selection = int(input(">>> "))

            # Logic for checking sport
            if sports[sport_selection-1]["level"] == 0:
                print("SPORT: " + random.choice(sports[sport_selection]["start_messages"]))
                sports[sport_selection-1]["level"] = 1

        else:
            print("You must be at least 6 years old to play a sport!")
    elif sport_selection == "2":
        print("MANAGE SPORTS")
        tempbin = []
        # Print out participating sports
        for i in range(len(sports)):
            if sports[i]["level"] >= 1:
                print(str(i+1) + ": " + sports[i]["name"])
                tempbin.append(i)
        sport_selection = int(input(">>> "))
        print(tempbin)
        selectedsport = tempbin[sport_selection-1]
        print(sportskey[selectedsport] + " Options")
        print("1. Quit")

        if sports[selectedsport] == 1:
            # Join academy program
            print("2. Join Advanced Program")

        sport_selection = input(">>> ")
        print(sport_selection)
        match sport_selection:
            case "1":
                sports[selectedsport] = 0
            case "2":

                sports[selectedsport] = 2
                print("You have joined the academy program for this sport")
            case _:
                print("ERROR: Invalid selection")
        time.sleep(5)
        print(sports[0])




cycle()
