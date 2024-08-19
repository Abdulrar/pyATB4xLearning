# Task #6
# Develop a Python script that calculates the square and cube of a given number.
import math

num = int(input("Enter the number\n"))

square = num*num
print("square of the given number is: ", square)

cube = (num**3)  # Or ---> cube pow (num, 3)
print("cube of the given number is: ", cube)

cube2 = math.pow(num, 3)
print("cube2 of the given number is: ", cube2)