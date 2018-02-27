people = 30 
cars = 40 
trucks = 15

#prints a line if the value of cars is greater than people 
if cars > people: 
	print("We should take the cars.")
#if the first condition isn't met, a second one is put up 
elif cars < people: 
	print("We should not take the cars.")
#in all other cases, we can't decide 
else: 
	print("We can't decide.")

if trucks > cars: 
	print("That's too many trucks.")
elif trucks < cars: 
	print("Maybe we could take the trucks.")
else: 
	print("We still can't decide.")

if people > trucks: 
	print("Alright, let's just take the trucks.")
else:
	print("Fine, let's just stay home then.")