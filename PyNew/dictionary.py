# dictionary = chanageable, unordered colllection of unique key
#              fast because they use hashing,allow faster access

capitals = {'US':'Washington',
            'India':'New Dehil',
            'China':'Beijing',
            'Russia':'Moscow'}
print(capitals.get('Germany')) #check key is in the dic or not
print(capitals.keys())
print(capitals.values())
print(capitals.items())
capitals.update({'Germany':'Berlin'}) #add
capitals.update({'US':'Las Vegas'}) #change value
capitals.pop('China') #remove elemant
#capitals.clear()

for key,value in capitals.items():
    print(key,value)