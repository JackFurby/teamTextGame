from characters import Player, Cannibal
from random import randint

player_fighting = {
	"health": 100,
	"strength": 30,
	"defence": 20,
	"alive": True
}

cannibal_fighting = {
	"health": 100,
	"strength": 30,
	"defence": 20,
	"evolved": False,
	"alive": True
}

def player_attack():

	while True:
		print("1. POWER Strike")
		print("2. Precision Strike")

		type_of_attack = input("> ")

		if type_of_attack == "1":

			dmg_dealt = randint(0, player_fighting["strength"])
			print(player_fighting["strength"])
			print(dmg_dealt)
			if dmg_dealt == 0:
				return "\nYou missed."

			elif dmg_dealt < cannibal_fighting["defence"]:
				return "\nYour attack was blocked."

			else:
				cannibal_fighting["health"] -= dmg_dealt
				return "\nYou deal " + str(dmg_dealt) + " damage to " + Cannibal["name"] + "."

		elif type_of_attack == "2":

			dmg_dealt = randint(0, player_fighting["strength"] - 15)
			cannibal_fighting["health"] -= dmg_dealt

			return "\nYou deal " + str(dmg_dealt) + " damage to " + Cannibal["name"] + "."

		else:
			print("\nPlease choose option 1 or 2")

def cannibal_attack():

	if cannibal_fighting["evolved"] == False:
		evolve = randint(1, 10)
		if evolve == 1:
			cannibal_fighting["evolved"] == True
			cannibal_fighting["strength"] = cannibal_fighting["strength"] * 2
			return "\nWhat?\n" + Cannibal["name"] + " is evolving!"

	
	type_of_attack = randint(0, 1)

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
	
	elif type_of_attack == 1:

		print("\n" + Cannibal["name"] + " uses scratch")

		dmg_dealt = randint(0, cannibal_fighting["strength"] - 20)
		player_fighting["health"] -= dmg_dealt

		return Cannibal["name"] + " deals " + str(dmg_dealt) + " damage to you."


def fight_main():
	print("It's just you and " + Cannibal["name"] +", you have a knife and he seems unarmed.")
	print("It's time to FIGHT FOR YOUR LIFE!")
	print("Before the battle begins you have to remember, are you RIGHT or LEFT handed?")

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


	while cannibal_fighting["alive"] == True and player_fighting["alive"] == True:
		print("\n" + Player["name"] + " HP: " + str(player_fighting["health"]) + "\n")
		print("\n" + Cannibal["name"] + " HP: " + str(cannibal_fighting["health"]) + "\n")

		print(player_attack())

		if cannibal_fighting["health"] > 1:
			print(cannibal_attack())
			if player_fighting["health"] < 1:
				player_fighting["alive"] = False
		else:
			cannibal_fighting["alive"] = False

	if player_fighting["alive"] == True:
		print("\nCongratulations you survived with " + str(player_fighting["health"]) + " HP.\n")

	else:
		print("\nHAHAHA " + Cannibal["name"] + " killed you and now he's going to eat you.\nHe survived with " + str(cannibal_fighting["health"]) + " HP if you were wondering.\n")