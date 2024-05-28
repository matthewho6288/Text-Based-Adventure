# -*- coding: utf-8 -*-
"""
Text Adventure Game
An adventure in making adventure games.

To test your current solution, run the `test_my_solution.py` file.

Refer to the instructions on Canvas for more information.

"I have neither given nor received help on this assignment."
author: Matthew Ho
"""
__version__ = 8

# 2) print_introduction: Print a friendly welcome message for your game
#This consumes nothing and returns nothing. It only prints and introduction.
def print_introduction():
    print("In the middle of the night a loud thud awakens you from slumber.")
# 3) get_initial_state: Create the starting player state dictionary
#This consumes nothing and returns the player state and the dictionary: state.
def get_initial_state():
    state = {"game status" : "playing", "location" : "Bedroom", "Has key" : False, "Dropped banana peel" : False}
    return state
# 4) print_current_state: Print some text describing the current game world
#This consumes the state dicitonary and returns nothing. It prints your current state.
def print_current_state(state):
    print("\nYou are are currently at the" , state["location"])
    if state['Has key'] is True:
        print ("You have your car key.")
    if state['Dropped banana peel'] is True:
        print ("The banana peel is on the floor behind you.")
# 5) get_options: Return a list of commands available to the player right now
#This consumes a state(dictionary) and returns a list of strings.
def get_options(state):
    if state["location"] is "Bedroom":
        return ["Lock the bedroom door.","Go to first floor."]
    elif state["location"] == "First floor":
        return ["Go to bedroom", "make sure the doors and windows are locked.", "Go to the front door.", "Go to the kitchen."]
    elif state["location"] ==  "Front door":
        return ["Open door.", "Go to basement.", "Go to first floor"]
    elif state["location"] == "Basement":
        return ["Get baseball bat.", "Go to front door"]
    elif state["location"] == "Kitchen":
        return ["Get knife.", "Get Banana.", "Get car key.", "Go to garage."]
    elif state["location"] == "Garage":
        if state["Has key"] == True:
            if state["Dropped banana peel"] == True:
                return["drive to police station."]
        else:
            return["Go to the kitchen"]
# 6) print_options: Print out the list of commands available
#This consumes a list of options and returns nothing. This prints the options on individual lines.
def print_options(options):
    for option in options:
        print ("*", option)
# 7) get_user_input: Repeatedly prompt the user to choose a valid command
#This consumers a list of options for commands and returns nothing. It only prints
def get_user_input(options):
    inside = False
    while inside is False:
        command = input("Decide What you will do next or 'quit': ")
        if 'quit' in command:
            inside = True
        else:
            for item in options:
                if command in item:
                    inside = True
                elif inside is False:
                    print("The command you have typed is not valid")
    return command
# 8) process_command: Change the player state dictionary based on the command
#This consumes a command and the state(dictionary) and returns nothing. It changes the state(dictionary)
def process_command(command, state):
    if command in "Lock the bedroom door.":
        state["game status"] = "lose"
        print("After locking your bedroom door, you fell asleep and home invader broke in and killed you.")
    elif command in "Go to first floor.":
        state["location"] = "First floor"
    elif command in "make sure the doors and windows are locked.":
        state = state
        print("After checking the doors and windows, someone knocks loudly at the front door.")
    elif command in "Go to the front door.":
        state["location"] = "Front door"
        print("The knocking gets louder and faster.")
    elif command in "Go to the kitchen.":
        state["location"] = "Kitchen"
    elif command in "Go to bedroom.":
        state["location"] = "Bedroom"
    elif command in "Open door.":
        state["game status"] = "lose"
    elif command in "Go to basement.":
        state["location"] = "Basement"
        print("After going to the basement, the knocking still gets louder and the person knock start yelling death threats")
    elif command in "Get baseball bat.":
        state["game status"] = "lose"
        print('''The man breaks in, and it turns out the man outside is 6'10 and very strong.
              Without trying he easily overpowers you and kills you with your own bat''')
    elif command in "Get knife.":
        state["game status"] = "lose"
        print("Unfortunately, the man breaks and into your house and disarms you instantly. He then stabs you.")
    elif command in "Get Banana.":
        state["Dropped banana peel"] = True
        print("In a state of panic you eat a banana and drop peel behind you.")
    elif command in "Get car key.":
        state["Has key"] = True
        print("You are now able to use your car")
    elif command in "Go to garage.":
        state["location"] = "Garage"
    elif command in "drive to police station.":
        state["location"] = "Police Station"
        state["game status"] = "win"
    elif command in "quit":
        state["game status"] = "quit"
    

# 9) print_game_ending: Print a victory, lose, or quit message at the end
#This consumes a dictionary(state) and returns nothing. It prints messages based on the game status.
def print_game_ending(state):
    if state["game status"] is "win":
        print("Congratulations, you survived the home invader and help the cops capture him.")
    if state["game status"] is "lose":
        print("After killing you, the man steals all of your belongings")
        print("and learns about the people close to you so he can rob and kill them next.")
    if state["game status"] is "quit":
        print("You've given up at life and decide to blow up your house killing you and the robber.")
    if state["game status"] is "playing":
        print(None)
        
# Command Paths to give to the unit tester
WIN_PATH = ["Go to first floor.", "make sure the doors and windows are locked.", "Go to the kitchen.",
            "Get car key.", "Get Banana.", "Go to garage.", "drive to police station."]
LOSE_PATH = ["Lock the bedroom door"]
#"drive to police station."
# 1) Main function that runs your game, read it over and understand
# how the player state flows between functions.
def main():
    # Print an introduction to the game
    print_introduction()
    # Make initial state
    the_player = get_initial_state()
    # Check victory or defeat
    while the_player['game status'] == 'playing':
        # Give current state
        print_current_state(the_player)
        # Get options
        available_options = get_options(the_player)
        # Give next options
        print_options(available_options)
        # Get Valid User Input
        chosen_command = get_user_input(available_options)
        # Process Commands and change state
        process_command(chosen_command, the_player)
    # Give user message
    print_game_ending(the_player)

# Executes the main function
if __name__ == "__main__":
    '''
    You might comment out the main function and call each function
    one at a time below to try them out yourself '''
    main()
    ## e.g., comment out main() and uncomment the line(s) below
    # print_introduction()
    # print(get_initial_state())
    # ...