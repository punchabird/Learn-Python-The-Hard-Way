#rewriting our while loop to use a for loop 

i = 0
numbers = []
#print i repeatedly until we hit 6
for i in range(i, 6): 
	print(f"At the top i is {i}")
	#each time we print i, add it to the list in numbers
	numbers.append(i)

	print("Numbers now: ", numbers)
	print(f"At the bottom i is {i}")

print("The numbers: ")

for num in numbers: 
	print(num)

