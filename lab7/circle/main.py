import pygame
pygame.init()

width = 1000
height = 1000
screen = pygame.display.set_mode((width,height))

clock = pygame.time.Clock()
color_white = (255,255,255)
x_coord_circle = 100
y_coord_circle = 40
running = True
while running:
    screen.fill(color_white)
    my_circle = pygame.draw.circle(screen,'red',(x_coord_circle,y_coord_circle),25)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                y_coord_circle-=20
            if event.key == pygame.K_DOWN:
                y_coord_circle+=20
            if event.key == pygame.K_LEFT:
                x_coord_circle-=20
            if event.key == pygame.K_RIGHT:
                x_coord_circle+=20
            if x_coord_circle < 40:
                x_coord_circle = 40 # it can not be 0
            if y_coord_circle < 40:
                y_coord_circle = 40 # it can not be 0
            if x_coord_circle>960:
                x_coord_circle = 960
            if y_coord_circle>960:
                y_coord_circle = 960
    pygame.display.flip()
    clock.tick(60)