myset = {"apple","banana","cherry"}

#set are used to store multiple items in a single variable

# a set is a collection which is unordered,unchangeable,unindexed

print(myset)

# duplicate values will be ignored

thisset = {"apple","banana","cherry","apple"}
print(thisset)

# True and 1 are considered the same value in sets

set1 = {True,1,2,3}
print(set1)

# False and 0 are considered the same value in sets

# length - len()

print(len(set1))

# a set can contain different data types

set2 = set(("apple","banana","cherry"))
print(set2)

# loop through the set

for x in set2:
    print(x)

print("banana" in set2)
print("banana" not in set2)

# add items - add()

set2.add("kiwi")
print(set2)

# to add items from another set - update()
tropical = {"pineapple","mango","papaya"}
set2.update(tropical)
print(set2)

thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]
thisset.update(mylist)
print(thisset)

# to remove an item - remove() , discard()

set2.remove("banana")
print(set2)

set2.discard("apple")
print(set2)

# remove a random item - pop()

set1.pop()
print(set1)

# clear the set - clear()

tropical.clear()
print(tropical)

# del - delete the set complitely

del tropical

for x in myset:
    print(x)

# The union() and update() methods joins all items from both sets.
# The intersection() method keeps ONLY the duplicates.
# The difference() method keeps the items from the first set that are not in the other set(s).
# The symmetric_difference() method keeps all items EXCEPT the duplicates.

set1 = {"a", "b", "c"}
set2 = {1, 2, 3}

set3 = set1.union(set2)
print(set3)

# union = |

set3 = {"John", "Elena"}
set4 = {"apple", "bananas", "cherry"}

mysett = set1.union(set2, set3, set4)
print(mysett)

set5 = set1.intersection(set2)
print(set5)

# intersection = &


set1.intersection_update(set2)
print(set1)

# defference = -

# symmetric_difference - ^

set7 = set1^set2
print(set7)

set8 = {"apple", "banana", "cherry"}
set9 = {"google", "microsoft", "apple"}

set8.difference_update(set9)
print(set8)