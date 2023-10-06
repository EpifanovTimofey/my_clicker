import pygame
import text
import knopka
import workers

pygame.init()


def money1():
    money.chislo += plus.chislo * procent


def plus1():
    if money.chislo < prokachka.chislo:
        return
    money.chislo -= prokachka.chislo
    plus.chislo += rost_plus.chislo
    rost_plus.chislo += 2
    prokachka.chislo *= 1.05
    lvl_main.chislo += 1
    plus_and_procent.chislo = plus.chislo * procent


def prockachka_w2_def():
    global w2_prokachka, procent
    if money.chislo < prokachka_w2.chislo:
        return
    lvl_worker2.chislo += 1
    money.chislo -= prokachka_w2.chislo
    prokachka_w2.chislo *= w2_prokachka
    w2_prokachka += w2_plus
    clock.chislo += clock_w2_plus.chislo
    clock_w2_plus.chislo += 2
    if lvl_worker2.chislo == 2:
        procent += 0.2
        spisok_text.append(bonus)
        plus_and_procent.chislo = plus.chislo * procent


def pass_plus():
    money.chislo += clock.chislo


w2_prokachka = 1.02
w2_plus = 0.02283
procent = 1

lvl_main = text.Text(100, 440, "Уровень: ", "#168FFF", 1, "#FEFF55")
lvl_worker2 = text.Text(610, 340, "Уровень: ", "#168FFF", 0, "#FEFF55")
money = text.Text(624, 0, "Ваши деньги: ", "#4A310A", 100000, "#FFEB87")
prokachka = text.Text(624, 42, "Цена апгрейда: ", "#FFC122", 10, "#F2DBFF")
prokachka_w2 = text.Text(610, 580, "Цена прокачки: ", "#4A310A", 10000, "#FFEB87")
plus = text.Text(624, 86, "Денег за нажатие: ", "#2B9418", 2, "#FF2A2A")
plus_and_procent = text.Text(624, 86, "C процентами: ", "#2B9418", 2, "#FF2A2A", True, 574)
rost_plus = text.Text(624, 42, "Прирост за клик: ", "#FFC122", 2, "#F2DBFF", True, 574)
clock_w2_plus = text.Text(610, 622, "Прирост за апгрейд: ", "#3227FF", 2, "#FFDC3A")
clock = text.Text(624, 132, "Денег в секунду: ", "#3227FF", 0, "#FFDC3A")
bonus = text.Text(610, 664, "Бонус за клик: +", "#168FFF", 20, "#FEFF55", text2="% ")
yellow_knopka = knopka.Knopka("sprites/controls/up_yellow.png", 38, 38, 580, 44, plus1)
green_knopka = knopka.Knopka("sprites/controls/up_green.png", 38, 38, 560, 580, prockachka_w2_def)
worker3 = workers.Worker("sprites/worker/worker3.png", [1000, 600], [200, 200], "sprites/worker/worker3_inv.png", 50000,
                         30, 5, money)

spisok_text = [money, prokachka, plus, rost_plus, clock, lvl_main, lvl_worker2, prokachka_w2, clock_w2_plus,
               plus_and_procent]
