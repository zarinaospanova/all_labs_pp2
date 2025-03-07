# 1 task 
import os
path = '/Users/darinaospanova/Documents/pp2_all_labs/labs/lab6'
my_list = os.listdir(path)
print('Only directories: ')

# we have to join the 'path' and the 'element' inside this path

# we have to join the 'path' and the 'element' inside this path

for element in my_list:
    full_path = os.path.join(path, element)
    if os.path.isdir(full_path):
        print(element)

print('-----------------------')

print('Only files: ')

for element in my_list:
    full_path = os.path.join(path, element)
    if os.path.isfile(full_path):
        print(element)

print('-----------------------')

print('Directories and files: ')

for element in my_list: 
    print(element)

# 2 task 
print(os.access(path, os.F_OK)) # existence
print(os.access(path, os.R_OK)) # readability 
print(os.access(path, os.W_OK)) # writability
print(os.access(path, os.X_OK)) # executability 

# 3 task 
if os.path.exists(path):
    base = os.path.basename(path)
    print(base) # it returns only the filename 
    print(path[:-len(base)]) # getting the result of the directory which leads to our 'base'

# 4 task 
with open('/Users/darinaospanova/Documents/pp2_all_labs/labs/lab6/directories_files/sample.txt', 'r') as my_file:
    cnt = 0
    for line in my_file:
        cnt += 1
print(cnt)

# 5 task 
my_list = ['1. apple', '2. banana', '3. cherry', '4. mango']

with open('/Users/darinaospanova/Documents/pp2_all_labs/labs/lab6/directories_files/sample.txt', 'r') as my_file:
    for fruit in my_list:
        my_file.write(fruit + '\n')

# 6 task 
for i in range(65, 91):
    with open(chr(i), 'x') as my_file: # Creating files with the names 'A', 'B', 'C', ...
        pass

# 7 task 
with open('/Users/darinaospanova/Documents/pp2_all_labs/labs/lab6/directories_files/sample.txt', 'r') as my_file:
    with open('sample.txt', 'w') as my_file_2:
        content = my_file_2.read()
        my_file_2.write(content)

# 8 task
if os.path.exists(path):
    if os.access(path, os.F_OK) and os.access(path, os.R_OK) and os.access(path, os.W_OK):
        os.remove(path)
    else: 
        print('File is not accessible')
else:
    print('File does not exist')
    
# os.rmdir - removes a directory 
# os.remove - removes a files