global_var = 10


def read_global_var():

    print(global_var) # Accessing global variable without declaration


def write_global_var():

    global global_var # Declaring the intention to modify

    global_var = 5


read_global_var() # Outputs: 10

write_global_var()

print(global_var) # Outputs: 5
