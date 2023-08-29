import pygame,sys
import player
pygame.init()
Player=player.Player()

window = pygame.display.set_mode((pygame.display.Info().current_w,pygame.display.Info().current_h))

r=pygame.Rect(100,100,900,900)
pygame.draw.rect(window,(135,0,178),r,0)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.flip()



