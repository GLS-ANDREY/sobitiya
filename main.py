import pygame
import time
import random

pygame.init()
b = pygame.font.SysFont("arial", 30, True, True)
g = random.randint(0, 100)
e = pygame.display.set_mode([1000, 700])

while True:
    loc = random.randint(0,255)
    col = random.randint(0,255)
    rgb = random.randint(0,255)
    rk = random.randint(100, 900)
    kr = random.randint(100, 600)
    s = pygame.event.get()

    for a in s:
        if a.type == pygame.KEYDOWN and a.key != pygame.K_SPACE:
            q = a.key
            t = str(q)
            r = b.render("klavisha" + t, True, [loc, col, rgb])
            e.blit(r, [rk, kr])

        if a.type == pygame.KEYDOWN and a.key == pygame.K_SPACE:
            rr = b.render("probel", True, [200, 200, 201])
            e.blit(rr, [500, 350])

        if a.type == pygame.MOUSEBUTTONDOWN:
            c = print(a.pos)
            t = str(c)
            rrr = b.render("click " + t, True, [200, 200, 201])
            e.blit(rrr, [500, 400])

        if a.type == pygame.KEYDOWN:
            print(a.key)
        if a.type == pygame.MOUSEBUTTONDOWN:
            print(a.button)
        if a.type == pygame.KEYDOWN or a.type == pygame.MOUSEBUTTONDOWN:
            print(a.type)

    pygame.display.flip()