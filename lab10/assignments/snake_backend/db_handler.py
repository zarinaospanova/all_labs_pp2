import psycopg2

# Устанавливаем соединение с базой данных
conn = psycopg2.connect(
    database='snake_game',
    user='postgres', 
    host='localhost', 
    password='Akbota1981@',
    port=5432
)

conn.autocommit = True

# Запросы для создания таблиц
query_create_table_users = """
    CREATE TABLE IF NOT EXISTS users (
        user_id SERIAL NOT NULL PRIMARY KEY,
        username VARCHAR(255) UNIQUE NOT NULL
    )
"""

query_create_table_user_scores = """
    CREATE TABLE IF NOT EXISTS user_scores (
        score_id SERIAL NOT NULL PRIMARY KEY,
        user_id INT REFERENCES users(user_id) ON DELETE CASCADE,
        score INT NOT NULL,
        level INT NOT NULL
    )
"""

# Функции

# Функция для выполнения любых запросов
def execute_query(query, params=None):
    try:
        with conn.cursor() as cur:
            if params:
                cur.execute(query, params)
            else:
                cur.execute(query)
            conn.commit()
    except (psycopg2.DatabaseError, Exception) as error:
        print(f"Ошибка выполнения запроса: {error}")

# Функция для добавления нового пользователя
def add_user(name):
    command = 'INSERT INTO users(username) VALUES (%s) RETURNING user_id'
    try:
        with conn.cursor() as cur:
            cur.execute(command, (name,))
            user_id = cur.fetchone()[0]  # Получаем user_id нового пользователя
            conn.commit()
            return user_id
    except (psycopg2.DatabaseError, Exception) as error:
        print(f"Ошибка добавления пользователя: {error}")
        return None

# Функция для проверки, существует ли пользователь в базе данных
def check_user_exists(name):
    command = 'SELECT user_id FROM users WHERE username = %s'
    try:
        with conn.cursor() as cur:
            cur.execute(command, (name,))
            result = cur.fetchone()  # Получаем первый результат
            return result is not None  # Возвращаем True, если пользователь существует
    except (psycopg2.DatabaseError, Exception) as error:
        print(f"Ошибка проверки существования пользователя: {error}")
        return False

# Функция для добавления нового результата в таблицу
def add_new_score(user_id, score, level):
    command = "INSERT INTO user_scores(user_id, score, level) VALUES (%s, %s, %s)"
    try:
        with conn.cursor() as cur:
            cur.execute(command, (user_id, score, level))
            conn.commit()
    except (psycopg2.DatabaseError, Exception) as error:
        print(f"Ошибка добавления нового результата: {error}")

# Функция для обработки результата пользователя
def process_score(username, score, level):
    user_exists = check_user_exists(username)
    
    if not user_exists:
        # Если пользователь не существует, добавляем его и получаем его user_id
        user_id = add_user(username)
    else:
        # Если пользователь существует, получаем его user_id
        user_id = get_user_id(username)

    if user_id:
        add_new_score(user_id, score, level)

# Функция для получения user_id для заданного имени пользователя
def get_user_id(username):
    command = 'SELECT user_id FROM users WHERE username = %s'
    try:
        with conn.cursor() as cur:
            cur.execute(command, (username,))
            result = cur.fetchone()
            return result[0] if result else None
    except (psycopg2.DatabaseError, Exception) as error:
        print(f"Ошибка получения user_id: {error}")
        return None

# Функция для отображения самого высокого уровня пользователя
def show_highest_level(username):
    command = 'SELECT MAX(level) FROM user_scores WHERE username = %s'
    try:
        with conn.cursor() as cur:
            cur.execute(command, (username,))
            result = cur.fetchone()
            return result[0] if result else None  # Возвращаем максимальный уровень или None, если уровни не найдены
    except (psycopg2.DatabaseError, Exception) as error:
        print(f"Ошибка получения самого высокого уровня: {error}")
        return None

# Этот блок кода выполнится только если файл будет запущен напрямую
if __name__ == '__main__':
    username = input('Введите ваше имя пользователя: ')  # Получаем имя пользователя с ввода
    score = 100  # Пример балла
    level = 1  # Пример уровня
    process_score(username, score, level)  # Обрабатываем результат и уровень для пользователя
    highest_level = show_highest_level(username)  # Показываем самый высокий уровень пользователя
    print(f"Самый высокий уровень: {highest_level}")
    # Раскомментируйте, чтобы создать таблицы, если их еще нет
    # execute_query(query_create_table_users)
    # execute_query(query_create_table_user_scores)
