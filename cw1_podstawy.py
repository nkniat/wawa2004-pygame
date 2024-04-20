import pygame
from sys import exit
pygame.init()  # zainicjalizowanie silnika pygame

WIDTH, HEIGHT = 800, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Moja pierwsza gra')
clock = pygame.time.Clock()

X, Y = 10, 10
FIGURE_WIDTH, FIGURE_HEIGHT = 10 , 10

# nieskonczona pętla do utrzymania okienka gry
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    #pygame.draw.rect(screen, "White", (X, Y, FIGURE_WIDTH, FIGURE_HEIGHT))
    # pygame.draw.line(screen, (255, 0, 0), (X, Y), (X, Y + 200), 5)  # linia pionowa
    # pygame.draw.line(screen, (0, 255, 0), (X, Y), (X + 200, Y), 5)  # linia pozioma
    # # pygame.draw.line(screen, (0, 0, 255), (X, Y), (X + 200, Y + 200), 5)  # linia po przekątnej

    # step = 0
    # for _ in range(WIDTH):
    #     for _ in range(HEIGHT):
    #         pygame.draw.rect(screen, "White", (X + step, Y + step, FIGURE_WIDTH, FIGURE_HEIGHT))
    #         step += 10

    # # wypisywanie tekstu
    # font = pygame.font.SysFont('Arial', 24)
    # label = font.render('Hello World!', 1, 'White')
    # # żeby pokazać napis na ekranie
    # screen.blit(label, (X, Y))

    step = 5
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        X -= step
    if keys[pygame.K_RIGHT]:
        X += step
    if keys[pygame.K_UP]:
        Y -= step
    if keys[pygame.K_DOWN]:
        Y += step

    screen.fill('Black')
    pygame.draw.rect(screen, "White", (X, Y, FIGURE_WIDTH, FIGURE_HEIGHT))

    pygame.display.update()
    clock.tick(60)
