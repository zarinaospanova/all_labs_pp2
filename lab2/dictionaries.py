thisdict = {
    "name": "Zarina",
    "surname": "Ospanova",
    "year": "1"
}
print(thisdict)

# dictionary items 
print(thisdict["name"])

# length - len()
print(len(thisdict))

dict1 = dict(name = "Zarina",age = "17",country = "KZ")
print(dict1)

x = thisdict["surname"]
y = thisdict.get("surname")

# keys() - return a list of all the keys in the dict
z = thisdict.keys()

# values() - return a list of all values in the dict
q = thisdict.values()

w = thisdict.items()
print(w)

# check if key exist

if "surname" in thisdict:
    print("YES")

# change values

thisdict["year"] = 4

# update() - change values

thisdict.update({"name" : "Zara"})

# add an item

thisdict["country"] = "KZ"
print(thisdict)

# remove the items from a dictionary - pop()
thisdict.pop("country")
print(thisdict)

# remove the last item

thisdict.popitem()
print(thisdict)

# loop through a dict

 # all key names 
for x in thisdict:
    print(x)

for x in thisdict.keys():
    print(x)

# all values 
for x in thisdict:
    print(thisdict[x])

for  x in thisdict.values():
    print(x)

# print both keys and values 

for x,y in thisdict.items():
    print(x,y)

# copy a dictionary - copy()

mydict = thisdict.copy()
print(mydict)

mydict2 = dict(thisdict)
print(mydict2)

# nested dictionaries - a dict can contain dicts, this is called nested dict

myfamily = {
    "person1" : {
        "name" : "Yerlan",
        "year" : 1977
    },
    "person2" : {
        "name" : "Akbota",
        "year" : 1981
    },
    "person3" : {
        "name" : "Zarina",
        "year" : 2007
    },
    "person4" : {
        "name" : "Darya",
        "year" : 2010
    },

    "person5" : {
        "name" : "Yernar",
        "year" : 2012
    }
}

# or 

child1 = {
  "name" : "Zarina",
  "year" : 2007
}
child2 = {
  "name" : "Darya",
  "year" : 2010
}
child3 = {
  "name" : "Yernar",
  "year" : 2012
}

my_siblings = {
  "child1" : child1,
  "child2" : child2,
  "child3" : child3
}

# access items in nested dict

print(myfamily["person1"]["name"])

# loop through nested dict - items()

for x, obj in myfamily.items():
    print(x)

    for y in obj :
        print(y + ':' ,obj[y])

