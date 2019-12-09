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
img_sumo_player2 = pygame.image.load("images/green.png").convert_alpha()
img_ile = pygame.image.load("images/ile.png").convert_alpha()

# creation d'un rect pour la position du sumo
position_perso = img_sumo_player.get_rect()


# actualisation de la fenetre
pygame.display.flip()

# assignement des variables

x_perso1, y_perso1, x_perso2, y_perso2 = 545, 300, 210, 300 # declaration des valeurs x et y de bases = positions de base des joueurs

position_perso.move(100, 100)

vx_perso1 = vy_perso1 = vx_perso2 = vy_perso2 = 0 # vitesse x et y des joueurs

my_collisions = []

continuer = 1
gravite = 2.5


# creation de la boucle principal
while continuer:
    for evenement in pygame.event.get():
        if evenement.type == QUIT:
            continuer = 0

        if evenement.type == KEYDOWN:

            if evenement.key == K_UP: # permet de faire le saut aux sumos
                if y_perso1 == 330: # on ne permet au sumos de sauter que quand ils sont à la hauteur de la plateforme
                    vy_perso1 = -25 # hauteur du saut

            if evenement.key == K_w:
                if y_perso2 == 330:
                    vy_perso2 = -25

            if evenement.key == K_SPACE:
                print("y1 : ", y_perso1, "x1", x_perso1, "\ny2 : ", y_perso2, "x2", x_perso2)


    timer.tick(60)
    # creation de la variable keypress
    keypress = pygame.key.get_pressed()

    vy_perso1 += gravite  # ajout de la gravité pour ralentir le saut des personnages et leur permettre de retomber
    min(20, vy_perso1)

    vy_perso2 += gravite
    min(20, vy_perso2)

    vx_perso1 = (keypress[K_RIGHT] - keypress[K_LEFT]) * 5  # se sont des booléans qui valent 1 quand une touche est préssé

    vx_perso2 = (keypress[K_d] - keypress[K_a]) * 5

    x_perso1 += vx_perso1  # actualisation de la position du personnage par rapport à sa vitesse
    y_perso1 += vy_perso1

    x_perso2 += vx_perso2
    y_perso2 += vy_perso2


    if x_perso1 >= 86 and x_perso1 <= 649:  # permet au personnages de tomber quand il n'est plus sur la plateforme
        y_perso1 = min(330, y_perso1)

    if x_perso2 >= 86 and x_perso2 <= 649:
        y_perso2 = min(330, y_perso2)


    if y_perso1 >= 600 or y_perso2 >= 600:  # ferme le jeu quand l'un des sumos tombe de l'écran
        continuer = 0







    # affichage des images
    window.blit(img_background, (0, 0))
    window.blit(img_ile, (longueur / 2 - 500 / 2, hauteur / 2 - 30))
    window.blit(img_sumo_player, (x_perso1, y_perso1))
    window.blit(img_sumo_player2, (x_perso2, y_perso2))

    pygame.display.flip()

pygame.quit()
