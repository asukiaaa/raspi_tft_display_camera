import io, picamera, pygame, sys, os
from pygame.locals import *
os.environ["SDL_FBDEV"] = "/dev/fb1"

pygame.init()

# set up the window
screen = pygame.display.set_mode((160, 124), 0, 32)

# set up the colors
BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
RED   = (255,   0,   0)
GREEN = (  0, 255,   0)
BLUE  = (  0,   0, 255)

# draw on the surface object
screen.fill(BLACK)

basicfont = pygame.font.SysFont(None, 15)
text = basicfont.render('Hello World!', True, WHITE)
textrect = text.get_rect()
#textrect.centerx = screen.get_rect().centerx
textrect.left = screen.get_rect().centerx
textrect.centery = screen.get_rect().centery
screen.blit(text, textrect)

#width = 640
#height = 480
width = 480
height= 640
rgb_buffer = bytearray(width * height * 3)
camera = picamera.PiCamera()
camera.resolution = (width, height)
camera.rotation = 90
offset = 22

# run the game loop
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    stream = io.BytesIO()
    camera.capture(stream, format='rgb')
    stream.seek(0)
    stream.readinto(rgb_buffer)
    stream.close()
    img = pygame.image.frombuffer(rgb_buffer, (width, height), 'RGB')
    img = pygame.transform.scale(img, (int(img.get_width() * 80 / img.get_height()), 80))
    #img = pygame.transform.scale(img, (80, int(img.get_height() * 80 / img.get_width())))
    #img = pygame.transform.rotate(img, -90)

    screen.blit(img, (0, offset))
    pygame.display.update()
