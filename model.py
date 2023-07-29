import pygame
import text

pygame.init()

t1 = text.Text(624, 0, "Ваши деньги: ", "#4A310A", 0, "#FFEB87")
t2 = text.Text(624, 42, "Цена апгрейда: ", "#FFC122", 10, "#F2DBFF")
t3 = text.Text(624, 86, "Денег за нажатие: ", "#2B9418", 2, "#FF2A2A")
t4 = text.Text(624, 42, "Прирост за клик: ", "#FFC122", 2, "#F2DBFF", True, 574)

spisok_text = [t1, t2, t3, t4]

r1 = pygame.Rect([580, 44, 38, 38])

money = 0
plus = 2
rost_plus = 2
prokachka = 10
uroven_glav = 1


def money1():
    global money
    money += plus
    t1.cvet = "green"
    t1.new_chislo(money)
    print(t1.cvet)



def plus1():
    global plus, rost_plus, prokachka, uroven_glav, money
    if money >= prokachka:
        money -= prokachka
        plus += rost_plus
        rost_plus += 2
        prokachka *= 1.05
        uroven_glav += 1
        t1.cvet = "red"
        t1.new_chislo(money)
        t2.new_chislo(prokachka)
        t3.new_chislo(plus)
        t4.new_chislo(rost_plus)
