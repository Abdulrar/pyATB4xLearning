import math
# Task #4
# Write a Python program to calculate the area of a circle given its radius
# using the formula  area=π×r^2 ( Take pie as 3.14)

radius5 = float(input('Enter the radius of the circle\n'))
Area = math.pi*math.pow(radius5,2)  # or
Area2 = 3.14*(radius5**2)
print('Area of the circle is', Area)
print('Area of the circle is', f"{Area:.3f}")
print('Area2 of the circle is', Area2)

# single line code
print(math.pi*(math.pow(radius5,2)))
