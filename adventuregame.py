print("""You wake up in a grassy clearing surrounded by trees. 
A small river runs into the forest on the left.
To your right, there is a faint orange light in the distance.
Which way do you walk?
	""")

walk = input("> ")

if walk == "left": 
	print("You follow the river for a while.")
	print("Eventually, you find that it feeds into a large lake in the woods.")
	print("The water is a deep blue, and sits perfectly still.")

	lake_action = input("> ")

	if lake_action == "swim": 
		print("You take your shoes off and jump in the lake.")
		print("A pair of hands grabs you and pulls you under without warning.")
		print("You struggle to break free as your lungs fill with water. You drowned!")

	elif lake_action == "fish": 
		print("A zombie fish emerges from the water and swallows you whole.")
		print("You died!")

	else: 
		print(f"You're not quite sure that {lake_action} was the right option. Maybe try something else?")

elif walk == "right":
	print("You follow the orange light on the right.")
	print("Turns out it was a stream of fast-flowing molten lava.")
	print("You died!")

elif walk == "forward": 
	print("As you put your right foot forward, the ground splits apart.")
	print("A large crack forms in the earth, and you fall in.")
	print("You died!")

else: 
	print("You can't seem to decide on a path.")
	print("This clearing looks pretty comfy though.")
	print("Maybe it's time... to sleep a while...")
	print("You close your eyes, this time for good.")
