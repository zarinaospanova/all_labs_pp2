# variables w3school

a = 10
b = "Kate"
print(a)
print(b)


# casting 
x = str(10) # x will be '10'  - string
y = int(10) #y will be 10  - integer
z = float(10) #z will be 10.0  - float

# get the type 
q = 5
w = "Anna"
print(type(q))
print(type(w))

#Single or Double Quotes?
e = "Kim"
r = 'Kim'  # they are same as 

#Variable Names
myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"

#Many values to Multiple Variables
i,o,p = "LA","New York","Boston"
print(i)
print(o)
print(p)

# One Value to Multiple Variables
v = f = g = "Harvard"
print(v)
print(f)
print(g)

# Global Variables
t = "MIT"

def myFunc():
    print("The best university in the world is" + t)
myFunc()

# Camel Case
myVariableName = "Zara"

# Pascal Case
MyVariableName = "Zarina"

# Snake Case
my_variable_name = "ZARA"

"""
1.A variable name must start with a letter or the underscore character
2.A variable name cannot start with a number
3.A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
4.Variable names are case-sensitive (age, Age and AGE are three different variables)
5.A variable name cannot be any of the Python keywords.

"""