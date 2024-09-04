class Person:
    # Class Variables
    # Instance variables
    # name = "Amit" # hardcoded value
    def __init__(self, name):
        self.name = name

    def walk(self):
        return self.name


amit = Person("Jr_Amit")
pramod = Person("Jr_Pramod")
print(amit.name)
print(pramod.name)
print("Who is walking with the object pramod -> ", pramod.walk())
print("Who is walking with the object pramod -> ", amit.walk())
