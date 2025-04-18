import psycopg2
import csv

# Дерекқормен байланыс
conn = psycopg2.connect(
    database="phonebook1",   # Дерекқор аты
    user="postgres",         # Пайдаланушы аты
    password="Akbota1981@",  # Пайдаланушы паролі
    host="localhost",        # Сервер адресі
    port="5432"              # Порт
)
conn.autocommit = True  # Өзгерістерді автоматты түрде сақтау
cur = conn.cursor()

# Кесте құру
def create_table():
    cur.execute("""
        CREATE TABLE IF NOT EXISTS phonebook1 (
            user_id SERIAL PRIMARY KEY,
            username VARCHAR(255),
            phone_number VARCHAR(20)
        )
    """)
    print("Кесте құрылды немесе бар кесте тексерілді.")

# Консоль арқылы дерек енгізу
def insert_from_console():
    username = input("Атыңды енгіз: ")
    phone = input("Телефон номеріңді енгіз: ")
    # Деректерді базаға енгізу
    cur.execute("INSERT INTO phonebook (username, phone_number) VALUES (%s, %s)", (username, phone))
    
    conn.commit()  # Коммит жасап, өзгерістерді сақтау
    print("Жаңа жазба енгізілді:")
    print(f"Аты: {username}, Телефон нөмірі: {phone}")
    print_all()

# CSV файл арқылы дерек енгізу
def insert_from_csv(csv_file):
    with open(csv_file, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            cur.execute("INSERT INTO phonebook (username, phone_number) VALUES (%s, %s)", (row[0], row[1]))
    
    conn.commit()  # CSV деректерін енгізген соң, өзгерістерді сақтау
    print("CSV файлынан деректер енгізілді.")
    print_all()

# Барлық жазбаларды шығару
def print_all():
    cur.execute("SELECT * FROM phonebook")
    rows = cur.fetchall()  # Барлық жазбаларды алу
    print("\nБарлық жазбалар:")
    for row in rows:
        print(row)

# Негізгі меню
def menu():
    create_table()  # Кестені құру
    while True:
        print("""
МӘЗІР:
1 - Консоль арқылы енгізу
2 - CSV арқылы енгізу
3 - Барлығын шығару
0 - Шығу
        """)
        choice = input("Команданы таңда: ")
        if choice == '1':
            insert_from_console()  # Консоль арқылы дерек енгізу
        elif choice == '2':
            csv_path = input("CSV файлының жолын енгіз: ")
            insert_from_csv(csv_path)  # CSV файлынан дерек енгізу
        elif choice == '3':
            print_all()  # Барлық деректерді шығару
        elif choice == '0':
            print("Бағдарламадан шығу...")
            break
        else:
            print("Қате таңдау. Қайтадан көр.")

    cur.close()  # Қосылымды жабу
    conn.close()  # Дерекқормен байланыс жабу

menu()  # Бағдарламаны бастау
