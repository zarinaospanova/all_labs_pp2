# 1 
from datetime import date, timedelta 
def sub_5():
    return date.today() - timedelta(5) # date.today() returns "today's" date, timedelta() returns time duration
print(sub_5())

# 2
from datetime import timedelta, date
def get_yesterday():
    return date.today() - timedelta(1)
def get_tomorrow():
    return date.today() + timedelta(1)

print("Yesterday:", get_yesterday())
print("Today:", date.today())
print("Tomorrow:", get_tomorrow())

# 3 
from datetime import datetime

print(datetime.now().replace(microsecond = 0)) # replace() is used to modify specific attributes(in our case 'microsecond')
# result: 2025-02-21 20:58:43

# 4 
import datetime

# print(todayyy.hour)
# print(todayyy.minute)
# print(todayyy.second)
# print(todayyy.date())

def difference():
    first_input = input("Enter the first date as follows DD-MM-YYYY HH:MM:SS: ") # getting the first date
    second_input = input("Enter the second date as follows DD-MM-YYYY HH:MM:SS: ") # getting the first date

    first_date = datetime.datetime.strptime(first_input, "%d-%m-%Y %H:%M:%S") # getting the first timedelta object
    second_date = datetime.datetime.strptime(second_input, "%d-%m-%Y %H:%M:%S") # getting the second timedelta object

    diff = abs(first_date - second_date) # the difference between the two dates

    return diff.total_seconds() # getting the difference in seconds

print(difference())

