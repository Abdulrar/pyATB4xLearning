#  Break - Based on condition , exit the loop
for i in range(0, 10, 1):  # 0 to 9 , start
    print(i)

# range(0, 10, 1)
# range(0, 10)
# range(10)     #  above 3 statements are same

for i in range(10):  # 0 to 9 , start
    print(i, end=" ")

print("\n-----------")

for i in range(-10): # No output in this case
    print(i, end=" ")