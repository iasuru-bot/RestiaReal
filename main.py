import pygame, yamso , chevalax , Brickbreaker, Dino_run_run
from pygame.locals import *
from Couleur import *

def menu_gen():
    pygame.init()
    size = 760, 660

    screen = pygame.display.set_mode(size)
    pygame.display.set_caption('Restia')

    programicon = pygame.image.load('image_logo.png')
    pygame.display.set_icon(programicon)

    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((102, 0, 102))
    image_fond = pygame.image.load("fondmenu3.0.jpg")
    background.blit(image_fond, (-125, 0))

    # Affichage d'un texte  
    font = pygame.font.Font(None, 36)
    text = font.render("Bienvenue sur la plateforme de jeux", True, (255, 230, 255))
    textpos = text.get_rect()
    textpos.top = background.get_rect().top + 60
    textpos.centerx = background.get_rect().centerx
    background.blit(text, textpos)
    image_logo = pygame.image.load("titre.png")
    background.blit(image_logo, (226, 372))

    # Affichage du fond des boutons
    # Fond du yams
    top_touryams = background.get_rect().bottom - 188
    left_touryams = background.get_rect().left + 158
    touryams = pygame.Rect(left_touryams, top_touryams, 85, 30)
    pygame.draw.rect(background, (255, 39, 126), touryams, width=0, border_radius=3)
    pygame.draw.rect(background, BLACK, touryams, width=2, border_radius=3)

    # Fond du chevaux
    top_tourchevaux = background.get_rect().bottom - 88
    left_tourchevaux = background.get_rect().left + 142
    tourchevaux = pygame.Rect(left_tourchevaux, top_tourchevaux, 118, 30)
    pygame.draw.rect(background, (255, 39, 126), tourchevaux, width=0, border_radius=3)
    pygame.draw.rect(background, BLACK, tourchevaux, width=2, border_radius=3)

    # Fond du dino
    top_tourdino = background.get_rect().bottom - 188
    left_tourdino = background.get_rect().left + 471
    tourdino = pygame.Rect(left_tourdino, top_tourdino, 158, 30)
    pygame.draw.rect(background, (255, 39, 126), tourdino, width=0, border_radius=3)
    pygame.draw.rect(background, BLACK, tourdino, width=2, border_radius=3)

    # Fond du casse-brique
    top_tourbrique = background.get_rect().bottom - 88
    left_tourbrique = background.get_rect().left + 455
    tourbrique = pygame.Rect(left_tourbrique, top_tourbrique, 191, 30)
    pygame.draw.rect(background, (255, 39, 126), tourbrique, width=0, border_radius=3)
    pygame.draw.rect(background, BLACK, tourbrique, width=2, border_radius=3)

    yams = font.render("Yamso", True, BLACK)
    yamspos = yams.get_rect()
    yamspos.bottom = background.get_rect().bottom - 160
    yamspos.centerx = background.get_rect().left + 200
    background.blit(yams, yamspos)

    chevaux = font.render("Chevalax", True, BLACK)
    chevauxpos = chevaux.get_rect()
    chevauxpos.bottom = background.get_rect().bottom - 60
    chevauxpos.centerx = background.get_rect().left + 200
    background.blit(chevaux, chevauxpos)

    dino = font.render("Dino run run", True, BLACK)
    dinopos = dino.get_rect()

    dinopos.bottom = background.get_rect().bottom - 160
    dinopos.centerx = background.get_rect().left + 550
    background.blit(dino, dinopos)

    casse_brique = font.render("Super Breakeur", True, BLACK)
    casse_briquepos = casse_brique.get_rect()
    casse_briquepos.bottom = background.get_rect().bottom - 60
    casse_briquepos.centerx = background.get_rect().left + 550
    background.blit(casse_brique, casse_briquepos)

    # Musique du fond
    pygame.mixer.music.load("musique_fond.wav")
    pygame.mixer.music.set_volume(0.1)
    pygame.mixer.music.play(-1)

    # fond du bouton mute
    groupe_fond = pygame.sprite.Group()
    fondmute = yamso.Carre(710, 10, 40, 40, (255, 39, 126), 0, background, 3)
    groupe_fond.add(fondmute)
    fondmute = yamso.Carre(710, 10, 40, 40, BLACK, 3, background, 3)
    groupe_fond.add(fondmute)

    mute = 0
    image_mute = pygame.image.load("mute.png")
    image_unmute = pygame.image.load("unmute.png")

    # Afficher le tout dans la fenêtre
    screen.blit(background, (0, 0))
    screen.blit(image_unmute, (712, 12))
    pygame.display.flip()

    gameover = False
    while not gameover:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameover = True

            # fonctionnement des bouttons
            elif event.type == MOUSEBUTTONDOWN and event.button == 1:

                if touryams.collidepoint(event.pos):
                    pygame.mixer.music.fadeout(500)
                    yamso.menu_yamso(screen)

                elif tourchevaux.collidepoint(event.pos):
                    pygame.mixer.music.fadeout(500)
                    chevalax.menu()

                elif tourdino.collidepoint(event.pos):
                    pygame.mixer.music.fadeout(500)
                    Dino_run_run.debut_jeu()

                elif tourbrique.collidepoint(event.pos):
                    pygame.mixer.music.fadeout(500)
                    Brickbreaker.jeu_super_breakeur()

                elif fondmute.carre.collidepoint(event.pos):
                    if mute == 0:
                        pygame.mixer.music.set_volume(0)
                        mute += 1
                        fondmute = yamso.Carre(710, 10, 40, 40, (255, 39, 126), 0, screen, 3)
                        groupe_fond.add(fondmute)
                        fondmute = yamso.Carre(710, 10, 40, 40, BLACK, 3, screen, 3)
                        groupe_fond.add(fondmute)
                        screen.blit(image_mute, (712, 12))
                        pygame.display.flip()
                    else:
                        pygame.mixer.music.set_volume(0.1)
                        mute -= 1
                        fondmute = yamso.Carre(710, 10, 40, 40, (255, 39, 126), 0, screen, 3)
                        groupe_fond.add(fondmute)
                        fondmute = yamso.Carre(710, 10, 40, 40, BLACK, 3, screen, 3)
                        groupe_fond.add(fondmute)
                        screen.blit(image_unmute, (712, 12))
                        pygame.display.flip()

                else:
                    print("Click dehors")

    pygame.quit()
    quit()


if __name__ == '__main__':
    menu_gen()
