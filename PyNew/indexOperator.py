# access to a sequence's element (str,list,tuple)

name = "bro code"

if (name[1].islower()):
    name = name.capitalize()
print(name)

first_name = name[:3].upper()
print(first_name)

last_name = name[4:].lower()
print(last_name)

last_char = name[-1]
print(last_char)