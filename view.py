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
    text1()
    knopka()
    pygame.display.flip()


def text1():
    model.t1.draw(dis)
    model.t2.draw(dis)


# def text1():
#     text_shrift1 = text_shrift.render("Ваши деньги: "+str(int(model.money)), True, "#4A310A")
#     dis.blit(text_shrift1, [600, 0])
#     text_shrift1 = text_shrift.render("Цена апгрейда: "+str(int(model.prokachka)), True, "#FFC122")
#     dis.blit(text_shrift1, [644, 42])


def knopka():
    prokachka1 = pygame.image.load("sprites/controls/up_yellow.png")
    prokachka1_1 = pygame.transform.scale(prokachka1, [38, 38])
    dis.blit(prokachka1_1, [600, 44])
