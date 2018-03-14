#learning about while-loops 

i = int(input("Enter a number.> "))
range_increase = int(input("Enter another number. >"))
numbers = []

def number_crunch(i, range_increase):
	while i < 6:
		print(f"At the top i is {i}")
		numbers.append(i)

		i = i + range_increase

		print("Numbers now: ", numbers)
		print(f"At the bottom i is {i}")

	print("The numbers: ")

number_crunch(i, range_increase)

for num in numbers: 
	print(num)

