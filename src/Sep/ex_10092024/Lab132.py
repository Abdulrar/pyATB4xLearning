import os

# operating system - files, path related to the OS

# print(os.name) # posix - unix based - system mac or linus, windows - nt
# if os.name == 'posix':
#     print("using mac")
# else:
#     print("windows")

# print(os.getcwd())
# os.chdir("/Users/promode/Downloads/postman_collections/project1")
# print(os.getcwd())
# os.mkdir('new_directory')
# os.makedirs('parent/child/grandchild')
# print(os.listdir('.'))
# for file in os.listdir('.'):
#     print(file)


# os.remove('example.txt')
# os.rmdir('new_directory')

# os.rename('old_name.txt', 'new_name.txt')

full_path = os.path.join('/users/reddipalle.r/PycharmProjects/pyATB4xLearning/src/Sep/ex_10092024/AbdulFile', 'AbdulText')
# "C:\Users\reddipalle.r\PycharmProjects\pyATB4xLearning\src\Sep"
# "C:\Users\reddipalle.r\PycharmProjects\pyATB4xLearning\src\Sep\ex_10092024\AbdulFile\AbdulText"
# "src/Sep/ex_10092024/AbdulFile/AbdulText"  ---> Path content from root


print(full_path)

print(os.path.exists('AbdulText'))

print(os.path.isfile('AbdulText'))

print(os.path.isdir('directory_name'))
