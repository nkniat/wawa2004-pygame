# Tutaj pisz swój kod, młody padawanie ;-)
WIDTH = 800
HEIGHT = 400

player = Actor('girl_stay', (60, 250))
floor = Actor('ground', (400, 380))
mushroom = Actor('mushroom', (500, 300))

speedy = 0
points = 0

player.dead = False


def draw():
    global points

    screen.clear()

    screen.draw.text("Punkty: " + str(points), (0, 0))

    player.draw()
    floor.draw()
    mushroom.draw()


def update():
    global speedy, points

    if player.dead == False:
        if player.colliderect(floor):  # kolizja
            if keyboard.space:  # skok
                speedy = -20
                player.image = 'girl_jump'  # zmiena obrazka na skok
            else:
                space = 0
                player.y = 250
                player.image = 'girl_stay'
        else:
            speedy = speedy + 1
        player.y += speedy

        # poruszanie grzyb
        mushroom.x -= 4
        if mushroom.x < -100:
            mushroom.x = 900
            points += 1  # punktacja

    if player.colliderect(mushroom):  # kolizja z grzybem
        player.dead = True  # koniec gry