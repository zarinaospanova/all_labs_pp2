# 1 
import math
a = float( input("Input degree: "))
print("Output radian: ", a*math.pi/180)

# 2 
import math
h = float( input("Height: ") )
a = float( input("Base, first value: ") )
b = float( input("Base, second value: ") )
print("Expected Output: ", (a+b)*h/2)

# 3 
import math
n = float(input("Input number of sides: "))
a = float( input("Input the length of a side: "))
each_degree = (math.pi*(n-2))/(2*n)
each_area = math.tan(each_degree)* (a*a/4)
print(each_area * n)

# 4 
import math
a = float(input("Length of base: ") )
b = float(input("Height of parallelogram: "))
print("Expected Output: ", a * b)
