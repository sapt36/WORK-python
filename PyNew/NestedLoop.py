rows = int(input("How many rows? "))
columns = int(input("How many columns? "))
symbol = input("Enter a symbol to use: ")

for i in range(rows):
    for j in range(columns):
        print(symbol,end="") #,end = "" let it stay in one line
    print() #outer loop 換行