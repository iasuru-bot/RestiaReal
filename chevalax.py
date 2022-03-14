import pygame
from pygame.locals import *
import main, yamso, lancerdes, time
from Couleur import *


class Pion(pygame.sprite.Sprite):
    def __init__(self, picture_path, pos_x, pos_y, couleur, surface):
        super().__init__()
        self.color = couleur
        self.etat = 0  # Etat 0 = zone départ 1=zone de course 2=zone escalier 3=pion sortie
        self.posx_base = pos_x
        self.posy_base = pos_y
        self.image = pygame.image.load(picture_path).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = pos_x
        self.rect.y = pos_y
        self.case = -1

    def moveto(self, posi_x, posi_y):
        self.rect.x = posi_x
        self.rect.y = posi_y


class Joueur(pygame.sprite.Sprite):
    def __init__(self, numero_joueur, couleur, res_des):
        super().__init__()
        self.numero = numero_joueur
        self.couleur = couleur
        self.de = res_des
        self.pion_gagne = 0


def tri_tab(tableau_de, ordre_joueur, ordre_couleur):
    for i in range(len(tableau_de) - 1, 0, -1):
        for j in range(i):
            if tableau_de[j] > tableau_de[j + 1]:
                tableau_de[j + 1], tableau_de[j] = tableau_de[j], tableau_de[j + 1]
                ordre_joueur[j + 1], ordre_joueur[j] = ordre_joueur[j], ordre_joueur[j + 1]
                ordre_couleur[j + 1], ordre_couleur[j] = ordre_couleur[j], ordre_couleur[j + 1]
    return tableau_de, ordre_joueur, ordre_couleur


def jeu(joueurs, pions, joueur1, joueur2, joueur3, joueur4, screen):
    pygame.display.set_caption('Chevalax')

    font = pygame.font.Font(None, 36)
    fond_fin = pygame.font.Font(None, 50)
    top_carre = screen.get_rect().top + 0
    left_carre = screen.get_rect().left + 0
    carre = pygame.Rect(left_carre, top_carre, 760, 660)
    pygame.draw.rect(screen, WHITE, carre, width=0)

    image_plateau = pygame.image.load("chevaux.png")
    screen.blit(image_plateau, (130, 40))

    # fond du bouton mute
    groupe_fond = pygame.sprite.Group()
    fondmute = yamso.Carre(710, 5, 38, 38, WHITE, 0, screen, 3)
    groupe_fond.add(fondmute)
    fondmute = yamso.Carre(710, 5, 38, 38, BLACK, 3, screen, 3)
    groupe_fond.add(fondmute)

    mute = 0
    image_mute = pygame.image.load("mute.png")
    image_unmute = pygame.image.load("unmute.png")
    screen.blit(image_unmute, (712, 7))

    # bouton retour
    groupe_bouton = pygame.sprite.Group()
    fondretour = yamso.Carre(screen.get_rect().centerx - 366, screen.get_rect().top + 10, 92, 34, (255, 51, 51), 0,
                             screen, 0)
    groupe_bouton.add(fondretour)
    fondretour = yamso.Carre(screen.get_rect().centerx - 366, screen.get_rect().top + 10, 92, 34, PUR_BLACK, 3,
                             screen, 0)
    groupe_bouton.add(fondretour)

    retour = font.render("Quitter", True, (102, 0, 0))
    retour_pos = retour.get_rect()
    retour_pos.top = screen.get_rect().top + 17
    retour_pos.centerx = screen.get_rect().centerx - 320
    screen.blit(retour, retour_pos)

    # bouton pour lancer le dé

    top_lancer_des = screen.get_rect().bottom - 340
    left_lancer_des = screen.get_rect().left + 15
    lancer_des = pygame.Rect(left_lancer_des, top_lancer_des, 100, 30)
    pygame.draw.rect(screen, GREY, lancer_des, width=0)
    pygame.draw.rect(screen, BLACK, lancer_des, width=2)

    lancer = font.render("Lancer", True, BLACK)
    lancer_pos = lancer.get_rect()
    lancer_pos.top = screen.get_rect().top + 325
    lancer_pos.centerx = screen.get_rect().centerx - 320
    screen.blit(lancer, lancer_pos)

    # fond ecran de fin
    top_fin = screen.get_rect().top + 30
    left_fin = screen.get_rect().left + 30
    fin = pygame.Rect(left_fin, top_fin, 700, 600)

    top_partie = screen.get_rect().top + 135
    left_partie = screen.get_rect().left + 290
    partie = pygame.Rect(left_partie, top_partie, 185, 5)

    fin_partie = fond_fin.render("Partie finie", True, BLACK)
    fin_partiepos = fin_partie.get_rect()
    fin_partiepos.top = screen.get_rect().top + 100
    fin_partiepos.centerx = screen.get_rect().centerx - 0

    top_rejouer = screen.get_rect().top + 420
    left_rejouer = screen.get_rect().left + 120
    rejouer_fin = pygame.Rect(left_rejouer, top_rejouer, 120, 40)

    rejouer = font.render("REJOUER", True, PUR_BLACK)
    rejouerpos = rejouer.get_rect()
    rejouerpos.top = screen.get_rect().top + 430
    rejouerpos.centerx = screen.get_rect().centerx - 200

    top_quitter = screen.get_rect().top + 420
    left_quitter = screen.get_rect().left + 520
    quitter_fin = pygame.Rect(left_quitter, top_quitter, 120, 40)

    quitter = font.render("QUITTER", True, PUR_BLACK)
    quitterpos = quitter.get_rect()
    quitterpos.top = screen.get_rect().top + 430
    quitterpos.centerx = screen.get_rect().centerx + 200

    top_merci = screen.get_rect().top + 335
    left_merci = screen.get_rect().left + 235
    merci_fin = pygame.Rect(left_merci, top_merci, 300, 5)

    merci = fond_fin.render("Merci d'avoir joué", True, PUR_BLACK)
    mercipos = merci.get_rect()
    mercipos.top = screen.get_rect().top + 300
    mercipos.centerx = screen.get_rect().centerx + 0
    # affichage du dé
    top_aff_des = screen.get_rect().top + 150
    left_aff_des = screen.get_rect().left + 15
    aff_des = pygame.Rect(left_aff_des, top_aff_des, 100, 100)
    pygame.draw.rect(screen, GREY, aff_des, width=0)
    pygame.draw.rect(screen, BLACK, aff_des, width=2)
    # affichage du tour

    top_tour = screen.get_rect().bottom - 200
    left_tour = screen.get_rect().left + 15
    tour = pygame.Rect(left_tour, top_tour, 100, 40)
    pygame.draw.rect(screen, BLACK, tour, width=2)

    tourjoueur = font.render("Tour", True, BLACK)
    tour_joueurpos = tourjoueur.get_rect()
    tour_joueurpos.top = screen.get_rect().top + 430
    tour_joueurpos.centerx = screen.get_rect().centerx - 320
    screen.blit(tourjoueur, tour_joueurpos)

    pygame.display.flip()
    gameover = False
    groupe_de = pygame.sprite.Group()
    print(pions)
    groupe_pion = pygame.sprite.Group()
    # apparition des pions
    if pions == 1:
        if joueur1 == 1 or joueur2 == 1 or joueur3 == 1 or joueur4 == 1:
            groupe_pion.add(Pion("Pions_r.png", 620, 120, 1, screen))
        if joueur1 == 2 or joueur2 == 2 or joueur3 == 2 or joueur4 == 2:
            groupe_pion.add(Pion("Pions_b.png", 220, 120, 2, screen))
        if joueur1 == 3 or joueur2 == 3 or joueur3 == 3 or joueur4 == 3:
            groupe_pion.add(Pion("Pions_j.png", 220, 510, 3, screen))
        if joueur1 == 4 or joueur2 == 4 or joueur3 == 4 or joueur4 == 4:
            groupe_pion.add(Pion("Pions_v.png", 620, 510, 4, screen))
    elif pions == 2:
        if joueur1 == 1 or joueur2 == 1 or joueur3 == 1 or joueur4 == 1:
            groupe_pion.add(Pion("Pions_r.png", 560, 120, 1, screen), Pion("Pions_r.png", 660, 120, 1, screen))
        if joueur1 == 2 or joueur2 == 2 or joueur3 == 2 or joueur4 == 2:
            groupe_pion.add(Pion("Pions_b.png", 170, 120, 2, screen), Pion("Pions_b.png", 260, 120, 2, screen))
        if joueur1 == 3 or joueur2 == 3 or joueur3 == 3 or joueur4 == 3:
            groupe_pion.add(Pion("Pions_j.png", 170, 510, 3, screen), Pion("Pions_j.png", 260, 510, 3, screen))
        if joueur1 == 4 or joueur2 == 4 or joueur3 == 4 or joueur4 == 4:
            groupe_pion.add(Pion("Pions_v.png", 560, 510, 4, screen), Pion("Pions_V.png", 660, 510, 4, screen))
    elif pions == 3:
        if joueur1 == 1 or joueur2 == 1 or joueur3 == 1 or joueur4 == 1:
            groupe_pion.add(Pion("Pions_r.png", 560, 90, 1, screen), Pion("Pions_r.png", 660, 90, 1, screen),
                            Pion("Pions_r.png", 610, 140, 1, screen))
        if joueur1 == 2 or joueur2 == 2 or joueur3 == 2 or joueur4 == 2:
            groupe_pion.add(Pion("Pions_b.png", 170, 90, 2, screen), Pion("Pions_b.png", 260, 90, 2, screen),
                            Pion("Pions_b.png", 220, 140, 2, screen))
        if joueur1 == 3 or joueur2 == 3 or joueur3 == 3 or joueur4 == 3:
            groupe_pion.add(Pion("Pions_j.png", 170, 450, 3, screen), Pion("Pions_j.png", 260, 450, 3, screen),
                            Pion("Pions_j.png", 220, 510, 3, screen))
        if joueur1 == 4 or joueur2 == 4 or joueur3 == 4 or joueur4 == 4:
            groupe_pion.add(Pion("Pions_v.png", 560, 450, 4, screen), Pion("Pions_V.png", 660, 450, 4, screen),
                            Pion("Pions_V.png", 610, 510, 4, screen))
    elif pions == 4:
        if joueur1 == 1 or joueur2 == 1 or joueur3 == 1 or joueur4 == 1:
            groupe_pion.add(Pion("Pions_r.png", 560, 70, 1, screen), Pion("Pions_r.png", 660, 70, 1, screen),
                            Pion("Pions_r.png", 560, 170, 1, screen), Pion("Pions_r.png", 660, 170, 1, screen))

        if joueur1 == 2 or joueur2 == 2 or joueur3 == 2 or joueur4 == 2:
            groupe_pion.add(Pion("Pions_b.png", 170, 70, 2, screen), Pion("Pions_b.png", 260, 70, 2, screen),
                            Pion("Pions_b.png", 170, 170, 2, screen), Pion("Pions_b.png", 260, 170, 2, screen))

        if joueur1 == 3 or joueur2 == 3 or joueur3 == 3 or joueur4 == 3:
            groupe_pion.add(Pion("Pions_j.png", 170, 450, 3, screen), Pion("Pions_j.png", 260, 450, 3, screen),
                            Pion("Pions_j.png", 170, 550, 3, screen), Pion("Pions_j.png", 260, 550, 3, screen))
        if joueur1 == 4 or joueur2 == 4 or joueur3 == 4 or joueur4 == 4:
            groupe_pion.add(Pion("Pions_v.png", 560, 450, 4, screen), Pion("Pions_v.png", 660, 450, 4, screen),
                            Pion("Pions_v.png", 560, 550, 4, screen), Pion("Pions_v.png", 660, 550, 4, screen))

    tableau_coordonnee = [(475, 46), (475, 97), (475, 147), (475, 197), (475, 250), (525, 250), (577, 250), (626, 250),
                          (678, 250), (678, 304), (683, 356), (630, 356), (580, 356), (530, 356), (479, 356),
                          (479, 410), (479, 460), (479, 510), (479, 560), (421, 557), (361, 557), (361, 507),
                          (361, 457), (361, 407), (361, 357), (306, 357), (256, 357), (206, 357), (156, 357),
                          (156, 303), (158, 252), (208, 252), (258, 252), (308, 252), (361, 252), (361, 197),
                          (361, 147), (361, 97), (361, 48), (420, 46)]
    tableau_terrain = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    print(tableau_terrain.count(0))
    tableau_escalier_rouge = [(419, 95), (419, 145), (419, 195), (418, 248)]
    tableau_escalier_vert = [(628, 304), (578, 304), (528, 303), (475, 303)]
    tableau_escalier_jaune = [(421, 507), (422, 457), (422, 407), (422, 353)]
    tableau_escalier_bleu = [(206, 303), (256, 303), (306, 303), (358, 302)]

    groupe_pion.draw(screen)
    pygame.display.flip()

    # initialisation de l'ordre de passage

    tourjoueurs1 = font.render("J1", True, BLACK)
    tour_joueurspos = tourjoueurs1.get_rect()
    tour_joueurspos.top = screen.get_rect().top + 470
    tour_joueurspos.centerx = screen.get_rect().centerx - 320
    screen.blit(tourjoueurs1, tour_joueurspos)

    tourjoueurs2 = font.render("J2", True, BLACK)

    tourjoueurs3 = font.render("J3", True, BLACK)

    tourjoueurs4 = font.render("J4", True, BLACK)
    pygame.display.flip()

    passage = 0
    tab_des = []
    tourjoueurs = []
    affichage_joueur = ["J1", "J2", "J3", "J4"]
    groupe_joueur = pygame.sprite.Group()
    tab_couleur = [joueur1, joueur2, joueur3, joueur4]
    ordre_couleur = []

    if tab_couleur[passage] == 1:
        couleur_fond = RED
    elif tab_couleur[passage] == 2:
        couleur_fond = BLUE
    elif tab_couleur[passage] == 3:
        couleur_fond = YELLOW
    elif tab_couleur[passage] == 4:
        couleur_fond = GREEN
    groupe_tour = pygame.sprite.Group()
    groupe_tour.add(
        yamso.Carre(screen.get_rect().left + 15, screen.get_rect().bottom - 200, 100, 40, couleur_fond, 0, screen, 0),
        yamso.Carre(screen.get_rect().left + 15, screen.get_rect().bottom - 200, 100, 40, BLACK, 2, screen, 0))
    premier_tour = yamso.Texte(affichage_joueur[passage], 50, screen.get_rect().bottom - 190, BLACK, 36, screen)

    pygame.display.flip()
    while passage != joueurs:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == MOUSEBUTTONDOWN and event.button == 1:
                if fondretour.carre.collidepoint(event.pos):
                    menu()
                elif fondmute.carre.collidepoint(event.pos):
                    if mute == 0:
                        pygame.mixer.music.set_volume(0)
                        mute += 1
                        fondmute = yamso.Carre(710, 5, 38, 38, WHITE, 0, screen, 3)
                        groupe_fond.add(fondmute)
                        fondmute = yamso.Carre(710, 5, 38, 38, BLACK, 3, screen, 3)
                        groupe_fond.add(fondmute)
                        screen.blit(image_mute, (712, 7))
                        pygame.display.flip()
                    else:
                        pygame.mixer.music.set_volume(0.1)
                        mute -= 1
                        fondmute = yamso.Carre(710, 5, 38, 38, WHITE, 0, screen, 3)
                        groupe_fond.add(fondmute)
                        fondmute = yamso.Carre(710, 5, 38, 38, BLACK, 3, screen, 3)
                        groupe_fond.add(fondmute)
                        screen.blit(image_unmute, (712, 7))
                        pygame.display.flip()
                elif lancer_des.collidepoint(event.pos):
                    lancerdes.animation_lancage_des_chevalax(screen)
                    res_de = lancerdes.lancer_chevalax()
                    posi_x = 65
                    posi_y = 200
                    # Affichage du résultat du tirage des dés
                    if res_de == 1:
                        de1 = yamso.De("des_1.png", posi_x, posi_y)
                        groupe_de.add(de1)
                        groupe_de.draw(screen)
                    elif res_de == 2:
                        de2 = yamso.De("des_2.png", posi_x, posi_y)
                        groupe_de.add(de2)
                        groupe_de.draw(screen)
                    elif res_de == 3:
                        de3 = yamso.De("des_3.png", posi_x, posi_y)
                        groupe_de.add(de3)
                        groupe_de.draw(screen)
                    elif res_de == 4:
                        de4 = yamso.De("des_4.png", posi_x, posi_y)
                        groupe_de.add(de4)
                        groupe_de.draw(screen)
                    elif res_de == 5:
                        de5 = yamso.De("des_5.png", posi_x, posi_y)
                        groupe_de.add(de5)
                        groupe_de.draw(screen)
                    elif res_de == 6:
                        de6 = yamso.De("des_6.png", posi_x, posi_y)
                        groupe_de.add(de6)
                        groupe_de.draw(screen)

                    nouv_joueur = Joueur(passage + 1, tab_couleur[passage], res_de)
                    groupe_joueur.add(nouv_joueur)
                    tourjoueurs.append(nouv_joueur.numero)
                    tab_des.append(nouv_joueur.de)
                    ordre_couleur.append(tab_couleur[passage])

                    passage += 1
                    if passage == 4:
                        break
                    if tab_couleur[passage] == 1:
                        couleur_fond = RED
                    elif tab_couleur[passage] == 2:
                        couleur_fond = BLUE
                    elif tab_couleur[passage] == 3:
                        couleur_fond = YELLOW
                    elif tab_couleur[passage] == 4:
                        couleur_fond = GREEN
                    groupe_tour = pygame.sprite.Group()
                    groupe_tour.add(
                        yamso.Carre(screen.get_rect().left + 15, screen.get_rect().bottom - 200, 100, 40, couleur_fond,
                                    0, screen,
                                    0),
                        yamso.Carre(screen.get_rect().left + 15, screen.get_rect().bottom - 200, 100, 40, BLACK, 2,
                                    screen, 0))
                    premier_tour = yamso.Texte(affichage_joueur[passage], 50,
                                               screen.get_rect().bottom - 190, BLACK, 36,
                                               screen)
                    pygame.display.flip()

    print(tourjoueurs)
    tab_des, tourjoueurs, ordre_couleur = tri_tab(tab_des, tourjoueurs, ordre_couleur)
    tourjoueurs = tourjoueurs[::-1]
    print(tourjoueurs)

    tableau_affichage_joueur = []
    for i in range(0, len(tourjoueurs)):
        str1 = "J" + str(tourjoueurs[i])
        tableau_affichage_joueur.append(str1)
    # le jeu
    print(tableau_affichage_joueur)

    tour_partie = ordre_couleur[::-1]
    tour_joueur = 0
    tour_jeu = tour_partie[tour_joueur]
    if tour_jeu == 1:
        couleur_fond = RED
    elif tour_jeu == 2:
        couleur_fond = BLUE
    elif tour_jeu == 3:
        couleur_fond = YELLOW
    elif tour_jeu == 4:
        couleur_fond = GREEN
    groupe_tour = pygame.sprite.Group()
    groupe_tour.add(
        yamso.Carre(screen.get_rect().left + 15, screen.get_rect().bottom - 200, 100, 40, couleur_fond, 0, screen,
                    0),
        yamso.Carre(screen.get_rect().left + 15, screen.get_rect().bottom - 200, 100, 40, BLACK, 2, screen, 0))
    premier_tour = yamso.Texte(tableau_affichage_joueur[tour_joueur], 50, screen.get_rect().bottom - 190, BLACK, 36,
                               screen)
    pygame.display.flip()

    clock = pygame.time.Clock()

    while not gameover:

        for joueur in groupe_joueur:
            if joueur.pion_gagne == pions:
                print("c'est la fin le joueur", joueur.numero, "a gagné")

                # affichage de l'ecran de fin
                pygame.draw.rect(screen, (65, 167, 216), fin, width=0)
                pygame.draw.rect(screen, BLACK, fin, width=2)
                pygame.draw.rect(screen, BLACK, partie, width=0)
                pygame.draw.rect(screen, BLACK, merci_fin, width=0)
                pygame.draw.rect(screen, (200, 8, 21), quitter_fin, width=0)
                pygame.draw.rect(screen, BLACK, quitter_fin, width=2)
                pygame.draw.rect(screen, (1, 215, 88), rejouer_fin, width=0)
                pygame.draw.rect(screen, BLACK, rejouer_fin, width=2)

                screen.blit(fin_partie, fin_partiepos)
                screen.blit(rejouer, rejouerpos)
                screen.blit(quitter, quitterpos)
                screen.blit(merci, mercipos)
                if joueur.couleur == 1:
                    couleur_fond = RED
                elif joueur.couleur == 2:
                    couleur_fond = BLUE
                elif joueur.couleur == 3:
                    couleur_fond = YELLOW
                elif joueur.couleur == 4:
                    couleur_fond = GREEN
                groupe_fond_fin= pygame.sprite.Group
                groupe_fond_fin.add(yamso.Carre(295, 190, 110, 38, couleur_fond, 0, screen, 3))

                str1 = "Le  joueur " + str(joueur.numero) + "  a gagné"
                joueur_vainqueur = font.render(str1, True, BLACK)
                joueurpos = joueur_vainqueur.get_rect()
                joueurpos.top = fin_partiepos.bottom + 65
                joueurpos.centerx = screen.get_rect().centerx
                screen.blit(joueur_vainqueur, joueurpos)
                pygame.display.flip()

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        gameover = True
                    # fonctionnement des bouttons
                    elif event.type == MOUSEBUTTONDOWN and event.button == 1:

                        if quitter_fin.collidepoint(event.pos):
                            main.menu_gen()
                        elif rejouer_fin.collidepoint(event.pos):
                            menu()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameover = True
            # fonctionnement des bouttons
            elif event.type == MOUSEBUTTONDOWN and event.button == 1:

                if fondretour.carre.collidepoint(event.pos):
                    menu()
                elif fondmute.carre.collidepoint(event.pos):
                    if mute == 0:
                        pygame.mixer.music.set_volume(0)
                        mute += 1
                        fondmute = yamso.Carre(710, 5, 38, 38, WHITE, 0, screen, 3)
                        groupe_fond.add(fondmute)
                        fondmute = yamso.Carre(710, 5, 38, 38, BLACK, 3, screen, 3)
                        groupe_fond.add(fondmute)
                        screen.blit(image_mute, (712, 7))
                        pygame.display.flip()
                    else:
                        pygame.mixer.music.set_volume(0.1)
                        mute -= 1
                        fondmute = yamso.Carre(710, 5, 38, 38, WHITE, 0, screen, 3)
                        groupe_fond.add(fondmute)
                        fondmute = yamso.Carre(710, 5, 38, 38, BLACK, 3, screen, 3)
                        groupe_fond.add(fondmute)
                        screen.blit(image_unmute, (712, 7))
                        pygame.display.flip()
                elif lancer_des.collidepoint(event.pos):
                    lancerdes.animation_lancage_des_chevalax(screen)
                    res_de = lancerdes.lancer_chevalax()
                    posi_x = 65
                    posi_y = 200
                    # Affichage du résultat du tirage des dés
                    if res_de == 1:
                        de1 = yamso.De("des_1.png", posi_x, posi_y)
                        groupe_de.add(de1)
                        groupe_de.draw(screen)
                    elif res_de == 2:
                        de2 = yamso.De("des_2.png", posi_x, posi_y)
                        groupe_de.add(de2)
                        groupe_de.draw(screen)
                    elif res_de == 3:
                        de3 = yamso.De("des_3.png", posi_x, posi_y)
                        groupe_de.add(de3)
                        groupe_de.draw(screen)
                    elif res_de == 4:
                        de4 = yamso.De("des_4.png", posi_x, posi_y)
                        groupe_de.add(de4)
                        groupe_de.draw(screen)
                    elif res_de == 5:
                        de5 = yamso.De("des_5.png", posi_x, posi_y)
                        groupe_de.add(de5)
                        groupe_de.draw(screen)
                    elif res_de == 6:
                        de6 = yamso.De("des_6.png", posi_x, posi_y)
                        groupe_de.add(de6)
                        groupe_de.draw(screen)
                    pygame.display.flip()
                    continuer = 0
                    while continuer == 0:
                        for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                continuer += 1
                                gameover = True
                            # Evenement si on clique sur le pion pour jouer de la couleur demandé. Ex: si c'est au rouge de jouer il faut cliquer sur un pion rouge
                            elif event.type == MOUSEBUTTONDOWN and event.button == 1:
                                if fondmute.carre.collidepoint(event.pos):
                                    if mute == 0:
                                        pygame.mixer.music.set_volume(0)
                                        mute += 1
                                        fondmute = yamso.Carre(710, 5, 38, 38, WHITE, 0, screen, 3)
                                        groupe_fond.add(fondmute)
                                        fondmute = yamso.Carre(710, 5, 38, 38, BLACK, 3, screen, 3)
                                        groupe_fond.add(fondmute)
                                        screen.blit(image_mute, (712, 7))
                                        pygame.display.flip()
                                    else:
                                        pygame.mixer.music.set_volume(0.1)
                                        mute -= 1
                                        fondmute = yamso.Carre(710, 5, 38, 38, WHITE, 0, screen, 3)
                                        groupe_fond.add(fondmute)
                                        fondmute = yamso.Carre(710, 5, 38, 38, BLACK, 3, screen, 3)
                                        groupe_fond.add(fondmute)
                                        screen.blit(image_unmute, (712, 7))
                                        pygame.display.flip()
                                if fondretour.carre.collidepoint(event.pos):
                                    menu()

                                for sprite in groupe_pion:
                                    if fondretour.carre.collidepoint(event.pos):
                                        menu()
                                    if sprite.rect.collidepoint(event.pos) and tour_jeu == sprite.color:
                                        print('Ce pion est de la bonne couleur')
                                        # Si le pion choisi est dans l'écurie et qu'on a fait 6
                                        if sprite.etat == 0 and res_de == 6:
                                            print("Sortie pion sur case départ en fonction couleur")
                                            # sortie pion
                                            if sprite.color == 1:
                                                print("Le pion a sortir est rouge")
                                                if tableau_terrain[0] == sprite.color:
                                                    print(
                                                        "le pion peut pas sortir car il y a déjà un rouge sur la case")
                                                else:
                                                    for i in groupe_pion:
                                                        if i.case == 0:
                                                            i.moveto(i.posx_base, i.posy_base)
                                                            i.etat = 0
                                                            print("Le pion mange l'autre")
                                                    nouv_pos_x, nouv_pos_y = tableau_coordonnee[0]
                                                    sprite.moveto(nouv_pos_x, nouv_pos_y)
                                                    tableau_terrain[0] = sprite.color
                                                    sprite.case = 0
                                                    sprite.etat = 1

                                            elif sprite.color == 2:
                                                print("Le pion a sortir est Bleu")
                                                if tableau_terrain[30] == sprite.color:
                                                    print("le pion peut pas sortir car il y a déjà un bleu sur la case")
                                                else:
                                                    for i in groupe_pion:
                                                        if i.case == 30:
                                                            i.moveto(i.posx_base, i.posy_base)
                                                            i.etat = 0
                                                            print("Le pion mange l'autre")
                                                    nouv_pos_x, nouv_pos_y = tableau_coordonnee[30]
                                                    sprite.moveto(nouv_pos_x, nouv_pos_y)
                                                    tableau_terrain[30] = sprite.color
                                                    sprite.case = 30
                                                    sprite.etat = 1

                                            elif sprite.color == 3:
                                                print("Le pion a sortir est jaune")
                                                if tableau_terrain[20] == sprite.color:
                                                    print(
                                                        "le pion peut pas sortir car il y a déjà un jaune sur la case")
                                                else:
                                                    for i in groupe_pion:
                                                        if i.case == 20:
                                                            i.moveto(i.posx_base, i.posy_base)
                                                            i.etat = 0
                                                    nouv_pos_x, nouv_pos_y = tableau_coordonnee[20]
                                                    sprite.moveto(nouv_pos_x, nouv_pos_y)
                                                    tableau_terrain[20] = sprite.color
                                                    sprite.case = 20
                                                    sprite.etat = 1

                                            elif sprite.color == 4:
                                                print("Le pion a sortir est vert")
                                                if tableau_terrain[10] == sprite.color:
                                                    print("le pion peut pas sortir car il y a déjà un vert sur la case")

                                                else:
                                                    for i in groupe_pion:
                                                        if i.case == 10:
                                                            i.moveto(i.posx_base, i.posy_base)
                                                            i.etat = 0
                                                            print("Le pion mange l'autre")
                                                    nouv_pos_x, nouv_pos_y = tableau_coordonnee[10]
                                                    sprite.moveto(nouv_pos_x, nouv_pos_y)
                                                    tableau_terrain[10] = sprite.color
                                                    sprite.case = 10
                                                    sprite.etat = 1

                                        elif sprite.etat == 1:

                                            if sprite.color == 1 and sprite.case == 39 and res_de == 1:
                                                # Test pour monter l'escalier
                                                libre = True
                                                for i in groupe_pion:
                                                    if i.etat == 2 and i.case == 1 and i.color == sprite.color:
                                                        libre = False
                                                print('allo rouge')
                                                if libre == True:
                                                    nouv_pos_x, nouv_pos_y = tableau_escalier_rouge[0]
                                                    sprite.moveto(nouv_pos_x, nouv_pos_y)
                                                    tableau_terrain[sprite.case] = 0
                                                    sprite.case = 1
                                                    sprite.etat = 2
                                            elif sprite.color == 2 and sprite.case == 29 and res_de == 1:
                                                # Test pour monter l'escalier
                                                libre = True
                                                for i in groupe_pion:
                                                    if i.etat == 2 and i.case == 1 and i.color == sprite.color:
                                                        libre = False
                                                print('allo bleu')
                                                if libre == True:
                                                    nouv_pos_x, nouv_pos_y = tableau_escalier_bleu[0]
                                                    sprite.moveto(nouv_pos_x, nouv_pos_y)
                                                    tableau_terrain[sprite.case] = 0
                                                    sprite.case = 1
                                                    sprite.etat = 2
                                            elif sprite.color == 3 and sprite.case == 19 and res_de == 1:
                                                # Test pour monter l'escalier
                                                libre = True
                                                for i in groupe_pion:
                                                    if i.etat == 2 and i.case == 1 and i.color == sprite.color:
                                                        libre = False
                                                print('allo jaune')
                                                if libre == True:
                                                    nouv_pos_x, nouv_pos_y = tableau_escalier_jaune[0]
                                                    sprite.moveto(nouv_pos_x, nouv_pos_y)
                                                    tableau_terrain[sprite.case] = 0
                                                    sprite.case = 1
                                                    sprite.etat = 2
                                            elif sprite.color == 4 and sprite.case == 9 and res_de == 1:
                                                # Test pour monter l'escalier
                                                libre = True
                                                for i in groupe_pion:
                                                    if i.etat == 2 and i.case == 1 and i.color == sprite.color:
                                                        libre = False
                                                print('allo vert')
                                                if libre == True:
                                                    nouv_pos_x, nouv_pos_y = tableau_escalier_vert[0]
                                                    sprite.moveto(nouv_pos_x, nouv_pos_y)
                                                    tableau_terrain[sprite.case] = 0
                                                    sprite.case = 1
                                                    sprite.etat = 2

                                            elif sprite.color == 1 and (sprite.case + res_de) > 39:
                                                # test pour voir si libre devant
                                                libre_devant = True
                                                for i in range(1, res_de):
                                                    if (sprite.case + i) > 39:
                                                        break
                                                    if tableau_terrain[(sprite.case + i) % 40] != 0:
                                                        libre_devant = False
                                                        print("Le pion ne peut pas avancer car pas libre devant")
                                                # Si libre devant alors je calcule les surplus que j'ai
                                                if libre_devant == True:
                                                    tableau_terrain[sprite.case] = 0
                                                    ancienne_case = sprite.case
                                                    en_trop = sprite.case + res_de - 39
                                                    sprite.case = 39
                                                    tableau_terrain[sprite.case] = sprite.color
                                                    # Test derriere moi avec la valeur en trop
                                                    libre_derriere = True
                                                    for i in range(1, en_trop):
                                                        if tableau_terrain[39 - i] != 0:
                                                            libre_derriere = False
                                                            print("Le pion ne peut pas avancer car pas libre derriere")
                                                    if libre_derriere == True:
                                                        # Si libre j'effectue le mouvement
                                                        if tableau_terrain[39 - en_trop] != 0:
                                                            for i in groupe_pion:
                                                                if i.case == 39 - en_trop and i.etat == 1:
                                                                    i.moveto(i.posx_base, i.posy_base)
                                                                    i.etat = 0
                                                        nouv_pos_x, nouv_pos_y = tableau_coordonnee[39 - en_trop]
                                                        sprite.moveto(nouv_pos_x, nouv_pos_y)
                                                        tableau_terrain[sprite.case] = 0
                                                        sprite.case = 39 - en_trop
                                                        tableau_terrain[sprite.case] = sprite.color
                                                    else:
                                                        tableau_terrain[sprite.case] = 0
                                                        sprite.case = ancienne_case
                                                        tableau_terrain[sprite.case] = sprite.color



                                            elif sprite.color == 2 and (
                                                    sprite.case + res_de) > 29 and 29 >= sprite.case >= 22:
                                                # test pour voir si libre devant
                                                libre_devant = True
                                                for i in range(1, res_de):
                                                    if (sprite.case + i) > 29:
                                                        break
                                                    if tableau_terrain[(sprite.case + i) % 40] != 0:
                                                        libre_devant = False
                                                        print("Le pion ne peut pas avancer car pas libre devant")
                                                # Si libre devant alors je calcule les surplus que j'ai
                                                if libre_devant == True:
                                                    tableau_terrain[sprite.case] = 0
                                                    ancienne_case = sprite.case
                                                    en_trop = sprite.case + res_de - 29
                                                    sprite.case = 29
                                                    tableau_terrain[sprite.case] = sprite.color
                                                    # Test derriere moi avec la valeur en trop
                                                    libre_derriere = True
                                                    for i in range(1, en_trop):
                                                        if tableau_terrain[29 - i] != 0:
                                                            libre_derriere = False
                                                            print("Le pion ne peut pas avancer car pas libre derriere")
                                                    if libre_derriere == True:
                                                        # Si libre j'effectue le mouvement
                                                        if tableau_terrain[29 - en_trop] != 0:
                                                            for i in groupe_pion:
                                                                if i.case == 29 - en_trop and i.etat == 1:
                                                                    i.moveto(i.posx_base, i.posy_base)
                                                                    i.etat = 0
                                                        nouv_pos_x, nouv_pos_y = tableau_coordonnee[29 - en_trop]
                                                        sprite.moveto(nouv_pos_x, nouv_pos_y)
                                                        tableau_terrain[sprite.case] = 0
                                                        sprite.case = 29 - en_trop
                                                        tableau_terrain[sprite.case] = sprite.color
                                                    else:
                                                        tableau_terrain[sprite.case] = 0
                                                        sprite.case = ancienne_case
                                                        tableau_terrain[sprite.case] = sprite.color

                                            elif sprite.color == 3 and (
                                                    sprite.case + res_de) > 19 and 19 >= sprite.case >= 12:
                                                # test pour voir si libre devant
                                                libre_devant = True
                                                for i in range(1, res_de):
                                                    if (sprite.case + i) > 19:
                                                        break
                                                    if tableau_terrain[(sprite.case + i) % 40] != 0:
                                                        libre_devant = False
                                                        print("Le pion ne peut pas avancer car pas libre devant")
                                                # Si libre devant alors je calcule les surplus que j'ai
                                                if libre_devant == True:
                                                    tableau_terrain[sprite.case] = 0
                                                    ancienne_case = sprite.case
                                                    en_trop = sprite.case + res_de - 19
                                                    sprite.case = 19
                                                    tableau_terrain[sprite.case] = sprite.color
                                                    # Test derriere moi avec la valeur en trop
                                                    libre_derriere = True
                                                    for i in range(1, en_trop):
                                                        if tableau_terrain[9 - i] != 0:
                                                            libre_derriere = False
                                                            print("Le pion ne peut pas avancer car pas libre derriere")
                                                    if libre_derriere == True:
                                                        # Si libre j'effectue le mouvement
                                                        if tableau_terrain[19 - en_trop] != 0:
                                                            for i in groupe_pion:
                                                                if i.case == 19 - en_trop and i.etat == 1:
                                                                    i.moveto(i.posx_base, i.posy_base)
                                                                    i.etat = 0
                                                        nouv_pos_x, nouv_pos_y = tableau_coordonnee[19 - en_trop]
                                                        sprite.moveto(nouv_pos_x, nouv_pos_y)
                                                        tableau_terrain[sprite.case] = 0
                                                        sprite.case = 19 - en_trop
                                                        tableau_terrain[sprite.case] = sprite.color
                                                    else:
                                                        tableau_terrain[sprite.case] = 0
                                                        sprite.case = ancienne_case
                                                        tableau_terrain[sprite.case] = sprite.color


                                            elif sprite.color == 4 and (
                                                    sprite.case + res_de) > 9 and 9 >= sprite.case >= 2:
                                                # test pour voir si libre devant
                                                libre_devant = True
                                                for i in range(1, res_de):
                                                    if (sprite.case + i) > 9:
                                                        break
                                                    if tableau_terrain[(sprite.case + i) % 40] != 0:
                                                        libre_devant = False
                                                        print("Le pion ne peut pas avancer car pas libre devant")
                                                # Si libre devant alors je calcule les surplus que j'ai
                                                if libre_devant == True:
                                                    tableau_terrain[sprite.case] = 0
                                                    ancienne_case = sprite.case
                                                    en_trop = sprite.case + res_de - 9
                                                    sprite.case = 9
                                                    tableau_terrain[sprite.case] = sprite.color
                                                    # Test derriere moi avec la valeur en trop
                                                    libre_derriere = True
                                                    for i in range(1, en_trop):
                                                        if tableau_terrain[19 - i] != 0:
                                                            libre_derriere = False
                                                            print("Le pion ne peut pas avancer car pas libre derriere")
                                                    if libre_derriere == True:
                                                        # Si libre j'effectue le mouvement
                                                        if tableau_terrain[9 - en_trop] != 0:
                                                            for i in groupe_pion:
                                                                if i.case == 9 - en_trop and i.etat == 1:
                                                                    i.moveto(i.posx_base, i.posy_base)
                                                                    i.etat = 0
                                                        nouv_pos_x, nouv_pos_y = tableau_coordonnee[9 - en_trop]
                                                        sprite.moveto(nouv_pos_x, nouv_pos_y)
                                                        tableau_terrain[sprite.case] = 0
                                                        sprite.case = 9 - en_trop
                                                        tableau_terrain[sprite.case] = sprite.color
                                                    else:
                                                        tableau_terrain[sprite.case] = 0
                                                        sprite.case = ancienne_case
                                                        tableau_terrain[sprite.case] = sprite.color

                                            else:
                                                # Tester les res_de cases devant lui pour voir s'il peut avancer
                                                nouv_case = (sprite.case + res_de) % 40
                                                libre = True
                                                for i in range(1, res_de):
                                                    if tableau_terrain[(sprite.case + i) % 40] != 0:
                                                        libre = False
                                                        print("Le pion ne peut pas avancer")
                                                if libre == True:
                                                    for i in groupe_pion:
                                                        if i.case == nouv_case and i.etat == 1:
                                                            i.moveto(i.posx_base, i.posy_base)
                                                            i.etat = 0
                                                            print(
                                                                "le pion mange un autre pion car il arrive pile dessus")
                                                    print("Le pion avance sur la course")
                                                    nouv_pos_x, nouv_pos_y = tableau_coordonnee[nouv_case]
                                                    sprite.moveto(nouv_pos_x, nouv_pos_y)
                                                    tableau_terrain[sprite.case] = 0
                                                    sprite.case = nouv_case
                                                    tableau_terrain[sprite.case] = sprite.color

                                        elif sprite.etat == 2:
                                            print('yo je monte')
                                            if res_de == 2:
                                                libre = True
                                                for i in groupe_pion:
                                                    if i.etat == 2 and i.case == 2 and i.color == sprite.color:
                                                        libre = False
                                                if sprite.color == 1 and sprite.case == 1:
                                                    # Test pour monter l'escalier
                                                    if libre == True:
                                                        nouv_pos_x, nouv_pos_y = tableau_escalier_rouge[1]
                                                        sprite.moveto(nouv_pos_x, nouv_pos_y)
                                                        sprite.case += 1
                                                elif sprite.color == 2 and sprite.case == 1:
                                                    # Test pour monter l'escalier
                                                    if libre == True:
                                                        nouv_pos_x, nouv_pos_y = tableau_escalier_bleu[1]
                                                        sprite.moveto(nouv_pos_x, nouv_pos_y)
                                                        sprite.case += 1
                                                elif sprite.color == 3 and sprite.case == 1:
                                                    # Test pour monter l'escalier
                                                    if libre == True:
                                                        nouv_pos_x, nouv_pos_y = tableau_escalier_jaune[1]
                                                        sprite.moveto(nouv_pos_x, nouv_pos_y)
                                                        sprite.case += 1
                                                elif sprite.color == 4 and sprite.case == 1:
                                                    # Test pour monter l'escalier
                                                    if libre == True:
                                                        nouv_pos_x, nouv_pos_y = tableau_escalier_jaune[1]
                                                        sprite.moveto(nouv_pos_x, nouv_pos_y)
                                                        sprite.case += 1
                                            elif res_de == 3:
                                                libre = True
                                                for i in groupe_pion:
                                                    if i.etat == 2 and i.case == 3 and i.color == sprite.color:
                                                        libre = False
                                                if sprite.color == 1 and sprite.case == 2:
                                                    # Test pour monter l'escalier
                                                    if libre == True:
                                                        nouv_pos_x, nouv_pos_y = tableau_escalier_rouge[2]
                                                        sprite.moveto(nouv_pos_x, nouv_pos_y)
                                                        sprite.case += 1
                                                elif sprite.color == 2 and sprite.case == 2:
                                                    # Test pour monter l'escalier
                                                    if libre == True:
                                                        nouv_pos_x, nouv_pos_y = tableau_escalier_bleu[2]
                                                        sprite.moveto(nouv_pos_x, nouv_pos_y)
                                                        sprite.case += 1
                                                elif sprite.color == 3 and sprite.case == 2:
                                                    # Test pour monter l'escalier
                                                    if libre == True:
                                                        nouv_pos_x, nouv_pos_y = tableau_escalier_jaune[2]
                                                        sprite.moveto(nouv_pos_x, nouv_pos_y)
                                                        sprite.case += 1
                                                elif sprite.color == 4 and sprite.case == 2:
                                                    # Test pour monter l'escalier
                                                    if libre == True:
                                                        nouv_pos_x, nouv_pos_y = tableau_escalier_jaune[2]
                                                        sprite.moveto(nouv_pos_x, nouv_pos_y)
                                                        sprite.case += 1
                                            elif res_de == 4:
                                                libre = True
                                                for i in groupe_pion:
                                                    if i.etat == 2 and i.case == 4 and i.color == sprite.color:
                                                        libre = False
                                                if sprite.color == 1 and sprite.case == 3:
                                                    # Test pour monter l'escalier
                                                    if libre == True:
                                                        nouv_pos_x, nouv_pos_y = tableau_escalier_rouge[3]
                                                        sprite.moveto(nouv_pos_x, nouv_pos_y)
                                                        sprite.case += 1
                                                elif sprite.color == 2 and sprite.case == 3:
                                                    # Test pour monter l'escalier
                                                    if libre == True:
                                                        nouv_pos_x, nouv_pos_y = tableau_escalier_bleu[3]
                                                        sprite.moveto(nouv_pos_x, nouv_pos_y)
                                                        sprite.case += 1
                                                elif sprite.color == 3 and sprite.case == 3:
                                                    # Test pour monter l'escalier
                                                    if libre == True:
                                                        nouv_pos_x, nouv_pos_y = tableau_escalier_jaune[3]
                                                        sprite.moveto(nouv_pos_x, nouv_pos_y)
                                                        sprite.case += 1
                                                elif sprite.color == 4 and sprite.case == 3:
                                                    # Test pour monter l'escalier
                                                    if libre == True:
                                                        nouv_pos_x, nouv_pos_y = tableau_escalier_jaune[3]
                                                        sprite.moveto(nouv_pos_x, nouv_pos_y)
                                                        sprite.case += 1
                                            elif res_de == 6 and sprite.case == 4:
                                                sprite.etat = 3
                                                for joueur in groupe_joueur:
                                                    if joueur.couleur == sprite.color:
                                                        joueur.pion_gagne += 1
                                                sprite.kill()

                                        else:
                                            print("Le pion ne peut pas être joué !")

                                        if res_de != 6:
                                            # Tour du joueur suivant
                                            tour_joueur += 1
                                            if tour_joueur == len(tour_partie):
                                                tour_joueur = 0
                                            tour_jeu = tour_partie[tour_joueur]
                                        continuer += 1
                                        if tour_jeu == 1:
                                            couleur_fond = RED
                                        elif tour_jeu == 2:
                                            couleur_fond = BLUE
                                        elif tour_jeu == 3:
                                            couleur_fond = YELLOW
                                        elif tour_jeu == 4:
                                            couleur_fond = GREEN
                                        groupe_tour = pygame.sprite.Group()
                                        groupe_tour.add(
                                            yamso.Carre(screen.get_rect().left + 15, screen.get_rect().bottom - 200,
                                                        100, 40, couleur_fond, 0, screen,
                                                        0),
                                            yamso.Carre(screen.get_rect().left + 15, screen.get_rect().bottom - 200,
                                                        100, 40, BLACK, 2, screen, 0))
                                        premier_tour = yamso.Texte(tableau_affichage_joueur[tour_joueur], 50,
                                                                   screen.get_rect().bottom - 190, BLACK, 36,
                                                                   screen)
                                        pygame.display.flip()

                                groupe_pion.update()
                                screen.blit(image_plateau, (130, 40))
                                groupe_pion.draw(screen)
                                pygame.display.flip()
        # Number of frames per secong e.g. 60
        clock.tick(60)
    pygame.quit()
    quit()


def prepjeu(screen):
    pygame.display.set_caption("Chevalax")

    fond_prep_jeu = pygame.Surface(screen.get_size())
    fond_prep_jeu = fond_prep_jeu.convert()
    fond_prep_jeu.fill(PERFECT_BLUE)

    # afficher la fenêtre
    screen.blit(fond_prep_jeu, (0, 0))


    # Fond du titre
    bandeau = pygame.Rect(0, 75, 760, 38)
    pygame.draw.rect(screen, (0, 0, 102), bandeau, width=10)
    pygame.draw.rect(screen, (0, 105, 204), bandeau, width=0)

    groupe_bandeau = pygame.sprite.Group()
    fondprep_cheval = yamso.Carre(screen.get_rect().centerx - 225, screen.get_rect().top + 50, 450, 90, (109, 50, 204),
                                  0, screen, 20)
    groupe_bandeau.add(fondprep_cheval)
    fond_prep_cheval = yamso.Carre(screen.get_rect().centerx - 225, screen.get_rect().top + 50, 450, 90, (0, 0, 102),
                                   10, screen, 20)
    groupe_bandeau.add(fond_prep_cheval)
    degrade_prep_cheval = yamso.Carre(screen.get_rect().centerx - 220, screen.get_rect().top + 55, 440, 80,
                                      (0, 105, 204),
                                      10, screen, 20)
    groupe_bandeau.add(degrade_prep_cheval)

    # Fond bouton
    groupe_bouton = pygame.sprite.Group()
    fondretour = yamso.Carre(screen.get_rect().centerx - 366, screen.get_rect().top + 10, 92, 34, (255, 51, 51), 0,
                             screen, 0)
    groupe_bouton.add(fondretour)
    fondretour = yamso.Carre(screen.get_rect().centerx - 366, screen.get_rect().top + 10, 92, 34, PUR_BLACK, 3,
                             screen, 0)
    groupe_bouton.add(fondretour)

    # fond du choix 2
    top_j2 = screen.get_rect().bottom - 388
    left_j2 = screen.get_rect().left + 315
    j2 = pygame.Rect(left_j2, top_j2, 120, 30)
    pygame.draw.rect(screen, (109, 50, 204), j2, width=0)
    pygame.draw.rect(screen, BLACK, j2, width=2)

    # fond du choix 3
    top_j3 = screen.get_rect().bottom - 188
    left_j3 = screen.get_rect().left + 160
    j3 = pygame.Rect(left_j3, top_j3, 118, 30)
    pygame.draw.rect(screen, (109, 50, 204), j3, width=0)
    pygame.draw.rect(screen, BLACK, j3, width=2)

    # fond du choix 4
    top_j4 = screen.get_rect().bottom - 188
    left_j4 = screen.get_rect().left + 455
    j4 = pygame.Rect(left_j4, top_j4, 120, 30)
    pygame.draw.rect(screen, (109, 50, 204), j4, width=0)
    pygame.draw.rect(screen, BLACK, j4, width=2)

    # Affichage d'un texte

    font = pygame.font.Font(None, 36)
    titre = font.render("Chevalax :", True, BLACK)
    titrepos = titre.get_rect()
    titrepos.top = screen.get_rect().top + 70
    titrepos.centerx = screen.get_rect().centerx
    screen.blit(titre, titrepos)

    sous_titre = font.render("Veuillez choisir vos paramètres:", True, BLACK)
    textpos = sous_titre.get_rect()
    textpos.top = screen.get_rect().top + 100
    textpos.centerx = screen.get_rect().centerx
    screen.blit(sous_titre, textpos)

    consigne = font.render("Combien y a-t-il de joueur ?", True, BLACK)
    consignepos = consigne.get_rect()
    consignepos.top = screen.get_rect().top + 150
    consignepos.centerx = screen.get_rect().centerx
    screen.blit(consigne, consignepos)

    retour_menu = font.render("Retour", True, (102, 0, 0))
    retour_menupos = retour_menu.get_rect()
    retour_menupos.top = screen.get_rect().top + 17
    retour_menupos.centerx = screen.get_rect().centerx - 320
    screen.blit(retour_menu, retour_menupos)

    joueur_2 = font.render("2 joueurs", True, BLACK)
    joueur_2pos = joueur_2.get_rect()
    joueur_2pos.bottom = screen.get_rect().bottom - 360
    joueur_2pos.centerx = screen.get_rect().left + 375
    screen.blit(joueur_2, joueur_2pos)

    joueur_3 = font.render("3 joueurs", True, BLACK)
    joueur_3pos = joueur_3.get_rect()
    joueur_3pos.bottom = screen.get_rect().bottom - 160
    joueur_3pos.centerx = screen.get_rect().left + 220
    screen.blit(joueur_3, joueur_3pos)

    joueur_4 = font.render("4 joueurs", True, BLACK)
    joueur_4pos = joueur_4.get_rect()
    joueur_4pos.bottom = screen.get_rect().bottom - 160
    joueur_4pos.centerx = screen.get_rect().left + 515
    screen.blit(joueur_4, joueur_4pos)

    # fond du bouton mute
    groupe_fond = pygame.sprite.Group()
    fondmute = yamso.Carre(710, 5, 38, 38, PERFECT_BLUE, 0, screen, 3)
    groupe_fond.add(fondmute)
    fondmute = yamso.Carre(710, 5, 38, 38, BLACK, 3, screen, 3)
    groupe_fond.add(fondmute)

    mute = 0
    image_mute = pygame.image.load("mute.png")
    image_unmute = pygame.image.load("unmute.png")
    screen.blit(image_unmute, (712, 7))

    pygame.display.flip()
    joueurs = 5  # on le met a 5 car de 1 à 4 on aura des valeurs existantes et 0 le rendrait egal au choix inital.
    pions = 0
    gameover = False
    rep_q1 = 0
    rep_q2 = 0
    joueur1 = 0  # 0 va considérer que la personne n'a pas choisi de couleur. Les valeurs de  1 à 4 vont être les différentes couleurs
    joueur2 = 0
    joueur3 = 0
    joueur4 = 0
    choix = 0
    groupe_choix = pygame.sprite.Group()
    while not gameover:
        if rep_q1 == 1:
            # fond du nouveau carré qui va "effacer les autres"
            top_carre = screen.get_rect().top + 150
            left_carre = screen.get_rect().left + 0
            carre = pygame.Rect(left_carre, top_carre, 760, 520)
            pygame.draw.rect(screen, PERFECT_BLUE, carre, width=0)

            # fonds des choix

            top_pion1 = screen.get_rect().bottom - 380
            left_pion1 = screen.get_rect().left + 160
            pion1 = pygame.Rect(left_pion1, top_pion1, 120, 30)
            pygame.draw.rect(screen, (109, 50, 204), pion1, width=0)
            pygame.draw.rect(screen, BLACK, pion1, width=2)

            top_pion2 = screen.get_rect().bottom - 380
            left_pion2 = screen.get_rect().left + 455
            pion2 = pygame.Rect(left_pion2, top_pion2, 120, 30)
            pygame.draw.rect(screen, (109, 50, 204), pion2, width=0)
            pygame.draw.rect(screen, BLACK, pion2, width=2)

            # fond du choix 3
            top_pion3 = screen.get_rect().bottom - 188
            left_pion3 = screen.get_rect().left + 160
            pion3 = pygame.Rect(left_pion3, top_pion3, 118, 30)
            pygame.draw.rect(screen, (109, 50, 204), pion3, width=0)
            pygame.draw.rect(screen, BLACK, pion3, width=2)

            # fond du choix 4
            top_pion4 = screen.get_rect().bottom - 188
            left_pion4 = screen.get_rect().left + 455
            pion4 = pygame.Rect(left_pion4, top_pion4, 120, 30)
            pygame.draw.rect(screen, (109, 50, 204), pion4, width=0)
            pygame.draw.rect(screen, BLACK, pion4, width=2)

            # affichage des textes

            consigne = font.render("Combien voulez-vous de pions ?", True, BLACK)
            consignepos = consigne.get_rect()
            consignepos.top = screen.get_rect().top + 150
            consignepos.centerx = screen.get_rect().centerx
            screen.blit(consigne, consignepos)

            pions1 = font.render("1 pion", True, BLACK)
            pions1pos = pions1.get_rect()
            pions1pos.bottom = screen.get_rect().bottom - 350
            pions1pos.centerx = screen.get_rect().left + 220
            screen.blit(pions1, pions1pos)

            pions2 = font.render("2 pions", True, BLACK)
            pions2pos = pions2.get_rect()
            pions2pos.bottom = screen.get_rect().bottom - 350
            pions2pos.centerx = screen.get_rect().left + 515
            screen.blit(pions2, pions2pos)

            pions3 = font.render("3 pions", True, BLACK)
            pions3pos = pions3.get_rect()
            pions3pos.bottom = screen.get_rect().bottom - 160
            pions3pos.centerx = screen.get_rect().left + 220
            screen.blit(pions3, pions3pos)

            pions4 = font.render("4 pions", True, BLACK)
            pions4pos = pions4.get_rect()
            pions4pos.bottom = screen.get_rect().bottom - 160
            pions4pos.centerx = screen.get_rect().left + 515
            screen.blit(pions4, pions4pos)

            pygame.display.flip()
            rep_q1 += 1

        if rep_q2 == 1:
            # fond du nouveau carré qui va "effacer les autres"
            top_carre = screen.get_rect().top + 150
            left_carre = screen.get_rect().left + 0
            carre = pygame.Rect(left_carre, top_carre, 760, 520)
            pygame.draw.rect(screen, PERFECT_BLUE, carre, width=0)

            # fonds des choix

            top_couleur1 = screen.get_rect().bottom - 380
            left_couleur1 = screen.get_rect().left + 160
            couleur1 = pygame.Rect(left_couleur1, top_couleur1, 120, 30)
            pygame.draw.rect(screen, RED, couleur1, width=0)
            pygame.draw.rect(screen, BLACK, couleur1, width=2)

            top_couleur2 = screen.get_rect().bottom - 380
            left_couleur2 = screen.get_rect().left + 455
            couleur2 = pygame.Rect(left_couleur2, top_couleur2, 120, 30)
            pygame.draw.rect(screen, BLUE, couleur2, width=0)
            pygame.draw.rect(screen, BLACK, couleur2, width=2)

            # fond du choix 3
            top_couleur3 = screen.get_rect().bottom - 188
            left_couleur3 = screen.get_rect().left + 160
            couleur3 = pygame.Rect(left_couleur3, top_couleur3, 118, 30)
            pygame.draw.rect(screen, YELLOW, couleur3, width=0)
            pygame.draw.rect(screen, BLACK, couleur3, width=2)

            # fond du choix 4
            top_couleur4 = screen.get_rect().bottom - 188
            left_couleur4 = screen.get_rect().left + 455
            couleur4 = pygame.Rect(left_couleur4, top_couleur4, 120, 30)
            pygame.draw.rect(screen, GREEN, couleur4, width=0)
            pygame.draw.rect(screen, BLACK, couleur4, width=2)

            # affichage des textes

            consigne = font.render("Quelle couleur voulez-vous prendre ?", True, BLACK)
            consignepos = consigne.get_rect()
            consignepos.top = screen.get_rect().top + 150
            consignepos.centerx = screen.get_rect().centerx
            screen.blit(consigne, consignepos)

            rouge = font.render("Rouge", True, BLACK)
            rougepos = rouge.get_rect()
            rougepos.bottom = screen.get_rect().bottom - 350
            rougepos.centerx = screen.get_rect().left + 220
            screen.blit(rouge, rougepos)

            choix_j1 = font.render("J1", True, BLACK)
            choix_j1pos = choix_j1.get_rect()
            choix_j1pos.bottom = screen.get_rect().bottom - 15
            choix_j1pos.centerx = screen.get_rect().left + 20
            screen.blit(choix_j1, choix_j1pos)

            choix_j2 = font.render("J2", True, BLACK)
            choix_j2pos = choix_j2.get_rect()
            choix_j2pos.bottom = screen.get_rect().bottom - 15
            choix_j2pos.centerx = screen.get_rect().left + 70
            screen.blit(choix_j2, choix_j2pos)

            if joueurs == 3 or joueurs == 4:
                choix_j3 = font.render("J3", True, BLACK)
                choix_j3pos = choix_j3.get_rect()
                choix_j3pos.bottom = screen.get_rect().bottom - 15
                choix_j3pos.centerx = screen.get_rect().left + 120
                screen.blit(choix_j3, choix_j3pos)

                if joueurs == 4:
                    choix_j4 = font.render("J4", True, BLACK)
                    choix_j4pos = choix_j4.get_rect()
                    choix_j4pos.bottom = screen.get_rect().bottom - 15
                    choix_j4pos.centerx = screen.get_rect().left + 170
                    screen.blit(choix_j4, choix_j4pos)

            bleu = font.render("Bleu", True, BLACK)
            bleupos = bleu.get_rect()
            bleupos.bottom = screen.get_rect().bottom - 350
            bleupos.centerx = screen.get_rect().left + 515
            screen.blit(bleu, bleupos)

            jaune = font.render("Jaune", True, BLACK)
            jaunepos = jaune.get_rect()
            jaunepos.bottom = screen.get_rect().bottom - 160
            jaunepos.centerx = screen.get_rect().left + 220
            screen.blit(jaune, jaunepos)

            vert = font.render("Vert", True, BLACK)
            vertpos = vert.get_rect()
            vertpos.bottom = screen.get_rect().bottom - 160
            vertpos.centerx = screen.get_rect().left + 515
            screen.blit(vert, vertpos)

            pygame.display.flip()
            rep_q2 += 1
            r = 0
            b = 0
            j = 0
            v = 0

        # Partie affichant les couleurs en dessous de chaque joueurs
        if choix != 0 and color != 0:
            coordonnex = [3, 53, 103, 153]
            coordonney = 618
            fond_joueur = yamso.Carre(coordonnex[choix - 1], coordonney, 35, 28, color, 0, screen, 0)
            groupe_choix.add(fond_joueur)

            if choix == 1:
                choix_j1 = font.render("J1", True, BLACK)
                choix_j1pos = choix_j1.get_rect()
                choix_j1pos.bottom = screen.get_rect().bottom - 15
                choix_j1pos.centerx = screen.get_rect().left + 20
                screen.blit(choix_j1, choix_j1pos)
            elif choix == 2:

                choix_j2 = font.render("J2", True, BLACK)
                choix_j2pos = choix_j2.get_rect()
                choix_j2pos.bottom = screen.get_rect().bottom - 15
                choix_j2pos.centerx = screen.get_rect().left + 70
                screen.blit(choix_j2, choix_j2pos)
            elif choix == 3:
                choix_j3 = font.render("J3", True, BLACK)
                choix_j3pos = choix_j3.get_rect()
                choix_j3pos.bottom = screen.get_rect().bottom - 15
                choix_j3pos.centerx = screen.get_rect().left + 120
                screen.blit(choix_j3, choix_j3pos)
            else:
                choix_j4 = font.render("J4", True, BLACK)
                choix_j4pos = choix_j4.get_rect()
                choix_j4pos.bottom = screen.get_rect().bottom - 15
                choix_j4pos.centerx = screen.get_rect().left + 170
                screen.blit(choix_j4, choix_j4pos)
            pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameover = True
            if choix == joueurs:
                jeu(joueurs, pions, joueur1, joueur2, joueur3, joueur4, screen)
            # fonctionnement des bouttons
            elif event.type == MOUSEBUTTONDOWN and event.button == 1:

                if fondretour.carre.collidepoint(event.pos):
                    menu()
                elif fondmute.carre.collidepoint(event.pos):
                    if mute == 0:
                        pygame.mixer.music.set_volume(0)
                        mute += 1
                        fondmute = yamso.Carre(710, 5, 38, 38, PERFECT_BLUE, 0, screen, 3)
                        groupe_fond.add(fondmute)
                        fondmute = yamso.Carre(710, 5, 38, 38, BLACK, 3, screen, 3)
                        groupe_fond.add(fondmute)
                        screen.blit(image_mute, (712, 7))
                        pygame.display.flip()
                    else:
                        pygame.mixer.music.set_volume(0.1)
                        mute -= 1
                        fondmute = yamso.Carre(710, 5, 38, 38, PERFECT_BLUE, 0, screen, 3)
                        groupe_fond.add(fondmute)
                        fondmute = yamso.Carre(710, 5, 38, 38, BLACK, 3, screen, 3)
                        groupe_fond.add(fondmute)
                        screen.blit(image_unmute, (712, 7))
                        pygame.display.flip()
                elif rep_q1 == 0:
                    if j2.collidepoint(event.pos) and rep_q1 == 0:
                        joueurs = 2
                        rep_q1 = 1
                        print('joueurs:', joueurs)
                    elif j3.collidepoint(event.pos) and rep_q1 == 0:
                        joueurs = 3
                        rep_q1 = 1
                        print('joueurs:', joueurs)
                    elif j4.collidepoint(event.pos) and rep_q1 == 0:
                        joueurs = 4
                        rep_q1 = 1
                        print("Joueurs:", joueurs)
                elif rep_q2 == 0 and rep_q1 == 2:
                    if pion1.collidepoint(event.pos) and rep_q2 == 0:
                        pions = 1
                        rep_q2 = 1

                        print("pions:", pions)
                    elif pion2.collidepoint(event.pos) and rep_q2 == 0:
                        pions = 2
                        rep_q2 = 1

                        print("pions:", pions)
                    elif pion3.collidepoint(event.pos) and rep_q2 == 0:
                        pions = 3
                        rep_q2 = 1

                        print("pions:", pions)
                    elif pion4.collidepoint(event.pos) and rep_q2 == 0:
                        pions = 4
                        rep_q2 = 1

                elif rep_q2 == 2:

                    if couleur1.collidepoint(event.pos) and choix < joueurs:
                        color = RED
                        if joueur1 == 0 and r == 0:
                            joueur1 = 1  # le joueur 1 va être rouge
                            r = 1
                            choix += 1

                            print(" J1 est rouge :", joueur1)

                        elif joueur2 == 0 and r == 0:
                            joueur2 = 1  # le joueur 2 va être rouge
                            r = 1
                            choix += 1

                            print(" J2 est rouge :", joueur2)

                        elif joueur3 == 0 and r == 0:
                            joueur3 = 1  # le joueur 2 va être rouge
                            r = 1
                            choix += 1

                            print(" J3 est rouge :", joueur3)

                        elif joueur4 == 0 and r == 0:
                            joueur4 = 1  # le joueur 2 va être rouge
                            r = 1
                            choix += 1

                            print(" J4 est rouge :", joueur4)
                        else:
                            color = 0

                    elif couleur2.collidepoint(event.pos) and choix < joueurs:
                        color = BLUE
                        if joueur1 == 0 and b == 0:
                            joueur1 = 2  # le joueur 1 va être blue
                            b = 1
                            choix += 1
                            print(" J1 est bleu :", joueur1)
                        elif joueur2 == 0 and b == 0:
                            joueur2 = 2  # le joueur 2 va être bleu
                            b = 1
                            choix += 1
                            print(" J2 est bleu :", joueur2)
                        elif joueur3 == 0 and b == 0:
                            joueur3 = 2  # le joueur 3 va être bleu
                            b = 1
                            choix += 1
                            print(" J3 est bleu :", joueur3)
                        elif joueur4 == 0 and b == 0:
                            joueur4 = 2  # le joueur 4 va être bleu
                            b = 1
                            choix += 1
                            print(" J4 est bleu :", joueur4)
                        else:
                            color = 0

                    elif couleur3.collidepoint(event.pos) and choix < joueurs:
                        color = YELLOW
                        if joueur1 == 0 and j == 0:
                            joueur1 = 3  # le joueur 1 va être jaune
                            j = 1
                            choix += 1
                            print(" J1 est jaune :", joueur1)
                        elif joueur2 == 0 and j == 0:
                            joueur2 = 3  # le joueur 2 va être jaune
                            j = 1
                            choix += 1
                            print(" J2 est jaune :", joueur2)
                        elif joueur3 == 0 and j == 0:
                            joueur3 = 3  # le joueur 3 va être jaune
                            j = 1
                            choix += 1
                            print(" J3 est jaune :", joueur3)
                        elif joueur4 == 0 and j == 0:
                            joueur4 = 3  # le joueur 4 va être jaune
                            j = 1
                            choix += 1
                            print(" J4 est jaune :", joueur4)
                        else:
                            color = 0

                    elif couleur4.collidepoint(event.pos) and choix < joueurs:
                        color = GREEN
                        if joueur1 == 0 and v == 0:
                            joueur1 = 4  # le joueur 1 va être vert
                            v = 1
                            choix += 1
                            print(" J1 est vert :", joueur1)
                        elif joueur2 == 0 and v == 0:
                            joueur2 = 4  # le joueur 2 va être vert
                            v = 1
                            choix += 1
                            print(" J2 est vert :", joueur2)
                        elif joueur3 == 0 and v == 0:
                            joueur3 = 4  # le joueur 3 va être vert
                            v = 1
                            choix += 1
                            print(" J3 est vert :", joueur3)
                        elif joueur4 == 0 and v == 0:
                            joueur4 = 4  # le joueur 4 va être vert
                            v = 1
                            choix += 1
                            print(" J4 est vert :", joueur4)
                        else:
                            color = 0


                else:
                    print("Click dehors")

    pygame.quit()
    quit()


def regles(screen):
    pygame.display.set_caption('Restia-Chevalax (règles)')

    fond_regle_cheval = pygame.Surface(screen.get_size())
    fond_regle_cheval = fond_regle_cheval.convert()
    fond_regle_cheval.fill(PERFECT_BLUE)

    # afficher la fenêtre
    screen.blit(fond_regle_cheval, (0, 0))


    # Fond du titre
    bandeau = pygame.Rect(0, 75, 760, 38)
    pygame.draw.rect(screen, (0, 0, 102), bandeau, width=10)
    pygame.draw.rect(screen, (0, 105, 204), bandeau, width=0)

    groupe_bandeau = pygame.sprite.Group()
    fondregle_cheval = yamso.Carre(screen.get_rect().centerx - 225, screen.get_rect().top + 50, 450, 90,
                                   (109, 50, 204), 0, screen, 20)
    groupe_bandeau.add(fondregle_cheval)
    fondregle_cheval = yamso.Carre(screen.get_rect().centerx - 225, screen.get_rect().top + 50, 450, 90, (0, 0, 102),
                                   10, screen, 20)
    groupe_bandeau.add(fondregle_cheval)
    degrade_regle_cheval = yamso.Carre(screen.get_rect().centerx - 220, screen.get_rect().top + 55, 440, 80,
                                       (0, 105, 204), 10, screen, 20)
    groupe_bandeau.add(degrade_regle_cheval)

    # Fond bouton

    groupe_bouton = pygame.sprite.Group()
    fondretour = yamso.Carre(screen.get_rect().centerx - 366, screen.get_rect().top + 10, 92, 34, (255, 51, 51), 0,
                             screen, 0)
    groupe_bouton.add(fondretour)
    fondretour = yamso.Carre(screen.get_rect().centerx - 366, screen.get_rect().top + 10, 92, 34, PUR_BLACK, 3,
                             screen, 0)
    groupe_bouton.add(fondretour)

    # fond du texte
    top_fondtexte = screen.get_rect().top + 200
    left_fondtexte = screen.get_rect().left + 50
    fondtexte = pygame.Rect(left_fondtexte, top_fondtexte, 660, 340)
    degradetexte = pygame.Rect(left_fondtexte + 5, top_fondtexte + 5, 650, 330)
    pygame.draw.rect(screen, (109, 50, 204), fondtexte, width=0, border_radius=5)
    pygame.draw.rect(screen, DARK_BLUE, fondtexte, width=10, border_radius=5)
    pygame.draw.rect(screen, BLUE, degradetexte, width=10, border_radius=5)

    # Affichage des règles

    regle = ["Le chevalax est un jeu qui peut se jouer jusqu'à 4. On commence par lancer ",
             "les dés pour déterminer qui commence. Une fois l'ordre de passage établi,",
             "on lance les dés pour jouer. On ne peut sortir un cheval que lorsqu'on fait ",
             "un 6. On se deplace alors de sorte à faire le tour du terrain. Vous ne pouvez ",
             "pas dépasser un autre pion. Si vous voulez le dépasser, vous devez le ",
             "manger. Il faut alors etre sur la même case. Une fois à la fin, il faut monter ",
             "les escaliers. Mais avant il faut se placer parfaitement devant. Si vous ne le ",
             "pouvez pas, il faudra reculer. Pour monter les escaliers, il faut faire le score ",
             "écrit puis à la fin un 6. La partie se termine lorsque tout les chevaux sont",
             " rentrés dans l'écurie.", ]
    posy = screen.get_rect().top + 225
    posx = screen.get_rect().left + 70
    for i in range(0, 10):
        nv_regle = yamso.Texte(regle[i], posx, posy, BLACK, 26, screen)
        posy += 25

    # Affichage d'un texte

    font = pygame.font.Font(None, 36)
    titre = yamso.Texte("Bienvenue sur Chevalax :", screen.get_rect().centerx - 150, screen.get_rect().top + 70, BLACK,
                        36,
                        screen)

    sous_titre = yamso.Texte("Voici les règles:", screen.get_rect().centerx - 90, screen.get_rect().top + 100,
                             BLACK, 36, screen)

    retour = yamso.Texte("Retour", screen.get_rect().centerx - 360, screen.get_rect().top + 16, (102, 0, 0), 36, screen)

    # fond du bouton mute
    groupe_fond = pygame.sprite.Group()
    fondmute = yamso.Carre(710, 5, 38, 38, PERFECT_BLUE, 0, screen, 3)
    groupe_fond.add(fondmute)
    fondmute = yamso.Carre(710, 5, 38, 38, BLACK, 3, screen, 3)
    groupe_fond.add(fondmute)

    mute = 0
    image_mute = pygame.image.load("mute.png")
    image_unmute = pygame.image.load("unmute.png")
    screen.blit(image_unmute, (712, 7))

    pygame.display.flip()
    gameover = False
    while not gameover:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameover = True
            # fonctionnement des bouttons
            elif event.type == MOUSEBUTTONDOWN and event.button == 1:

                if fondretour.carre.collidepoint(event.pos):
                    menu()
                elif fondmute.carre.collidepoint(event.pos):
                    if mute == 0:
                        pygame.mixer.music.set_volume(0)
                        mute += 1
                        fondmute = yamso.Carre(710, 5, 38, 38, PERFECT_BLUE, 0, screen, 3)
                        groupe_fond.add(fondmute)
                        fondmute = yamso.Carre(710, 5, 38, 38, BLACK, 3, screen, 3)
                        groupe_fond.add(fondmute)
                        screen.blit(image_mute, (712, 7))
                        pygame.display.flip()
                    else:
                        pygame.mixer.music.set_volume(0.1)
                        mute -= 1
                        fondmute = yamso.Carre(710, 5, 38, 38, PERFECT_BLUE, 0, screen, 3)
                        groupe_fond.add(fondmute)
                        fondmute = yamso.Carre(710, 5, 38, 38, BLACK, 3, screen, 3)
                        groupe_fond.add(fondmute)
                        screen.blit(image_unmute, (712, 7))
                        pygame.display.flip()
                else:
                    print("Click dehors")

    pygame.quit()
    quit()


def menu():
    pygame.init()
    size = width, height = 760, 660

    screen = pygame.display.set_mode((size))
    pygame.display.set_caption('Restia-Chevalax')

    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill(PERFECT_BLUE)

    # Musique du fond
    pygame.mixer.music.load("Chevalax.wav")
    pygame.mixer.music.set_volume(0.1)
    pygame.mixer.music.play(-1)

    # Afficher le tout dans la fenêtre
    screen.blit(background, (0, 0))

    # Fond du titre
    bandeau = pygame.Rect(0, 75, 760, 38)
    pygame.draw.rect(screen, (0, 0, 102), bandeau, width=10)
    pygame.draw.rect(screen, (0, 105, 204), bandeau, width=0)

    groupe_bandeau = pygame.sprite.Group()
    fondmenu_cheval = yamso.Carre(screen.get_rect().centerx - 225, screen.get_rect().top + 50, 450, 90,
                                  (109, 50, 204), 0, screen, 20)
    groupe_bandeau.add(fondmenu_cheval)
    fondmenu_cheval = yamso.Carre(screen.get_rect().centerx - 225, screen.get_rect().top + 50, 450, 90, (0, 0, 102),
                                  10, screen, 20)
    groupe_bandeau.add(fondmenu_cheval)
    degrade_menu_cheval = yamso.Carre(screen.get_rect().centerx - 220, screen.get_rect().top + 55, 440, 80,
                                      (0, 105, 204), 10, screen, 20)
    groupe_bandeau.add(degrade_menu_cheval)

    # Fond bouton
    groupe_bouton = pygame.sprite.Group()
    fondregle = yamso.Carre(screen.get_rect().centerx - 65, screen.get_rect().top + 477, 131, 34, (109, 50, 204), 0,
                            screen, 0)
    groupe_bouton.add(fondregle)
    fondregle = yamso.Carre(screen.get_rect().centerx - 65, screen.get_rect().top + 477, 131, 34, (0, 0, 102), 3,
                            screen, 0)
    groupe_bouton.add(fondregle)

    fondjeu = yamso.Carre(screen.get_rect().centerx - 50, screen.get_rect().top + 329, 100, 34, (109, 50, 204), 0,
                          screen, 0)
    groupe_bouton.add(fondjeu)
    fondjeu = yamso.Carre(screen.get_rect().centerx - 50, screen.get_rect().top + 329, 100, 34, (0, 0, 102), 3,
                          screen, 0)
    groupe_bouton.add(fondjeu)

    fondretour = yamso.Carre(screen.get_rect().centerx - 366, screen.get_rect().top + 10, 92, 34, (255, 51, 51), 0,
                             screen, 0)
    groupe_bouton.add(fondretour)
    fondretour = yamso.Carre(screen.get_rect().centerx - 366, screen.get_rect().top + 10, 92, 34, PUR_BLACK, 3,
                             screen, 0)
    groupe_bouton.add(fondretour)

    # Affichage d'un texte
    titre = yamso.Texte("Bienvenue sur Chevalax :", screen.get_rect().centerx - 150, screen.get_rect().top + 70, BLACK,
                        36,
                        screen)
    sous_titre = yamso.Texte("Veuillez choisir une direction", screen.get_rect().centerx - 170,
                             screen.get_rect().top + 100,
                             BLACK, 36, screen)
    regle = yamso.Texte("Les règles", screen.get_rect().centerx - 60, screen.get_rect().top + 480, BLACK, 36, screen)
    jeu = yamso.Texte("Le jeu", screen.get_rect().centerx - 34, screen.get_rect().top + 335, BLACK, 36, screen)
    retour = yamso.Texte("Retour", screen.get_rect().centerx - 360, screen.get_rect().top + 16, (102, 0, 0), 36, screen)

    # fond du bouton mute
    groupe_fond = pygame.sprite.Group()
    fondmute = yamso.Carre(710, 5, 38, 38, PERFECT_BLUE, 0, screen, 3)
    groupe_fond.add(fondmute)
    fondmute = yamso.Carre(710, 5, 38, 38, BLACK, 3, screen, 3)
    groupe_fond.add(fondmute)

    mute = 0
    image_mute = pygame.image.load("mute.png")
    image_unmute = pygame.image.load("unmute.png")
    screen.blit(image_unmute, (712, 7))
    pygame.display.flip()
    gameover = False
    while not gameover:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameover = True

            # fonctionnement des boutons
            elif event.type == MOUSEBUTTONDOWN and event.button == 1:

                if fondjeu.carre.collidepoint(event.pos):
                    prepjeu(screen)

                elif fondregle.carre.collidepoint(event.pos):
                    regles(screen)
                elif fondretour.carre.collidepoint(event.pos):
                    pygame.mixer.music.fadeout(500)
                    main.menu_gen()
                elif fondmute.carre.collidepoint(event.pos):
                    if mute == 0:
                        pygame.mixer.music.set_volume(0)
                        mute += 1
                        fondmute = yamso.Carre(710, 5, 38, 38, PERFECT_BLUE, 0, screen, 3)
                        groupe_fond.add(fondmute)
                        fondmute = yamso.Carre(710, 5, 38, 38, BLACK, 3, screen, 3)
                        groupe_fond.add(fondmute)
                        screen.blit(image_mute, (712, 7))
                        pygame.display.flip()
                    else:
                        pygame.mixer.music.set_volume(0.1)
                        mute -= 1
                        fondmute = yamso.Carre(710, 5, 38, 38, PERFECT_BLUE, 0, screen, 3)
                        groupe_fond.add(fondmute)
                        fondmute = yamso.Carre(710, 5, 38, 38, BLACK, 3, screen, 3)
                        groupe_fond.add(fondmute)
                        screen.blit(image_unmute, (712, 7))
                        pygame.display.flip()
                else:
                    print("Click dehors")

    pygame.quit()
    quit()
