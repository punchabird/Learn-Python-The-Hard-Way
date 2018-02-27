#imports argv feature from the sys package so we can unpack arguments
from sys import argv 
#our script will unpack two arguments to variables, the script name and filename
script, filename = argv
#opens your specified file, returns a file object, and assigns it to the variable txt 
txt = open(filename)
#this prints the contents of the file 
print(f"Here's your file {filename}:")
#txt specifies the file object without having to type it out, then reads the contents with no restrictions
print(txt.read())
txt.close()
#this prompts the user for input and assigns it to filePagain
print("Type the filename again.")
file_again = input("> ")
#opens file_again, returns a file object, and assigns it to txt_again
txt_again = open(file_again)
#prints the results 	
print(txt_again.read())
txt_again.close()

#close() closes the file and frees up system resources taken up by it
#after you do this, attempts to read it will automatically fail 

