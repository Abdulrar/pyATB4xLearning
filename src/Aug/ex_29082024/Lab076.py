# List
# List - Collection of Items( Duplicate is allowed)
my_list = [1, 2, 3]  # Same type of data (int)
# my_list2 = [1, True, "Pramod", 12.34]

print(my_list)
print("Length of list ---> ",len(my_list))

print(my_list[0])
print(my_list[2])
# print(my_list[10])  # list index out of range - exception

my_list[0] = "Pramod"
my_list[1] = "Dutta"
my_list[2] = "Dutta2"
# my_list[10] = "Dutta44" # list assignment index out of range

# Indexing
print("element at the index 0 - ", my_list[0])
print("element at the index 1 - ", my_list[1])
print("element at the index 2 - ", my_list[2])

print(my_list)
for element in my_list:
    print("for loop list iteration ---> ",element)

# for i in range(1, 10):  # [1,2,3,4,5,6,7,8,9]
#     print(i)

    # range(1,10,1) -> list -> [1,2,3,4,5,6,7,8,9]

print(" - -------------")
my_list = [1, 2, 3]

print("before append list ---> ",my_list)
# append()
my_list.append(4)  # Append object to the end of the list.
my_list.append(5)
print("Appended list --> ",my_list)

# extend()
my_list.extend([7, 8, 9])
my_list.extend([10])
my_list.extend(["Pramod"])
print(my_list)
print("Length of list ---> ",len(my_list))

# insert()
my_list.insert(1, "Dutta")
print(my_list)
print("Length of list ---> ",len(my_list))

my_list[1] = "Amit"
print(my_list)

my_list.insert(0, 0)
print(my_list)
my_list.insert(-1,"Lucky") # it will insert reverse of index
print(my_list)

# remove()
my_list.remove("Amit")
print(my_list)

# my_list.replace() # no replace key in list
# print(my_list)
print(" --------------------------")
print(" --------------------------")

my_copy_list = my_list.copy()
print(" Actual items list  --> ",my_list)
print("Shallow copy of list--> ",my_copy_list)

my_copy_list.clear()
print(my_list)
print(my_copy_list)

my_list.remove("Pramod")
#my_list.sort() # only we can sort if the list is having similar items
#my_list.sort(reverse=False)
print("remove & not sort --> ",my_list)

my_list.reverse()
print(my_list)

my_list.remove("Lucky")
print(my_list)
# print(my_list.sort(reverse=True)) it will print 'None' always first list sort out of print then try to print list
my_list.sort()
print("sorted list --> ",my_list)
my_list.sort(reverse=True)
print(my_list)
my_list.sort(reverse=False)
print(my_list)

# name = "Pramod"
# name = name.upper()
# print(name)
#
# # for - loop
#
l1 = [1, 99, 13]
l2 = [4, 2, 3]
l3 = l1 + l2
l3.sort()
print(l3)
