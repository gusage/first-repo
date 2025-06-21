# The Warrior Path Game
# A simple text-based adventure game where the player navigates through rooms, collects items, and faces challenges.

import os

def clear():
    pass
    os.system('cls' if os.name == 'nt' else 'clear')  # Clear the console for better readability
def showInstructions(): # Function to show the game instructions
    print('''
            Welcome to The Warrior Path!
            You can move around the rooms by typing 'go <direction>'.
            Available directions are north, south, east, and west.
            You can also pick up items by typing 'take <item>' and drop them with 'drop <item>'.
            Type 'quit' to exit the game.
            Type 'help' to see these instructions again.
          ''')
inventory = [] # This is the player's inventory where items will be stored
rooms = { # This is the game map with rooms and their connections
        "hall"         : {
            "south": "garden",
            "west" : "bedroom",
            "east" : "dinning room",
            "north": "library",
            },
        "garden"         : {
            "north": "hall",
            "west" : "bathroom",
            "east" : "living room",
            },
        "bedroom"      : {
            "east" : "hall",
            "south": "bathroom",
            "north": "storage",
            "items": "key" # This is a key that can be used to unlock the garden
            },
        "dinning room" : {
            "west" : "hall",
            "south": "living room",
            "north" : "kitchen",
            },
        "library"      : {
            "south": "hall",
            "west" : "storage",
            "east" : "kitchen",
            },
        "bathroom"     : {
            "east" : "garden",
            "north": "bedroom",
            "items": "monster"  # This is a monster that can be defeated with sword and shield
            },
        "living room"  : {
            "west" : "garden",
            "north": "dinning room",
            "items": "sword"  # This is a sword that can be used to defeat the monster
            },
        "storage": {
            "south": "bedroom",
            "east" : "library",
            "items": "shield" # This is a shield that can be used to defeat the monster
            },
        "kitchen"      : {
            "south": "dinning room",
            "west" : "library",
            "items": "monster"  # This is a monster that can be defeated with sword and shield
            }
        }
current_room = "hall" # This is the starting room of the game
showInstructions()

while True:
    def status(): # Function to display the current status of the game
        print("----------------------------------------------")
        print(f"You are in the {current_room}.")
        if "items" in rooms[current_room] and rooms[current_room]["items"]:
            print("You see:", rooms[current_room]["items"])
        if inventory:
            print("Your inventory contains:", ", ".join(inventory))
        else:
            print("Your inventory is empty.")
        print("Available directions:", ", ".join(rooms[current_room].keys()))
    print("----------------------------------------------")
    status()
    move = input(">")
    move = move.split(" ", 1)
    clear()
    if move[0] == "go": # If the player wants to move to another room
        if move[1] in rooms[current_room]:
            current_room = rooms[current_room][move[1]]
        else:
            print("You can't go that way!")
    elif move[0] == "take": # If the player wants to take an item
        if move[1] not in inventory:
            print(f"You have taken the {move[1]}.")
            inventory.append(move[1])
            rooms[current_room]["items"] = "" # Clear the item from the room after taking it 
    elif move[0] == "drop": # If the player wants to drop an item
        if move[1] in inventory:
            inventory.remove(move[1])  # Remove the item from the inventory
            print(f"You have dropped the {move[1]}.")
            if "items" in rooms[current_room]: # If the room already has items, append the dropped item
                rooms[current_room]["items"] += f", {move[1]}"
            else: # If the room does not have items, set it to the dropped item
                rooms[current_room]["items"] = move[1]
        else: # If the item is not in the inventory, inform the player
            print(f"You don't have the {move[1]}.")
    elif move[0] == "help": # If the player wants to see the instructions
        showInstructions() 
    elif move[0] == "quit": # If the player wants to quit the game
        print("Thanks for playing! Goodbye!")
        break
    else:
        print("Invalid command. Type 'help' for instructions.") # Handle invalid commands
# VICTORY CONDITION
    if "key" in inventory and "shield" in inventory and "sword" in inventory and current_room == "garden": # If the player has collected all items and is in the garden
        print("Congratulations! You have collected all the items and completed The Warrior Path!")
        print("You are now ready to face any challenge that comes your way!")
        break
    elif "key" in inventory and current_room == "garden": # If the player has the key but not the sword and shield
        print("You have the key to unlock the garden, but you need a sword and shield to defeat the monster.")
    elif "sword" in inventory and "shield" in inventory and current_room == "garden": # If the player has the sword and shield but not the key
        print("You have the sword and shield, but you need the key to unlock the garden.")
    elif "sword" in inventory and current_room == "garden": # If the player has the sword but not the shield and key
        print("You have the sword, but you need the shield to defeat the monster and the key to open the garden.")
    elif "shield" in inventory and current_room == "garden": # If the player has the shield but not the sword and key
        print("You have the shield, but you need the sword to defeat the monster and the key to open the garden.")
# LOSS CONDITION
    if "items" in rooms[current_room] and rooms[current_room]["items"] == "monster": # If the player encounters a monster in the current room
        print(f"You are in the {current_room}.")
        print("You have encountered a monster! You need a sword and shield to defeat it.")
        if "sword" in inventory and "shield" in inventory: # If the player has both sword and shield
            print("You have defeated the monster with your sword and shield!")
            rooms[current_room]["items"] = ""
            print("You can now continue your journey.")
        else: # If the player does not have both sword and shield
            print("You have been defeated by the monster. Game over.")
            break