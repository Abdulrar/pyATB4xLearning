# Task #11 -
# ✅ Fibonaci series 0,0+1, 0+1+1, if n = 7 ---> 0, 1, 2, 3, 5, 8, 13
# Fionacciseries : is the sum of first two numbers

count = int(input('Enter the count to print Fibonacci series: '))
firstNum = 0
secondNum = 1
print(firstNum)
# print(secondNum)
if count <= 0:
    print("Please enter count is greater than zero")
else:
    for i in range(0, count):
        thirdNum = firstNum + secondNum
        print(thirdNum)
        # print('--------',i)

        firstNum = secondNum
        secondNum = thirdNum
