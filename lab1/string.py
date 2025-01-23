#strings w3school

print("Hi")

#Quotes Inside Quotes
print("She is called 'Maya'")
print('He is called "John"')

#Assign String to a Variable
a = "Hii"
print(a)

#Slicing
v = "Salem,KBTU"
print(v[2:5])  # the first character has index 0

#Slice from the start
print(v[:5])

#Slice to the end 
print(v[2:])

#Negative indexing
print(v[-5:-2])

#Modife strings 
print(v.upper()) #upper case
print(v.lower()) #lower case 
print(v.strip()) # remove whitespace - Whitespace is 
#the space before and/or after the actual text, and very 
#often you want to remove this space. 

print(v.replace("S","s")) #replace string
print(v.split(",")) #split string returns:['salem' , 'KBTU']

#String Concatenation
x = "Hello"
y  = "Almaty"
c = x + y
print(c)

#string format
age = 36
txt = f"My name is Anna , I am {age}"

#\'	Single Quote	
# \	Backslash	
# \n	New Line	
# \r	Carriage Return	
# \t	Tab	
# \b	Backspace	
# \f	Form Feed	
# \ooo	Octal value	
# \xhh	Hex value	

