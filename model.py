import pygame
import text

pygame.init()

money = text.Text(624, 0, "Ваши деньги: ", "#4A310A", 0, "#FFEB87")
prokachka = text.Text(624, 42, "Цена апгрейда: ", "#FFC122", 10, "#F2DBFF")
plus = text.Text(624, 86, "Денег за нажатие: ", "#2B9418", 2, "#FF2A2A")
rost_plus = text.Text(624, 42, "Прирост за клик: ", "#FFC122", 2, "#F2DBFF", True, 574)

spisok_text = [money, prokachka, plus, rost_plus]

r1 = pygame.Rect([580, 44, 38, 38])

uroven_glav = 1


def money1():
    money.chislo += plus.chislo


def plus1():
    global uroven_glav
    if money.chislo >= prokachka.chislo:
        money.chislo -= prokachka.chislo
        plus.chislo += rost_plus.chislo
        rost_plus.chislo += 2
        prokachka.chislo *= 1.05
        uroven_glav += 1
