import pygame


class Text:

    def __init__(self, x, y, text, color_text, chislo, color_background=None, levo=False, x_ri=None):
        self.x = x
        self.y = y
        self.text = text
        self.color_text = color_text
        self.color_background = color_background
        self.shrift = pygame.font.SysFont("arial", 34, True)
        self.chislo1 = chislo
        self.levo = levo
        self.x_ri = x_ri
        self.a = self.shrift.render(self.text + str(int(self.chislo1)), True, self.color_text, self.color_background)


    def draw(self, dis):
        if self.levo:
            self.x = self.x_ri - self.a.get_width()
        dis.blit(self.a, [self.x, self.y])

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

    @property
    def chislo(self):
        return self.chislo1

    @chislo.setter
    def chislo(self, new):
        self.a = self.shrift.render(self.text + str(int(new)), True, self.color_text, self.color_background)
        self.chislo1 = new


