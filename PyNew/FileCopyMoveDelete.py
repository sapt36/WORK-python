import shutil #copy and delete folder
import os #move and delete file,empty_folder

shutil.copyfile('copy.txt','text.txt')
# src,dst (dst not exist will auto create one)

# copy() = copyfile() + permission mode + destination can be a directory
# copy2() = copy() + copied metadata

src = "text.txt" # can change to folder
dst = "C:\\Users\\853uj\\OneDrive\\桌面\\text.txt"

try:
    if os.path.exists(dst):
        print("There is already a file there!")
    else:
        os.replace(src,dst)   # move file
        print(src+" was moved!")
except FileNotFoundError:
    print(src+" was not found!")

path = "text.txt"
path2 = "folder"
try:
    #os.remove(path) # delete file
    os.rmdir(path2) # delete directory
    #shutil.rmtree(path2) #delete directory containing files
except FileNotFoundError:
    print("File not found")
except PermissionError:
    print("You don't have permission to delete")
except OSError:
    print("You cannot delete directoty that have file")
else:
    #print(path+" was deleted")
    print(path2+" was deleted")