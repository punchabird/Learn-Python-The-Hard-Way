
#create a function called cheese and crackers with two arguments, how much cheese and how many boxes of crackers
def cheese_and_crackers(cheese_count, boxes_of_crackers): 
	#print out a line that passes the cheese count into a formatted string for a complete sentence
	print(f"You have {cheese_count} cheeses!")
	#finish the printed string with the argument for boxes of crackers
	print(f"You have {boxes_of_crackers} boxes of crackers!")
	#print two more lines, then create a new line at the end of the function
	print("Man that's enough for a party!")
	print("Get a blanket. \n")

#you can give the function numbers by calling it and simply putting numbers in as arguments 
print("We can just give the function numbers directly.")
cheese_and_crackers(20, 30)

#it's also possible to assign numbers to variables, then use those variables as arguments in the function instead
print("OR, we can use variables from our script:")
amount_of_cheese = 10 
amount_of_crackers = 50 

cheese_and_crackers(amount_of_cheese, amount_of_crackers)

#math operations follow normal rules even when they're arguments inside a function
print("We can even do math inside too!")
cheese_and_crackers(10 + 20, 5 + 6)


#and you can use math and variables together to create new numbers for your function 
print("And we can combine the two, variables and math:")
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)