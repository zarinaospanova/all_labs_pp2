# Python file open

# File handling 
# the open() function takes two parametres : filename , mode 

# modes :
# "r" - read - default value , error if the file does not exist 
# "a" - append - opens a file for appending , creates the file if it does not existv 
# "w" - write - opens a file for writing , creates the file if it does not exist 
# "x" - create - creates the specified file , returns an error if the file exists
# "t" - text - default value . text mode 
# "b" - binary - binary mode(e.g images)

# Syntax

# top open a file for reading it is enough to specify name of the file 
# f = open("demofile.txt")

# to code above is the same as:
# f = open("demofile.txt",'rt)
# because "r" for raed, "t" for text are the default values, you do not need to specify them

# open afile on the server 

# if the file lopcated in the same folder as python:
# f = open("demofile.txt","r")
# print(f.read())

# if the file in a different location , you will have to specify the  file path,like this :
# f = open("D:\\myfiles\welcome.txt","r")
# print(f.read())

# read only parts of the file 
# how manuy characters you want to return :
# f = open("demofile.txt","r")
# print(f.read(5))

# read line() method - return one line 
# f = open("demofile.txt","r")
# print(f.readline())

# read first two lines 
# f = open("demofile.txt","r")
# print(f.readline())
# print(f.readline())

# by using loops , you can read the whole file, line by line
# f = open("demofile.txt","r")
# for x in f:
#    print(x)

# Close files - close() method 
# f = open("demofile.txt","r")
# print(f.readline())
# f.close()

# write to an existing file 
# f = open("demofile.txt","a")
# f.write("Now he file has more content")
# f.close()

# open and read the file aafter the appending:
# f = open("demofile.txt","r")
# print(f.read())

# f = open("demofile3.txt", "w")
# f.write("Woops! I have deleted the content!")
# f.close()

#open and read the file after the overwriting:
# f = open("demofile3.txt", "r")
# print(f.read())


# Create a new file 
# "x" - create

# f = open("myfile.txt","x") - a new empty file is created

# create a new file if it does not exist 
# f = open("myfile.txt","w")

# Delete a file 
# to delete afile,you must omport the OS module,and run its os.remove() function:

# import os
# os.remove("demofile.txt)

# Check if file exists , then delete it
# import os
# if os.path.exists("demofile.txt"):
#    os.remove("demofile.txt")
# else:
#    print("The file does not exist")

# delete Folder
# to delete an entire folder, use the os.rmdir() method

# import os
# os.rmdir("myfolder")
