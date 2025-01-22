a = int(input())
b = int(input())
n = int(input())

x = a*n
y = b*n

if(y%100==0):
    x += int(y/100)
    y = 0

print(x,y)