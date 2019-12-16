# Créé par ppenot, le 16/12/2019 en Python 3.4

from pygame.locals import *
import pygame
import time
from constantes import hauteur, longueur

pygame.init()
window = pygame.display.set_mode((longueur, hauteur))

# affichage du titre de la fenetre
pygame.display.set_caption("SumOctogone")

# affichage de l'icone
img_icone = pygame.image.load("images/logo.png").convert_alpha()
pygame.display.set_icon(img_icone)


bg = pygame.image.load("images/background menu.png").convert()

img_sumo_player = pygame.image.load("images/white.png").convert_alpha()



class Player:

    def __init__(self, perso, life, x, y):
        self.image_perso = perso
        self.vx = 0
        self.vy = 0
        self.life = life
        self.x = x
        self.y = y
        self.keypress = pygame.key.get_pressed()
        self.gravite = 2.5

    def jump(self):
        if keypress[K_UP]:
            if self.y == 330:
                vy -25

    def draw(self, surface):
        surface.blit(self.image_perso, (self.x, self.y))



sumo1 = Player(img_sumo_player, 100, 0, 0)

sumo1.draw(window)


continuer = 1

while continuer:
    for evenement in pygame.event.get():
        if evenement.type == QUIT:
            continuer = 0






pygame.quit()
