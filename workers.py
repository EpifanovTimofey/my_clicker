import pygame
import pictures, knopka


class Worker:

    def __init__(self, picture, coord, size, picture_inv):
        self.coord = coord
        self.size = size
        self.picture = picture
        self.a = pictures.Picture(picture_inv, self.size, self.coord)
        self.knopka = knopka.Knopka("sprites/controls/up_green.png", 38, 38, self.coord[0] + self.size[0] / 1.5, self.coord[1] + 100, self.razmorozka)

    def draw(self, dis):
        self.a.draw(dis)
        self.knopka.draw(dis)

    def razmorozka(self):
        self.a = pictures.Picture(self.picture, self.size, self.coord)