import pygame
from fighter import Fighter

pygame.init()

info = pygame.display.Info()
SCREEN_WIDTH = info.current_w
SCREEN_HEIGHT = info.current_h
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.FULLSCREEN)

pygame.display.set_caption("Fener Arena")

#set framerate
clock = pygame.time.Clock()
FPS = 60

#RENKLER
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)

#load backgorund image
bg_image = pygame.image.load("assets/images/background/saracoglu_arkaplan.jpg").convert_alpha()

# ARKAPLAN ÇİZME / DRAW BACKGROUND
def draw_bg():
    scaled_bg = pygame.transform.scale(bg_image, (SCREEN_WIDTH, SCREEN_HEIGHT))
    screen.blit(scaled_bg, (0,0))

# SAĞLIK BARI ÇİZME
def draw_health_bar(health, x ,y):
    ratio = health / 100
    pygame.draw.rect(screen, WHITE, (x - 1, y - 1, 404, 34))
    pygame.draw.rect(screen, RED, (x, y, 400, 30))
    pygame.draw.rect(screen, YELLOW, (x, y, 400 * ratio, 30))

#create two instances of fighters
fighter_1 = Fighter(SCREEN_WIDTH * 0.2, SCREEN_HEIGHT * 0.52, SCREEN_WIDTH, SCREEN_HEIGHT)
fighter_2 = Fighter(SCREEN_WIDTH * 0.7, SCREEN_HEIGHT * 0.52, SCREEN_WIDTH, SCREEN_HEIGHT)




#------------- OYUN DÖNGÜSÜ -------------

run = True
while run:

    clock.tick(FPS)
    #draw bg
    draw_bg()

    #SHOW PLAYER STATS
    draw_health_bar(fighter_1.health, SCREEN_WIDTH * 0.02, SCREEN_HEIGHT * 0.03)
    draw_health_bar(fighter_2.health, SCREEN_WIDTH * 0.58, SCREEN_HEIGHT * 0.03)
 
    #karakterleri hareket ettir
    fighter_1.move(SCREEN_WIDTH, SCREEN_HEIGHT, screen, fighter_2)
    #fighter_2.move(SCREEN_WIDTH, SCREEN_HEIGHT, screen, fighter_1)

    #draw fighters
    fighter_1.draw(screen)
    fighter_2.draw(screen)

    #event handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False


    #update display
    pygame.display.update()

#exit pygame
pygame.quit()