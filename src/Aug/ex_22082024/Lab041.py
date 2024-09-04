# for i in range(1, 10, 1):  # to start 1 to stop 10-1, step = 1
#     print(i)

# 1,2,3,4,5,6,7,8,9

# for praveen in range(1, 5, 1):  # 1 to 4
#     print(praveen, end=" ")

# for i in range(3, 5): # 3,4
#     print(i)

# Range(start, stop-1, step)  step is how may step if we want to skip

print("\n1--------------")

for i in range(1, 10, 2): # 1 , 3 ,5 ,7, 9
    print(i, end=' ')

print("\n2--------------")

for j in range(-1, -10, -2):
    print(j, end=" ")

print("\n3--------------")

for j in range(1, 10, -2):  # No output in this case , should be start, stop and step mines (-) OR Plus (+)
    print(j, end=" ")      # OR start is greater than stop then we can use mines (-) in step below statement example

print("\n4--------------")

for j in range(10, 0, -2):
    print(j, end=" ")

print("\n5--------------")

for j in range(10, 0, 2): # No output in this case also,
    print(j, end=" ")


