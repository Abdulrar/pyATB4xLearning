# Escape Sequence
print("Hello World")
print("Hello\nWorld") # \n -> newline
print("Hello\tWorld") # \t -> tabline
print("Hello\bWorld") # \b -> backspace


# dir1 = 'C:\pramod\n.txt'
# print(dir1)  # single cotes are not work for above directory pat we have to use double cotes

# dir2 = "C:\pramod\n.txt"
# print(dir2)
# Where this r concept(raw string) will be used?
# Automation API, Web Automation, file_path = r concept - raw string
dir3 = r"C:\pramod\n.txt"
dir4 = r'C:\pramod\n.txt'
print(dir3)
print(dir4)

# name1 = 'pramod'utta'
# To fix above 20 issue Escape Seq (slash \). - Single cote
name2 = 'pramod\'utta'
name3 = "Pramod'utta"
print(name2)
print(name3)