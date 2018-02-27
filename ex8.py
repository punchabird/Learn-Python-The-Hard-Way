formatter = "{} {} {} {}"

print(formatter.format(1, 2, 3, 4))
print(formatter.format("one", "two", "three", "four"))
print(formatter.format(formatter, formatter, formatter, formatter))
print(formatter.format(
		"Try your",
		"Own text here",
		"Maybe a poem",
		"Or a song about fear"
	))

#I use a function to turn formatter into other strings
#when I use formatter.format() I call the formatter function 
#pass to it four arguments, which match up with the bracket 
#calling format on formatter makes a new string that replaces {} with four variables 

