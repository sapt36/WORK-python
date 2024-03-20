student = ("Bro",21,"male")
#tuple = ordered and unchangeable, used to group related data
print(student.count("Bro"))
print(student.index("male"))

for x in student:
    print(x)

if "Bro" in student:
    print("Bro is here!")