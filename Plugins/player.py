import pygame,pathlib
class Player:
    def __init__(self):
        self.health=10
        #self.rect=pygame.Rect() 
        self.image=pygame.image.load(pathlib.Path('..','Images','Chronos.png'))