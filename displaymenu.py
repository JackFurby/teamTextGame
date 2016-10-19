from gameparser import *

def display_instructions():
	#Print instructions
	print("\nINSTRUCTIONS\n")
	print("The aim of the game is to survive. There's a cannibal on the loose in the asylum and it time for his din dins")
	print("To move, take, drop, search etc. follow the onscreen instructions. And to open the map you type 'open map'.")
    print("Be weary though you can't carry everything!")
	print("\nHOW CAN YOU WIN?\n")
	print("Don't get killed...")
	print("HINT: There is a key where could you use it?")
	print("HINT: There might be more than one way to win but if you can't escape how?")



	


def display_start_menu():
	
	#Loops until user plays the game
	while True:

		print("1. Play\n2. Instructions")

		user_input = input("> ")

		#Checks user input
		if normalise_input(user_input) == ['play']:
			break
		elif normalise_input(user_input) == ['instructions']:
			display_instructions()
		else:
			print("\nPlease choose option 1, or 2\n")


