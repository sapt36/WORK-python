age = int(input("Your age?:"))

if age == 100:
    print("You are 100")
if age >= 18:
    print("You are an adult!")
elif age < 0: #else if
    print("You haven't been born yet!")
else:
    print("You are young!")
