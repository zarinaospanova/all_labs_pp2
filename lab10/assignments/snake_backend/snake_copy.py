import pygame, random, time, sqlite3

pygame.init()

# Constants for screen size and colors
HEIGHT = 720
WIDTH = 720
COLOR_GRAY = (128, 128, 128)
COLOR_BLACK = (0, 0, 0)
COLOR_WHITE = (255, 255, 255)
COLOR_RED = (255, 0, 0)
COLOR_GREEN = (0, 255, 0)
COLOR_LIGHTBLUE = (144, 255, 255)
COLOR_BLUE = (0, 0, 255)
COLOR_PURPLE = (128, 0, 128)
COLOR_YELLOW = (255, 255, 0)

# Initialize the clock and set the FPS
clock = pygame.time.Clock()
FPS = 5

# Global variables to keep track of the score and level
count_food = 0
count_level = 1

# Index for random colors
color_index = 1 
color_random = COLOR_BLUE

# Initialize the game screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Fonts for text rendering
font = pygame.font.SysFont('Arial', 30)
font_endgame = pygame.font.SysFont('Arial', 80)

# Sound effect for eating food
sound_food = pygame.mixer.Sound('/Users/darinaospanova/Documents/pp2_all_labs/labs/lab9/snake/food_eating.wav')

# Define the size of each cell in the grid
CELL = 30

# Function to draw the chessboard background
def draw_chess_board():
    colors = [COLOR_GRAY, COLOR_WHITE]
    for i in range(HEIGHT // CELL):
        for j in range(WIDTH // CELL):
            pygame.draw.rect(screen, colors[(i + j) % 2], (i * CELL, j * CELL, CELL, CELL))

# Point class to represent coordinates of segments in the snake and food
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

# Snake class to handle the snake's behavior
class Snake:
    def __init__(self):
        self.body = [Point(3, 10), Point(4, 10), Point(5, 10)]  # Initial snake body
        self.dx = 1  # Horizontal movement
        self.dy = 0  # Vertical movement 

    # Method to move the snake
    def move(self):
        for i in range(len(self.body) - 1, 0, -1):
            self.body[i].x = self.body[i - 1].x
            self.body[i].y = self.body[i - 1].y
        self.body[0].x += self.dx
        self.body[0].y += self.dy

    # Method to draw the snake on the screen
    def draw_snake(self):
        head = self.body[0]
        pygame.draw.rect(screen, COLOR_RED, (head.x * CELL, head.y * CELL, CELL, CELL))  # Draw head
        for segment in self.body[1:]:
            pygame.draw.rect(screen, COLOR_GREEN, (segment.x * CELL, segment.y * CELL, CELL, CELL))  # Draw body

    # Check if the snake collides with the food
    def check_collision(self, food):
        global FPS, count_food, count_level
        head = self.body[0]
        if head.x == food.pos.x and head.y == food.pos.y:
            self.body.append(Point(head.x, head.y))  # Add a new segment to the snake
            food.generate_random_pos()  # Generate new food position
            if color_index == 0:
                count_food += 3
            elif color_index == 1:
                count_food += 2
            elif color_index == 2:
                count_food += 1
            sound_food.play()  # Play food eating sound
            if count_food % 5 == 0:
                count_level += 1  # Increase level every 5 food items eaten
                FPS += 2  # Increase game speed

    # Check if the snake collides with the wall
    def check_collision_wall(self):
        head = self.body[0]
        if head.x > WIDTH // CELL - 1 or head.x < 0 or head.y < 0 or head.y > HEIGHT // CELL - 1:
            return True
        return False

# Food class to handle food's behavior
class Food:
    def __init__(self):
        self.pos = Point(10, 10)  # Initial food position
        self.food_colors = [COLOR_PURPLE, COLOR_BLUE, COLOR_LIGHTBLUE]  # Available food colors
        self.creation_time = time.time()  # Time when food was created
        self.food_lifetime = 5  # Food lifetime in seconds

    # Generate a new random position for the food
    def generate_random_pos(self):
        temp_x = random.randint(0, WIDTH // CELL - 1)
        temp_y = random.randint(0, HEIGHT // CELL - 1)
        
        if all((segment.x != temp_x or segment.y != temp_y) for segment in snake.body):  # Avoid food spawning on the snake
            self.pos.x = temp_x
            self.pos.y = temp_y
            self.creation_time = time.time()  # Update food creation time
        else:
            self.generate_random_pos()  # Recurse to generate new position if it collides with the snake

    # Draw the food on the screen
    def draw_food(self):
        pygame.draw.rect(screen, color_random, (self.pos.x * CELL, self.pos.y * CELL, CELL, CELL))

    # Generate a random color for the food
    def generate_random_color(self):
        global color_index, color_random
        color_index = random.randint(0, 2)
        color_random = self.food_colors[color_index]

    # Check if the food's lifetime has expired
    def check_food_lifetime(self):
        if time.time() - self.creation_time > self.food_lifetime:
            return True
        return False

# Initialize snake and food objects
food = Food()
snake = Snake()

# Connect to SQLite database (create if not exists)
conn = sqlite3.connect('snake_game.db')
cursor = conn.cursor()

# Create table if not exists to store the score and level
cursor.execute('''CREATE TABLE IF NOT EXISTS game_data (
                    id INTEGER PRIMARY KEY,
                    score INTEGER,
                    level INTEGER)''')
conn.commit()

# Function to save the score and level to the database
def save_game_data(score, level):
    cursor.execute('INSERT INTO game_data (score, level) VALUES (?, ?)', (score, level))
    conn.commit()

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False  # Exit the game
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT and snake.dx != -1:
                snake.dx = 1
                snake.dy = 0
            if event.key == pygame.K_LEFT and snake.dx != 1:
                snake.dx = -1
                snake.dy = 0
            if event.key == pygame.K_DOWN and snake.dy != -1:
                snake.dx = 0
                snake.dy = 1
            if event.key == pygame.K_UP and snake.dy != 1:
                snake.dx = 0
                snake.dy = -1

    # Check if snake collides with the wall
    if snake.check_collision_wall():
        running = False
        screen.fill(COLOR_GREEN)  # Fill the screen with green (end screen)

        # Display final score and level
        image_endgame_score = font_endgame.render("Total Score: " + str(count_food), True, COLOR_BLACK)
        image_endgame_score_rect = image_endgame_score.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 50))
        image_endgame_level = font_endgame.render("Level: " + str(count_level), True, COLOR_BLACK)
        image_endgame_level_rect = image_endgame_level.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 50))

        # Blit the text on the screen
        screen.blit(image_endgame_score, image_endgame_score_rect)
        screen.blit(image_endgame_level, image_endgame_level_rect)    

        # Save the game data (score and level)
        save_game_data(count_food, count_level)

        pygame.display.flip()

        time.sleep(5)  # Wait for 5 seconds before quitting the game

    screen.fill(COLOR_BLACK)  # Fill the screen with black for the new frame
    draw_chess_board()  # Draw the chessboard background

    # Move the snake and check for collisions
    snake.move()
    snake.check_collision(food)

    # Check if the food has expired, regenerate if so
    if food.check_food_lifetime():
        food.generate_random_color()
        food.generate_random_pos()

    # Draw food and snake
    food.draw_food()
    snake.draw_snake()

    # Render and display score and level on the screen
    score_text = font.render(f"Score: {count_food}", True, COLOR_BLUE)
    level_text = font.render(f'Level: {count_level}', True, COLOR_RED)
    screen.blit(score_text, (10, 10))
    screen.blit(level_text, (600, 10))

    pygame.display.flip()  # Update the screen with new drawings
    clock.tick(FPS)  # Control the game speed (frame rate)

# Close the database connection
conn.close()

pygame.quit()  # Quit Pygame
