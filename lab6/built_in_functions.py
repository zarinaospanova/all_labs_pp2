# 1 task
import functools
my_list = [1,2,3,4,5,6]

result = functools.reduce(lambda x,y: x*y,my_list)
print(result)


# 2 task
my_text = "KBTU is the best university!"
cnt_upper = 0
cnt_lower = 0

# ord() - 1 character in UniCode
for letter in my_text:
    if ord(letter) >= 65 and ord(letter)<= 90:
        cnt_upper += 1
    elif ord(letter)>= 97 and ord(letter)<= 122:
        cnt_lower += 1
print("Uppercase letters:",cnt_upper)
print("Lowercase letters:" , cnt_lower)


# 3 task 
message = "2002"
reversed_object = reversed(message) # reversed() function returns a reversed iterator, which we can iterate through
reversed_message = ''
for i in reversed_object:
    reversed_message += i

if message == reversed_message:
    print("The string is a palindrome")
else:
    print("The string is not a palindrome")

# 4 task 
import time, math
number = int(input("Enter the number: "))
delay = int(input("Enter the delay time in milliseconds: "))
square_root = pow(number,1/2)
time.sleep((delay/1000)) # time.sleep() - gets seconds as an argument,so we divide milliseconds by 1000 to ger seconds 
print(f'Square root of {number} after {delay} milliseconds is {math.sqrt(number)}')

# 5 task 
my_tuple = (True,True,True,True)

if all(my_tuple):
    print(True)
else:
    print(False)
# That's how the all() function works (it returns True if the iterable is empty)