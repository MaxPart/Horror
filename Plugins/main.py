import pygame,sys
import player
pygame.init()
Player=player.Player()

width_base=pygame.display.Info().current_w
height_base=pygame.display.Info().current_h

window = pygame.display.set_mode((width_base,height_base))
window.fill((105,0,158))

r=pygame.Rect(100,100,int(width_base)-200,int(height_base)-200)
pygame.draw.rect(window,(135,0,178),r,0)

font = pygame.font.SysFont('Bahnschrift', 80, bold=True)
text = font.render(str(f"MaxPart's game"), True, 'green')
window.blit(text,(int(width_base//2-350),int(height_base//2-200)))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.flip()



