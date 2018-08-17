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
	meal, and a small black book. """))

	search = input("> ")
	

	if search == "fridge": 


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

		return 'portal_room'
	else: 
		print(dedent(f"""You press {code} on the vending machine, 
			but nothing seems to have happened. Maybe try another?""")



