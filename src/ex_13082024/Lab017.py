"""""
Create a program , take 2 inputs from the user num1, num2 and give them
max
pow num1 to num2
sub, mul, sum, div.
Format your out with f{""}
"""""

num1 = int(input("Enter the num1 val "))
num2 = int(input("Enter the num2 val "))

maxValue = max(num1, num2)
print(maxValue)
powValue = pow(num1, num2)
print(powValue)
subValue = num1 - num2
print(subValue)
mulValue = num1 * num2
print(mulValue)
sumValue = num1 + num2
print(sumValue)
divValue = num1 / num2
print(divValue)

print("Results format--------")

print(f"{maxValue}")
print(f"{powValue}")
print(f"{subValue}")
print(f"{mulValue}")
print(f"{sumValue}")
print(f"{divValue}")
print(f"{divValue:.4f}")
