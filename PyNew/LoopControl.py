while True:
    name = input("Enter your name: ")
    if name != "":
        break #terminate loop
phone_number = "123-456-7890"

for i in phone_number:
    if i == "-":
        continue #skip to the next iterations
    print(i, end="") #replace new line char to nothing("")

for i in range(1,21): #similar to continue
    if i==13:
        pass #do nothing
    else:
        print(i)