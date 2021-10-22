# Coarse: CS 30
# Period:3
# Date created: 20/09/21
# Date las modified: 22/10/21
# Name: Rabi Jasteen Juancito
# Description: RPG simple menu corrections

import sys

# User’s lists
characters = ["kuro", "adachi"]
actions = ["attack", "explore", "quit"]
directions = ["up", "down", "left", "right"]

# User is ask if they want to play
print("Welcome Traveler! Would you like to play?")

# User will input yes or no
choice = input("yes? or no? ")
if choice == "yes":
        print("Pick a character: ")
        for c in characters:
            print(f"- {c}")
        character_input = input("Character: ")
else:
    print("Maybe next time.")
    sys.exit()


# Direction and action function question
def direction_question():
    """ ask user where they want to go"""
    print("Where do you want to go? ")


def action_question():
    """ ask user what they want to do"""
    print("What do you want to do?")


# Action funtion after user inputs
def action_function():
    """ print the list of actions"""
    for a in actions:
        print(f"- {a}")
    action_input = input("Action: ")

    if action_input == "attack":
        print("K.O. Game Over!")
        sys.exit()

    elif action_input == "explore":
        for d in directions:
            print(f"- {d}")
        direction_input = input("Go: ")

        if direction_input.lower() in directions:
            print(f"Go {direction_input}!")
            print("NICE JOB! You unlocked the other side.")
            sys.exit()

    elif action_input == "quit":
        print("BYE BYE!")
        sys.exit()

    else:
        print("Invalid action!")
        sys.exit()

while True:
    # If user picks kuro
    if character_input == "kuro":
        direction_question()
        for d in directions:
            print(f"- {d}")
        direction_input = input("Go: ")

        if direction_input == "up":
            print("WATCH OUT!! Enemy is coming towards you!")
            action_function()

        elif direction_input == "down":  # Terminate
            print("You just fell in a hole. K.O")
            sys.exit()

        elif direction_input == "left":  # Terminate
            print("YAY! You found a key.")
            sys.exit()

        elif direction_input == "right":  # Terminate
            print("Uh Oh! You've been captured! Better luck time.")
            sys.exit()

        else:
            print("Invalid direction!")
            sys.exit()

    # If user picks adachi or invalid character
    elif character_input == "adachi":
        direction_question()
        for d in directions:
            print(f"- {d}")
        direction_input = input("Go: ")

        if direction_input == "down":
            print("Someone's shooting at you")
            action_function()

        elif direction_input == "up":  # Terminate
            print("Cool! You found the treasure.")
            sys.exit()

        elif direction_input == "right":  # Terminate
            print("YAY!! You just unlocked the other side.")
            sys.exit()

        elif direction_input == "left":  # Terminate
            print("POISON TERRITORY. YOU'RE DEAD.")
            sys.exit()

        else:
            print("Invalid direction!")
            sys.exit()

    # If user picks invalid character
    else:
        print("Invalid character!")
        sys.exit()

