import random

n = int(input())
a = n%10
b = n//10%10
c = n//100%10
d = n//1000

if (a==d )and (b == c):
    print(1)
else:
    print(random.randint(0,999))