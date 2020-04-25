# Simulacion del juego de flappy bird

import pygame

end = False

bg_color = (156, 156, 156)
player_color = (0,0,0)
pygame.init()

window = 700,500

clock = pygame.time.Clock()

screen = pygame.display.set_mode(window)

x = 350
y = 250
y_vel = 0

def player(x, y):
    pygame.draw.circle(screen, player_color, [x, y], 20)

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
    y = y + y_vel
    pygame.display.update()
    clock.tick(60)
pygame.quit()
