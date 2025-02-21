# 1 
n = int(input('Enter the number: '))

def squares(n):
    start = 1
    while (start ** 2) <= n: # a generator of squares of integers up to a given n
        yield start ** 2
        start += 1

for i in squares(n):
    print(i)

# 2
# printing even numbers between 0 and n 
n = int(input("Enter the number: "))

def even_nums(n):
    start = 0
    while start <= n: # if we put our condition for checking even numbers next to 'start <= n', we'll our function will stop when it would reach 1 won't continue
        if start % 2 == 0:
            yield start
        start += 1

for i in even_nums(n):
    print(i)

# 3 
# numbers divisible by 3 and 4 between 0 and n 

n = int(input("Enter the number: "))

def div_3_4(n):
    start = 0
    while start <= n:
        if start % 3 == 0 and start % 4 == 0:
            yield start
        start += 1
    
for i in div_3_4(n):
    print(i)

# 4 
# squares between a and b

a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

def squares_a_b(a, b):
    start = 1
    while start ** 2 <= b: # the 'while' loop works until we reach the 'b'
        if start ** 2 >= a: # if our the square of 'start' is greater or equal to a, yield it, 
            yield start ** 2
        start += 1 # otherwise just increment 'start' by 1

for i in squares_a_b(a, b):
    print(i)

# 5 
# numbers from n to 0

n = int(input("Enter the number greater than 0: "))

def from_n_to_0(n):
    start = n
    while start >= 0: # we get the numbers from n to 0, including 0
        yield start
        start -= 1

for i in from_n_to_0(n):
    print(i)

