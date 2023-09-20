import pygame, pictures


class Knopka:

    def __init__(self, picture, r1, r2, x, y, action):
        self.a = pictures.Picture(picture, [r1, r2], [x, y])
        self.x = x
        self.y = y
        self.r1 = r1
        self.r2 = r2
        self.rect = pygame.Rect(self.x, self.y, self.r1, self.r2)
        self.action = action

    def draw(self, dis: pygame.Surface):
        self.a.draw(dis)

    def events(self, spisok):
        for f in spisok:
            if f.type == pygame.MOUSEBUTTONDOWN and f.button == pygame.BUTTON_LEFT and self.rect.collidepoint(f.pos):
                self.action()
                spisok.remove(f)
