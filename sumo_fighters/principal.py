import pygame
from pygame.locals import *
from constantes import *

pygame.init()

# creation de la fenetre window
window = pygame.display.set_mode((longueur, hauteur))

# affichage du titre de la fenetre
pygame.display.set_caption("SumOctogone")

# affichage de l'icone
img_icone = pygame.image.load("images/logo.png").convert_alpha()
pygame.display.set_icon(img_icone)

# creation d'un timer
timer = pygame.time.Clock()

# chargement des différentes images du jeu
img_background = pygame.image.load("images/background menu.png").convert()
img_sumo_player = pygame.image.load("images/white.png").convert_alpha()
img_ile = pygame.image.load("images/ile.png").convert_alpha()

# creation d'un rect pour la position du sumo
position_perso = img_sumo_player.get_rect(center=(270, 300))

# actualisation de la fenetre
pygame.display.flip()

# assignement des variables
x, y = 270, 300
vx = 0  # vitesse x
vy = 0  # vitesse y
continuer = 1
gravite = 2


# creation de la boucle pour laisser la fenetre ouverte
while continuer:
    for evenement in pygame.event.get():
        if evenement.type == QUIT:
            continuer = 0

        if evenement.type == KEYDOWN:
            if evenement.key == K_UP:
                if y == 330:
                    vy = -25

            if evenement.key == K_SPACE:
                print(y)


    timer.tick(60)
    # creation de la variable keypress
    keypress = pygame.key.get_pressed()

    vy += gravite
    min(20, vy)

    vx = (keypress[K_RIGHT] - keypress[K_LEFT]) * 5

    x += vx
    y += vy


    if x >= 86 and x <= 649:
        y = min(330, y)

    if y >= 600:
        continuer = 0





    # affichage des images
    window.blit(img_background, (0, 0))
    window.blit(img_ile, (longueur / 2 - 500 / 2, hauteur / 2 - 30))
    window.blit(img_sumo_player, (x, y))

    pygame.display.flip()

pygame.quit()

