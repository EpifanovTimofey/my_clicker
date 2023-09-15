import pygame, pictures

import model

dis = pygame.display.set_mode([1300, 850])
place = pictures.Picture("sprites/place/place1.jpg", [1300, 850], [0, 0])
worker_main = pictures.Picture("sprites/worker/worker1.png", [307, 357], [20, 480])
plus = pictures.Picture("sprites/controls/plus.png", [38, 38], [580, 88])
coin = pictures.Picture("sprites/controls/coin.png", [38, 38], [580, 0])
yellow_knopka = pictures.Picture("sprites/controls/up_yellow.png", [38, 38], [model.r1.x, model.r1.y])
green_knopka = pictures.Picture("sprites/controls/up_green.png", [38, 38], [610, 380])
clock = pictures.Picture("sprites/controls/clock.png", [38, 38], [580, 132])
obvodka_worker1 = pictures.Picture("sprites/worker/worker2_inv.png", [730/2.5, 1330/2.5], [400,830-1330/2.5])
pygame.init()

spisok_pictures = [place, worker_main, plus, coin, yellow_knopka, clock, obvodka_worker1, green_knopka]

def mainview():
    for p in spisok_pictures:
        p.draw(dis)
    text1()
    pygame.display.flip()


def text1():
    for s in model.spisok_text:
        s.draw(dis)
