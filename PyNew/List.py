food = ["pizza","hamburger","hotdog","spaghetti",1,1.23]
food[2] = True
print(food[0])
print(food[5])
print(food[2])

food.append("ice cream") # add at the end of the list
food.insert(0,"cake") # add at the index you eant
for x in food:
    print(x)
# food.sort()  only same data type can use
food.clear() #remove all element in list
for x in food:
    print(x)