import pygame
import text
import knopka
import workers

pygame.init()


def money1():
    money.chislo += plus.chislo


def plus1():
    if money.chislo < prokachka.chislo:
        return
    money.chislo -= prokachka.chislo
    plus.chislo += rost_plus.chislo
    rost_plus.chislo += 2
    prokachka.chislo *= 1.05
    lvl_main.chislo += 1


def pass_plus():
    money.chislo += clock.chislo


lvl_main = text.Text(100, 440, "Уровень: ", "#168FFF", 1, "#FEFF55")
money = text.Text(624, 0, "Ваши деньги: ", "#4A310A", 10000000, "#FFEB87")
prokachka = text.Text(624, 42, "Цена апгрейда: ", "#FFC122", 10, "#F2DBFF")
plus = text.Text(624, 86, "Денег за нажатие: ", "#2B9418", 2, "#FF2A2A")
plus_and_procent = text.Text(624, 86, "C процентами: ", "#2B9418", 2, "#FF2A2A", True, 574)
rost_plus = text.Text(624, 42, "Прирост за клик: ", "#FFC122", 2, "#F2DBFF", True, 574)
clock = text.Text(624, 132, "Денег в секунду: ", "#3227FF", 0, "#FFDC3A")
bonus = text.Text(610, 664, "Бонус за клик: +", "#168FFF", 20, "#FEFF55", text2="% ")
yellow_knopka = knopka.Knopka("sprites/controls/up_yellow.png", 38, 38, 580, 44, plus1)
worker3 = workers.Worker("sprites/worker/worker3.png", [540, 550], [200, 300], "sprites/worker/worker3_inv.png", 50000,
                         30, 5, money, clock)
worker2 = workers.Worker("sprites/worker/worker2.png", [320, 550], [200, 300], "sprites/worker/worker2_inv.png", 10000,
                         20, 2, money, clock)

spisok_text = [money, prokachka, plus, rost_plus, clock, lvl_main, plus_and_procent]
