#tuple - collection which is ordered and unchangeable

tuple1 = ("banana","cherry","pineapple")
print(tuple1)

#tuple items are ordered,unchangeable,and allow duplicate values
# tuple items are indexed,the first item has index [0]

#When we say that tuples are ordered, it means that the items 
# have a defined order, and that order will not change.

#Tuples are unchangeable, meaning that we cannot change, add or remove 
# items after the tuple has been created.

#allow duplicates

tuple2 = ("apple","banana","banana","cherry","apple")

#tuple length - len() function

print(len(tuple1))

#create tuple with one item , after this one item add comma

tuple3 = ("banana",)

#tuple items can be of any data type
tuple4 = (1,2,3,4,5,6)

# tuple can contain different data types
tuple5 = ("KBTU",100,True)

# access tuple items 
print(tuple1[1])

#negative indexing
print(tuple2[-2])

#range of index
print(tuple5[1:3])
print(tuple5[:3])
print(tuple5[2:])

print(tuple2[-2:-1])
#This example returns the items from index -2 (included) to index -1 (excluded)

#check if item exists

if "apple" in tuple2:
    print("Yes,'apple' is in the fruits tuple")

#change tuple values

x = ('apple','banana','cherry')
y = list(x)
y[1] = 'kiwi'
x = tuple(y)
print(x)

#add items

q = ("MIT","Harvard","Oxford")
w = list(q)
w.append("Stanford")
q = tuple(w)

#add tuple to tuple

first = ("Astana","Almaty","Shymkent")
second = ("Shymbulak",)
first += second
print(first)

#remove items
first1 = ("Zarina","Akbota","Darya","Tomi")
second2 = list(first1)
second2.remove("Tomi")
first1 = tuple(second2)

#del - delete the tuple

#packing a tuple 
fruits = ("banana","cherry","kiwi")

#unpacking a tuple
(yellow,red,green) = fruits
print(yellow)
print(red)
print(green)

#using Asterisk
fruits2 = ("apple", "banana", "cherry", "strawberry", "raspberry")
(green,yellow,*red) = fruits2
print(green)
print(yellow)
print(red)

fruits3 = ("apple", "mango", "papaya", "pineapple", "cherry")
(green, *tropic, red) = fruits3
print(green)
print(tropic)
print(red)

#loop through a tuple

new_tuple = ("Kazakhstan","Russia","USA","China")
for x in new_tuple:
    print(x)

for i in range(len(new_tuple)):
    print(new_tuple[i])

i=0
while i<len(new_tuple):
    print(new_tuple[i])
    i+=1

#join two tuples
tuplee1 = ("a","b","c")
tuplee2 = (1,2,3,)
tuplee3 = tuplee1 + tuplee2
print(tuplee3)

# multiply tuples
mytuple = fruits * 2
print(mytuple)

# tuple methods
# count() - Returns the number of times a specified value occurs in a tuple
# index() - Searches the tuple for a specified value and returns the position of where it was found

print(fruits.count("apple"))
print(new_tuple.index("USA"))