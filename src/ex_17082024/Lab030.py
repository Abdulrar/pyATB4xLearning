# Task #5
# Create a program that takes two numbers as input and prints whether the first number is greater than, less than,
# or equal to the second number.

num1 = int(input("Enter the first num: "))
num2 = int(input("Enter the second num: "))

if num1 > num2:
    print("First number is greater than second number that is: ", num1)
elif num1 < num2:
    print("First number is less than second number that is: ", num2)
else:
    print("First number is equal to than second number.")