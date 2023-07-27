import pygame

class Text:

    def __init__(self, x, y, text, color_text, chislo, color_background = None, levo = False):
        self.x = x
        self.y = y
        self.text = text
        self.color_text = color_text
        self.color_background = color_background
        self.shrift = pygame.font.SysFont("arial", 34, True)
        self.chislo = chislo
        self.levo = levo

    def draw(self, dis):
        a = self.shrift.render(self.text + str(int(self.chislo)), True, self.color_text, self.color_background)
        if self.levo and self.x + a.get_width() >= 580:
            self.x = 580 - (a.get_width() + 6)
        dis.blit(a, [self.x, self.y])