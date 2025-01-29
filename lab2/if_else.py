a = 45
b = 300
if b>a:
    print(" b is greater than a")

# tab is important !

a1 = 322
b1 = 136
if a1 > b1:
    print("a1 is greater than b1")
elif a1 == b1:
    print("a1 and b1 are equal")

# elif - when if statements were not true , then try elif statements

a2 = 200
b2 = 33
if b2 > a2:
  print("b is greater than a")
elif a2 == b2:
  print("a2 and b2 are equal")
else:
  print("a2 is greater than b2")

# else - if other statements were false , this one will be work

# short hand if 
if a>b: print("a is greater")

# short hand if else

print("A" if a>b else print("B"))

# and - conjunction

q = 5
w = 6
c = 9
if c>q and c>w:
   print("Both conditions are true")

# or - disjunction

a = 200
b = 33
c = 500
if a > b or a > c:
  print("At least one of the conditions is True")

# not - negation

a = 33
b = 200
if not a>b:
   print("a is not graeter than b")

# nested if

x = 41

if x > 10:
  print("Above ten,")
  if x > 20:
    print("and also above 20!")
  else:
    print("but not above 20.")

# pass statement

a = 33
b = 200

if b > a:
  pass