#Pseudo-random
import random

x = random.randint(1,6)
print(x)
y = random.random() # 0~1 float number
print(y)
myList = ['rock','paper','scissors']
z = random.choice(myList)
print(z)
cards = [2,3,4,5,6,7,8,9,"J","Q","K","A"]
random.shuffle(cards)
print(cards)