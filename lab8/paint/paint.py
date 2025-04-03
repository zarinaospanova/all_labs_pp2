import pygame 
pygame.init()

# screen/surface
x = 800
y = 800
screen = pygame.display.set_mode((x,y))
clock = pygame.time.Clock()
screen.fill("white")

# color selection
C_BLACK = (0,0,0)
C_WHITE = (255,255,255)
C_RED = (255,0,0)
C_GREEN = (0,255,0)
C_BLUE = (0,0,255)

C_CURRENT = C_RED
radius = 5 # radius of line

drawing = False
last_pos = None 
shape_mode = "line" 

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            drawing = True
            last_pos = event.pos
        if event.type == pygame.MOUSEBUTTONUP:
            drawing = False
            last_pos = None

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                C_CURRENT = C_BLUE
            if event.key == pygame.K_2:
                C_CURRENT = C_BLACK
            if event.key == pygame.K_3:
                C_CURRENT = C_RED
            if event.key == pygame.K_0:
                C_CURRENT = C_WHITE
            if event.key == pygame.K_4:
                C_CURRENT = C_GREEN
            if event.key == pygame.K_r:
                shape_mode = "rectangle"
            if event.key == pygame.K_c:
                shape_mode = "circle"
            if event.key == pygame.K_l:
                shape_mode = "line"
    if drawing:
        mouse_pos = pygame.mouse.get_pos()
        if shape_mode == "rectangle" and last_pos:
                mouse_pos = pygame.mouse.get_pos()
                center = last_pos
                x, y = min(last_pos[0], mouse_pos[0]), min(last_pos[1], mouse_pos[1])
                width, height = abs(last_pos[0] - mouse_pos[0]), abs(last_pos[1] - mouse_pos[1])
                pygame.draw.rect(screen, C_CURRENT, (x, y, width, height), radius)

        if shape_mode == "circle" and last_pos:
                mouse_pos = pygame.mouse.get_pos()
                center = last_pos
                radius_circle = int(((mouse_pos[0] - center[0]) ** 2 + (mouse_pos[1] - center[1]) ** 2) ** 0.5)
                pygame.draw.circle(screen, C_CURRENT, center, radius_circle, radius)

        if shape_mode == "line" and last_pos:
                mouse_pos = pygame.mouse.get_pos()
                if last_pos:
                    pygame.draw.line(screen,C_CURRENT,last_pos,mouse_pos,radius)
                    last_pos = mouse_pos
    pygame.display.update()
    clock.tick(120)
pygame.quit()