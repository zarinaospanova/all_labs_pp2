import pygame, random, time

pygame.init()

WIDTH = 400
HEIGHT = 600

COLOR_BLACK = (0, 0, 0)
COLOR_RED = (255, 0, 0)
COLOR_GREEN = (0, 255, 0)
COLOR_BLUE = (0, 0, 255)
SCORE = 0
ENEMY_SPEED = 5
LEVEL = 0

screen = pygame.display.set_mode((WIDTH, HEIGHT))

image_background = pygame.image.load('/Users/darinaospanova/Documents/pp2_all_labs/labs/lab9/racer/AnimatedStreet.png')
image_player = pygame.image.load('/Users/darinaospanova/Documents/pp2_all_labs/labs/lab9/racer/Player.png')
image_enemy = pygame.image.load('/Users/darinaospanova/Documents/pp2_all_labs/labs/lab9/racer/Enemy.png')

image_golden_coin = pygame.image.load('/Users/darinaospanova/Documents/pp2_all_labs/labs/lab9/racer/bronze.png')
image_silver_coin = pygame.image.load('/Users/darinaospanova/Documents/pp2_all_labs/labs/lab9/racer/silver.png')
image_bronze_coin = pygame.image.load('/Users/darinaospanova/Documents/pp2_all_labs/labs/lab9/racer/bronze.png')

scaled_image_golden_coin = pygame.transform.scale(image_golden_coin, (50, 50)) # scaling our coin
scaled_image_bronze_coin = pygame.transform.scale(image_bronze_coin, (30, 30))
scaled_image_silver_coin = pygame.transform.scale(image_silver_coin, (40, 40))

font = pygame.font.SysFont('Arial', 60) # getting the font
font_score = pygame.font.SysFont('Srial', 20)
font_small = pygame.font.SysFont('Arial', 20)
image_game_over = font.render('Game Over', True, COLOR_BLACK) # getting the text with our font
image_game_over_rect = image_game_over.get_rect(center = (WIDTH // 2, HEIGHT // 2)) # getting the rect object of our text

font_level = pygame.font.SysFont('Arial', 20)

pygame.mixer.music.load('/Users/darinaospanova/Documents/pp2_all_labs/labs/lab9/racer/background.wav')
pygame.mixer.music.play(-1) # -1 is for playing the music infinitely
sound_crash = pygame.mixer.Sound('/Users/darinaospanova/Documents/pp2_all_labs/labs/lab9/racer/crash.wav')

image_background_rect = image_background.get_rect()

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = image_player
        self.rect = self.image.get_rect()
        self.speed = 5
        self.rect.centerx = WIDTH // 2
        self.rect.top = HEIGHT - self.rect.h

    def move(self):
        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[pygame.K_RIGHT]:
            self.rect.move_ip(self.speed, 0)
        if pressed_keys[pygame.K_LEFT]:
            self.rect.move_ip(-self.speed, 0)
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = image_enemy
        self.rect = self.image.get_rect()
        self.speed = 10

    def generate_coord(self):
        self.rect.left = random.randint(0, WIDTH - self.rect.w)
        self.rect.bottom = 0

    def move(self):
        self.rect.move_ip(0, ENEMY_SPEED + LEVEL)
        if self.rect.top > HEIGHT: # if the top of the image is greater than the HEIGHT of the screen
            self.generate_coord()  # we generate the new random coord for our image to appear
                                   # at the top of the screen

class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.images = [scaled_image_golden_coin, scaled_image_silver_coin, scaled_image_bronze_coin]
        self.image = self.images[self.random_coin()]
        self.rect = self.image.get_rect()
        self.positions = [70, 140, 210]
        self.rect.top = 10
        self.speed = 5
        # self.random_pos() # setting the initial random position
        self.coin_index = 0

    def random_pos(self):
        global SCORE
        self.coin_index = self.random_coin() # setting the random index for our coin
        self.image = self.images[self.coin_index]
        self.rect = self.image.get_rect()
        self.rect.left = self.positions[random.randint(0, 2)]
        self.rect.top = 10

    def random_coin(self):
        return random.randint(0, 2)

    def move(self):
        self.rect.move_ip(0, self.speed)
        if self.rect.top > HEIGHT:
            self.random_pos()

player = Player()
enemy = Enemy()
coin = Coin()

all_sprites = pygame.sprite.Group() # grouping all sprites in one place
all_sprites.add(player, enemy, coin)
enemy_sprites = pygame.sprite.Group()
enemy_sprites.add(enemy)
coin_sprites = pygame.sprite.Group()
coin_sprites.add(coin)

clock = pygame.time.Clock()
FPS = 60

running = True
while running: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.blit(image_background, image_background_rect)
    scores = font_small.render(str(SCORE), True, COLOR_BLUE)
    screen.blit(scores, (WIDTH - 40, 10))
    image_font_level = font_level.render('Level: ' + str(LEVEL), True, COLOR_RED)
    screen.blit(image_font_level, (40, 10))
    
    for entity in all_sprites:
        entity.move()
        screen.blit(entity.image, entity.rect)

    if pygame.sprite.spritecollideany(player, enemy_sprites): # first parameter is the sprite that will be
                                                              # checked if it's collided with the group of sprites
                                                              # in the second parameters
        sound_crash.play()
        screen.fill(COLOR_RED)
        screen.blit(image_game_over, image_game_over_rect)
        image_total_score = font_score.render('Your Score: ' + str(SCORE), True, COLOR_GREEN)
        image_total_score_rect = image_total_score.get_rect()
        image_total_score_rect.center = (WIDTH // 2, HEIGHT // 2 + 100)
        screen.blit(image_total_score, image_total_score_rect) # showing the total score
        

        for entity in all_sprites: # entity.kill() effectively makes the sprite no longer be drawn or updated 
            entity.kill() # by those groups
        pygame.display.flip()
        time.sleep(5)
        running = False
    
    if pygame.sprite.spritecollideany(player, coin_sprites):
        if coin.coin_index == 0:
            SCORE += 15
        elif coin.coin_index == 1:
            SCORE += 10
        elif coin.coin_index == 2:
            SCORE += 5
        LEVEL = SCORE // 50 
        coin.random_pos() # repositioning the coin

    pygame.display.flip()
    clock.tick(FPS)