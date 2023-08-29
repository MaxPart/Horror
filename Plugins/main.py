import pygame,sys
import player
pygame.init()
Player=player.Player()

width_base=pygame.display.Info().current_w
height_base=pygame.display.Info().current_h

window = pygame.display.set_mode((width_base,height_base))
window.fill((32,0,56))

r=pygame.Rect(100,100,int(width_base)-200,int(height_base)-200)
pygame.draw.rect(window,(50,0,87),r,0)

font = pygame.font.SysFont('comic_sans', 100, bold=True)
text = font.render(str(f"HorrorTubbies"), True, 'green')
window.blit(text,(int(width_base//2-400),int(height_base//2-300)))

font = pygame.font.SysFont('comic_sans', 40, bold=True)
text = font.render(str(f" Vers:0.1"), True, 'yellow')
window.blit(text,(int(width_base//350-2),int(height_base//200-2)))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.flip()



