import pygame

pygame.init()
win = pygame.display.set_mode((600, 600))
pygame.display.set_caption("Pygame Zadanie 2")

# deklarowanie kolorów
ZOLTY = (255, 255, 0)
CZARNY = (0, 0, 0)
BIALY=(255,255,255)

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    pygame.draw.rect(win, BIALY, (1, 1, 600, 600))
    pygame.draw.circle(win, CZARNY, (100, 100), 50, 0)

    pygame.draw.rect(win, ZOLTY, (75, 75, 50, 50))

    pygame.display.update()