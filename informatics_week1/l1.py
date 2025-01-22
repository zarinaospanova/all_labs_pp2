n = int(input())
h = n//3600
san = 0
while(h>12):
    h = n//3600
    san+=1
    continue
# 12*3*3600 = 129 600
n = n - h*san*3600
m = n//60
s = n%60
print(str(h) + ":" +str(m) + ":" + str(s))