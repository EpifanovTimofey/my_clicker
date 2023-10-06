import pygame
import pictures, knopka, text


class Worker:

    def __init__(self, picture, coord, size, picture_inv, money_buy, bonus, pass_money, money):
        self.coord = coord
        self.size = size
        self.picture = picture
        self.money = money
        self.money_buy_plus = 1.02
        self.money_buy_plus_plus = 0.02283
        self.worker_picture = pictures.Picture(picture_inv, self.size, self.coord)

        self.knopka = knopka.Knopka("sprites/controls/up_green.png", 38, 38, self.coord[0] + self.size[0] / 1.5,
                                    self.coord[1] + 100, self.level_up)

        self.text_lvl = text.Text(coord[0], coord[1] - 84, "ЛВЛ: ", "#168FFF", 0, "#FEFF55")
        self.text_clock = text.Text(coord[0], coord[1] - 126, "+", "#3227FF", pass_money, "#FFDC3A", text2=" в сек.")
        self.text_bonus = text.Text(coord[0], coord[1] - 168, "Бонус: ", "#168FFF", bonus, "#FEFF55", text2="%")
        self.text_buy = text.Text(coord[0], coord[1] - 42, "Цена: ", "#4A310A", money_buy, "#FFEB87")

        self.spisok_draw = [self.worker_picture, self.knopka, self.text_buy, self.text_clock, self.text_bonus,
                            self.text_lvl]

    def draw(self, dis):
        for s in self.spisok_draw:
            s.draw(dis)

    def level_up(self):
        if self.money.chislo >= self.text_buy.chislo:
            self.text_lvl.chislo += 1

            self.money.chislo -= self.text_buy.chislo
            self.text_buy.chislo *= self.money_buy_plus
            self.money_buy_plus += self.money_buy_plus_plus

            self.spisok_draw.remove(self.worker_picture)
            self.worker_picture = pictures.Picture(self.picture, self.size, self.coord)
            self.spisok_draw.append(self.worker_picture)
