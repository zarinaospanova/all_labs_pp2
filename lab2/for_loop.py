# for loop - we use it for iterating over a sequence

universities = ["KBTU","MIT","HARVARD"]
for x in universities:
    print(x)

# looping through a string

for x in "Almaty":
    print(x)

# break statement
for x in universities:
    print(x)
    if x == "KBTU":
        break


for x in universities:
    if x == "MIT":
        break
    print(x)

# continue statement

for x in universities:
    if x == "KBTU":
        continue
    print(x)

# the range function

for x in range(7): # it is not a values of 0 to 7 , just of 0 to 6
    print(x)

for x in range(2,9): # it is of 2 to 8 not including 9
    print(x)

for x in range(2,9,2): # it is of 2 to 8 with 2 (default is 1)
    print(x)

# else in for loop

for x in range(7):
    print(x)
else:
    print("finished")

# nested loops 

adj = ["red","big","beautiful"]
nouns = ["apple","buildings","butterfly"]

for x in adj:
    for y in nouns:
        print(x,y)

# to pass statement

for x in [0,1,2]:
    pass