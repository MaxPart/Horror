import pygame,sys
pygame.init()

window = pygame.display.set_mode((1960,1080))
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
