"""
Task #7
✅ Leap Year Checker:

https://github.com/PramodDutta/PyATB4xLearning/blob/main/src/tasks/img_1.png

Create a program that determines whether a given year is a leap year. 
A leap year is divisible by 4, but not by 100 unless it is also divisible by 400. 
Use an if-else statement to make this determination.

"""""

year = int(input('Enter the year:\n'))

if (year % 4 == 0) and (year % 100 != 0):
    print(year, ' is a leap year')
elif (year % 400 == 0) and (year % 100 == 0):
    print(year, ' is a leap year')
else:
    print(year, ' is not a leap year')