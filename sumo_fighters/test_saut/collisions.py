#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pygame
from pygame.locals import *

# On initialise pygame
pygame.init()
taille_fenetre = (600, 400)
fenetre_rect = pygame.Rect((0, 0), taille_fenetre)
screen_surface = pygame.display.set_mode(taille_fenetre)

BLEU_NUIT = (5, 5, 30)
VERT = (0, 255, 0)
JAUNE = (255, 255, 0)

timer = pygame.time.Clock()

joueur = pygame.Surface((25, 25))
joueur.fill(JAUNE)
# Position du joueur
x, y = 25, 100
# Vitesse du joueur
vx, vy = 0, 0
# Gravité vers le bas donc positive
GRAVITE = 3

mur = pygame.Surface((25, 25))
mur.fill(VERT)

niveau = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
]


def dessiner_niveau(surface, niveau):
    """Dessine le niveau sur la surface donnée.

    Utilise la surface `mur` pour dessiner les cases de valeur 1
    """
    for j, ligne in enumerate(niveau):
        for i, case in enumerate(ligne):
            if case == 1:
                surface.blit(mur, (i * 25, j * 25))


# Boucle événementielle
continuer = True
while continuer:
    for event in pygame.event.get():
        if event.type == QUIT:
            continuer = False
        elif event.type == KEYDOWN:
            if event.key == K_SPACE:
                if y == 300:
                    vy = -25

    timer.tick(30)
    keys_pressed = pygame.key.get_pressed()
    vx = (keys_pressed[K_RIGHT] - keys_pressed[K_LEFT]) * 5
    vy += GRAVITE
    vy = min(20, vy)  # On limite la vitesse de la chute à un max de 20
    # Chaque frame (1/30 sec) on avance de la vitesse vx et vy. C'est comme
    # si on admettait que le temps unitaire était de 1/30 de sec.
    x += vx
    y += vy
    # Limitons pour le moment jusqu'où le personnage peut tomber
    y = min(300, y)

    screen_surface.fill(BLEU_NUIT)
    dessiner_niveau(screen_surface, niveau)
    screen_surface.blit(joueur, (x, y))
    pygame.display.flip()

pygame.quit()

