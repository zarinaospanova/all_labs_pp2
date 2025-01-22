import random

a = int(input())
b = int(input())

bbb = False
if (a%b == 0) or (b%a == 0):
    print(1)
else:
    print(random.randint(0,100000))