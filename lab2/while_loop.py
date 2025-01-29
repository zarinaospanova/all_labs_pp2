# python loops : while loop , for loops

# while loop 

i = 1
while i < 6:
    print(i)
    i += 1

# remember for increment i, or else the loop will continue forever

# the break statement

# break - we can stop the llop even if the while condition is true

i = 1
while i < 6:
    print(i)
    if i == 3:
        break
    i += 1

# continue - if the statement is true , we can continue 

i = 0
while i < 6:
    i += 1
    print(i)
    if i == 3:
        continue
    print(i)

# the else statement

i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6")
