import pygame
from jeu import Jeu


def debut_jeu():
    # modifiable(nom de la fenetre)
    pygame.display.set_caption("Dino Run Run")
    ecran = pygame.display.set_mode((760, 660))

    # modifiable(arriere-plan du jeu)
    arrierePlan = pygame.image.load('assets/game-background-4956017_1920.jpg')

    # modifiable(écran titre)
    banniere = pygame.image.load('assets/accueil.png')

    jeu = Jeu()

    musique = 1
    clock = pygame.time.Clock()
    running = True
    while running:
        ecran.blit(arrierePlan, (-140,-320))
        if jeu.debutJeu:
            jeu.lancement(ecran)
            jeu.score += 1
        else:
            ecran.blit(banniere, (120, 500))
            if musique == 1:
                pygame.mixer.music.load('assets/jump-and-run-tropics.wav')
                pygame.mixer.music.set_volume(0.1)
                pygame.mixer.music.play(-1)
                musique = musique * 0
            if jeu.presse.get(pygame.K_SPACE):
                jeu.start()
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                jeu.presse[event.key] = True
            elif event.type == pygame.KEYUP:
                jeu.presse[event.key] = False
        clock.tick(60)
