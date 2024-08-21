"""
Task #8
✅ Triangle Classifier:

https://github.com/PramodDutta/PyATB4xLearning/blob/main/src/tasks/img.png

Write a program that classifies a triangle based on its side lengths. 
Given three input values representing the lengths of the sides, 
determine if the triangle is equilateral (all sides are equal), 
isosceles (exactly two sides are equal), or scalene (no sides are equal). 
Use an if-else statement to classify the triangle.

"""""

side_length1 = int(input('Enter the first side length:\n'))
side_length2 = int(input('Enter the first side length:\n'))
side_length3 = int(input('Enter the first side length:\n'))

if side_length1 == side_length2 and side_length2 == side_length3:
    print('all sides are equal its an equilateral triangle')
elif side_length1 == side_length2 or side_length1 == side_length3 or side_length2 == side_length3:
    print('exactly two sides are equal its an isosceles')
else:
    print('its a scalene no sides are equal')




