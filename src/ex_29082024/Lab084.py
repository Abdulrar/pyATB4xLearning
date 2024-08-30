set1 = set(["TheTestingAcademy", "For", "TheTestingAcademy"])
print(len(set1))

set2 = set(["TheTestingAcademy", "For", "TheTestingAcademy.."])
print(len(set2))

for i in set2:
    print(i)

set2.add("Pramod")
set2.add("Pramod")

print(set2)

name = "Pramod"
print(name.upper())