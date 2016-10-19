#!/usr/bin/python3

from random import randint
from location import rooms
from location import lockedRooms
from displaymenu import *
from characters import *
from items import *
from ending import *
from gameparser import *
import shutil
import simpleaudio as sa
from combat import *

def use_spray(Player_current_room, Hannibal_current_room):
    
    if item_pepperspray in Players["Doc"]["inventory"]:
        response = input("To repel inmate with pepper spray enter yes: ").lower()
        if response == "yes":
            Players["Hannibal the cannibal"]["current_room"] = cannibal_move()
            print("Hannibal has ran, but he hasn't ran far!!")
            items_list["pepperSpray"]["use"] = items_list["pepperSpray"]["use"] + 1
            if items_list["pepperSpray"]["use"] == 3:
                Players["Doc"]["inventory"].remove(item_pepperspray)
            return True
        else:
            return False
    else:
        return False

def random_generate_items():

    #This function will randomly generate items into rooms.

    #It creates a list of all the rooms other than the room the player is starting in.
    list_of_rooms = []

    for i in rooms:
        if not(rooms[i] == Player["current_room"] or rooms[i]==rooms["Reception"]):
            list_of_rooms.append(rooms[i])

    #This loops through all the items in the game and spawns them in random rooms
    for i in items_list:
        #A random number is generated in the range of the list, the room with this random number assigned to it is where the item is generated.
        if items_list[i]["name"]!="Knife":
            item_location = randint(0, len(list_of_rooms) - 1)

            #Add the phone to the items in the room
            list_of_rooms[item_location]["items_hidden"].append(items_list[i])

def list_of_items(items):
    """This function takes a list of items (see items.py for the definition) and
    returns a comma-separated list of item names (as a string). For example:

    >>> list_of_items([item_phone, item_key])
    'Samsung Galaxy Note 7, The key'

    >>> list_of_items([item_key])
    'The key'

    >>> list_of_items([])
    ''

    >>> list_of_items([item_key, item_phone, item_knife])
    'The key, Samsung Galaxy Note 7, Knife'

    """
    itemList = []
    for item_list in items:
        itemList.append(item_list['name'])
    return(', '.join(itemList))
    

def print_room_items(room):
    """This function takes a room as an input and nicely displays a list of items
    found in this room (followed by a blank line). If there are no items in
    the room, nothing is printed. See map.py for the definition of a room, and
    items.py for the definition of an item. This function uses list_of_items()
    to produce a comma-separated list of item names."""
    if room['items'] == []:
        return None
    else:
        print("There is " + list_of_items(room['items']) + " here.")
        print()

def print_inventory_items(items):
    """This function takes a list of inventory items and displays it nicely, in a
    manner similar to print_room_items(). The only difference is in formatting:
    print "You have ..." instead of "There is ... here.". For example:

    >>> print_inventory_items(Players["Doc"]["inventory"])

    """
    if items:
        print("You have " + list_of_items(items) + ".\n")

def print_room(room):
    """This function takes a room as an input and nicely displays its name
    and description. The room argument is a dictionary with entries "name",
    "description" etc. (see map.py for the definition). The name of the room
    is printed in all capitals and framed by blank lines. Then follows the
    description of the room and a blank line again. If there are any items
    in the room, the list of items is printed next followed by a blank line
    (use print_room_items() for this). For example:

    >>> print_room(rooms["Room 666"])
    <BLANKLINE>
    ROOM 666
    <BLANKLINE>
    add me
    <BLANKLINE>

    >>> print_room(rooms["Reception"])
    <BLANKLINE>
    RECEPTION
    <BLANKLINE>
    The reception is more like an extension of the hall. There are two
    chairs behind the desk and files litter both the floor and workspace.
    You would offer to help clean but there is no one around.
    <BLANKLINE>

    >>> print_room(rooms["Office 1"])
    <BLANKLINE>
    OFFICE 1
    <BLANKLINE>
    Your office is small with a chair by your desk and a bench against the wall.
    There is a door to the east leading to Room 483.
    <BLANKLINE>

    Note: <BLANKLINE> here means that doctest should expect a blank line.
    """
    # Display room name
    print()
    print(room["name"].upper())
    print()
    # Display room description
    print(room["description"])
    print()
    print_room_items(room)

def print_menu(exits, room_items, inv_items):
    """This function displays the menu of available actions to the player. The
    argument exits is a dictionary of exits as exemplified in map.py. The
    arguments room_items and inv_items are the items lying around in the room
    and carried by the player respectively. The menu should, for each exit,
    call the function print_exit() to print the information about each exit in
    the appropriate format. The room into which an exit leads is obtained
    using the function exit_leads_to(). Then, it should print a list of commands
    related to items: for each item in the room print

    "TAKE <ITEM ID> to take <item name>."

    and for each item in the inventory print

    "DROP <ITEM ID> to drop <item name>."

    For example, the menu of actions available at the Reception may look like this:

    You can:
    GO EAST to your personal tutor's office.
    GO WEST to the parking lot.
    GO SOUTH to MJ and Simon's room.
    TAKE BISCUITS to take a pack of biscuits.
    TAKE HANDBOOK to take a student handbook.
    DROP ID to drop your id card.
    DROP LAPTOP to drop your laptop.
    DROP MONEY to drop your money.
    What do you want to do?

    """
    print("You can:")
    # Iterate over available exits
    for direction in exits:
        # Print the exit name and where it leads to
        print_exit(direction, exit_leads_to(exits, direction))
    for items in room_items:
        print("TAKE", items['id'].upper(), "to take", items['name'] + ".")
    for items in inv_items:
        print("DROP", items['id'].upper(), "to drop your", items['id'] + ".")
    print("OPEN MAP to display map.")
    if "file" in Players["Doc"]["current_room"]:
        print("OPEN FILE to open file.")
    if Players["Doc"]["current_room"]["searched"] == False:
        print("SEARCH ROOM to search room.")
    if Players["Doc"]["current_room"]["name"] == "Office 2":
        if rooms["Office 2"]["phone"] == True:
            print("USE PHONE to call for help.")
    print("What do you want to do?")

def exit_leads_to(exits, direction):
    """This function takes a dictionary of exits and a direction (a particular
    exit taken from this dictionary). It returns the name of the room into which
    this exit leads. For example:

    >>> exit_leads_to(rooms["Office 1"]["exits"], "east")
    "Room 483"
    >>> exit_leads_to(rooms["Reception"]["exits"], "south")
    "Room 123"
    >>> exit_leads_to(rooms["Emergency room"]["exits"], "south")
    'Office 2'
    """
    return rooms[exits[direction]]["name"]

def print_exit(direction, leads_to):
    """This function prints a line of a menu of exits. It takes a direction (the
    name of an exit) and the name of the room into which it leads (leads_to),
    and should print a menu line in the following format:

    GO <EXIT NAME UPPERCASE> to <where it leads>.

    For example:
    >>> print_exit("east", "Room 483")
    GO EAST to Room 483.
    >>> print_exit("north", "Room 234")
    GO NORTH to Room 234.
    """
    print("GO " + direction.upper() + " to " + leads_to + ".")

def is_valid_exit(curr_room, chosen_exit,player):
    """This function checks, given a dictionary "exits" and
    a players's choice "chosen_exit" whether the player has chosen a valid exit.
    It returns True if the exit is valid, and False otherwise. Assume that
    the name of the exit has been normalised by the function normalise_input().
    For example:

    >>> is_valid_exit(rooms["Office 1"]["exits"], "east")
    True
    >>> is_valid_exit(rooms["Office 1"]["exits"], "up")
    False
    >>> is_valid_exit(rooms["Room 666"]["exits"], "west")
    False
    >>> is_valid_exit(rooms["Room 123"]["exits"], "north")
    True
    """   
    
    if chosen_exit in curr_room["exits"]:
    #Create a list of the exits in the format that they appear in lockedRooms
        goingrooms=[]
        for ex in curr_room["exits"]:
            goingrooms.append(str(curr_room["exits"][ex]+ex))
        #Create a string with the room the user wants to go to in the format that
        #appears in lockedRooms
        inrooms=str(curr_room["exits"][chosen_exit]+chosen_exit)
        #If the character moving is doc
        if player=="Doc":
            #Check if the player has the key
            if "key" in Players["Doc"]["inventory"]:
                print("The door between Reception and Room 123 is locked")
                lockedRooms.pop("Receptionsouth", None)
                print("The door between Reception and Room 251 is locked")
                lockedRooms.pop("Receptioneast", None)
                #Check if the switch is on or off
                if rooms["Emergency room"]["switch"]:
                    print("The door between Room 251 and Room 347 is locked")
                    lockedRooms["Room 251south"]="Room 347north"
                else:
                    print("The door between Room 251 and Room 347 is unlocked")
                    lockedRooms.pop("Room 251south", None)
            #Check if the switch is on or off
            elif rooms["Emergency room"]["switch"]:
                print("The door between Room 251 and Room 347 is locked")
                lockedRooms["Room 251south"]="Room 347north"
                print("The door between Reception and Room 123 is unlocked")
                lockedRooms.pop("Receptionsouth", None)
                print("The door between Reception and Room 251 is locked")
                lockedRooms["Receptioneast"]="Room 251west"
            #If the player has no key and the switch is of:
            else:
                print("The door between Room 251 and Room 347 is unlocked")
                lockedRooms.pop("Room 251south", None)
                print("The door between Reception and Room 123 is locked")
                lockedRooms["Receptionsouth"]="Room 123north"
                print("The door between Reception and Room 251 is locked")
                lockedRooms["Receptioneast"]="Room 251west"
            #Check if the exit chosen is a possible exit
            if chosen_exit in curr_room["exits"]:
                for name in lockedRooms:
                    #Check if the room the user is going to is locked
                    if name in goingrooms:
                        #Check if the door joining both rooms is locked
                        if inrooms in lockedRooms:
                            print("\nSorry this path is blocked")
                            return False
                        else:
                            return True
                    #Check if the room the user is in is locked
                    elif name == inrooms:
                        #Check if the door joining both rooms is locked
                        if lockedRooms[name] in goingrooms:
                            print("\nSorry this path is blocked")
                            return False
                        else:
                            return True
                #If the room the user is in or going to isn't locked:
                else:
                    return True
            #If the user input an exit that doesn't exist:
            else:
                print("\nYou cannot go there")
                return False
        #If the character moving is the cannibal:
        else:
            #If switch is on:
            if rooms["Emergency room"]["switch"]:
                lockedRooms["Room 251south"] = "Room 347north"
                lockedRooms.pop("Receptionsouth", None)
                lockedRooms["Receptioneast"] = "Room 251west"
            #If switch is off
            else:
                lockedRooms.pop("Room 251south", None)
                lockedRooms["Receptionsouth"] = "Room 123north"
                lockedRooms["Receptioneast"] = "Room 251west"
            #If the exit is a valid exit:
            if chosen_exit in curr_room["exits"]:
                for name in lockedRooms:
                    #If the room the character is going to is locked:
                    if name in goingrooms:
                        #If the door between the room he is in and 
                            #where he is going to is locked:
                        if inrooms in lockedRooms:
                            return False
                        else:
                            return True
                    #If the room the character is in is locked:
                    elif name == inrooms:
                        #If the door between the room he is in and 
                            #where he is going to is locked:
                        if lockedRooms[name] in goingrooms:
                            return False
                        else:
                            return True
                else:
                    return True
            else:
                return False
    else:
        return False
    

#This function changes the Cannibal's position to a new random one
def cannibal_move():
    """ The function moves Hannibal to a new room based on his available exits"""
    
    play_curr=Players["Doc"]["current_room"]
    exits=Players["Hannibal the cannibal"]["current_room"]["exits"]
    x=len(exits) - 1
    r=randint(0, x)
    k=""
    for k in exits:
        if r == 0:
            break
        r=r-1
    x = k
    if is_valid_exit(Players["Hannibal the cannibal"]["current_room"], x, "Hannibal"):
        Players["Hannibal the cannibal"]["current_room"]= move(Players["Hannibal the cannibal"]["current_room"]["exits"], x)

def move(exits, direction):
    """This function returns the room into which the player will move if, from a
    dictionary "exits" of avaiable exits, they choose to move towards the exit
    with the name given by "direction". For example:

    >>> move(rooms["Office 2"]["exits"], "south") == rooms["Canteen"]
    True
    >>> move(rooms["Office 1"]["exits"], "east") == rooms["Room 483"]
    True
    >>> move(rooms["Reception"]["exits"], "west") == rooms["Room 123"]
    False
    """
    
    # Next room to go to
    return rooms[exits[direction]]
    
def prox_check(Player_current_room, Hannibal_current_room, screen_size):
    """This for loop checks if the cannibal is in a room near the player and alerts him"""    
    
    han_exit_dir = [] #list for Hannibal current_room exitis
    han_exit = [] #list for Hannibal current_room exits names
    doc_exit_dir = [] #list for Doc current_room exitis
    doc_exit = [] #list for Doc current_room exits names
    for k in Hannibal_current_room["exits"]:
        han_exit_dir.append(k) #add a direction to list
        #print(han_exit_dir)
        for l in han_exit_dir:
            han_exit.append(Hannibal_current_room["exits"][l]) #adds room name to list based on direction
            han_exit = list(set(han_exit)) #remove duplicates in list
            #print(han_exit, "han")

    for k in Player_current_room["exits"]:
        doc_exit_dir.append(k) #add a direction to list
        #print(doc_exit_dir)
        for l in doc_exit_dir:
            doc_exit.append(Player_current_room["exits"][l]) #adds room name to list based on direction
            doc_exit = list(set(doc_exit)) #remove duplicates in list
            #print(doc_exit,"doc")
    
    
    if Hannibal_current_room == Player_current_room: #if Doc and Hannibal in same room return
        print("""Oh no, you see a humanoid shape covered in blood... something 
            tells you that it isn't his. It is getting closer and you suddenly 
            realise, it's Hannibal the Cannibal!!!""")
        use_spray(Player_current_room, Hannibal_current_room)	
        if use_spray == True:
            return
        else:
            if item_knife in Player["inventory"] :
                fight_main()
            return

    
    if any(i in han_exit for i in doc_exit) == True: #checks to see if any items in Doc and Hannibal exit lists match
        print("\n", "You hear faint footsteps".center(screen_size))
        wave_obj = sa.WaveObject.from_wave_file('audio/footsteps.wav')
        play_obj = wave_obj.play()
    
    elif Player_current_room["name"] in han_exit: #if rooms are next to each other print
        print("\n", "!!!WARNING!!!".center(screen_size))
        print("You hear someone breathing nearby...".center(screen_size))
        wave_obj = sa.WaveObject.from_wave_file('audio/breathing.wav')
        play_obj = wave_obj.play()

def execute_go(direction):
    """This function, given the direction (e.g. "south") updates the current room
    to reflect the movement of the player if the direction is a valid exit
    (and prints the name of the room into which the player is
    moving). Otherwise, it prints "You cannot go there."
    """
    if is_valid_exit(Players["Doc"]["current_room"], direction,"Doc") == True:
        Players["Doc"]["current_room"] = move(Players["Doc"]["current_room"]["exits"], direction)
        print("\nYou are now in", Players["Doc"]["current_room"]["name"] + ".")
        return True
    else:
        print("You cannot go there.")
        return False

def execute_take(item_id):
    """This function takes an item_id as an argument and moves this item from the
    list of items in the current room to the player's inventory. However, if
    there is no such item in the room, this function prints
    "You cannot take that."
    """

    takeItem = []
    for item in Players["Doc"]["current_room"]['items']:
        takeItem.append(item['id'])
    if item_id in takeItem:
        Players["Doc"]["inventory"] = Players["Doc"]["inventory"] + ([d for d in (Players["Doc"]["current_room"]['items']) if d.get('id') == item_id])
        
        Players["Doc"]["invent_weight"] = 0
        for i in Players["Doc"]["inventory"]:
            Players["Doc"]["invent_weight"] = Players["Doc"]["invent_weight"] + i["weight"] # works out weight in Doc inventory
            #print(i["weight"])
        if Players["Doc"]["invent_weight"] > 2: #max weight Doc can carry
            Players["Doc"]["inventory"] = [d for d in Players["Doc"]["inventory"] if d.get('id') != item_id] # if ivent_weight is to much
            print("Your carrying to much weight. drop something first.")
        else:
            #print(Players["Doc"]["current_room"]['items'])
            Players["Doc"]["current_room"]['items'] = [d for d in (Players["Doc"]["current_room"]['items']) if d.get('id') != item_id] #remove item picked up from room
            #print(Players["Doc"]["current_room"]['items'])
            print(item_id + " added to your inventory.")
        #print(Players["Doc"]["invent_weight"])
        #print(i["weight"]) 
    else:
        print("You cannot take that.")

def execute_drop(item_id):
    """This function takes an item_id as an argument and moves this item from the
    player's inventory to list of items in the current room. However, if there is
    no such item in the inventory, this function prints "You cannot drop that."
    """

    dropItem = []
    for item in Players["Doc"]["inventory"]:
        dropItem.append(item['id'])
    if item_id in dropItem:
        #print(Players["Doc"]["current_room"]['items'])
        Players["Doc"]["current_room"]['items'] = Players["Doc"]["current_room"]['items'] + [d for d in Player["inventory"] if d.get('id') == item_id]
        #print(Players["Doc"]["current_room"]['items'])
        #print(inventory)
        Players["Doc"]["inventory"] = [d for d in Players["Doc"]["inventory"] if d.get('id') != item_id]
        #print(inventory)
        print(item_id + " removed from your inventory.")
        
        Players["Doc"]["invent_weight"] = 0
        for i in Players["Doc"]["inventory"]: # works out invent_weight for Doc
            Players["Doc"]["invent_weight"] = Players["Doc"]["invent_weight"] + i["weight"]
        
    else:
        print("You cannot drop that.")

def execute_open(open_id):
    """This function takes an open_id as an argument and shows a map of the current game.
    """
    
    if open_id == "map":
        if rooms["Emergency room"]["switch"]:
            if open_id == "map":
                #print map based of current room "Doc" is in
                for line in Players["Doc"]["current_room"]["map"][1]:
                    print(line)
            else:
                return
        else:
            if open_id == "map":
                #print map based of current room "Doc" is in
                for line in Players["Doc"]["current_room"]["map"][0]:
                    print(line)
            else:
                return
    
    if "file" in Players["Doc"]["current_room"]:
        if open_id == "file":
            print()
            print(Players["Doc"]["current_room"]["file"])
    
def execute_search(search_id):
    """this function allows the user to search the room they are currently in to find
    items in the room and possibly more things to do"""
    
    if search_id == "room":
        Players["Doc"]["current_room"]["items"] = Players["Doc"]["current_room"]["items_hidden"]
    
        if Players["Doc"]["current_room"]["items"] == []:
            print("\n""You found nothing")
        else:
            print("\n""Item(s) found")
        Players["Doc"]["current_room"]["searched"] = True
        return True
    else:
        return False
    
def execute_turn(turn_id):
    if turn_id == "switch":
        rooms["Emergency room"]["switch"]=not rooms["Emergency room"]["switch"]
        print("Something has changed in the map")
        return True
    else:
        print("Sorry you can't turn that")
        return False
    
def execute_use(use_id):
    if use_id == "phone":
        rooms["Office 2"]["phone"] = False
        print("Help is on the way, hold tight until they arrive.")
    else:
        print("Use what?")   
def execute_command(command):
    """This function takes a command (a list of words as returned by
    normalise_input) and, depending on the type of action (the first word of
    the command: "go", "take", or "drop"), executes either execute_go,
    execute_take, execute_drop, or execute_open supplying the second word as the argument.

    """

    if 0 == len(command):
        return

    if command[0] == "go":
        if len(command) > 1:
            execute_go(command[1])
            sa.stop_all()
            prox_check(Players["Doc"]["current_room"], Players["Hannibal the cannibal"]["current_room"], screen_size)
            if execute_go == True:
                cannibal_move()
                sa.stop_all()
                prox_check(Players["Doc"]["current_room"], Players["Hannibal the cannibal"]["current_room"], screen_size)
        else:
            print("Go where?")

    elif command[0] == "take":
        if len(command) > 1:
            execute_take(command[1])
        else:
            print("Take what?")

    elif command[0] == "drop":
        if len(command) > 1:
            execute_drop(command[1])
        else:
            print("Drop what?")

    elif command[0] == "open":
        if len(command) > 1:
            execute_open(command[1])
        else:
            print("Open what?")
            
    elif command[0] == "use":
        if len(command) > 1:
            execute_use(command[1])
        else:
            print("use what?")
            
    elif command[0] == "search":
        if len(command) > 1:
            execute_search(command[1])
            if execute_search == True:
                cannibal_move()
            sa.stop_all()
            prox_check(Players["Doc"]["current_room"], Players["Hannibal the cannibal"]["current_room"], screen_size)
        else:
            print("Cannot search that")
    
    elif command[0] == "turn":
        if len(command) > 1:
            execute_turn(command[1])
            if execute_turn == True:
                cannibal_move()            
            sa.stop_all()
            prox_check(Players["Doc"]["current_room"], Players["Hannibal the cannibal"]["current_room"], screen_size)
        else:
            print("Turn what?")
    #Way to exit the game without having to crash it
    elif command[0] == "exit":
        return False
    
    else:
        print("This makes no sense.")

def menu(exits, room_items, inv_items):
    """This function, given a dictionary of possible exits from a room, and a list
    of items found in the room and carried by the player, prints the menu of
    actions using print_menu() function. It then prompts the player to type an
    action. The players's input is normalised using the normalise_input()
    function before being returned.

    """

    # Display menu
    print_menu(exits, room_items, inv_items)

    # Read player's input
    user_input = input("> ")

    # Normalise the input
    normalised_user_input = normalise_input(user_input)

    return normalised_user_input
   
# This is the entry point of our program
def main():

    # Display the start menu
    display_start_menu()
    # Add each item to a random room
    random_generate_items()
    # Main game loop
    while True:
        if Players["Doc"]["escape"] == True:
            print(endings["escape"])
            break
        
        elif Players["Doc"]["alive"] == False:
            print(endings["die"])
            break
            
        elif Players["Hannibal the cannibal"]["alive"] == False:
            print(endings["live"])
            break
        
        
        
        
            
        
        else:
            if rooms["Office 2"]["phone"] == False:
                global phone_used
                phone_used = phone_used + 1
                if phone_used > 2:
                    Players["Doc"]["escape"] = True
                
            # Display game status (room description, inventory etc.)
            print_room(Players["Doc"]["current_room"])
            print_inventory_items(Players["Doc"]["inventory"])

            # Show the menu with possible actions and ask the player
            command = menu(Players["Doc"]["current_room"]["exits"], Players["Doc"]["current_room"]["items"], Players["Doc"]["inventory"])
            # Execute the player's command
            if execute_command(command)==False:
                break
            
                
# Are we being run as a script? If so, run main().
# '__main__' is the name of the scope in which top-level code executes.
# See https://docs.python.org/3.4/library/__main__.html for explanation

# Works out size of terminal to be used with printing warnings
screen_size = shutil.get_terminal_size().columns

phone_used = 0 #how many goes have passed since phone used

if __name__ == "__main__":
    main()