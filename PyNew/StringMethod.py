name = "Bro code"
name2 = "123"
name3 = "Brocode"
print(len(name))
print(name.find("B"))
print(name.capitalize())

print(name.isdigit())
print(name2.isdigit())
print(name.isalpha())
print(name3.isalpha())

print(name.replace("o","a"))
print(name*3) #3 same string concat

#string slicing = create a substring by extracting elements
#                 from another string
first_name = name[0]
print(first_name)
first_two_name = name[0:2] #=name[:2]
print(first_two_name)
last_name = name[4:]
print(last_name)
Every_two_name = name[1:8:2] # r  o e
print(Every_two_name)
Reversed_name = name[::-1] #[0:end:-1]
print(Reversed_name)

website = "http://google.com"
slice = slice(7,-4) #m index is 17 and -1
print(website[slice])
website2 = "http://wikipedia.com"
print(website2[slice])