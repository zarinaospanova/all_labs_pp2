# DATE

import datetime

x = datetime.datetime.now() # year, month, day, hour, minute, second, microsecond
print(x)

# return the year and the name of the weekday
print(x.year)
print(x.strftime('%A'))

print("-----------------")

y = datetime.datetime(2025, 2, 12)
print(y.strftime('%p'))

# %a: Abbreviated weekday name (e.g., "Mon", "Tue", "Wed").
# %w: Weekday as a number 0-6, where 0 is Sunday.
# %d: Day of the month as a number 01-31.
# %B: Full month name (e.g., "January", "February").
# %b: Abbreviated month name (e.g., "Jan", "Feb").
# %m: Month as a number 01-12.
# %Y: Year with century (e.g., 2023).
# %y: Year without century (e.g., 23).
# %H: Hour (24-hour clock) 00-23.
# %I: Hour (12-hour clock) 01-12.
# %M: Minute 00-59.
# %S: Second 00-59.
# %p: AM/PM.

# ITER
# Iterator is an object that consists of countable number of values
my_str = 'apple'

my_iter = iter(my_str)

print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))

print()


# how for loop works
my_list = ['Apple', "Banana", "Cherry", 'Coconut']

# for i in my_list: 
#     print(i)

looper = iter(my_list)
while True:
    try:
        obj = next(looper)
        print(obj)
    except StopIteration: 
        break



#Creating an Iterator Object/Class

class Nums:
    def __iter__(self):
        self.a = 1
        return self
    
    def __next__(self):
        # In the __next__() method, we can add a terminating condition to raise an error if the iteration is done a specified number of times
        if self.a <= 10:
            x = self.a
            self.a += 1
            return x
        else:
            raise StopIteration
    
my_class = Nums() 
my_iter = iter(my_class) # Now, our class becomes an iterator object 

for x in my_iter: # now we can iterate through the 'my_iter' and print each member of it
    print(x)

# JSON 
import json

x = '{ "name":"John", "age":30, "city":"New York"}'

y = json.loads(x) # loads() method is for converting from json to python

print(y['age'])

t = {
  "name": "John",
  "age": 30,
  "city": "New York"
}

z = json.dumps(t)

print(z)

print('------------------')
# Converting from python to json 

print(json.dumps({"name": "John", "age": 30}))
print(json.dumps(['apple', 'banana']))
print(json.dumps(('apple', 'banana')))
print(json.dumps('hello'))
print(json.dumps(12))
print(json.dumps(14.12))
print(json.dumps(True))
print(json.dumps(None))

print('------------------')

r = {
    "name" : 'John', 
    'age' : 30, 
    'married' : True,
    'divorced' : False, 
    'children' : ("Ann", "Billy"), 
    'pets' : None, 
    'cars' : [
    {'model' : "BMW 230", 'mpg' : 27.5},
    {"model" : "Ford Edge", 'mpg' : 24.1}
    ]
}

print(json.dumps(r, indent = 4, separators = ('. ', ': '), sort_keys = True)) # sort_keys = True sorts the result by the keys
# separators has two parameters, 1. separates each object 2. separates keys and values

# MATH
import math
x = math.sqrt(64) # Result: 8.0
print(x)
y = math.ceil(-1.2)
print(y)

"""
# MODULES

i use commemts thats why my vscode gives me error , when i try to use import modules

def Hello():
    print("Hello, world!")
person1 = {
    'name' : "John",
    'age' :  36,
    'country' :  'Iceland'
}
from modules import person1 # 'as mx'    # importing only parts from a module
import platform 

# When using a function from a module, use the syntax: module_name.function_name.

# mx.Hello()

# a = mx.person1
# print(a)

a = person1
print(a)

# Other built-in modules in python
x = platform.system()
print(x)

# dir() is used to return the list with all the functions and variables in a module 
y = dir(platform)
print(y)

# z = dir(mx)
# print(z)

# When importing using the from keyword, do not use the module name when referring to elements in the module. 
# Example: person1["age"], not mymodule.person1["age"]
"""
# SAMPLE
def print_func(name):
    print('Hello ' + name)

# SCOPE
# A variable created inside a function will exist only inside that function 

def print_num():
    x = 4
    print(x)

print_num()

# the variable is not available outside the function, but it's available for any function inside the function 
def my_func():
    x = 300
    def inner_func():
        print(x)
    inner_func()

my_func()


# a global variable is available on a global and local scopes
y = 200

def my_func1():
    print(200)

my_func1()

# if you write the variable name inside and outside of the function, python will treat them separately

t = 10

def my_func2():
    t = 20
    print(t)

my_func2()

print(t)



# global keyword # 1 
def my_func3():
    global z
    z = 5

my_func3()

print(z)
print()

# changing the global variable inside the function # 2
u = 400

def my_func4():
    global u
    u = 500

my_func4()

print(u)


# 'nonlocal' keyword is used inside nested functions
def my_func5():
    q = 24
    def my_func6():
        nonlocal q
        q = 36
    my_func6()
    print(q)

my_func5()