import pygame
import time
import random

pygame.init()
b = pygame.font.SysFont("arial", 30, True, True)
e = pygame.display.set_mode([1000, 700])

while True:
    g = random.randint(0, 100)
    loc = random.randint(0, 255)
    col = random.randint(0, 255)
    rgb = random.randint(0, 255)
    rk = random.randint(100, 900)
    kr = random.randint(100, 600)
    s = pygame.event.get()

    for a in s:
        if a.type == pygame.QUIT:
            exit()

        if a.type == pygame.KEYDOWN and a.key != pygame.K_SPACE:
            q = a.key
            t = str(q)
            r = b.render("klavisha" + t, True, [loc, col, rgb])
            e.blit(r, [rk, kr])

        if a.type == pygame.KEYDOWN and a.key == pygame.K_SPACE:
            rr = b.render("probel", True, [200, 200, 201])
            e.blit(rr, [500, 350])

        if a.type == pygame.MOUSEBUTTONDOWN:
            t = str(a.pos[0])
            t2 = str(a.pos[1])
            rrr = b.render("click:  x = " + t + " y = " + t2, True,
                           [random.randint(0, 250), random.randint(0, 250), random.randint(0, 250)])
            e.blit(rrr, [a.pos[0], a.pos[1]])

        if a.type == pygame.MOUSEMOTION:
            k = a.pos
            pygame.draw.circle(e,
                    [random.randint(0, 250), random.randint(0, 250), random.randint(0, 250)],k,3)
        if a.type == pygame.KEYDOWN:
            print(a.key)
        if a.type == pygame.MOUSEBUTTONDOWN:
            print(a.button)
        if a.type == pygame.KEYDOWN or a.type == pygame.MOUSEBUTTONDOWN:
            print(a.type)

    pygame.display.flip()
