#trapped at the drive thru adventure game
from sys import exit

order_cost = 0
wallet = 10

#pickup window, shames you if you don't take the ketchup
def pickup_window(): 
	print("You pull up to the last window and see a large woman holding a bag which probably contains your food.")
	print("\'Would you like ketchup?\' she asks.")

	ketchup_choice = input("> ")

	if "yes" in ketchup_choice: 
		print("Sure thing.")
		dead("You get 10 packets of ketchup in your bag, and head home to eat. Nice!")
	else: 
		print("You monster! Who doesn't like ketchup?")
		dead("The woman shames you for a bit and you drive home with your food, but a bit embarrassed.")


#I don't know yet how to elegantly combine str and int so here I ask the player to reconfirm for this if/else
def payment_window(): 
	global order_cost 
	print("As you drive up to the second window, you pull out your wallet to pay.")
	print(f"Looks like your order cost {order_cost} dollars.")

	if order_cost > wallet: 
		dead("Turns out you can't actually pay for all that. Lay off the avocado toast!")
	else: 
		print(f"Everything checks out! You hand the cashier {order_cost} dollars and drive to the second window.")
		pickup_window()

#asks the player to pick an item off of the menu, loops back if you want more. You also can't afford cheeseburgers.
def order_window(): 
	print("Despite being a McDonald's, there are only 4 items on the menu. You look at the board and see:")
	print(" Hamburger \n Cheeseburger \n McNuggets \n French Fries")
	print("What do you order?")

	global order_cost 

	order_choice = input("> ")


	if "Hamburger" or "hamburger" in order_choice: 
		order_cost += 4
		print("Will that be all?")
		thats_all = input("> ")
		if "yes" in thats_all: 
			payment_window()
		else: 
			print("What else do you want?")
			order_window()
	elif "Cheeseburger" or "cheeseburger" in order_choice: 
		order_cost += 6
		print("Is that all?") 
		order_window()
	elif "McNuggets" or "mcnuggets" in order_choice: 
		order_cost += 3
		print("Will that be all?")
		thats_all = input("> ")
		if "yes" in thats_all: 
			payment_window()
		else: 
			print("What else do you want?")
			order_window()
	elif "Fries" or "fries" in order_choice: 
		order_cost += 2
		print("Will that be all? ")
		thats_all = input("> ")
		if "yes" in thats_all: 
			payment_window()
		else: 
			print("What else do you want?")
			order_window()
	else: 
		print("You hear a loud horn behind you. Long line of cars stacking up. Better hurry up and decide!")
		order_window()

#exits the program when you reach the end of a story branch and explains why things ended
def dead(why):
	print(why)
	exit(0)
#Starts you off in front of the drive thru, but you won't eat if you can't control the gas
def start(): 
	print("You're in line at the drive thru. How hard do you step on the gas?")

	choice = input("> ")

	if "floor" in choice: 
		dead("Your car explodes all of a sudden and the drive thru goes up in flames.")
	elif "a little" in choice: 
		print("The car in front of you moves forward just enough for you to pull up to the order window.")
		order_window()
	elif "lot" in choice: 
		dead("The car surges forward and smashes into the rear fender of the vehicle ahead. Its driver exits the car and shoots you.")
	else: 
		print("Not sure what that means. Do you step on the gas a lot, a little, or floor it?")
		start()

start()
