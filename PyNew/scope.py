name = "Chen" # global scope
def display_name():
    name = "Andrew" # local scope (only ava inside this function)
    print(name)

display_name()
print(name)