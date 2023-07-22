import pygame
import text

pygame.init()

t1 = text.Text(600, 0, "Ваши деньги: ", "#4A310A", 0)
t2 = text.Text(644, 42, "Цена апгрейда: ", "#FFC122", 10)

r1 = pygame.Rect([600, 44, 38, 38])

money = 0
plus = 2
rost_plus = 0
prokachka = 10
uroven_glav = 1


def money1():
    global money
    money += plus
    t1.chislo = money

def plus1():
    global plus, rost_plus, prokachka, uroven_glav, money
    if money >= prokachka:
        money -= prokachka
        rost_plus += 2
        plus += rost_plus
        prokachka *= 1.05
        uroven_glav += 1
        t1.chislo = money
        t2.chislo = prokachka
