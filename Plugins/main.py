import pygame,sys
pygame.init()

window = pygame.display.set_mode((pygame.display.Info().current_w,pygame.display.Info().current_h))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()



