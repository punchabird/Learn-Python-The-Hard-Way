from textwrap import dedent
from sys import exit 

class Engine(object): 

	def __init__(self, scene_map): 
		self.scene_map = scene_map

	def play(self): 
		current_scene = self.scene_map.opening_scene()
		last_scene  self.scene_map.next_scene('finished')

		while current_scene != last_scene: 
			next_scene_name = current_scene.enter()
			current_scene = self.scene_map.next_scene(next_scene_name)
			#be sure to print out the last scene
			current_scene.enter()

class Scene(object):
	"""The basic scene object. We'll implement levels
	in the game as subclasses of Scene."""
	def enter(self): 
		print("This scene is not yet configured.")
		print("Subclass it and implement enter().")

class Death(Scene):
	"""When the player is killed the game will go
	to this level and print out a short message 
	before exiting."""
	def enter(self): 
		print("You died!")
		exit(1)

class PrisonCell(Scene):
	"""The first level of the game. The player
	will start off in a prison cell, faced with
	a choice on how to escape and get past a
	lone guard."""
	def __init__(self, arg):
		super(GameStart, self).__init__()
		self.arg = arg
		
class PrisonHallway(Scene):
	"""After exiting the cell, you end up in
	a hallway with three other doors. The
	player must choose and explore each to 
	complete the game."""
	def __init__(self, arg):
		super(Prisonhallway, self).__init__()
		self.arg = arg
		
class SecurityDoor(Scene):
	"""This door is the level before the final
	scene in the game. The player has to find
	a key in order to advance past it."""
	def __init__(self, arg):
		super(SecurityDoor, self).__init__()
		self.arg = arg
		
class Armory(Scene):
	"""One of the three doors that the player
	is able to venture through is the armory.
	Exploring the armory can reward the player
	with weaponry to be used later on, or trip
	an alarm that results in their death."""
	def __init__(self, arg):
		super(Armory, self).__init__()
		self.arg = arg
		
class WardenOffice(Scene):
	"""The Warden's office is the level before
	the end. There's a chance to encounter the
	Warden in the office, but if not, he appears
	in the final level."""
	def __init__(self, arg):
		super(WardenOffice, self).__init__()
		self.arg = arg
						
class PrisonExit(Scene):
	"""After stepping through the security door,
	the player is almost to the end of the level.
	If s/he didn't encounter the Warden previously,
	a battle will ensue that determines whether
	they successfully finish the level."""
	def __init__(self, arg):
		super(PrisonExit, self).__init__()
		self.arg = arg
		