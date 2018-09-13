from sys import exit
import os 
os.system("my_adventure_game_pt2.py")

class Engine(object): 

	def __init__(self, scene_map): 
		self.scene_map = scene_map

	def play(self): 
		current_scene = self.scene_map.opening_scene()
		last_scene = self.scene_map.next_scene('finished')

		while current_scene != last_scene: 
			next_scene_name = current_scene.enter()
			current_scene = self.scene_map.next_scene(next_scene_name)

		current_scene.enter() 


class Map(object): 

	scenes = {


	}

	def __init__(self, start_scene):
		pass

	def next_scene(self, scene_name): 
		pass

	def opening_scene(self): 
		pass 


class Death(Scene): 

	print("You died!")

class 	

class Kitchen(Scene): 

	print(dedent("""It's a pretty small kitchen you've stumbled
	into. Next to a short countertop with a sink and faucet is 
	an old electric range with oven, as well as a small fridge
	with a few notes stuck on. Off to the left is the dining
	table, on top of which sits the remnants of an evening
	meal, and a small black book. Looks like there's also a door 
	that leads downstairs, just to the right."""))

	CodeFound = False

	KitchenSearch = input("> ")
	

	if KitchenSearch == "fridge": 

		print(dedent("""You sift through the notes on the fridge.
			It looks like there isn't anything of significance - 
			grocery lists, passive-aggressive reminders, phone 
			numbers....and a note that simply says 'Coke 2821'."""))
		CodeFound = True 
		return 'HouseKitchen'

	elif KitchenSearch == "book": 

		print(dedent("""You flip open the black book on the table.
			It appears to be a journal of some sort. Written in black
			ink on cream-colored paper, someone has written the words: 

			UNIVERSE PORTAL 

			all journals to activate

			it is """))
		return 'HouseKitchen'

	elif KitchenSearch == "sink":

		print(dedent("""Nothing to see here. Just an old sink."""))

	elif KitchenSearch == "range": 

		print(dedent("""Old stovetop. Used recently and still in 
			good shape."""))

	elif KitchenSearch == "door":

		print(dedent("""Looks like this door leads down into
			the basement. Time to see what's down there!"""))
		return 'HouseBasement'

	else: 

		print(dedent("""Not quite sure what that means."""))


class Basement(Scene): 

	print(dedent("""The basement downstairs is surprisingly bare.
		A ratty green sofa occupies the center of the room facing
		directly opposite a television. Off to the left is a vending
		machine."""))

	BasementSearch = input("> ")

	if BasementSearch == "vending machine": 

		print(dedent("""You decide to check out the vending machine."""))
		return 'SecurityDoor'

	elif BasementSearch == "couch":

		print(dedent("""Nothing to see except an old green couch -
			but wait! Jammed in between the cushions you see another
			black book. Flipping past the first few pages, you find
			more scribbles. Among them is a single word circled in 
			bold red ink: 

			Wednesday"""))
		return 'HouseBasement'

	elif BasementSearch == "television": 

		print(dedent("""You try pressing the power button for the
			television, but nothing comes on."""))
		return	'HouseBasement'

	else: 

		print(dedent("""Not quite sure what that means. 
			Try something else."""))
		return 'HouseBasement'





class SecurityDoor(Scene): 

	print(dedent("""You find yourself standing in front of what 
		appears to be a vending machine. Something isn't quite 
		right about how sits on the floor, though. 
		The way it's placed reminds you of a hinge - 
		almost like a door? Maybe thumbing a code into 
		the keypad could work."""))

	code = input("> ")

	if code == "2821": 

		print(dedent("""You type in the code '2821', and cross
		your fingers. The vending machine lets out a loud hissing 
		noise, then slowly swings open to reveal a hidden passageway.
		It's a door! Now that a path is open, you run through to see
		what's inside."""))

		return 'PortalRoom'

	elif code !== "2821": 

		print(dedent(f"""You press {code} on the vending machine, 
			but nothing seems to have happened. Maybe try another?""")

	else: 

		print(dedent("""Not quite sure what you meant there.
		Try something else!"""))








