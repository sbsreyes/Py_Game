# Simulacion del juego de flappy bird

import pygame

end = False

bg_color = (156, 156, 156)

pygame.init()

window = 700,500

clock = pygame.time.Clock()

screen = pygame.display.set_mode(window)

while not end:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            end = True


    screen.fill((155,155,155))
    pygame.display.update()
    clock.tick(60)
pygame.quit()
