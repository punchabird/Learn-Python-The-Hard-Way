
#define a variable types_of_people and sets the value to 10
types_of_people = 10
#x is a formatted string that takes the value from types_of_people
x = f"There are {types_of_people} types of people."

binary = "binary"
do_not = "don't"
#y is another formatted string that incorporateds the vlaues from binary and do_not
y = f"Those who do know {binary} and those who {do_not}."

print(x)
print(y)

print(f"I said: {x}")
print(f"I also said: {y}")

hilarious = False
#brackets allow me to insert a variable into a string then format
joke_evaluation = "Isn't that joke so funny?! {}"
#I'm formatting the string value given by joke_evaluation, and also inserting the value of hilarious
print(joke_evaluation.format(hilarious))

w = "This is the left side of..."
e = "a string with a right side."
#this concatenates w and e
print(w + e)
