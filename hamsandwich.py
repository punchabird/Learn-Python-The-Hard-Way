def sandwich_ingredients (slices_of_bread, slices_of_meat, slices_of_cheese):
	print(f"We're making a sandwich with {slices_of_meat} slices of meat and {slices_of_cheese} slices of cheese.")
	print(f"To envelop all of that deliciousness, we're putting {slices_of_bread} slices of bread around it.")
	print("It'll be the ultimate sandwich!")

sandwich_ingredients(int(input("How many slices of bread? ")) + 4, input("How many slices of meat? "), input("How many slices of cheese? "))

