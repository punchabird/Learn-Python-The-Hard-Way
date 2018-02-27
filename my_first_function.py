def sandwich_ingredients (slices_of_bread, slices_of_meat, slices_of_cheese):
	print(f"We're making a sandwich with {slices_of_meat} slices of meat and {slices_of_cheese} slices of cheese.")
	print(f"To envelop all of that deliciousness, we're putting {slices_of_bread} slices of bread around it.")
	print("It'll be the ultimate sandwich!")

#giving function numbers directly 
sandwich_ingredients(10, 20, 30)

#variables as arguments
bulging_bread_bag = 100
incredibly_large_ham = 409560
the_big_cheese = 69

sandwich_ingredients(bulging_bread_bag, incredibly_large_ham, the_big_cheese)

#doing math inside function arguments
sandwich_ingredients(10 + 230, 100 * 2, 59 - 20)

#math and variables together
sandwich_ingredients(bulging_bread_bag / 2, incredibly_large_ham - 230483, the_big_cheese + 1)

ask_for_bread = input("How many slices of bread?")
ask_for_meat = input("How many slices of meat?")
ask_for_cheese = input("How many slices of cheese?")

#taking inputs as arguments
sandwich_ingredients(input("How many slices of bread? "), input("How many slices of meat? "), input("How many slices of cheese? "))

#modifying inputs with numbers
sandwich_ingredients(int(input("How many slices of bread? ")) + 5, input("How many slices of meat? "), input("How many slices of cheese? "))
