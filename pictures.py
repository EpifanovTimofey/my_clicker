import pygame


class Picture:

    def __init__(self, picture, size, coord):
        self.picture = picture
        self.size = size
        self.coord = coord
        a = pygame.image.load(self.picture)
        self.a = pygame.transform.scale(a, self.size)

    def draw(self, dis: pygame.Surface):
        dis.blit(self.a, self.coord)

