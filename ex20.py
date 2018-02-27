#import the argv feature so we can unpack arguments to variables
from sys import argv
#we set the name of the script and a file as our arguments
script, input_file = argv
#we'll make a function that prints a file after reading it
def print_all(f): 
	print(f.read())
#then, we'll have another function that rewinds by moving to the first byte in the file 
def rewind(f): 
	f.seek(0)
#and a third function that prints the number of lines, and a single line from a file 
def print_a_line(line_count, f): 
	#f maintains the current position in the file when we read a line
	print(line_count, f.readline())
#this assigns the file we gave when we ran our script to a variable 
current_file = open(input_file)
#we print the entire contents of the file
print("First let's print the whole file: \n")

print_all(current_file)
#and then go to the first byte in the file
print("Now let's rewind, kind of like a tape.")

rewind(current_file)
#then we print three lines
print("Let's print three lines:")
#prints 1 and the first line in the file 
current_line = 1
#current line is 1
print_a_line(current_line, current_file)
#adds 1 to the value of current_line and prints the second line in the file 
current_line += 1
#current line is 2
print_a_line(current_line, current_file)
#adds 1 more to current_line and prints the third line in the file
current_line += 1
#current line is 3
print_a_line(current_line, current_file)

