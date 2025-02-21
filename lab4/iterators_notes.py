# Iterators
class MyNum: # Create an iterator class
    def __init__(self, start, stop, step):
        self.start = start # the attribute of the object for counting
        self.stop = stop 
        self.step = step

    def __iter__(self): # it returns itself
        return self
    
    def __next__(self): # the whole process of incrementing the value of variable occurs in this method
        if self.step > 0 and self.start > self.stop:
            raise StopIteration
        elif self.step < 0 and self.start < self.stop:
            raise StopIteration
        elif self.step == 0:
            raise StopIteration
        else:
            temp = self.start
            self.start += self.step
            return temp
    
my_nums = MyNum(1, 10, 1) # creating an object
reverse_of_my_nums = MyNum(10, 1, -1)

my_iter = iter(my_nums) # creating an iterator

# print(next(my_iter)) # 1 # getting the iteration 
# print(next(my_iter)) # 2
# print(next(my_iter)) # 3 

# for _ in range(5):
#     print(next(my_iter), end = ' ') # 4 5 6 7 8

# an Infinite Loop - if we don't have a 'StopIteration'
for num in my_nums:
    print(num, end = ' ')

print("\n-------------------")

for num in reverse_of_my_nums:
    print(num, end = ' ')

# Generators
# we don't have to use 'classes' for generators as in iterators. Generator is a function, which automatically creates __iter__() and __next__() functions
# generators use the keyword 'yield' 
# 'yield" doesn't 'stop' the function, we can start from the last values of the variables when calling the function again

print("\n----------------------")



def nums():
    start = 1
    while start < 10: # we use "while" loop, so that we 'stop' the function for a some time, and when calling it again, it would start from where it stopped
        yield start 
        start += 1

my_nums = nums() # creating a generator objects

print(next(my_nums)) # 1
print(next(my_nums)) # 2
print(next(my_nums)) # 3

print("-----------------")

def our_range(start, stop, step = 1):
    while (step > 0 and start < stop) or (step < 0 and start > stop):
        yield start
        start += step

my_range = our_range(1, 10)

print(next(my_range)) # 1
print(next(my_range)) # 2
print(next(my_range)) # 3

for num in my_range:
    print(num) # 4 5 6 7 8 9 10

print("-------------------")

for i in our_range(10, 1, -1): # we get our own 'range()' function
    print(i, end = ' ')