n = int(input())
# 9:00
# 45 +5 +45+15+45 = 155
lesson = n * 45
if(n%2==1):
    odd = n- 2
    even = n - odd - 1
else:
    odd = n -1
    even = n-odd-1
answer = lesson + (odd*5) + (even*15)
hour = answer//60
min = answer - (hour * 60)

hour = 9+hour

print(hour,min)