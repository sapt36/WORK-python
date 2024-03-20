import os

path = "C:\\Users\\853uj\\OneDrive\\桌面\\text.txt"

if os.path.exists(path):
    print("That location exists!")
    if os.path.isfile(path):
        print("That is a file")
    elif os.path.isdir(path):
        print("That is a directionary!")
else:
    print("That location doesn't exists!")
