#!/usr/bin/python3

from random import randint
from location import rooms
from characters import *
from items import *
from ending import *
from gameparser import *
import shutil
import simpleaudio as sa



def random_generate_items():

    #This function will randomly generate items into rooms.

    #It creates a list of all the rooms other than the room the player is starting in.
    list_of_rooms = []

    for i in rooms:
        if not(rooms[i] == Player["current_room"] or rooms[i]==rooms["Reception"]):
            list_of_rooms.append(rooms[i])

    #This loops through all the items in the game and spawns them in random rooms
    for i in items:
        #A random number is generated in the range of the list, the room with this random number assigned to it is where the item is generated.
        item_location = randint(0, len(list_of_rooms) - 1)

        #Add the phone to the items in the room
        list_of_rooms[item_location]["items"].append(items[i])



def list_of_items(items):
    """This function takes a list of items (see items.py for the definition) and
    returns a comma-separated list of item names (as a string). For example:

    >>> list_of_items([item_phone, item_key])
    'Samsung Galaxy Note 7, The key'

    >>> list_of_items([item_key])
    'The key'

    >>> list_of_items([])
    ''

    >>> list_of_items([item_key, item_phone, item_Knife])
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
    to produce a comma-separated list of item names. For example:

    >>> print_room_items(rooms["Reception"])
    There is a pack of biscuits, a student handbook here.
    <BLANKLINE>

    >>> print_room_items(rooms["Office"])
    There is a pen here.
    <BLANKLINE>

    >>> print_room_items(rooms["Admins"])

    (no output)

    Note: <BLANKLINE> here means that doctest should expect a blank line.

    """
    if room['items'] == []:
        return None
    else:
        print("There is " + list_of_items(room['items']) + " here.")
        print()

def print_inventory_items(items):
    """This function takes a list of inventory items and displays it nicely, in a
    manner similar to print_room_items(). The only difference is in formatting:
    print "You have ..." instead of "There is ... here.". For example:

    >>> print_inventory_items(inventory)
    You have .
    <BLANKLINE>

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

    >>> print_room(rooms["Office"])
    <BLANKLINE>
    THE GENERAL OFFICE
    <BLANKLINE>
    You are standing next to the cashier's till at
    30-36 Newport Road. The cashier looks at you with hope
    in their eyes. If you go west you can return to the
    Queen's Buildings.
    <BLANKLINE>
    There is a pen here.
    <BLANKLINE>

    >>> print_room(rooms["Reception"])
    <BLANKLINE>
    RECEPTION
    <BLANKLINE>
    You are in a maze of twisty little passages, all alike.
    Next to you is the School of Computer Science and
    Informatics reception. The receptionist, Matt Strangis,
    seems to be playing an old school text-based adventure
    game on his computer. There are corridors leading to the
    south and east. The exit is to the west.
    <BLANKLINE>
    There is a pack of biscuits, a student handbook here.
    <BLANKLINE>

    >>> print_room(rooms["Office 1"])
    <BLANKLINE>
    OFFICE 1
    <BLANKLINE>
    Your office is small with a chair by your desk and a bench against the wall.
    There is a door to the east leading to Therapy.
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

    print("What do you want to do?")


def is_valid_exit(curr_room, chosen_exit):
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
    if curr_room["name"] in lockedRooms:
        if lockedRooms[curr_room]["name"]==curr_room["exits"][direction]["name"]:
            print("\nSorry this path is blocked")
            return False
        elif chosen_exit in curr_room["exits"]:
            return True
        else:
            print("\nYou cannot go there")
    elif curr_room["exits"][direction]["name"] in lockedRooms:
        if lockedRooms[curr_room]["exits"][direction]["name"]==curr_room["name"]:
            print("\nSorry this path is blocked")
            return False
        elif chosen_exit in curr_room["exits"]:
            return True
        else:
            print("\nYou cannot go there")
    else:
        return chosen_exit in curr_room["exits"]

#This function needs no input and changes the Cannibal's position to a new random one
def cannibal_move():
    """ The function moves Hannibal to a new room based on his available exits"""
    
    play_curr=Players["Doc"]["current_room"]
    exits=Players["Hannibal the cannibal"]["current_room"]["exits"]
    x=len(exits)-1
    r=randint(0,x)
    k=""
    for k in exits:
        if r==0:
            break
        r=r-1
    x=k
    if is_valid_exit(Players["Hannibal the cannibal"]["current_room"],x):
        Players["Hannibal the cannibal"]["current_room"]= move(Players["Hannibal the cannibal"]["current_room"]["exits"], x)
def execute_go(direction):
    """This function, given the direction (e.g. "south") updates the current room
    to reflect the movement of the player if the direction is a valid exit
    (and prints the name of the room into which the player is
    moving). Otherwise, it prints "You cannot go there."
    """
    if is_valid_exit(Players["Doc"]["current_room"], direction):
        Players["Doc"]["current_room"] = move(Players["Doc"]["current_room"]["exits"], direction)
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
        #print(Players["Doc"]["current_room"]['items'])
        Players["Doc"]["current_room"]['items'] = [d for d in (Players["Doc"]["current_room"]['items']) if d.get('id') != item_id]
        #print(Players["Doc"]["current_room"]['items'])
        print(item_id + " added to your inventory.")
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
    else:
        print("You cannot drop that.")

def execute_open(open_id):
    """This function takes an open_id as an argument and shows a map of the current game.
    """
    
    if open_id == "map":
        #print map based of current room "Doc" is in
        for line in Players["Doc"]["current_room"]["map"]:
            print(line)
    else:
        return
        
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
            cannibal_move()
            sa.stop_all()

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
    
    
    if Hannibal_current_room == Player_current_room: #if Doc and HAnnibal in same room return
        return    
    
    if any(i in han_exit for i in doc_exit) == True: #checks to see if any items in Doc and Hannibal exit lists match
        print("You hear faint footsteps".center(screen_size))
        wave_obj = sa.WaveObject.from_wave_file('audio/footsteps.wav')
        play_obj = wave_obj.play()
    
    elif Player_current_room["name"] in han_exit: #if rooms are next to each other print
        print("!!!WARNING!!!".center(screen_size))
        print("You hear someone breathing nearby...".center(screen_size))
        wave_obj = sa.WaveObject.from_wave_file('audio/breathing.wav')
        play_obj = wave_obj.play()
   
# This is the entry point of our program
def main():

    # Add each item to a random room
    random_generate_items()
    # Works out size of terminal to be used with printing warnings
    screen_size = shutil.get_terminal_size().columns
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
            # Display game status (room description, inventory etc.)
            print_room(Players["Doc"]["current_room"])
            print_inventory_items(Players["Doc"]["inventory"])

            # Show the menu with possible actions and ask the player
            command = menu(Players["Doc"]["current_room"]["exits"], Players["Doc"]["current_room"]["items"], Players["Doc"]["inventory"])
            # Execute the player's command
            if execute_command(command)==False:
                break
            prox_check(Players["Doc"]["current_room"], Players["Hannibal the cannibal"]["current_room"], screen_size)
                
# Are we being run as a script? If so, run main().
# '__main__' is the name of the scope in which top-level code executes.
# See https://docs.python.org/3.4/library/__main__.html for explanation

if __name__ == "__main__":
    main()
