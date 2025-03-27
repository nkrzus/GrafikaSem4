from turtledemo.paint import switchupdown

import pygame
import math
import random
import numpy as np

def rysuj_wielokat(liczba_bokow=13, skala=1.0):
    pygame.init()
    win = pygame.display.set_mode((800, 800))
    pygame.display.set_caption(f"{liczba_bokow}-kąt")

    FIOLETOWY = (128, 0, 128)
    SZARY = (128, 128, 128)
    BIALY = (255, 255, 255)

    font = pygame.font.Font(None, 36)
    base_size = 150
    size = base_size * skala
    srodek = (200, 200)
    points = [(size * (1 + random.uniform(-0.2, 0.2)) * math.cos((2 * math.pi / liczba_bokow) * i),
               size * (1 + random.uniform(-0.2, 0.2)) * math.sin((2 * math.pi / liczba_bokow) * i))
              for i in range(liczba_bokow)]

    poly_surface = pygame.Surface((400, 400), pygame.SRCALPHA)
    poly_surface.fill((0, 0, 0, 0))
    przesuniete_punkty = [(x + 200, y + 200) for x, y in points]
    pygame.draw.polygon(poly_surface, FIOLETOWY, przesuniete_punkty)

    def shear_surface(surface, shear_x, shear_y):
        width, height = surface.get_size()
        new_width = int(width + abs(shear_x) * height)
        new_height = int(height + abs(shear_y) * width)
        sheared_surface = pygame.Surface((new_width, new_height), pygame.SRCALPHA)

        shear_matrix = np.array([
            [1, shear_x, 0],  # Shear w osi X
            [shear_y, 1, 0]  # Shear w osi Y
        ])

        # Ręczne przekształcanie pikseli
        for y in range(height):
            for x in range(width):
                new_x = int(x + shear_x * y)
                new_y = int(y + shear_y * x)

                # Pobranie koloru i narysowanie w nowym miejscu
                color = surface.get_at((x, y))
                if 0 <= new_x < new_width and 0 <= new_y < new_height:
                    sheared_surface.set_at((new_x, new_y), color)
        return sheared_surface

    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                run = False
            elif event.type == pygame.KEYDOWN:
                if pygame.K_1 <= event.key <= pygame.K_9:
                    pygame.draw.rect(win, SZARY, (0, 0, 800, 800))
                    match event.key:
                        case pygame.K_1:
                            pygame.draw.polygon(poly_surface, FIOLETOWY, przesuniete_punkty)
                            win.blit(poly_surface, poly_surface.get_rect(center=(400, 400)))
                            print("Wybrano opcję 1")
                        case pygame.K_2:
                            transformed_surface = pygame.transform.rotozoom(poly_surface, -45, 1.5)
                            win.blit(transformed_surface, transformed_surface.get_rect(center=(400, 400)))
                            print("Wybrano opcję 2")
                        case pygame.K_3:
                            transformed_surface = pygame.transform.flip(poly_surface, 0, 1)
                            transformed_surface = pygame.transform.scale(transformed_surface, (transformed_surface.get_height() ,transformed_surface.get_height()*1.8))
                            win.blit(transformed_surface, transformed_surface.get_rect(center=(400, 400)))
                            print("Wybrano opcję 3")
                        case pygame.K_4:
                            transformed_surface=shear_surface(poly_surface,0.7,0)
                            win.blit(transformed_surface, transformed_surface.get_rect(center=(400, 400)))
                            print("Wybrano opcję 4")
                        case pygame.K_5:
                            transformed_surface = pygame.transform.scale(poly_surface,(poly_surface.get_width()*2,poly_surface.get_height()*0.5))
                            win.blit(transformed_surface, transformed_surface.get_rect(center=(400,transformed_surface.get_height()/2)))
                           # win.blit(transformed_surface, transformed_surface.get_rect(center=(400, 400)))
                            print("Wybrano opcję 5")
                        case pygame.K_6:
                            transformed_surface = shear_surface(poly_surface, 0.7, 0)
                            transformed_surface=pygame.transform.rotate(transformed_surface,-90)
                            win.blit(transformed_surface, transformed_surface.get_rect(center=(400, 400)))
                            print("Wybrano opcję 6")
                        case pygame.K_7:
                            transformed_surface = pygame.transform.flip(poly_surface, 0, 1)
                            transformed_surface = pygame.transform.scale(transformed_surface, (
                            transformed_surface.get_height(), transformed_surface.get_height() * 1.8))
                            transformed_surface=pygame.transform.flip(transformed_surface,1,0)
                            win.blit(transformed_surface, transformed_surface.get_rect(center=(400, 400)))
                            print("Wybrano opcję 7")
                        case pygame.K_8:
                            transformed_surface = pygame.transform.scale(poly_surface, (
                            poly_surface.get_width() * 2, poly_surface.get_height() * 0.5))
                            transformed_surface = pygame.transform.rotate(transformed_surface,-30)
                            win.blit(transformed_surface, transformed_surface.get_rect(center=(400, 400)))
                            print("Wybrano opcję 8")
                        case pygame.K_9:
                            transformed_surface = pygame.transform.scale(poly_surface, (
                            poly_surface.get_height(), poly_surface.get_height() * 1.8))
                            transformed_surface = pygame.transform.rotate(transformed_surface,180)
                            transformed_surface = shear_surface(transformed_surface, 0, 0.7)
                            win.blit(transformed_surface, transformed_surface.get_rect(center=(400, 400)))
                            print("Wybrano opcję 9")
                        case _:
                            print("Wybrano zly klawisz")

        instrukcja = font.render("1-9: zmiana, ESC: wyjście", True, BIALY)
        win.blit(instrukcja, (20, 750))
        pygame.display.update()
    pygame.quit()
rysuj_wielokat(skala=1.0)
