import re 

# 1 task 
# Write a Python program that matches a string that has an 'a' followed by zero or more 'b''s.

# * --- zero or mopre characters 
# + --- one or more characters 
# b --- mathces the boundary between a word and a non - word character

with open('/Users/darinaospanova/Documents/pp2_all_labs/labs/lab5/test.txt','r') as my_file:
    my_text = my_file.read()

x = re.search('ab*',my_text)
print(x)

# 2 task 
# Write a Python program that matches a string that has an 'a' followed by two to three 'b'.

y = re.search('ab{2,3}',my_text)
print(y)

# 3 task 
# Write a Python program to find sequences of lowercase letters joined with a underscore.
print(re.findall('[a-z+_]',my_text))

# 4 task 
# Write a Python program to find the sequences of one upper case letter followed by lower case letters.
print(re.findall('[A-Z][a-z]+',my_text))

# 5 task 
# Write a Python program that matches a string that has an 'a' followed by anything, ending in 'b'.
print(re.findall('a.*b',my_text))

# 6 task 
# Write a Python program to replace all occurrences of space, comma, or dot with a colon. 
my_text = "Helllo. how are you, what's up"

def change(match): # 'change()' changes our match with colon
    return ":"

x = re.sub('[.,\s]', change, my_text) # finding characters that are either a dot, comma or a whitespace and whenever it's found -> call the function 'change'
print(x)

# 7 task 
# Write a python program to convert snake case string to camel case string.

import re

my_text = 'some_sample_data'

def to_camel_case(match):
    return match.group(1).upper()

x = re.sub('_([a-z])', to_camel_case, my_text) # we write ([a-z]) to get only the inner group, which is our letter after an underscore '_' 
print(x) # if we write it, [a-z], we will still have our underscores

# 8 task 
# Write a Python program to split a string at uppercase letters.

my_text = 'There Is Some Sample Text'
x = re.split(r'(?=[A-Z])', my_text)
print(x[1:])
# we group words to get the strings that start with 'A-Z' and has zero or more characters after
# if we don't write '?=', we would erase the found characters [A-Z] ---- we keep them using '?=', which 
# is called 'lookahead assertion' ---> it keeps everything inside the () brackets
# Example: if we write --- r",(?= )" --- the match is a comma followed by the space. 
# If we find a match we split our string at this place, but keep everything inside brackets, 
# which is the space
# re.split() -> splits everything before and after the match
# Matches if ... matches next, but doesn’t consume any of the string. This is called a lookahead assertion.
# For example, Isaac (?=Asimov) will match 'Isaac ' only if it’s followed by 'Asimov'.

# 9 task
# Write a Python program to insert spaces between words starting with capital letters.
my_text = 'HereIsSomeData'

x = re.sub('([a-z])([A-Z])', r'\1 \2', my_text) # first match: 'eI' ----> \1 -> 'e', \2 -> 'I'
                                                # second match: 'sS' ----> \1 -> 's', \2 -> 'S'
                                                # third match: 'eD' ----> \1 -> 'e', \2 -> 'D'      
print(x)

# 10 task
# Write a Python program to convert a given camel case string to snake case.
# hereIsSomeData -> here_is_some_data

my_text = 'hereIsSomeData'
def change(match):
    return match.group(1) + '_' + match.group(2).lower() # we get the match.group(1) ---> lowercase letters
                                                         # + '_' + match.group(2).lower() ---> turning uppercase letters to lowercase and
                                                         # adding everything together
x = re.sub('([a-z])([A-Z])', change, my_text) # first match: 'eI' ----> \1 -> 'e', \2 -> 'I'
                                              # second match: 'sS' ----> \1 -> 's', \2 -> 'S'
                                              # third match: 'eD' ----> \1 -> 'e', \2 -> 'D'   
print(x)