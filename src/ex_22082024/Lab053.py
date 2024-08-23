# Task #10 -
# ✅ Factorial n = 5 5! -->5*4*3*2*1 -> 120 3! -> 3*2*1* -> 6 4! -> 4*3*2*1 -> 24

num = int(input('Enter the number'))

f=1

for i in range(1, num+1):
    f = f*i

print(f)