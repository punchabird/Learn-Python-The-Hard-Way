#writing a script that also accepts arguments

from sys import argv #import adds features to your script from python
#read the WYSS section on how to run this 
script, first, second, third = argv #this line unpacks argv and assigns all the arguments to 4 variables 
#argv is argument variable, which holds arguments for the script

print("The script is called:", script)
print("Your first variable is:", first)
print("Your second variable is:", second)
print("Your third variable is:", third)
