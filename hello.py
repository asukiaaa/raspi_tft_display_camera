import pygame, sys, os
from pygame.locals import *
os.environ["SDL_FBDEV"] = "/dev/fb1"

pygame.init()

# set up the window
screen = pygame.display.set_mode((160, 124), 0, 32)
screen.fill((255, 255, 255))

basicfont = pygame.font.SysFont(None, 18)
text = basicfont.render('Hello World!', True, (100, 200, 100))
textrect = text.get_rect()
textrect.centerx = screen.get_rect().centerx
textrect.centery = screen.get_rect().centery
screen.blit(text, textrect)

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
