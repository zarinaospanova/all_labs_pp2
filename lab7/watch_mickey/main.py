import pygame 
from datetime import datetime

pygame.init()

width = 1000
height = 1000
COLOR_WHITE = (255,255,255)
screen = pygame.display.set_mode((width,height))
pygame.display.set_caption('Clock Mickey')

mickeys_body = pygame.image.load('labs/lab7/watch_mickey/images/clock.png').convert_alpha()
mickeys_right_hand = pygame.image.load('labs/lab7/watch_mickey/images/rightarm.png').convert_alpha()
mickeys_left_hand = pygame.image.load('labs/lab7/watch_mickey/images/leftarm.png').convert_alpha()

mickeys_body_rect = mickeys_body.get_rect(center = (width//2,height//2))
# mickey_icon = pygame.image.load('images/mickeyclock.jpeg')

# ANGLES 
min_angle = 0
sec_angle = 0

# MAIN BODY
clock = pygame.time.Clock()
running = True
while running:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        # Update time
        now = datetime.now()
        minutes = now.minute
        seconds = now.second


        screen.fill(COLOR_WHITE)
        min_angle = minutes * 6 + seconds * 0.1 # 0.1 degrees per second
        sec_angle = seconds * 6 # 6 degrees per sec

        # MINUTE 
        rotated_mickeys_right_hand = pygame.transform.rotate(mickeys_right_hand, -min_angle-45) # 
        rotated_mickeys_right_hand_rect = rotated_mickeys_right_hand.get_rect(center = (width//2,height//2))

        # SECOND 
        rotated_mickeys_left_hand = pygame.transform.rotate(mickeys_left_hand,-sec_angle - 45)
        rotated_mickeys_left_hand_rect = rotated_mickeys_left_hand.get_rect(center = (width//2,height//2))

        screen.blit(mickeys_body,mickeys_body_rect)
        screen.blit(rotated_mickeys_right_hand,rotated_mickeys_right_hand_rect)
        screen.blit(rotated_mickeys_left_hand,rotated_mickeys_left_hand_rect)

        pygame.display.flip()
        clock.tick(60)