import pygame
import psycopg2
import sys
import random

# ---------------- Дерекқорға қосылу ----------------
def connect_db():
    return psycopg2.connect(
        host="localhost",
        dbname="snake_game",
        user="postgres",
        password="Akbota1981@"
    )

# ---------------- Логин функциясы ----------------
def login():
    conn = connect_db()
    cur = conn.cursor()
    username = input("Өз атыңызды енгізіңіз: ")

    # Пайдаланушыны 'user' кестесінен тауып, оның ұпайы мен деңгейін аламыз
    cur.execute("""
        SELECT u.user_id, s.level, s.score 
        FROM "user" u
        LEFT JOIN user_score s ON u.user_id = s.user_id
        WHERE u.username = %s
    """, (username,))
    
    user = cur.fetchone()

    if user and user[1] is not None:
        print(f"Қош келдіңіз, {username}! Деңгейіңіз: {user[1]}, Ұпайыңыз: {user[2]}")
        return user[0], user[1], user[2]
    else:
        # Егер қолданушы жаңа болса — тіркейміз
        print("Жаңа қолданушы ретінде тіркелесіз.")
        cur.execute("INSERT INTO \"user\" (username) VALUES (%s) RETURNING user_id", (username,))
        user_id = cur.fetchone()[0]
        cur.execute("INSERT INTO user_score (user_id, level, score) VALUES (%s, %s, %s)", (user_id, 1, 0))
        conn.commit()
        return user_id, 1, 0

# ---------------- Ойын нәтижесін сақтау ----------------
def save_score(user_id, level, score):
    conn = connect_db()
    cur = conn.cursor()
    cur.execute("""
        UPDATE user_score SET level = %s, score = %s WHERE user_id = %s
    """, (level, score, user_id))
    conn.commit()

# ---------------- Pygame баптаулары ----------------
pygame.init()
WIDTH, HEIGHT = 600, 400
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

# Түстер
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# FPS және жылдамдық
clock = pygame.time.Clock()
speed = 15

# ---------------- Жылан логикасы ----------------
snake_block = 10
snake_list = []
length = 1

def draw_snake(snake_list):
    for block in snake_list:
        pygame.draw.rect(win, GREEN, [block[0], block[1], snake_block, snake_block])

# ---------------- Ойын ----------------
def game_loop(user_id, level, score):
    game_over = False
    x, y = WIDTH // 2, HEIGHT // 2
    dx, dy = 0, 0

    # Жеміс координаталары
    food_x = round(random.randrange(0, WIDTH - snake_block) / 10.0) * 10
    food_y = round(random.randrange(0, HEIGHT - snake_block) / 10.0) * 10

    global length
    length = 1
    snake_list.clear()

    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
                save_score(user_id, level, score)
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    dx = -snake_block
                    dy = 0
                elif event.key == pygame.K_RIGHT:
                    dx = snake_block
                    dy = 0
                elif event.key == pygame.K_UP:
                    dy = -snake_block
                    dx = 0
                elif event.key == pygame.K_DOWN:
                    dy = snake_block
                    dx = 0

        x += dx
        y += dy

        if x < 0 or x >= WIDTH or y < 0 or y >= HEIGHT:
            game_over = True
            break

        win.fill(WHITE)
        pygame.draw.rect(win, RED, [food_x, food_y, snake_block, snake_block])

        snake_head = [x, y]
        snake_list.append(snake_head)
        if len(snake_list) > length:
            del snake_list[0]

        for segment in snake_list[:-1]:
            if segment == snake_head:
                game_over = True
                break

        draw_snake(snake_list)
        pygame.display.update()

        # Жемісті жеген кезде
        if x == food_x and y == food_y:
            food_x = round(random.randrange(0, WIDTH - snake_block) / 10.0) * 10
            food_y = round(random.randrange(0, HEIGHT - snake_block) / 10.0) * 10
            length += 1
            score += 10
            if score % 50 == 0:
                level += 1
                global speed
                speed += 1

        clock.tick(speed)

    save_score(user_id, level, score)

# ---------------- Ойын басталады ----------------
if __name__ == "__main__":
    user_id, current_level, score = login()
    game_loop(user_id, current_level, score)
