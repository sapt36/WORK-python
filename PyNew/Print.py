#print
print("Name: %s / Age: %d."%(str(input("name: ")),int(input("age: "))))

#print string
animal = ["cow","chicken","tiger","lion"]
item = ["moon","sun","sky"]

print("The {} jumped over the {}".format(animal[1],item[2]))
# position argument
print("The {0} jumped over the {1}".format(animal[1],item[2]))
print("The {1} jumped over the {0}".format(animal[1],item[2]))
# keyword argument
print("The {a} jumped over the {b}".format(a=animal[1],b=item[2]))
# another way
text = "The {} jumped over the {}"
print(text.format(animal,item))

#space format
name = "Andrew"
print("Hello, my name is {}".format(name))
print("Hello, my name is {:10}. Nice to meet u.".format(name))#留10格
print("Hello, my name is {:>10} Nice to meet u.".format(name))#靠右
print("Hello, my name is {:^10} Nice to meet u.".format(name))#置中

#
number = 3.14159
print("The number pi is {:.2f}".format(number))
number2 = 1000
print("The number pi is {:,}".format(number2))
print("The number pi is {:b}".format(number2)) #to binary
print("The number pi is {:o}".format(number2)) #to octol
print("The number pi is {:X}".format(number2)) #Uppercase to hex
print("The number pi is {:E}".format(number2)) #Scientific notation