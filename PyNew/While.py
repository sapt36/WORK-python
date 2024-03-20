name = ""

while len(name) == 0:
    name = input("Enter your name: ")

print("Hello "+name)

#same result
name2 = None
while not name2:
    name2 = input("Enter that name: ")
print("hello "+name2)