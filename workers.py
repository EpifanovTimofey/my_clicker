import pygame
import pictures, knopka, text


class Worker:

    def __init__(self, picture, coord, size, picture_inv, money_buy:int, bonus_lvl:int, pass_money:int, money:text.Text, clock:text.Text, bonus, action):
        self.coord = coord
        self.size = size
        self.picture = picture
        self.money = money
        self.clock = clock
        self.pass_money = pass_money
        self.bonus = bonus
        self.action = action
        self.money_buy_plus = 1.02
        self.money_buy_plus_plus = 0.02283
        self.worker_picture = pictures.Picture(picture_inv, self.size, self.coord)

        self.text_lvl = text.Text(coord[0], coord[1] - 84, "ЛВЛ: ", "#168FFF", 0, "#FEFF55")
        self.text_clock = text.Text(coord[0], coord[1] - 126, "+", "#3227FF", pass_money, "#FFDC3A", text2=" в сек.")
        self.text_bonus = text.Text(coord[0], coord[1] - 168, "Бонус: ", "#168FFF", bonus_lvl, "#FEFF55", text2="%")
        self.text_buy = text.Text(coord[0], coord[1] - 42, "Цена: ", "#4A310A", money_buy, "#FFEB87")

        self.knopka = knopka.Knopka("sprites/controls/up_green.png", 38, 38, self.text_lvl.x + 140,
                                    self.text_lvl.y, self.level_up)

        self.spisok_draw = [self.worker_picture, self.knopka, self.text_buy, self.text_clock, self.text_bonus,
                            self.text_lvl]

    def draw(self, dis):
        for s in self.spisok_draw:
            s.draw(dis)

    def level_up(self):
        if self.money.chislo < self.text_buy.chislo:
            return
        self.text_lvl.chislo += 1

        self.money.chislo -= self.text_buy.chislo
        self.text_buy.chislo *= self.money_buy_plus
        self.money_buy_plus += self.money_buy_plus_plus

        self.clock.chislo += self.text_clock.chislo
        self.text_clock.chislo += self.pass_money

        self.spisok_draw.remove(self.worker_picture)
        self.worker_picture = pictures.Picture(self.picture, self.size, self.coord)
        self.spisok_draw.append(self.worker_picture)
        if self.text_lvl.chislo == 20:
            self.bonus[0] += self.text_bonus.chislo / 100
            self.action()
