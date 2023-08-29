import pygame,sys
import player,pathlib
pygame.init()
Player=player.Player()
pygame.display.set_caption("HorrorTubbies")
icon = pygame.image.load('Images/icon.png')

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

start_img=pygame.image.load(pathlib.Path('..','Images','start_btt.png')).convert_alpha()

class Button:
    def __init__(self,x,y,image,scale):
        width=image.get_width()
        height=image.get_height()
        x=x-130*scale
        y=y-50*scale
        self.image=pygame.transform.scale(image,(int(width*scale),int(height*scale)))
        self.rect=self.image.get_rect()
        self.rect.topleft = (x,y)
        self.clicked=False
    def draw(self):
        action=False
        pos=pygame.mouse.get_pos()
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0]==1 and self.clicked==False:
                self.clicked=True
                action=True
        if pygame.mouse.get_pressed()[0]==0:
            self.clicked=False
        window.blit(self.image, (self.rect.x,self.rect.y))
        return action

start_btt=Button(width_base//2,height_base//2,start_img,2)

while True:
    if start_btt.draw():
        print('Start')
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
    pygame.display.flip()



