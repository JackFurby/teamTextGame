from gameparser import *
from ending import image_to_ascii

def display_instructions():
	#Print instructions
	print("\nINSTRUCTIONS\n")
	print("The aim of the game is to survive. There's a cannibal on the loose in the asylum and ")
	print("it's time for his din dins. To move, take, drop, search etc. follow the onscreen instructions.")
	print("To open the map you type 'open map'. There's also a hidden turn command that works ")
	print("like the other commands but what could it be for and where could you use it?")
	print("Be weary though you can't carry everything!")
	print("\nHOW CAN YOU WIN?\n")
	print("Don't get killed...")
	print("HINT: There is a phone somewhere you could use to get help? if you survive long enough after..")
	print("HINT: There might be more than one way to win but if you can't escape how?")



	


def display_start_menu():
	
	#Loops until user plays the game
	while True:
		
		print(image_to_ascii("images/theward.jpg", 80, 20))

		print("1. Play\n2. Instructions")

		user_input = input("> ")

		#Checks user input
		if normalise_input(user_input) == ['1']:
			break
		elif normalise_input(user_input) == ['2']:
			display_instructions()
		else:
			print("\nPlease choose option 1, or 2\n")


