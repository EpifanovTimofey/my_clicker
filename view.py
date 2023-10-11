import pygame, pictures

import model

dis = pygame.display.set_mode([1300, 850])
place = pictures.Picture("sprites/place/place1.jpg", [1300, 850], [0, 0])
worker_main = pictures.Picture("sprites/worker/worker1.png", [307, 357], [20, 480])
plus = pictures.Picture("sprites/controls/plus.png", [38, 38], [580, 88])
coin = pictures.Picture("sprites/controls/coin.png", [38, 38], [580, 0])
clock = pictures.Picture("sprites/controls/clock.png", [38, 38], [580, 132])
obvodka_worker2 = pictures.Picture("sprites/worker/worker2_inv.png", [730 / 2.5, 1330 / 2.5], [400, 830 - 1330 / 2.5])
worker2 = pictures.Picture("sprites/worker/worker2.png", [730 / 2.5, 1330 / 2.5], [400, 830 - 1330 / 2.5])
pygame.init()

spisok_pictures = [place, worker_main, plus, coin, model.yellow_knopka, clock, model.worker3, model.worker2]


def main_view():
    for p in spisok_pictures:
        p.draw(dis)
    text1()
    pygame.display.flip()


def text1():
    for s in model.spisok_text:
        s.draw(dis)

