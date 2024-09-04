number = 3.14159265359
formated_number1 = f"{number:.5f}"
formated_number2 = f"{number:.4f}"

print(formated_number1)
print(formated_number2)
print(type(formated_number1))  # <class 'str'> ++++++++++++++++
print(formated_number1 + formated_number2)

# number = 3.14159265359
# formated_number = f"{number:.5f}" output: 3.14159
# formated_number = f"{number:.4f}" output: 3.1415 - it will be round figure 4th position num if that num >=5 i.e; 6
# print(formated_number)
#
# Format String
num = 90
print("This is the number you are working with "f"{num}")

# Table
# 2x1 = 2
# 2x2 = 4
# 2x10 = 20

table = 9
print(f"{table}*1={table}")
print(f"{table}*2={table*2}")
print(f"{table}*3={table*3}")
print(f"{table}*10={table*10}")

print(type(f"{table}*1={table}"))  # <class 'str'>

