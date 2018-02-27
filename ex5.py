name = 'Zed A. Shaw'
age = 35 #not a lie 
height = 74 #inches
weight = 180 #lbs 
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

print(f"Let's talk about {name}.")
print(f"He's {height} inches tall.")
print(f"He's {weight} pounds heavy.")
print("Actually that's not too heavy.")
print(f"He's got {eyes} eyes and {hair} hair.")

#this line is tricky, try to get it exactly right 
total = age + height + weight
print(f"If I add {age}, {height}, and {weight} I get {total}.")

#inch to centimeter conversion - 1 inch = 2.54 centimeters
height_cm = height * 2.54
#pound to kilogram - 1lb == 0.453592kg
weight_kg = weight * .453592

print(f"He's {height_cm} centimeters tall.")
print(f"He's {weight_kg} kilograms heavy.")
