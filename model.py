import pygame

money = 0
plus = 2
rost_plus = 0


def money1():
    global money
    money += plus


def plus1():
    global plus, rost_plus
    rost_plus += 2
    plus += rost_plus
