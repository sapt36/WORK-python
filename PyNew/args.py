# *args =  parameter that will pack all arguments into a tuple
#          let function can accept a varying amount of arguments

def add(*args):
    sum = 0
    for i in args:
        sum += i
    return sum

print(add(1,2,3,4,5,6))

def add(*stuff): #args is changable
    sum = 0
    stuff = list(stuff) # let all arguments become a list
    stuff[1] = 5 # then we can change the value of this list
    for i in stuff:
        sum += i
    return sum

print(add(1,2,3,4,5,6))