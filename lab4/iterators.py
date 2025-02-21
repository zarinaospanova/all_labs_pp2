# 1 
def gen(stop):
    start = 1
    while (start <= stop):
        yield start
        start+=1
n = int(input("Number N: "))
nums = gen(n)
for num in nums:
    print(num)

# 2
def gen(stop):
    start = 0
    while( start <= stop ):
        yield start
        start+=1
n = int(input("Number N: "))
nums = gen(n)
for num in nums:
    if num % 2 == 0:
        print(num, end=' ')

# 3 
def gen(stop):
    start = 0
    while( start <= stop ):
        if( start % 3 == 0 or start % 4 == 0):
            yield start
        start+=1
n = int(input("Number N: "))
nums = gen(n)
for num in nums:
    print(num)

# 4 
def gen(a, b):
    while ( a <= b ):
        yield a**2
        a+=1
a = int(input("a: "))
b = int(input("b: "))
nums = gen(a, b)
for num in nums:
    print(num, end=" ")

# 5 
def gen(start):
    while start >= 0:
        yield start
        start -= 1
start = int(input("number N: "))
nums = gen( start )
for num in nums:
    print(num)

