import pygame
from pygame.locals import *

#intializing
pygame.init()
width, height = 850, 720
screen = pygame.display.set_mode((width, height))
letter = 0
word = []
doodles = ["ladder", "bus", "man", "woman"]
clock = pygame.time.Clock()

#images
ladder = pygame.image.load("doodles/ladder.png")

#transform
ladder = pygame.transform.scale(ladder,(194,138))

#textbox
def message(text,color,xpos):
    font = pygame.font.Font("C:\Windows\Fonts\Impact.ttf",30)
    message = font.render(text,False,color)

    screen.blit(message,(xpos,height/2))

while True:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                if w in doodles:
                    word = []
                    doodle(w)

                else:
                    print("No word %s found" %w)
                    word = []

            elif event.key == pygame.K_BACKSPACE:
                if letter - 1 > 0:
                    word.pop(letter-1)
                    letter -= 1
                else:
                    word = []
                    letter = 0

            else:
                word.append(event.unicode)
                letter += 1

    w = ''.join(word)
    w = w.lower()
    message(w,(255,255,255),width/2)
    pygame.display.flip()
    screen.fill(0)
