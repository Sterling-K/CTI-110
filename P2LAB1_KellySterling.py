# Sterling Kelly
# November 8 2025
# P2LAB1
# This program asks the user for the radius of a circle and calculates
# the diameter, circumference, and area based on that radius.

# Get the radius from the user
radius = float(input("What is the radius of the circle? "))

# Perform calculations
diameter = radius * 2
circumference = 2 * 3.14159 * radius
area = 3.14159 * (radius ** 2)

# Display results with correct formatting
print("The diameter of the circle is", format(diameter, ".1f"))
print("The circumference of the circle is", format(circumference, ".2f"))
print("The area of the circle is", format(area, ".3f"))
