from sys import argv

script, bread, meat  = argv 
cheese = input("Wait. What kind of cheese do you want? ")

print("This script is called:", script, ". It's meant to assemble the ultimate sandwich!")
print("Your ultimate sandwich consists of %r, %r, and %r!" % (bread, meat, cheese))

#features that are imported into python are called 'modules'
