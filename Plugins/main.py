import pygame,sys
import player
pygame.init()
Player=player.Player()

window = pygame.display.set_mode((pygame.display.Info().current_w,pygame.display.Info().current_h))

#ПЕНИС

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()



