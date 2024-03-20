def hello(first,middle,last):
    print("Hello " + first +" "+ middle + last)
    name = middle+last+first
    return name

name = hello(middle="And",last="rew",first="Chen")
print(name)

print(input("Enter a number: "))
input(print(1)) #not good