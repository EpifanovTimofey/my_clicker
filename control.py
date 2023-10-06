import pygame, model
a = pygame.event.custom_type()
pygame.time.set_timer(a, 1000)


def p():
    p1 = pygame.event.get()
    model.green_knopka.events(p1)
    model.yellow_knopka.events(p1)
    model.worker3.knopka.events(p1)
    for f in p1:
        if f.type == pygame.QUIT:
            exit()
        if f.type == pygame.MOUSEBUTTONDOWN:
            if f.button == pygame.BUTTON_LEFT:
                model.money1()
        if f.type == a:
            model.pass_plus()