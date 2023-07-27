import pygame, text

import model

pygame.init()

dis = pygame.display.set_mode([1300, 850])


def mainview():
    mesto1 = pygame.image.load("sprites/place/place1.jpg")
    mesto1_1 = pygame.transform.scale(mesto1, [1300, 850])
    dis.blit(mesto1_1, [0, 0])
    mainwork1 = pygame.image.load("sprites/worker/worker1.png")
    mainwork1_1 = pygame.transform.scale(mainwork1, [614 / 2, 714 / 2])
    dis.blit(mainwork1_1, [20, 485])
    plus1 = pygame.image.load("sprites/controls/plus.png")
    plus1_1 = pygame.transform.scale(plus1, [38, 38])
    dis.blit(plus1_1, [580, 88])
    moneta1 = pygame.image.load("sprites/controls/coin.png")
    moneta1_1 = pygame.transform.scale(moneta1, [38, 38])
    dis.blit(moneta1_1, [580, 0])
    text1()
    knopka()
    pygame.display.flip()


def text1():
    for s in model.spisok_text:
        s.draw(dis)


def knopka():
    prokachka1 = pygame.image.load("sprites/controls/up_yellow.png")
    prokachka1_1 = pygame.transform.scale(prokachka1, [38, 38])
    dis.blit(prokachka1_1, [580, 44])
