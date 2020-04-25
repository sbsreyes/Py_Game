# Simulacion del juego de flappy bird

import pygame

end = False

bg_color = (156, 156, 156)
player_color = (0,0,0)
obst_color = (0,155,0)

pygame.init()

window = 700,500

clock = pygame.time.Clock()

screen = pygame.display.set_mode(window)

x = 350
y = 250
y_vel = 0
border = 480

xloc = 500
yloc = 0
xtam = 70
ytam = 70

vel_obst = 2.5

def player(x, y):
    pygame.draw.circle(screen, player_color, [x, y], 20)

def obst(xloc, yloc, xtam, ytam):
    pygame.draw.rect(screen, obst_color, [xloc, yloc, xtam, ytam])

def gameover():
    template = pygame.font.SysFont(None, 25)
    text = template.render('Game Over', True, player_color)
    screen.blit(text, [300,250])

while not end:
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            end = True

    if event.type == pygame.KEYDOWN:

        if event.key == pygame.K_UP:
            y_vel = -15

    if event.type == pygame.KEYUP:
        if event.key == pygame.K_UP:
            y_vel = 5

    screen.fill(bg_color)
    player(x, y)
    obst(xloc, yloc, xtam, ytam)

    y = y + y_vel
    xloc = xloc - vel_obst

    if xloc < -70:
        xloc = 600

    if y > border:
        gameover()
        y_vel = 0



    pygame.display.update()
    clock.tick(60)
pygame.quit()
