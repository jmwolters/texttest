import pygame
from pygame.locals import *

pygame.init()
width, height = 850, 720
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()

def message(text,color):
    font = pygame.font.Font("C:\Windows\Fonts\Calibri.ttf",30)
    message = font.render(text,1,color)
    screen.blit(message,(width/2,height/2))

while True:
    clock.tick(60)
    message("Test",(255,0,0))
