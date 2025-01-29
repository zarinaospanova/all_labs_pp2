mylist = ["MIT","Harvard","Oxford"]
print(mylist)

#len - length 
print(len(mylist))

list1 =[1,2,3,4,5,6]

list2 = [True,False,True]

print(type(list1))

list3 =list(("Almaty","Astana","Semey"))
print(list3)

#List - a collection is ordered and changeable.
#Tuple - a collection which is ordered and unchangeable.
#Sets - a collection  which is unordered,no duplicate,unindexed,unchangeable
#Dictionary - ordered and changeable. no duplicate

print(list3[1])
print(list2[-1])
print(mylist[1:3])
print(list1[2:])

list1[1] = 9
print(list1)

list2[1:2] = [False,True]
print(list2)

list1.append(8)
print(list1)

#append - add the elements at the end
#insert - add elements with index

list1.insert(1,4)
print(list1)

#extend - to add elements fron another list

list_f = ['banana','apple','watermelon']
list_s = ['tomato','carrot']
list_f.extend(list_s)
print(list_f)

# remove - renoves the specified item
list_f.remove('banana')
print(list_f)

#pop - removes the specified index
list_f.pop(1)
print(list_f)

#del - delete the list completely
#clear - clear the list
list2.clear()
print(list2)

for x in list_f:
    print(x)

for i in range(len(list_s)):
    print(list_s[i])

i = 0
while i<len(list_f):
    print(list_f[i])
    i+=1

[print(x) for x in list1]

newlist = [x for x in range(10) if x<5]

newlist_2 = ['hello' for x in list1]

newlist.sort()
#sort - sort by asc

list1.sort(reverse = True)
#.sort(reverse = True) - sort by desc
#.reverse - reverse elements just
list1.reverse()

#copy() - copy e;ements from yhe list
mylist = list1.copy()
mylist2 = list(list1)

list6 = list1 + list3
print(list6)

for x in list2:
    list1.append(x)
