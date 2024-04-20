import pygame
from sys import exit
pygame.init()  # zainicjalizowanie silnika pygame

WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Czerwony kapturek')
clock = pygame.time.Clock()
font = pygame.font.SysFont('Arial', 24)
step = 4
player_gravity = 0
game_active = True

sky_surface = pygame.image.load('images/background.png').convert()

text_surface = font.render("Moja fajna gra", 1, "Black")
text_rect = text_surface.get_rect(center=(300, 20))

mushroom_surface = pygame.image.load('images/mushroom.png').convert_alpha()
mushroom_rect = mushroom_surface.get_rect(bottomright=(700, 360))
#mushroom_pos_x = 700 # niepotrzebne już, bo będzie w atrybucie Rect jako 'x'

player_surface = pygame.image.load('images/girl_stay.png').convert_alpha()
player_rect = player_surface.get_rect(midbottom=(60, 360))

# ekran powitalny
game_name = font.render("Czerwony Kapturek", 1, "White")
game_rect = game_name.get_rect(center=(300, 20))

player_stand = pygame.image.load('images/girl_stay.png').convert_alpha()
player_stand = pygame.transform.scale2x(player_stand)
player_stand_rect = player_stand.get_rect(center=(300, 200))

game_msg = font.render("Naciśnij spację, aby zagrać", 1, "White")
game_msg_rect = game_msg.get_rect(center=(300, 360))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if game_active:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if player_rect.collidepoint(event.pos) and player_rect.bottom == 360:
                    player_gravity = -20
                    #print('kliknieto')
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and player_rect.bottom == 360:
                    #print("nacisnieto klawisz spacji")
                    player_gravity = -20
        else:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                game_active = True
                mushroom_rect.x = 700

    if game_active:
        screen.blit(sky_surface, (0, 0))
        screen.blit(text_surface, text_rect)
        screen.blit(player_surface, player_rect)

        # przesuwanie przeszkody
        mushroom_rect.x -= step
        if mushroom_rect.x < -100:
            mushroom_rect.x = 700
        screen.blit(mushroom_surface, mushroom_rect)

        # skakanie postaci
        # keys = pygame.key.get_pressed()
        # if keys[pygame.K_SPACE]:
        #     print('skok')

        player_gravity += 1
        player_rect.y += player_gravity
        if player_rect.bottom >= 360:
            player_rect.bottom = 360
        screen.blit(player_surface, player_rect)

        if player_rect.colliderect(mushroom_rect):
            game_active = False
            # pygame.quit()
            # exit()
            #print('Zderzenie')

        # mouse_pos = pygame.mouse.get_pos()
        # if player_rect.collidepoint(mouse_pos):
        #     print("zderzenie")

        #print(pygame.mouse.get_pressed())
    else:
        screen.fill("Black")
        screen.blit(game_name, game_rect)
        screen.blit(player_stand, player_stand_rect)
        screen.blit(game_msg, game_msg_rect)

    pygame.display.update()
    clock.tick(60)
