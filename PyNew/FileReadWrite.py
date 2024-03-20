try:
    with open('text.tx') as file:
        print(file.read())
    # call with open() will auto closed file for you
    print(file.closed)
except FileNotFoundError:
    print("That file was not found!")

text = "Yo!\nThis is text\nGood to see you!"
text2 = "\nHI jia!"
with open('text.txt','w') as file:
    file.write(text)
with open('text.txt','a') as file:
    file.write(text2)
