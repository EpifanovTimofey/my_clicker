import pygame, text

import model

pygame.init()

def mainview():
    dis.blit(kartinki_slovar["place1"], [0, 0])
    # pictures("sprites/place/place1.jpg", 1300, 850, 0, 0)
    # pictures("sprites/worker/worker1.png", 307, 357, 20, 480)
    # pictures("sprites/controls/plus.png", 38, 38, 580, 88)
    # pictures("sprites/controls/coin.png", 38, 38, 580, 0)
    # pictures("sprites/controls/up_yellow.png", 38, 38, model.r1.x, model.r1.y)
    text1()
    pygame.display.flip()


def text1():
    for s in model.spisok_text:
        s.draw(dis)


def pictures(kartinka, r1, r2, name):
    a = pygame.image.load(kartinka)
    b = pygame.transform.scale(a, [r1, r2])
    kartinki_slovar[name] = b


dis = pygame.display.set_mode([1300, 850])
kartinki_slovar = {}
pictures("sprites/place/place1.jpg", 1300, 850, "place1")