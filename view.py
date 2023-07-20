import pygame

import model

pygame.init()

dis = pygame.display.set_mode([1300, 850])


def mainview():
    mesto1 = pygame.image.load("sprites/place/place1.jpg")
    mesto1_1 = pygame.transform.scale(mesto1, [1300, 850])
    dis.blit(mesto1_1, [0, 0])
    mainwork1 = pygame.image.load("sprites/worker/worker1.png")
    mainwork1_1 = pygame.transform.scale(mainwork1, [614/2, 714/2])
    dis.blit(mainwork1_1, [20, 485])
    text()
    pygame.display.flip()


def text():
    text_shrift = pygame.font.SysFont("arial", 34, True)
    text_shrift1 = text_shrift.render("Ваши деньги: "+str(model.money), True, "#4A310A")
    dis.blit(text_shrift1, [560, 0])
