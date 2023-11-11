#A simple program to calculate the volume of a cone shape

#The equation for the volume of a cone is 
#(pi * r^2 * height) /3

#Define PI

PI = 3.14159

#take user input and convert it to integer type
radius = int(input("radius = "))

height = int(input("height = "))

cone_volume = (PI * radius**2 * height)  /  3

print(cone_volume)