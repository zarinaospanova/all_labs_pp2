import psycopg2, csv

conn = psycopg2.connect(database = "phonebook1", 
                        user = "postgres", 
                        host= 'localhost',
                        password = "Akbota1981@",
                        port = 5432)

conn.autocommit = True

command_create_db = 'CREATE DATABASE phone'
command_create_table = """
    CREATE TABLE phonebook1( 
        user_id SERIAL NOT NULL PRIMARY KEY, 
        username VARCHAR(255),
        phone_number VARCHAR(255)
    )
"""
command_insert_into_csv = 'INSERT INTO phonebook1 (username, phone_number) VALUES (%s, %s)'

command_update_phone = 'UPDATE phonebook1 SET phone_number = %s WHERE user_id = %s'

command_update_name = 'UPDATE phonebook1 SET username = %s WHERE user_id = %s'

command_filter_name_starts = "SELECT * FROM phonebook1 WHERE username LIKE %s"

command_filter_phone_starts = "SELECT * FROM phonebook1 WHERE phone_number LIKE %s"

command_delete_by_phone = "DELETE FROM phonebook1 WHERE phone_number = %s"

command_delete_by_name = "DELETE FROM phonebook1 WHERE username = %s"

cur = conn.cursor()

csv_file = '/Users/darinaospanova/Documents/pp2_all_labs/labs/lab10/assignments/phonebook/phones.csv'


def csv_to_db(csv_file):
    with open(csv_file, 'r') as file_csv:
        reader_csv = csv.reader(file_csv, delimiter = ',')
        for row in reader_csv:
            cur.execute(command_insert_into_csv, (row[0], row[1]))

# Inserting data into the PhoneBook.


# Printing every row of the table
def print_rows():
    cur.execute('SELECT * FROM phonebook1')
    results = cur.fetchall()
    for row in results:
        print(row)


# Inserting data to the table 
def insert_to_db():
    username = input('Enter the username: ')
    phone = input('Enter the phone number: ')
    cur.execute(command_insert_into_csv, (username, phone))

# 3 Updating data in the table (change user first name or phone)


# Changing by the name
def change_name():  
    new_username = input("Enter the new username: ")
    id = int(input('Enter the ID you want to change: '))
    cur.execute(command_update_name, (new_username, id))
    print_rows()

# Changing by the phone number
def change_phone_number():
    new_phone = input("Enter the new phone number: ")
    id = int(input('Enter the ID you want to change: '))
    cur.execute(command_update_phone, (new_phone, id))
    print_rows()

# Filtering by the name that starts by the user's input
def filter_name_start_by():
    starts_with = input("Enter the letters that have to start with: ")
    cur.execute(command_filter_name_starts, (starts_with + '%',))   
    results = cur.fetchall()
    for row in results:
        print(row)

# Filtering by the name taht starts by the user's input
def filter_phone_start_by():
    starts_with = input('Enter the digits that the phone number has to start with: ')
    cur.execute(command_filter_phone_starts, (starts_with + '%',)) # After cur.execute(...) the result of the 
    results = cur.fetchall()                                       # query is saved inside the cur object  
    for row in results: # .fetchall() takes all rows from the result of the last cur.execute() query 
        print(row)      # and returns them as a list of tuples

# Deleting by the phone number
def delete_by_phone():
    phone_number = input('Enter the phone you want to delete: ')
    cur.execute(command_delete_by_phone, (phone_number,))
    print_rows()

# Deleting by the name
def delete_by_name():
    name = input('Enter the name you want to delete: ')
    cur.execute(command_delete_by_name, (name,))
    print_rows()

def get_starting_with(letter):
    command = 'SELECT username FROM phonebook1 WHERE LEFT(username, 1) = %s'
    try:
        with conn.cursor() as cur:
            cur.execute(command, (letter,))
            result = cur.fetchall()
            print(result)
    except (psycopg2.DatabaseError, Exception) as error:
        print(error)

# Getting the user input
def get_user_input():
    commands = """    insert - Inserting into the database
    change name - Changing the name of the user by the id
    change phone number - Changing the phone number of the user by the id
    filter by name - Filtering by the name that starts with the given value
    filter by phone number - Filtering by the phone number that starts with the given value
    delete by name - Deleting record by the name 
    delete by phone number - Deleting record by the phone number
    print all - Printing all records in the table
    insert csv - Inserting all records to the database from the csv file
    start with letter - Selecting usernames starting with the given letter"""
    print(commands)
    user_input = input("Enter the command: ")
    if user_input == 'insert':
        insert_to_db()
    elif user_input == 'change name':
        change_name()
    elif user_input == 'change phone number':
        change_phone_number()
    elif user_input == 'filter by name':
        filter_name_start_by()
    elif user_input == 'filter by phone number':
        filter_phone_start_by()
    elif user_input == 'delete name':
        delete_by_name()
    elif user_input == 'delete phone number':
        delete_by_phone()
    elif user_input == 'print all':
        print_rows()
    elif user_input == 'insert csv':
        csv_to_db(csv_file)
        print_rows()
    elif user_input == 'start with letter':
        letter = input('Enter the letter: ')
        get_starting_with(letter)

# cur.execute(command_create_db)

# cur.execute(command_create_table)

get_user_input()

conn.commit()

cur.close()
conn.close()
