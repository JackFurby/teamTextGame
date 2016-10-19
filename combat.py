from characters import Player, Cannibal
from random import randint

#Create a dictionary with stats used for the player in the fight
player_fighting = {
	"health": 100,
	"strength": 30,
	"defence": 20,
	"alive": Player["alive"]
}

#Create a dictionary with stats used for the cannibal in the fight
cannibal_fighting = {
	"health": 100,
	"strength": 20,
	"defence": 20,
	"evolved": False,
	"alive": Cannibal["alive"]
}

def player_attack():

	while True:
		print("1. POWER Strike")
		print("2. Precision Strike")

		#Get the players input for either power or precision strike
		type_of_attack = input("> ")

		if type_of_attack == "1":

			#Generate a random number between 0 and the players strength
			dmg_dealt = randint(0, player_fighting["strength"])

			#checks if any damage is dealt
			#If damage is 0 the player missed
			if dmg_dealt == 0:
				return "\nYou missed."

			#If the damage is less than the cannibals defence the attack is blocked
			elif dmg_dealt < cannibal_fighting["defence"]:
				return "\nYour attack was blocked."

			#Otherwise deal the damage and take away the damage dealt calculation from the cannibals health
			else:
				cannibal_fighting["health"] -= dmg_dealt
				return "\nYou deal " + str(dmg_dealt) + " damage to " + Cannibal["name"] + "."

		#if its a precision strike the attack will always hit
		elif type_of_attack == "2":

			#The attack has a much lower maximum damage, calculate this value and take it away from the cannibals health
			dmg_dealt = randint(0, player_fighting["strength"] - 15)
			cannibal_fighting["health"] -= dmg_dealt

			return "\nYou deal " + str(dmg_dealt) + " damage to " + Cannibal["name"] + "."

		#if the player doesn't input 1 or 2 then loop until there is a valid input
		else:
			print("\nPlease choose option 1 or 2")

def cannibal_attack():

	#If the cannibal hasn't evolved yet the give a 1 in 10 chance to evolve
	if cannibal_fighting["evolved"] == False:
		evolve = randint(1, 10)
		if evolve == 1:
			#Set the evolved value to true and double the cannibal's strength
			cannibal_fighting["evolved"] == True
			cannibal_fighting["strength"] = cannibal_fighting["strength"] * 2
			return "\nWhat?\n" + Cannibal["name"] + " is evolving!"

	#Generate a random chance for either a bite or scratch
	type_of_attack = randint(0, 1)

	#If the number generated is 0 then the cannibal bites, this is the equivalent of a power strike.
	if type_of_attack == 0:

		print("\n" + Cannibal["name"] + " uses bite")

		dmg_dealt = randint(0, cannibal_fighting["strength"])

		if dmg_dealt == 0:
			return "\n" + Cannibal["name"] + " missed."

		elif dmg_dealt < cannibal_fighting["defence"]:
			return "\n" + Cannibal["name"] + "'s attack was blocked."

		else:
			player_fighting["health"] -= dmg_dealt
			return "\n" + Cannibal["name"] + " deals " + str(dmg_dealt) + " damage to you."
	
	#If the number generated is 0 then the cannival scratches which is the equivalent of a precision strike.
	elif type_of_attack == 1:

		print("\n" + Cannibal["name"] + " uses scratch")

		dmg_dealt = randint(0, cannibal_fighting["strength"] - 20)
		player_fighting["health"] -= dmg_dealt

		return Cannibal["name"] + " deals " + str(dmg_dealt) + " damage to you."


def fight_main():
	print("It's just you and " + Cannibal["name"] +", you have a knife and he seems unarmed.")
	print("It's time to FIGHT FOR YOUR LIFE!")
	print("Before the battle begins you have to remember, are you RIGHT or LEFT handed?")

	#loop until the user inputs either right or left and change the strength or defence appropriately
	while True:
		user_input = input("> ")
		user_input = user_input.lower()

		if user_input == "right":
			player_fighting["strength"] += 10
			break
		elif user_input == "left":
			player_fighting["defence"] += 10
			break
		else:
			print("Please enter either 'right' or 'left'.")

	print("\n" + Player["name"] + "     VS     " + Cannibal["name"] + "\n")


	#Loop the fight until someone dies
	while cannibal_fighting["alive"] == True and player_fighting["alive"] == True:
		print("\n" + Player["name"] + " HP: " + str(player_fighting["health"]) + "\n")
		print("\n" + Cannibal["name"] + " HP: " + str(cannibal_fighting["health"]) + "\n")

		print(player_attack())

		#Checks if the cannibal survived and if he did then the cannibal attacks
		if cannibal_fighting["health"] > 1:
			print(cannibal_attack())
			if player_fighting["health"] < 1:
				player_fighting["alive"] = False
		else:
			cannibal_fighting["alive"] = False

	if player_fighting["alive"] == True:
		print("\nCongratulations you survived with " + str(player_fighting["health"]) + " HP.\n")
		return True

	else:
		print("\nHAHAHA " + Cannibal["name"] + " killed you and now he's going to eat you.\nHe survived with " + str(cannibal_fighting["health"]) + " HP if you were wondering.\n")
		return False