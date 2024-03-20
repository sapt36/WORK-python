utensils = {"fork","spoon","knife","knife","knife"}
# set = unorder! fast than list! Not allow same element!
for x in utensils:
    print(x)
utensils.add("napkin")
utensils.remove("knife")
print(" ")
for i in utensils:
    print(i)
# utensils.clear() remove all elements in the set
print(" ")
dishes = {"bowl","plate","cup","fork"}
print(dishes.difference(utensils))
print(dishes.intersection(utensils))

utensils.update(dishes)

for j in utensils:
    print(j)

print(" ")
dinner_table = utensils.union(dishes)
for k in dinner_table:
    print(k)