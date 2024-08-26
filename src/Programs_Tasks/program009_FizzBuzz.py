""""
Task #9
✅ FizzBuzz Test: Write a program that prints numbers from 1 to 100. 
# Loop For However, for multiples of 3, print "Fizz" instead of the number, and for multiples of 5, print "Buzz.
" For numbers that are multiples of both 3 and 5, print "FizzBuzz."
"""""


for i in range(1, 20,3):
    print(i)

for j in range(0, 20, 2):
    print('-----------', j)

for k in range(1, 20):
    if k% 15 == 0 :
        print("FizzBuzz")
    elif k%5 == 0 :
        print("Buzz")
    elif k % 3 == 0:
        print("Fizz")
    else:
        print(k)
