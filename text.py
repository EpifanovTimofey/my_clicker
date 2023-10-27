import pygame


class Text:

    def __init__(self, x, y, text, color_text, chislo, color_background=None, levo=False, x_ri=None, text2=""):
        self.x = x
        self.y = y
        self.text = text
        self.text2 = text2
        self.color_text = color_text
        self.color_background = color_background
        self.shrift = pygame.font.SysFont("arial", 34, True)
        self.chislo1 = chislo
        self.levo = levo
        self.x_ri = x_ri
        self._draw_()

    def _draw_(self):
        self.a = self.shrift.render(self.text + str(int(self.chislo1)) + self.text2, True, self.color_text,
                                    self.color_background)
        stroka = ""
        chisla = ""
        o = int(self.chislo1)
        o = str(o)
        g = 0
        spisok_simvol = []
        spisok_bukv = ["K", "M", "ML", "T", "KV", "?"]
        l = len(o) % 3
        if l != 0:
            o = " " * (3 - l) + o
        for s in o:
            chisla += s
            g += 1
            if g == 3:
                g = 0
                spisok_simvol.append(chisla)
                chisla = ""
        print(self.chislo1)
        print(spisok_simvol)
        a = len(spisok_simvol)
        for s in spisok_simvol:
            if a == 1:
                stroka += s.lstrip("0")
                break
            if int(s) == 0:
                a -= 1
                continue
            stroka += s.lstrip("0") + spisok_bukv[a-2] + " "
            a -= 1
        stroka = stroka.strip(" ")
        self.a = self.shrift.render(self.text + stroka + self.text2, True, self.color_text,
                                    self.color_background)
        # if self.chislo1 >= 1000000:
        #     l = int(self.chislo1 // 1000000)
        #     l1 = int(self.chislo1 % 1000000)
        #     l1 = str(l1)
        #     if l1 == "0":
        #         l1 = ""
        #     stroka = str(l) + "M "
        #     mln_str = stroka
        #     o = 0
        #     if l1 != "":
        #         o = l1
        # if int(o) >= 1000:
        #     l1 = int(int(o) // 1000)
        #     l2 = int(int(o) % 1000)
        #     l2 = str(l2)
        #     if l2 == "0":
        #         l2 = ""
        #     stroka = str(l1) + "K " + str(l2)
        #     if self.chislo1 >= 1000000:
        #         stroka = mln_str + str(l1) + "K " + str(l2)
        #
        # if self.chislo1 < 1000:
        #     stroka = str(int(self.chislo1))

    def draw(self, dis):
        if self.levo:
            self.x = self.x_ri - self.a.get_width()
        dis.blit(self.a, [self.x, self.y])

    @property
    def chislo(self):
        return self.chislo1

    @chislo.setter
    def chislo(self, new):
        self.chislo1 = new
        self._draw_()
