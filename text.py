import pygame


class Text:

    def __init__(self, x, y, text, color_text, chislo, color_background=None, levo=False, x_ri=None):
        self.x = x
        self.y = y
        self.text = text
        self.color_text = color_text
        self.color_background = color_background
        self.shrift = pygame.font.SysFont("arial", 34, True)
        self.chislo = chislo
        self.levo = levo
        self.x_ri = x_ri
        self.a = self.shrift.render(self.text + str(int(self.chislo)), True, self.color_text, self.color_background)

    def draw(self, dis):
        if self.levo:
            self.x = self.x_ri - self.a.get_width()
        dis.blit(self.a, [self.x, self.y])

    def new_chislo(self, chislo):
        self.a = self.shrift.render(self.text + str(int(chislo)), True, self.color_text, self.color_background)
        self.chislo = chislo

    @property
    def cvet(self):
        if self.color_text == [255, 0, 0]:
            return "red"
        if self.color_text == [0, 255, 0]:
            return "green"
        else:
            return "error"

    @cvet.setter
    def cvet(self, new):
        if new == "red":
            self.color_text = [255, 0, 0]
        if new == "green":
            self.color_text = [0, 255, 0]
        else:
            print("error")

