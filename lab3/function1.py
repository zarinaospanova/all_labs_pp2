# 1 task
def converter(g):
    ounces = g * 28.3495231 
    return ounces

gram=float(input())
s=converter(gram)
print(s)


# 2 task
def centigrade(f):
    c = (5 / 9) * (f - 32)
    print(c)
fahrenheit = int(input())
centigrade(fahrenheit)


# 3 task 
def solve(numheads,numlegs):
    # rabbit - 1 head,4 legs
    # chicken - 1 head , 2 legs
    # x + y = 35    4x+2y = 94
    # x - rabbit , x - chicken
    # x + y = 35  2x + y = 47 ->  x = 12 y = 35-12 = 13
    y = (numlegs - 2 * numheads) // 2
    x = numheads - y
    return x,y

heads = int(input())
legs = int(input())
chickens,rabbits = solve(heads,legs)
print(chickens, rabbits)


# 4 task
def filter_prime(array):
    array2 = []
    for i in range(len(array)):
        sum = 0
        for j in range(1,array[i]+1):
            if array[i] % j == 0:
                sum+=1
        if sum == 2:
            array2.append(array[i])
    print(array2)

arr  = list(map(int,input().split()))
filter_prime(arr)


# 5 task
from itertools import permutations
def permutat(n):
    all=permutations(n)
    return list(arr)
word=input()
result=permutat(word)
print(result)


# 6 task
def reverse_sentence(sentence):
    # Split the sentence into words
    words = sentence.split()
    
    # Reverse the list of words
    reversed_words = words[::-1]
    
    # Join the reversed words back into a sentence
    reversed_sentence = ' '.join(reversed_words)
    
    return reversed_sentence

# Get input from the user
user_input = input("Enter a sentence: ")

# Call the function and print the reversed sentence
print(reverse_sentence(user_input))


# 7 task
def has_33(nums):
    for i in range(len(nums)-1):  
        if nums[i] == 3 and nums[i+1] == 3:  
            return True  
    return False  

arr = list(map(int, input("Enter numbers separated by space: ").split()))


if has_33(arr):
    print("True")
else:
    print("False")


# 8 task
def spy_game(nums):
    for i in range(len(nums)-2):
        if nums[i]==0 and nums[i+1]==0 and nums[i+2]==7:
            return True
    return False

arr = list(map(int,input("enter the numbers separated by space: ").split()))

if spy_game(arr) == True:
    print("True")
else:
    print("False")

# 9 task
# sphere volume formula: V = 4/3 * P * r^3

def sphere_volume(radius):
    V = 4/3 * 3.14 * (radius)**3
    print(V)
radius1 = int(input())
sphere_volume(radius1)

# 10 task
def uniq(nums):
    new_array = []
    for i in range(len(nums)):
        sum = 0
        for j in range(len(nums)):
            if nums[i] == nums[j]:
                sum += 1
        if sum >= 1 and nums[i] not in new_array:
            new_array.append(nums[i])
    print(new_array)

array = list(map(int,input("enter the numbers by space: ").split()))

uniq(array)


# 11 task
def palindrome(arr):
    if len(arr) % 2 == 0:
        length = int(len(arr)/2)
        # ata    noon 
        answer = False
        for i in range(length):
            if arr[i] == arr[length - i]:
                answer = True
        if answer == True:
            print("Yes,palindrome")
        else:
            print("No, not palindrome")
    else:
        length = int(len(arr))
        # level    01234  0==4
        answer = False
        for i in range(length):
            if arr[i] == arr[length-1]:
                answer = True
        if answer == True:
            print("Yes,palindrome")
        else:
            print("No, not palindrome")
arr_my = str(input())
palindrome(arr_my)

# 12 task
def histogram(nums):
    for i in range(len(nums)):
        print("*" * nums[i])

array = list(map(int,input("enter the numbers: ").split()))

histogram(array)

# 13 task
import random

def guess_the_number():
    number_to_guess = random.randint(1, 20)
    guesses_taken = 0

    name = str(input("Hello! What is your name?"))
    print("Well," + name + " , I am thinking of a number between 1 and 20.")
    while True:
        guess = int(input("Take a guess. "))
        guesses_taken += 1
        
        if guess < number_to_guess:
            print("Your guess is too low.")
        elif guess > number_to_guess:
            print("Your guess is too high.")
        else:
            print("Good job! You guessed my number in" + " "+ str(guesses_taken) + " guesses!")
            break

guess_the_number()
