# Ternary Operator


# if condition then do this
#     else do that

# if my_age > 13 then i can watch reels
#     else i can't watch'

# print("I will go GOA" if int(input("Enter your age")) > 18 else "Can't go, Stay Home ")

user_Age = int(input("Enter your age"))

if user_Age > 18:
    print("I will go GOA")
else:
    print("Can't go GOA, Stay Home ")

# if no rain tomorrow I will go to office
#   else I will do work from office

rain = True

if not rain:
    print('I will go to office')
else:
    print('I will do work from home')

# single line code
    print("single line code ------->\n I will go to office" if not rain else 'single line code ------->\nI will do work from home')

