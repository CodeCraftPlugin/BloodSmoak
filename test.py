import pygame
x= pygame.init()
from pygame import image,display,font,event
print(x)
screen = display.set_mode((600,600))
display.set_caption("Test")
a = image.load(filename=Ak47.png)
a.blit(screen,(300,600))
####GameLooop
while True:
    display.flip()

