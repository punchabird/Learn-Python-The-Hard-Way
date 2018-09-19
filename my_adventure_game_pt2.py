from textwrap import dedent
from sys import exit


class Scene(object): 

	def enter(self): 
		pass 


class Death(Scene): 

	print("You died!")
	exit(1)