from gameparser import *

def display_instructions():
	#Print instructions
	print("\nINSTRUCTIONS\n")
	print("The aim of the game is to survive.")
	print("You move around by typing go then the direction you want to go, so if you are in office 1 and it says 'GO EAST to Room 483', you type 'go east' then you go to room 483. To take an item you enter 'take [desired item]' and it will take it', same for drop item but type 'drop' instead of 'take'. And to open the map you type 'open map'. This is pretty fucking complicated so if you're still following GOOD JOB.")
	print("\nHOW CAN YOU WIN?\n")
	print("Work it out yourself, it's a pretty simple concept so working out how to win is part of the fun.")
	print("HINT: There is a key and a locked door in the reception.")
	print("HINT: There might be more than one way to win.")



	


def display_start_menu():
	
	#Loops until user plays the game
	while True:

		print("1. Play\n2. Instructions")

		user_input = input("> ")

		#Checks user input
		if normalise_input(user_input) == ['1']:
			break
		elif normalise_input(user_input) == ['2']:
			display_instructions()
		else:
			print("\nPlease choose option 1, or 2\n")


