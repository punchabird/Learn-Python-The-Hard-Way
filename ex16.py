from sys import argv

script, filename = argv

print(f"We're going to erase {filename}.")
#ctrl-c on the console initiates a keyboard interrupt, and stops the program
print("If you don't want that, hit CTRL-C (^C).")

print("If you do want that, hit RETURN.")
#asks for input and when we press enter we simply continue 

input("?")

print("Opening the file...")
#assigns the open filename to target
#w mode creates the file if it doesn't exist, empties if it does - it is intended for writing
#t would specify truncation, r for reading
target = open(filename, 'w')
#target creates the file and then it is truncated 
print("Truncating the file. Goodbye!")
target.truncate()

print("Now I'm going to ask you for three lines.")
#asks the user to input 3 lines, separately 
line1 = input("Line 1: ")
line2 = input("Line 2: ")
line3 = input("Line 3: ")

print("I'm going to write these to the file.")
#writes the 3 new lines to the file
target.write(f"{line1} \n {line2} \n {line3} \n")
#closes the file to free system resources
print("And finally, we close it.")
target.close()

