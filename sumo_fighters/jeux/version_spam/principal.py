from pygame.locals import *
from jeux.version_classique.constantes import *

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

# creation des rect pour les collsions des sumos
sumo_rect1 = img_sumo_player.get_rect()
sumo_rect2 = img_sumo_player2.get_rect()

# creation des rects pour les plateformes
rect_ile_pricipale = img_ile.get_rect()

# creations de toutes les fonctions


# actualisation de la fenetre
pygame.display.flip()

# assignement des variables

x_perso1, y_perso1, x_perso2, y_perso2 = 545, 300, 210, 300  # declaration des valeurs x et y de bases = positions de base des joueurs

vx_perso1 = vy_perso1 = vx_perso2 = vy_perso2 = 0  # vitesse x et y des joueurs

nb_saut_sumo1 = nb_saut_sumo2 = 0

vie_sumo1 = vie_sumo2 = 100

continuer = 1
gravite = 2.5

# creation de la boucle principal
while continuer:
    for evenement in pygame.event.get():
        if evenement.type == QUIT:
            continuer = 0

        if evenement.type == KEYDOWN:

            if nb_saut_sumo1 < 2:  # detecte si le sumo à fait 2 sauts ou pas
                if evenement.key == K_UP:
                    vy_perso1 = -25  # hauteur du saut
                    nb_saut_sumo1 += 1
            elif nb_saut_sumo1 >= 2:
                nb_saut_sumo1 = 0

            if nb_saut_sumo2 < 2:  # permet de faire le saut aux sumos
                if evenement.key == K_w:
                    vy_perso2 = -25  # hauteur du saut
                    nb_saut_sumo2 += 1
            elif nb_saut_sumo2 >= 2:
                nb_saut_sumo2 = 0

            if evenement.key == K_SPACE:
                print("y1 : ", y_perso1, "x1", x_perso1, " vie 1", vie_sumo1, "\ny2 : ", y_perso2, "x2", x_perso2,
                      "vie 2", vie_sumo2)

    timer.tick(60)
    # creation de la variable keypress
    keypress = pygame.key.get_pressed()

    vy_perso1 += gravite  # ajout de la gravité pour ralentir le saut des personnages et leur permettre de retomber
    min(20, vy_perso1)

    vy_perso2 += gravite
    min(20, vy_perso2)

    vx_perso1 = (keypress[K_RIGHT] - keypress[
        K_LEFT]) * 5  # se sont des booléans qui valent 1 quand une touche est préssé

    vx_perso2 = (keypress[K_d] - keypress[K_a]) * 5
    if keypress[K_e]:
        if keypress[K_RCTRL]:
            print("SPAAAAAAAAAAAM")
    if keypress[K_e]:  # permet de détécter si les sumos tapent
        if sumo_rect2.colliderect(
                sumo_rect1):  # si les sumos tapent et qu'ils se touchent en même temps alors le if est vérifié
            vie_sumo1 -= 1
            if vie_sumo1 <= 0:
                print("mort sumo 1")

    if keypress[K_RCTRL]:  # permet de détécter si les sumos tapent
        if sumo_rect1.colliderect(
                sumo_rect2):  # si les sumos tapent et qu'ils se touchent en même temps alors le if est vérifié
            vie_sumo2 -= 1
            if vie_sumo2 <= 0:
                print("mort sumo 2")

    if keypress[K_SPACE]:
        if sumo_rect1.colliderect(sumo_rect2):
            continuer = 0

    x_perso1 += vx_perso1  # actualisation de la position du personnage par rapport à sa vitesse
    y_perso1 += vy_perso1

    x_perso2 += vx_perso2
    y_perso2 += vy_perso2

    if sumo_rect1.colliderect(
            rect_ile_pricipale):  # permet au personnages de tomber quand il n'est plus sur la plateforme
        y_perso1 = min(330, y_perso1)

    else:
        pass

    if sumo_rect2.colliderect(rect_ile_pricipale):
        y_perso2 = min(330, y_perso2)

    else:
        pass

    if y_perso1 >= 600 or y_perso2 >= 600:  # ferme le jeu quand l'un des sumos tombe de l'écran
        continuer = 0

    sumo_rect1.topleft = (x_perso1, y_perso1)  # récupération de la position des rects pour les collisions
    sumo_rect2.topleft = (x_perso2, y_perso2)

    rect_ile_pricipale.topleft = (longueur / 2 - 500 / 2, hauteur / 2 - 30)

    # affichage des images
    window.blit(img_background, (0, 0))
    window.blit(img_ile, (longueur / 2 - 500 / 2, hauteur / 2 - 30))
    window.blit(img_sumo_player, (x_perso1, y_perso1))
    window.blit(img_sumo_player2, (x_perso2, y_perso2))

    pygame.display.flip()

pygame.quit()