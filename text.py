import pygame

class Text:

    def __init__(self, x, y, text, color, chislo):
        self.x = x
        self.y = y
        self.text = text
        self.color = color
        self.shrift = pygame.font.SysFont("arial", 34, True)
        self.chislo = chislo

    def draw(self, dis):
        a = self.shrift.render(self.text + str(int(self.chislo)), True, self.color)
        dis.blit(a, [self.x, self.y])