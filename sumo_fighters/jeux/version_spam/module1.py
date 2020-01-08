import pygame
pygame.init()
window = pygame.display.set_mode((800,600))
pygame.display.set_caption("ISN ILIES")

img_background = pygame.image.load("images/background menu.png")
logo = pygame.image.load("images/logo.png").convert_alpha()

img = img_background
pygame.display.flip()
mouse = pygame.mouse.get_pos
button = pygame.mouse.get_pressed
def cloture(): #Structure
    #Fermeture de la fenêtre
    game_over = False #Le Programme tourne normalement
    while not game_over: #Tant qu'il tourne = NP
        for event in pygame.event.get():
            if event.type == pygame.QUIT: #Si l'événement de Pygame qui s'execute est égale au boutton rouge X
                game_over= True   #La page se ferme
        pygame.mouse.get_pos = mouse
        pygame.mouse.get_pressed = button

        window.blit(img, (0,0))
        window.blit(logo, (800/2-101,30))
        pygame.display.flip() #rafraichissement du fond



cloture()
pygame.quit()
quit()