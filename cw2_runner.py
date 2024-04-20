import pygame
from sys import exit
pygame.init()  # zainicjalizowanie silnika pygame

WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Czerwony kapturek')
clock = pygame.time.Clock()
font = pygame.font.SysFont('Arial', 24)

sky_surface = pygame.image.load('images/background.png').convert()
text_surface = font.render("Moja gra", 1, "Black")

mushroom_surface = pygame.image.load('images/mushroom.png').convert_alpha()
mushroom_rect = mushroom_surface.get_rect(bottomright=(700, 360))
#mushroom_pos_x = 700 # niepotrzebne już, bo będzie w atrybucie Rect jako 'x'
step = 4

player_surface = pygame.image.load('images/girl_stay.png').convert_alpha()
player_rect = player_surface.get_rect(midbottom=(60, 360))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.blit(sky_surface, (0, 0))
    screen.blit(text_surface, (250, 10))
    screen.blit(player_surface, player_rect)

    mushroom_rect.x -= step
    if mushroom_rect.x < -100:
        mushroom_rect.x = 700
    screen.blit(mushroom_surface, mushroom_rect)

    pygame.display.update()
    clock.tick(60)
