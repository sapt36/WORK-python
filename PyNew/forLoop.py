import time

for i in range(10+1): #0~10
    print(i+1) #1~11
for j in range(50,100+1,2): #(start, end, every"2")
   print(j)
for k in "Bro code":
    print(k)
for seconds in range(10,0,-1): #count down from 10 to 1
    print(seconds)
    time.sleep(1) #every result delay 1 second
print("Happy new year!")