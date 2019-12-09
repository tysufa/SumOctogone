import pygame
from pygame.locals import *
from constantes import *

pygame.init()

# creation de la fenetre window
window = pygame.display.set_mode((longueur, hauteur))

# affichage du titre de la fenetre
pygame.display.set_caption("SumOctogone")

# affichage de l'icone


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
gravite = 2.5


# creation de la boucle pour laisser la fenetre ouverte
while continuer:
    for evenement in pygame.event.get():
        if evenement.type == QUIT:
            continuer = 0

        if evenement.type == KEYDOWN:
            if evenement.key == K_UP:
                vy = -30

    timer.tick(60)
    # creation de la variable keypress
    keypress = pygame.key.get_pressed()

    vy += gravite

    vx = (keypress[K_RIGHT] - keypress[K_LEFT]) * 3

    x += vx
    y += vy

    y = min(330, y)

    # affichage des images
    window.blit(img_background, (0, 0))
    window.blit(img_ile, (longueur / 2 - 500 / 2, hauteur / 2 - 30))
    window.blit(img_sumo_player, (x, y))

    pygame.display.flip()

