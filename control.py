import pygame, model

def p():
    p1 = pygame.event.get()
    for f in p1:
        if f.type == pygame.QUIT:
            exit()
        if f.type == pygame.MOUSEBUTTONDOWN:
            if f.button == pygame.BUTTON_LEFT:
                if model.r1.collidepoint(f.pos):
                    model.plus1()
                    continue
                model.money1()
