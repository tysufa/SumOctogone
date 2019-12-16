from pygame.locals import *
import pygame
import time
from jeux.version_spam.constantes import gravite, hauteur, longueur

pygame.init()
window = pygame.display.set_mode((longueur, hauteur))

# affichage du titre de la fenetre
pygame.display.set_caption("SumOctogone")

# affichage de l'icone
img_icone = pygame.image.load("images/logo.png").convert_alpha()
pygame.display.set_icon(img_icone)

