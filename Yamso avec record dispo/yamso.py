import pygame, main, lancerdes, resultat_yamso, time, record_yamso
from pygame.locals import *
from Couleur import *


class De(pygame.sprite.Sprite):
    def __init__(self, picture_path, pos_x, pos_y):
        super().__init__()
        self.image = pygame.image.load(picture_path)
        self.rect = self.image.get_rect()
        self.rect.center = [pos_x, pos_y]


class Texte(pygame.sprite.Sprite):
    def __init__(self, texte, pos_x, pos_y, color, taille_police, surface):
        super().__init__()
        self.font = pygame.font.Font(None, taille_police)
        self.ecrit = self.font.render(texte, True, color)
        self.pos = (pos_x, pos_y)
        surface.blit(self.ecrit, self.pos)


class Carre(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y, longueur, hauteur, couleur, epaisseur, surface, border_radius):
        super().__init__()
        self.carre = pygame.Rect(pos_x, pos_y, longueur, hauteur)
        pygame.draw.rect(surface, couleur, self.carre, width=epaisseur, border_radius=border_radius)


def combinaison_yamso_suivant(screen):
    fond_regle_yams = pygame.Surface(screen.get_size())
    fond_regle_yams = fond_regle_yams.convert()
    fond_regle_yams.fill(SKY_BLUE)
    screen.blit(fond_regle_yams, (0, 0))

    # Fond du titre
    top_fondtitre = screen.get_rect().top + 50
    left_fondtitre = screen.get_rect().centerx - 225
    fondtitre = pygame.Rect(left_fondtitre, top_fondtitre, 450, 90)
    degradetitre = pygame.Rect(left_fondtitre + 5, top_fondtitre + 5, 440, 80)
    bandeau = pygame.Rect(0, 75, 760, 38)

    pygame.draw.rect(screen, DARK_BLUE, bandeau, width=10)
    pygame.draw.rect(screen, BLUE, bandeau, width=0)
    pygame.draw.rect(screen, LIGHT_BLUE, fondtitre, width=0, border_radius=35)
    pygame.draw.rect(screen, DARK_BLUE, fondtitre, width=10, border_radius=35)
    pygame.draw.rect(screen, BLUE, degradetitre, width=10, border_radius=35)

    # Titre
    font = pygame.font.Font(None, 36)
    titre = font.render("Les combinaisons de la grille:", True, BLACK)
    titrepos = titre.get_rect()
    titrepos.top = screen.get_rect().top + 83
    titrepos.centerx = screen.get_rect().centerx
    screen.blit(titre, titrepos)

    # Fond du bouton retour
    top_fondretour = screen.get_rect().top + 10
    left_fondretour = screen.get_rect().left + 10
    fondretour = pygame.Rect(left_fondretour, top_fondretour, 92, 34)
    pygame.draw.rect(screen, SALMON_RED, fondretour, width=0)
    pygame.draw.rect(screen, BLACK, fondretour, width=3)
    # Affichage du bouton retour
    retour_menu = font.render("Retour", True, BORDEAUX)
    retour_menupos = retour_menu.get_rect()
    retour_menupos.top = screen.get_rect().top + 17
    retour_menupos.left = screen.get_rect().left + 17
    screen.blit(retour_menu, retour_menupos)

    # Fond des combinaisons
    top_fondtexte = screen.get_rect().top + 180
    left_fondtexte = screen.get_rect().centerx - 180
    fondtexte1 = pygame.Rect(left_fondtexte, top_fondtexte, 360, 450)
    degradetexte1 = pygame.Rect(left_fondtexte + 5, top_fondtexte + 5, 350, 440)
    pygame.draw.rect(screen, LIGHT_BLUE, fondtexte1, width=0, border_radius=5)
    pygame.draw.rect(screen, DARK_BLUE, fondtexte1, width=10, border_radius=5)
    pygame.draw.rect(screen, BLUE, degradetexte1, width=10, border_radius=5)
    pygame.display.flip()

    # Affichage des combinaisons restantes
    texte = pygame.font.Font(None, 23)
    sous_titre = texte.render("La suite des combinaisons:", True, BLACK)
    sous_titrepos = sous_titre.get_rect()
    sous_titrepos.top = 200
    sous_titrepos.left = 230
    screen.blit(sous_titre, sous_titrepos)
    grande_suite = texte.render("La grande suite (5 dés à la suite):", True, BLACK)
    grande_suitepos = grande_suite.get_rect()
    grande_suitepos.top = sous_titrepos.top + 30
    grande_suitepos.left = sous_titrepos.left
    screen.blit(grande_suite, grande_suitepos)
    grande_suitebis = texte.render("Le joueur gagnera 40 points.", True, BLACK)
    grande_suitebispos = grande_suitebis.get_rect()
    grande_suitebispos.top = grande_suitepos.top + 22
    grande_suitebispos.left = sous_titrepos.left
    screen.blit(grande_suitebis, grande_suitebispos)
    image_grande_suite = pygame.image.load("image_grande_suite.png")
    screen.blit(image_grande_suite, (sous_titrepos.left, grande_suitebispos.top + 25))

    yamso = texte.render("Le yamso (5 dés identiques):", True, BLACK)
    yamsopos = yamso.get_rect()
    yamsopos.top = grande_suitebispos.top + 100
    yamsopos.left = sous_titrepos.left
    screen.blit(yamso, yamsopos)
    yamsobis = texte.render("Le joueur gagnera 50 points.", True, BLACK)
    yamsobispos = yamsobis.get_rect()
    yamsobispos.top = yamsopos.top + 22
    yamsobispos.left = sous_titrepos.left
    screen.blit(yamsobis, yamsobispos)
    image_yamso = pygame.image.load("image_yamso.png")
    screen.blit(image_yamso, (sous_titrepos.left, yamsobispos.top + 25))

    chance = texte.render("La chance (somme des 5 dés):", True, BLACK)
    chancepos = chance.get_rect()
    chancepos.top = yamsobispos.top + 100
    chancepos.left = sous_titrepos.left
    screen.blit(chance, chancepos)
    chancebis = texte.render("Le joueur gagnera la somme des dés.", True, BLACK)
    chancebispos = chancebis.get_rect()
    chancebispos.top = chancepos.top + 22
    chancebispos.left = sous_titrepos.left
    screen.blit(chancebis, chancebispos)
    image_chance = pygame.image.load("image_chance.png")
    screen.blit(image_chance, (sous_titrepos.left, chancebispos.top + 25))

    pygame.display.flip()
    gameover = False
    while not gameover:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameover = True
            elif event.type == MOUSEBUTTONDOWN and event.button == 1:

                if retour_menupos.collidepoint(event.pos):
                    regle_yamso(screen)
                else:
                    print("Click dehors")
    pygame.quit()
    quit()


def combinaison_yamso(screen):
    fond_regle_yams = pygame.Surface(screen.get_size())
    fond_regle_yams = fond_regle_yams.convert()
    fond_regle_yams.fill(SKY_BLUE)
    screen.blit(fond_regle_yams, (0, 0))

    # Fond du titre
    top_fondtitre = screen.get_rect().top + 50
    left_fondtitre = screen.get_rect().centerx - 225
    fondtitre = pygame.Rect(left_fondtitre, top_fondtitre, 450, 90)
    degradetitre = pygame.Rect(left_fondtitre + 5, top_fondtitre + 5, 440, 80)
    bandeau = pygame.Rect(0, 75, 760, 38)

    pygame.draw.rect(screen, DARK_BLUE, bandeau, width=10)
    pygame.draw.rect(screen, BLUE, bandeau, width=0)
    pygame.draw.rect(screen, LIGHT_BLUE, fondtitre, width=0, border_radius=35)
    pygame.draw.rect(screen, DARK_BLUE, fondtitre, width=10, border_radius=35)
    pygame.draw.rect(screen, BLUE, degradetitre, width=10, border_radius=35)

    # Titre 
    font = pygame.font.Font(None, 36)
    titre = font.render("Les combinaisons de la grille:", True, BLACK)
    titrepos = titre.get_rect()
    titrepos.top = screen.get_rect().top + 83
    titrepos.centerx = screen.get_rect().centerx
    screen.blit(titre, titrepos)

    # fond du bouton suivant
    top_fondsuivant = screen.get_rect().top + 130
    left_fondsuivant = screen.get_rect().centerx + 250
    fondsuivant = pygame.Rect(left_fondsuivant, top_fondsuivant, 110, 34)
    pygame.draw.rect(screen, LIGHT_BLUE, fondsuivant, width=0)
    pygame.draw.rect(screen, DARK_BLUE, fondsuivant, width=3)
    # Fond du bouton retour
    top_fondretour = screen.get_rect().top + 10
    left_fondretour = screen.get_rect().left + 10
    fondretour = pygame.Rect(left_fondretour, top_fondretour, 92, 34)
    pygame.draw.rect(screen, SALMON_RED, fondretour, width=0)
    pygame.draw.rect(screen, BLACK, fondretour, width=3)

    # Affichage du bouton suivant
    suivant_combinaison = font.render("Suivant", True, BLACK)
    suivant_combinaisonpos = suivant_combinaison.get_rect()
    suivant_combinaisonpos.top = screen.get_rect().top + 137
    suivant_combinaisonpos.centerx = screen.get_rect().centerx + 305
    screen.blit(suivant_combinaison, suivant_combinaisonpos)

    # Affichage du bouton retour
    retour_menu = font.render("Retour", True, BORDEAUX)
    retour_menupos = retour_menu.get_rect()
    retour_menupos.top = screen.get_rect().top + 17
    retour_menupos.left = screen.get_rect().left + 17
    screen.blit(retour_menu, retour_menupos)

    # Fond des combinaisons
    top_fondtexte = screen.get_rect().top + 180
    left_fondtexte = screen.get_rect().left + 40
    fondtexte1 = pygame.Rect(left_fondtexte, top_fondtexte, 330, 450)
    degradetexte1 = pygame.Rect(left_fondtexte + 5, top_fondtexte + 5, 320, 440)
    pygame.draw.rect(screen, LIGHT_BLUE, fondtexte1, width=0, border_radius=5)
    pygame.draw.rect(screen, DARK_BLUE, fondtexte1, width=10, border_radius=5)
    pygame.draw.rect(screen, BLUE, degradetexte1, width=10, border_radius=5)
    fondtexte2 = pygame.Rect(left_fondtexte + 350, top_fondtexte, 330, 450)
    degradetexte2 = pygame.Rect(left_fondtexte + 355, top_fondtexte + 5, 320, 440)
    pygame.draw.rect(screen, LIGHT_BLUE, fondtexte2, width=0, border_radius=5)
    pygame.draw.rect(screen, DARK_BLUE, fondtexte2, width=10, border_radius=5)
    pygame.draw.rect(screen, BLUE, degradetexte2, width=10, border_radius=5)

    # Affichage des règles
    texte = pygame.font.Font(None, 20)
    regle = ["Le Yamso comporte 2 grilles: ",
             "La première grille est composé de 6 lignes. ",
             "Chaque ligne correspond à une face d'un dé.",
             "Pour compléter une case de la grille:",
             "On fait le total du nombre de chiffres choisi.",
             "Par exemple dans ce cas: ",
             "J'ai obtenu 5, 5, 5, 1 et 3.",
             "Si je choisis de compléter les 5 je note 15 pts",
             "Si je choisis de compléter les 1 je note 1 point",
             "Et si je choisis de compléter les 4 je note 0",
             "Lorsque la partie est terminée on fait la somme",
             "de cette grille et si le total est supérieur à 63",
             "alors 35 points bonus sont accordés."]
    hauteur_texte = 200
    for i in range(0, 6):
        affichage = texte.render(regle[i], True, BLACK)
        affichagepos = affichage.get_rect()
        affichagepos.top = hauteur_texte
        affichagepos.left = 57
        screen.blit(affichage, affichagepos)
        hauteur_texte += 22

    # Affichage des règles

    image_principe = pygame.image.load("image_principe.png")
    screen.blit(image_principe, (60, 350))

    hauteur_texte = 440
    for i in range(7, 13):
        affichage = texte.render(regle[i], True, BLACK)
        affichagepos = affichage.get_rect()
        affichagepos.top = hauteur_texte
        affichagepos.left = 57
        screen.blit(affichage, affichagepos)
        hauteur_texte += 22

    reglebis = ["La seconde grille est composé de 7 lignes:",
                "Le brelan (3 dés identiques) :", "le joueur gagnera la somme des dés.",
                "Le carré (4 dés identiques) :", "le joueur gagnera la somme des dés.",
                "Le full (un Brelan + une Paire) :", "le joueur gagnera 25 points.",
                "La petite suite (4 dés à la suite):", "le joueur gagnera 30 points.", ]
    hauteur_texte = 178
    for i in range(0, 3):
        hauteur_texte += 20
        affichage = texte.render(reglebis[i], True, BLACK)
        affichagepos = affichage.get_rect()
        affichagepos.top = hauteur_texte
        affichagepos.left = 407
        screen.blit(affichage, affichagepos)
    hauteur_texte -= 15
    hauteur_textebis = hauteur_texte + 20

    for i in range(3, 8, 2):
        hauteur_texte += 97
        affichage = texte.render(reglebis[i], True, BLACK)
        affichagepos = affichage.get_rect()
        affichagepos.top = hauteur_texte
        affichagepos.left = 407
        screen.blit(affichage, affichagepos)
    for i in range(4, 9, 2):
        hauteur_textebis += 97
        affichage = texte.render(reglebis[i], True, BLACK)
        affichagepos = affichage.get_rect()
        affichagepos.top = hauteur_textebis
        affichagepos.left = 407
        screen.blit(affichage, affichagepos)

    image_brelan = pygame.image.load("image_brelan.png")
    screen.blit(image_brelan, (405, 255))

    image_carre = pygame.image.load("image_carre.png")
    screen.blit(image_carre, (405, 354))

    image_full = pygame.image.load("image_full.png")
    screen.blit(image_full, (405, 450))

    image_petite_suite = pygame.image.load("image_petite_suite.png")
    screen.blit(image_petite_suite, (405, 548))

    pygame.display.flip()
    gameover = False
    while not gameover:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameover = True
            elif event.type == MOUSEBUTTONDOWN and event.button == 1:

                if retour_menupos.collidepoint(event.pos):
                    regle_yamso(screen)

                elif suivant_combinaisonpos.collidepoint(event.pos):
                    combinaison_yamso_suivant(screen)

                else:
                    print("Click dehors")
    pygame.quit()
    quit()


def regle_yamso(screen):
    pygame.display.set_caption('Restia-Yamso-Règles')
    fond_regle_yams = pygame.Surface(screen.get_size())
    fond_regle_yams = fond_regle_yams.convert()
    fond_regle_yams.fill(SKY_BLUE)
    screen.blit(fond_regle_yams, (0, 0))

    # Fond du titre
    top_fondtitre = screen.get_rect().top + 50
    left_fondtitre = screen.get_rect().centerx - 225
    fondtitre = pygame.Rect(left_fondtitre, top_fondtitre, 450, 90)
    degradetitre = pygame.Rect(left_fondtitre + 5, top_fondtitre + 5, 440, 80)
    bandeau = pygame.Rect(0, 75, 760, 38)

    pygame.draw.rect(screen, DARK_BLUE, bandeau, width=10)
    pygame.draw.rect(screen, BLUE, bandeau, width=0)
    pygame.draw.rect(screen, LIGHT_BLUE, fondtitre, width=0, border_top_left_radius=35, border_top_right_radius=20,
                     border_bottom_left_radius=35, border_bottom_right_radius=35)
    pygame.draw.rect(screen, DARK_BLUE, fondtitre, width=10, border_top_left_radius=35, border_top_right_radius=20,
                     border_bottom_left_radius=35, border_bottom_right_radius=35)
    pygame.draw.rect(screen, BLUE, degradetitre, width=10, border_top_left_radius=35, border_top_right_radius=20,
                     border_bottom_left_radius=35, border_bottom_right_radius=35)

    # fond du texte
    top_fondtexte = screen.get_rect().top + 200
    left_fondtexte = screen.get_rect().left + 50
    fondtexte = pygame.Rect(left_fondtexte, top_fondtexte, 660, 340)
    degradetexte = pygame.Rect(left_fondtexte + 5, top_fondtexte + 5, 650, 330)
    pygame.draw.rect(screen, LIGHT_BLUE, fondtexte, width=0, border_radius=5)
    pygame.draw.rect(screen, DARK_BLUE, fondtexte, width=10, border_radius=5)
    pygame.draw.rect(screen, BLUE, degradetexte, width=10, border_radius=5)

    # fond du bouton retour
    top_fondretour = screen.get_rect().top + 10
    left_fondretour = screen.get_rect().left + 10
    fondretour = pygame.Rect(left_fondretour, top_fondretour, 92, 34)
    pygame.draw.rect(screen, SALMON_RED, fondretour, width=0)
    pygame.draw.rect(screen, BLACK, fondretour, width=3)

    # fond du bouton combinaisons
    top_fondcombinaison = screen.get_rect().top + 550
    left_fondcombinaison = screen.get_rect().centerx - 125
    fondcombinaison = pygame.Rect(left_fondcombinaison, top_fondcombinaison, 250, 34)
    pygame.draw.rect(screen, LIGHT_BLUE, fondcombinaison, width=0)
    pygame.draw.rect(screen, DARK_BLUE, fondcombinaison, width=3)

    # Affichage d'un titre 
    font = pygame.font.Font(None, 36)
    titre = font.render("Les règles du Yamso :", True, BLACK)
    titrepos = titre.get_rect()
    titrepos.top = screen.get_rect().top + 83
    titrepos.centerx = screen.get_rect().centerx
    screen.blit(titre, titrepos)

    # affichage du bouton retour
    retour_menu = font.render("Retour", True, BORDEAUX)
    retour_menupos = retour_menu.get_rect()
    retour_menupos.top = screen.get_rect().top + 17
    retour_menupos.left = screen.get_rect().left + 17
    screen.blit(retour_menu, retour_menupos)

    texte = pygame.font.Font(None, 26)
    regle = ["Le Yamso se joue avec 5 dés et se finit une fois toutes les cases de la fiche  ",
             "de score remplies. Chaque joueur joue tout à tour et dispose de 3 lancers à ",
             "chaque coup. L’objectif étant de réaliser des combinaisons qui rapportent",
             "des points. Le joueur a le choix de reprendre tous ou une partie des dés à ",
             "chaque lancé, selon son gré, pour tenter d’obtenir la combinaison voulue.",
             "A chaque tour, le joueur doit obligatoirement inscrire son score dans une",
             "des cases de la feuille de marque que ce soit par un X ou par les points ",
             "qu’il a obtenu.Il peut arriver lors d’un tour que le résultat ne convienne pas ",
             "au joueur et qu’il se dise qu’il pourrait faire un plus grand score sur un autre",
             "tour. Il peut alors choisir de barrer une autre case à la place. Bien entendu, ",
             "il ne pourra plus faire cette combinaison par la suite. Soyez stratégique!"]
    hauteur_texte = 225
    for i in range(0, 11):
        affichage = texte.render(regle[i], True, BLACK)
        affichagepos = affichage.get_rect()
        affichagepos.top = hauteur_texte
        affichagepos.left = 70
        screen.blit(affichage, affichagepos)
        hauteur_texte += 25

    regle12 = texte.render("Bon jeu!", True, BLACK)
    regle12pos = regle12.get_rect()
    regle12pos.top = hauteur_texte
    regle12pos.centerx = affichagepos.centerx
    screen.blit(regle12, regle12pos)

    # Affichage du bouton pour voir les combinaisons
    combinaison = font.render("Les combinaisons", True, BLACK)
    combinaisonpos = combinaison.get_rect()
    combinaisonpos.top = screen.get_rect().top + 555
    combinaisonpos.centerx = screen.get_rect().centerx
    screen.blit(combinaison, combinaisonpos)

    pygame.display.flip()
    gameover = False
    while not gameover:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameover = True
            elif event.type == MOUSEBUTTONDOWN and event.button == 1:

                if retour_menupos.collidepoint(event.pos):
                    menu_yamso(screen)

                elif fondcombinaison.collidepoint(event.pos):
                    combinaison_yamso(screen)

                else:
                    print("Click dehors")
    pygame.quit()
    quit()


def jeu_yamso(screen):
    pygame.display.set_caption('Restia-Yamso-Le jeu')
    fond_menu_yams = pygame.Surface(screen.get_size())
    fond_menu_yams = fond_menu_yams.convert()
    fond_menu_yams.fill(SKY_BLUE)
    screen.blit(fond_menu_yams, (0, 0))

    # Fond du 1er tableau
    top_fond1ertableau = screen.get_rect().top + 50
    left_fond1ertableau = screen.get_rect().left + 55
    fond1ertableau = pygame.Rect(left_fond1ertableau, top_fond1ertableau, 310, 470)
    pygame.draw.rect(screen, LIGHT_BLUE, fond1ertableau, width=0, border_radius=15)
    pygame.draw.rect(screen, DARK_BLUE, fond1ertableau, width=10, border_radius=15)

    # Fond du 2eme tableau
    top_fond2emetableau = screen.get_rect().top + 50
    left_fond2emetableau = screen.get_rect().left + 405
    fond2emetableau = pygame.Rect(left_fond2emetableau, top_fond2emetableau, 310, 470)
    pygame.draw.rect(screen, LIGHT_BLUE, fond2emetableau, width=0, border_radius=15)
    pygame.draw.rect(screen, DARK_BLUE, fond2emetableau, width=10, border_radius=15)

    # Ligne des tableaux
    hauteur = 60 + 50
    for i in range(0, 8):
        pygame.draw.line(screen, DARK_BLUE, (60, hauteur), (362, hauteur), width=5)
        pygame.draw.line(screen, DARK_BLUE, (410, hauteur), (712, hauteur), width=5)
        hauteur += 50
    pygame.draw.line(screen, DARK_BLUE, (270, 60), (270, 515), width=5)
    pygame.draw.line(screen, DARK_BLUE, (620, 60), (620, 515), width=5)

    # Affichage texte 1er tableau
    texte = pygame.font.Font(None, 35)
    hauteur_texte = 73
    for i in range(0, 6):
        texte_a_afficher = "La somme des  " + str(i + 1)
        affichage = texte.render(texte_a_afficher, True, BLACK)
        affichagepos = affichage.get_rect()
        affichagepos.top = hauteur_texte
        affichagepos.left = left_fond1ertableau + 15
        screen.blit(affichage, affichagepos)
        hauteur_texte += 51

    total_somme = texte.render("Total sommes", True, BLACK)
    total_sommepos = total_somme.get_rect()
    total_sommepos.top = hauteur_texte
    total_sommepos.left = left_fond1ertableau + 15
    screen.blit(total_somme, total_sommepos)

    bonus = texte.render("Bonus si > à 62", True, BLACK)
    bonuspos = bonus.get_rect()
    bonuspos.top = hauteur_texte + 51
    bonuspos.left = left_fond1ertableau + 15
    screen.blit(bonus, bonuspos)

    total_1ertableau = texte.render("Total 1er tableau", True, BLACK)
    total_1ertableaupos = total_1ertableau.get_rect()
    total_1ertableaupos.top = bonuspos.top + 51
    total_1ertableaupos.left = left_fond1ertableau + 15
    screen.blit(total_1ertableau, total_1ertableaupos)

    # Affichage texte 2nd tableau
    texte_2tableau = ["Le brelan", "Le carré", "Le full", "La petite suite", "La grande suite", "Le Yamso",
                      "La chance", "Total 2e tableau", "Total general"]
    hauteur_texte = 73
    for i in range(0, 9):
        affichage = texte.render(texte_2tableau[i], True, BLACK)
        affichagepos = affichage.get_rect()
        affichagepos.top = hauteur_texte
        affichagepos.left = left_fond2emetableau + 15
        screen.blit(affichage, affichagepos)
        hauteur_texte += 51

    # Zone des grilles cliquables pour entrer le score
    fond_somme1 = pygame.Rect(left_fond1ertableau + 10, top_fond1ertableau + 10, fond1ertableau.width - 20, 48)
    fond_somme2 = pygame.Rect(left_fond1ertableau + 10, fond_somme1.bottom + 5, fond1ertableau.width - 20, 45)
    fond_somme3 = pygame.Rect(left_fond1ertableau + 10, fond_somme2.bottom + 5, fond1ertableau.width - 20, 45)
    fond_somme4 = pygame.Rect(left_fond1ertableau + 10, fond_somme3.bottom + 5, fond1ertableau.width - 20, 45)
    fond_somme5 = pygame.Rect(left_fond1ertableau + 10, fond_somme4.bottom + 5, fond1ertableau.width - 20, 45)
    fond_somme6 = pygame.Rect(left_fond1ertableau + 10, fond_somme5.bottom + 5, fond1ertableau.width - 20, 45)
    fond_brelan = pygame.Rect(left_fond2emetableau + 10, top_fond2emetableau + 10, fond2emetableau.width - 20, 48)
    fond_carre = pygame.Rect(left_fond2emetableau + 10, fond_brelan.bottom + 5, fond2emetableau.width - 20, 45)
    fond_full = pygame.Rect(left_fond2emetableau + 10, fond_carre.bottom + 5, fond2emetableau.width - 20, 45)
    fond_petite_suite = pygame.Rect(left_fond2emetableau + 10, fond_full.bottom + 5, fond2emetableau.width - 20, 45)
    fond_grande_suite = pygame.Rect(left_fond2emetableau + 10, fond_petite_suite.bottom + 5, fond2emetableau.width - 20,
                                    45)
    fond_yamso = pygame.Rect(left_fond2emetableau + 10, fond_grande_suite.bottom + 5, fond2emetableau.width - 20, 45)
    fond_chance = pygame.Rect(left_fond2emetableau + 10, fond_yamso.bottom + 5, fond2emetableau.width - 20, 45)

    # Bouton lancer
    top_lancer = screen.get_rect().top + 560
    left_lancer = screen.get_rect().left + 600
    fondlancer = pygame.Rect(left_lancer, top_lancer, 130, 40)
    pygame.draw.rect(screen, LIGHT_BLUE, fondlancer, width=0, border_radius=15)
    pygame.draw.rect(screen, DARK_BLUE, fondlancer, width=3, border_radius=15)

    texte_lancer = texte.render("Lancer", True, BLACK)
    texte_lancerpos = texte_lancer.get_rect()
    texte_lancerpos.top = top_lancer + 9
    texte_lancerpos.left = left_lancer + 24
    screen.blit(texte_lancer, texte_lancerpos)
    pygame.display.flip()

    # Initialisation des variables nécessaires au jeu
    lancer = 0
    dessin_start = 0
    nb_tour = 0
    groupe_de = pygame.sprite.Group()  # Groupe de sprites permettant de les afficher
    tableau_score = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]  # Tableau des scores
    tableau_score_actuel = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]  # Tableau des scores pour proposer comme solution
    tableau_position_score_sauvegarde = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                                         0]  # Tableau pour savoir les positions des scores sauvegardés
    groupe_resultat_texte = pygame.sprite.Group()
    groupe_effaceur = pygame.sprite.Group()

    gameover = False
    while not gameover:
        # Fin de la partie
        if nb_tour == 14:

            print("fin")
            resultat_final = resultat_yamso.calculer_score_final(tableau_score)

            somme_1er_tableau = Texte(str(resultat_final[0]), 310, 378, GOLD, 38, screen)
            groupe_resultat_texte.add(somme_1er_tableau)
            bonus_tableau = Texte(str(resultat_final[1]), 310, 428, GOLD, 38, screen)
            groupe_resultat_texte.add(bonus_tableau)
            somme_final_1er_tableau = Texte(str(resultat_final[2]), 310, 478, GOLD, 38, screen)
            groupe_resultat_texte.add(somme_final_1er_tableau)
            somme_2eme_tableau = Texte(str(resultat_final[3]), 650, 428, GOLD, 38, screen)
            groupe_resultat_texte.add(somme_2eme_tableau)
            resultat_global = Texte(str(resultat_final[4]), 650, 478, SALMON_RED, 38, screen)
            groupe_resultat_texte.add(resultat_global)
            pygame.display.flip()

            time.sleep(5)

            # Affichage de fin
            fondresultat = Carre(25, 100, 710, 500, LIGHT_BLUE, 0, screen, 10)
            groupe_effaceur.add(fondresultat)
            fondresultatcontour = Carre(25, 100, 710, 500, DARK_BLUE, 5, screen, 10)
            groupe_effaceur.add(fondresultatcontour)

            titre = Texte("Merci d'avoir joué(e) au Yamso", 150, 140, DARK_BLUE, 48, screen)
            sous_titre = Texte("Vous avez obtenu(e) un score total de :", 180, 220, DARK_BLUE, 33, screen)
            nbr_point = Texte(str(resultat_final[4]), 280, 290, DARK_BLUE, 54, screen)
            point = Texte("point(s)", 360, 290, DARK_BLUE, 54, screen)

            fondretour = Carre(100, 500, 150, 38, SALMON_RED, 0, screen, 3)
            groupe_effaceur.add(fondretour)
            fondretourcontour = Carre(100, 500, 150, 38, BORDEAUX, 3, screen, 3)
            groupe_effaceur.add(fondretourcontour)
            texte_retour = Texte("Retour menu", 103, 507, BORDEAUX, 34, screen)

            fondrecord = Carre(500, 500, 150, 38, GOLD, 0, screen, 3)
            groupe_effaceur.add(fondrecord)
            fondrecordcontour = Carre(500, 500, 150, 38, BLACK, 3, screen, 3)
            groupe_effaceur.add(fondrecordcontour)
            texte_record = Texte("Les records", 506, 507, BLACK, 34, screen)

            fondrejouer = Carre(300, 450, 150, 38, SKY_BLUE, 0, screen, 3)
            groupe_effaceur.add(fondrejouer)
            fondrejouercontour = Carre(300, 450, 150, 38, BLUE, 3, screen, 3)
            groupe_effaceur.add(fondrejouercontour)
            texte_rejouer = Texte("Rejouer", 329, 457, DARK_BLUE, 34, screen)

            # Récupére le nom du joueur pour le record
            nom_record = record_yamso.enregistrer_record(str(resultat_final[4]))
            str1 = "Bien joué " + nom_record + " ! Quelle partie !"
            gg = texte.render(str1, True, DARK_BLUE)  # Texte(str1, 255, 380, DARK_BLUE, 33, screen)
            ggpos = gg.get_rect()
            ggpos.top = 380
            ggpos.centerx = fondresultatcontour.carre.centerx
            screen.blit(gg, ggpos)

            pygame.display.flip()

            continuer = 0
            while continuer == 0:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        continuer = 1
                    elif event.type == MOUSEBUTTONDOWN and event.button == 1:
                        if fondretour.carre.collidepoint(event.pos):
                            menu_yamso(screen)
                        elif fondrecord.carre.collidepoint(event.pos):
                            record_yamso.afficher_record(screen)
                        elif fondrejouercontour.carre.collidepoint(event.pos):
                            jeu_yamso(screen)
            pygame.quit()
            quit()

        # Remise à zéro du fond à chaque nouveau tour
        elif lancer == 0 and dessin_start == 0:

            position_des_sauvegardes = [0, 0, 0, 0,
                                        0]  # tableau permettant de savoir quel dé est sauvegardé par le joueur
            # lorsqu'il est sauvegardé la position du dé est égale à 1 quand il est pas sauvegardé elle est égale à 0
            tableau_des = [0, 0, 0, 0, 0]  # Tableau permettant de stockés les résultats des dés
            # Le fond dès dés et le bouton lancer
            top_fonddes = screen.get_rect().top + 530
            left_fonddes = screen.get_rect().left + 55
            fonddes = pygame.Rect(left_fonddes, top_fonddes, 500, 110)
            pygame.draw.rect(screen, LIGHT_BLUE, fonddes, width=0, border_radius=15)
            pygame.draw.rect(screen, DARK_BLUE, fonddes, width=5, border_radius=15)

            taillede = 63
            hauteurde = 63
            coor_y = 549
            fond_d1 = pygame.Rect(69, coor_y, taillede, hauteurde)
            pygame.draw.rect(screen, DARK_BLUE, fond_d1, width=0, border_radius=15)
            fond_d2 = pygame.Rect(fond_d1.left + 100, coor_y, taillede, hauteurde)
            pygame.draw.rect(screen, DARK_BLUE, fond_d2, width=0, border_radius=15)
            fond_d3 = pygame.Rect(fond_d2.left + 100, coor_y, taillede, hauteurde)
            pygame.draw.rect(screen, DARK_BLUE, fond_d3, width=0, border_radius=15)
            fond_d4 = pygame.Rect(fond_d3.left + 100, coor_y, taillede, hauteurde)
            pygame.draw.rect(screen, DARK_BLUE, fond_d4, width=0, border_radius=15)
            fond_d5 = pygame.Rect(fond_d4.left + 100, coor_y, taillede, hauteurde)
            pygame.draw.rect(screen, DARK_BLUE, fond_d5, width=0, border_radius=15)

            pos_x = 310
            pos_y = 78
            for i in range(0, 6):
                if tableau_position_score_sauvegarde[i] == 0:
                    effaceur = Carre(pos_x - 5, pos_y - 5, 45, 30, LIGHT_BLUE, 0, screen, 0)
                    groupe_effaceur.add(effaceur)
                pos_y += 50
            pos_x = 650
            pos_y = 78
            for i in range(6, 13):
                if tableau_position_score_sauvegarde[i] == 0:
                    effaceur = Carre(pos_x - 5, pos_y - 5, 45, 30, LIGHT_BLUE, 0, screen, 0)
                    groupe_effaceur.add(effaceur)
                pos_y += 50

            pygame.display.flip()

            nb_tour += 1
            dessin_start = 1
            print(nb_tour)

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                gameover = True
            elif event.type == MOUSEBUTTONDOWN and event.button == 1:
                # Lancement des dés
                if fondlancer.collidepoint(event.pos) and lancer < 3:
                    dessin_start = 0
                    lancerdes.animation_lancage_des(tableau_des, position_des_sauvegardes, screen)
                    tableau_des = lancerdes.lancer_yamso(tableau_des, position_des_sauvegardes)
                    tableau_score_actuel = resultat_yamso.calcul_score(tableau_des, tableau_position_score_sauvegarde,
                                                                       tableau_score)

                    print(tableau_score_actuel)
                    # Affichage des scores futurs
                    pos_x = 310
                    pos_y = 78
                    for i in range(0, 6):
                        if tableau_position_score_sauvegarde[i] == 0:
                            # Effacer la case
                            effaceur = Carre(pos_x - 5, pos_y - 5, 45, 30, LIGHT_BLUE, 0, screen, 0)
                            groupe_effaceur.add(effaceur)

                            # Puis écrire le résultat prévu
                            resultat = Texte(str(tableau_score_actuel[i]), pos_x, pos_y, GREY, 35, screen)
                            groupe_resultat_texte.add(resultat)
                        pos_y += 50
                    pos_x = 650
                    pos_y = 78
                    for i in range(6, 13):
                        if tableau_position_score_sauvegarde[i] == 0:
                            # Effacer la case
                            effaceur = Carre(pos_x - 5, pos_y - 5, 45, 30, LIGHT_BLUE, 0, screen, 0)
                            groupe_effaceur.add(effaceur)

                            # Puis écrire le résultat prévu
                            resultat = Texte(str(tableau_score_actuel[i]), pos_x, pos_y, GREY, 35, screen)
                            groupe_resultat_texte.add(resultat)
                        pos_y += 50

                    lancer += 1
                    posi_x = 100
                    posi_y = 580
                    # Affichage du résultat du tirage des dés
                    for i in tableau_des:
                        if i == 1:
                            de1 = De("des_1.png", posi_x, posi_y)
                            groupe_de.add(de1)
                            groupe_de.draw(screen)
                        elif i == 2:
                            de2 = De("des_2.png", posi_x, posi_y)
                            groupe_de.add(de2)
                            groupe_de.draw(screen)
                        elif i == 3:
                            de3 = De("des_3.png", posi_x, posi_y)
                            groupe_de.add(de3)
                            groupe_de.draw(screen)
                        elif i == 4:
                            de4 = De("des_4.png", posi_x, posi_y)
                            groupe_de.add(de4)
                            groupe_de.draw(screen)
                        elif i == 5:
                            de5 = De("des_5.png", posi_x, posi_y)
                            groupe_de.add(de5)
                            groupe_de.draw(screen)
                        elif i == 6:
                            de6 = De("des_6.png", posi_x, posi_y)
                            groupe_de.add(de6)
                            groupe_de.draw(screen)
                        posi_x += 100
                    pygame.display.flip()

                # Sauvegarde des dés. Le contour du dé se met en or lorsqu'il est conservé pour le tirage prochain
                elif fonddes.collidepoint(event.pos) and lancer > 0:
                    if fond_d1.collidepoint(event.pos):
                        if position_des_sauvegardes[0] == 0:
                            pygame.draw.rect(screen, GOLD, fond_d1, width=6, border_radius=15)
                            position_des_sauvegardes[0] = 1
                        else:
                            pygame.draw.rect(screen, DARK_BLUE, fond_d1, width=6, border_radius=15)
                            position_des_sauvegardes[0] = 0

                    elif fond_d2.collidepoint(event.pos):

                        if position_des_sauvegardes[1] == 0:
                            pygame.draw.rect(screen, GOLD, fond_d2, width=6, border_radius=15)
                            position_des_sauvegardes[1] = 1

                        else:
                            pygame.draw.rect(screen, DARK_BLUE, fond_d2, width=6, border_radius=15)
                            position_des_sauvegardes[1] = 0

                    elif fond_d3.collidepoint(event.pos):

                        if position_des_sauvegardes[2] == 0:
                            pygame.draw.rect(screen, GOLD, fond_d3, width=6, border_radius=15)
                            position_des_sauvegardes[2] = 1

                        else:
                            pygame.draw.rect(screen, DARK_BLUE, fond_d3, width=6, border_radius=15)
                            position_des_sauvegardes[2] = 0

                    elif fond_d4.collidepoint(event.pos):

                        if position_des_sauvegardes[3] == 0:
                            pygame.draw.rect(screen, GOLD, fond_d4, width=6, border_radius=15)
                            position_des_sauvegardes[3] = 1

                        else:
                            pygame.draw.rect(screen, DARK_BLUE, fond_d4, width=6, border_radius=15)
                            position_des_sauvegardes[3] = 0

                    elif fond_d5.collidepoint(event.pos):

                        if position_des_sauvegardes[4] == 0:
                            pygame.draw.rect(screen, GOLD, fond_d5, width=6, border_radius=15)
                            position_des_sauvegardes[4] = 1

                        else:
                            pygame.draw.rect(screen, DARK_BLUE, fond_d5, width=6, border_radius=15)
                            position_des_sauvegardes[4] = 0
                    pygame.display.flip()

                # Sauvegarde du score.
                elif fond1ertableau.collidepoint(event.pos) and lancer > 0:
                    if fond_somme1.collidepoint(event.pos) and tableau_position_score_sauvegarde[0] == 0:
                        tableau_score[0] = tableau_score_actuel[0]
                        tableau_position_score_sauvegarde[0] += 1
                        resultat_sauvegarde = Texte(str(tableau_score[0]), 310, 78, GOLD, 35, screen)
                        groupe_resultat_texte.add(resultat_sauvegarde)
                        lancer = 0
                    elif fond_somme2.collidepoint(event.pos) and tableau_position_score_sauvegarde[1] == 0:
                        tableau_score[1] = tableau_score_actuel[1]
                        tableau_position_score_sauvegarde[1] += 1
                        resultat_sauvegarde = Texte(str(tableau_score[1]), 310, 128, GOLD, 35, screen)
                        groupe_resultat_texte.add(resultat_sauvegarde)
                        lancer = 0
                    elif fond_somme3.collidepoint(event.pos) and tableau_position_score_sauvegarde[2] == 0:
                        tableau_score[2] = tableau_score_actuel[2]
                        tableau_position_score_sauvegarde[2] += 1
                        resultat_sauvegarde = Texte(str(tableau_score[2]), 310, 178, GOLD, 35, screen)
                        groupe_resultat_texte.add(resultat_sauvegarde)
                        lancer = 0
                    elif fond_somme4.collidepoint(event.pos) and tableau_position_score_sauvegarde[3] == 0:
                        tableau_score[3] = tableau_score_actuel[3]
                        tableau_position_score_sauvegarde[3] += 1
                        resultat_sauvegarde = Texte(str(tableau_score[3]), 310, 228, GOLD, 35, screen)
                        groupe_resultat_texte.add(resultat_sauvegarde)
                        lancer = 0
                    elif fond_somme5.collidepoint(event.pos) and tableau_position_score_sauvegarde[4] == 0:
                        tableau_score[4] = tableau_score_actuel[4]
                        tableau_position_score_sauvegarde[4] += 1
                        resultat_sauvegarde = Texte(str(tableau_score[4]), 310, 278, GOLD, 35, screen)
                        groupe_resultat_texte.add(resultat_sauvegarde)
                        lancer = 0
                    elif fond_somme6.collidepoint(event.pos) and tableau_position_score_sauvegarde[5] == 0:
                        tableau_score[5] = tableau_score_actuel[5]
                        tableau_position_score_sauvegarde[5] += 1
                        resultat_sauvegarde = Texte(str(tableau_score[5]), 310, 328, GOLD, 35, screen)
                        groupe_resultat_texte.add(resultat_sauvegarde)
                        lancer = 0

                elif fond2emetableau.collidepoint(event.pos) and lancer > 0:
                    if fond_brelan.collidepoint(event.pos) and tableau_position_score_sauvegarde[6] == 0:
                        tableau_score[6] = tableau_score_actuel[6]
                        tableau_position_score_sauvegarde[6] += 1
                        resultat_sauvegarde = Texte(str(tableau_score[6]), 650, 78, GOLD, 35, screen)
                        groupe_resultat_texte.add(resultat_sauvegarde)
                        lancer = 0
                    elif fond_carre.collidepoint(event.pos) and tableau_position_score_sauvegarde[7] == 0:
                        tableau_score[7] = tableau_score_actuel[7]
                        tableau_position_score_sauvegarde[7] += 1
                        resultat_sauvegarde = Texte(str(tableau_score[7]), 650, 128, GOLD, 35, screen)
                        groupe_resultat_texte.add(resultat_sauvegarde)
                        lancer = 0
                    elif fond_full.collidepoint(event.pos) and tableau_position_score_sauvegarde[8] == 0:
                        tableau_score[8] = tableau_score_actuel[8]
                        tableau_position_score_sauvegarde[8] += 1
                        resultat_sauvegarde = Texte(str(tableau_score[8]), 650, 178, GOLD, 35, screen)
                        groupe_resultat_texte.add(resultat_sauvegarde)
                        lancer = 0
                    elif fond_petite_suite.collidepoint(event.pos) and tableau_position_score_sauvegarde[9] == 0:
                        tableau_score[9] = tableau_score_actuel[9]
                        tableau_position_score_sauvegarde[9] += 1
                        resultat_sauvegarde = Texte(str(tableau_score[9]), 650, 228, GOLD, 35, screen)
                        groupe_resultat_texte.add(resultat_sauvegarde)
                        lancer = 0
                    elif fond_grande_suite.collidepoint(event.pos) and tableau_position_score_sauvegarde[10] == 0:
                        tableau_score[10] = tableau_score_actuel[10]
                        tableau_position_score_sauvegarde[10] += 1
                        resultat_sauvegarde = Texte(str(tableau_score[10]), 650, 278, GOLD, 35, screen)
                        groupe_resultat_texte.add(resultat_sauvegarde)
                        lancer = 0
                    elif fond_yamso.collidepoint(event.pos) and tableau_position_score_sauvegarde[11] == 0:
                        tableau_score[11] = tableau_score_actuel[11]
                        tableau_position_score_sauvegarde[11] += 1
                        resultat_sauvegarde = Texte(str(tableau_score[11]), 650, 328, GOLD, 35, screen)
                        groupe_resultat_texte.add(resultat_sauvegarde)
                        lancer = 0
                    elif fond_chance.collidepoint(event.pos) and tableau_position_score_sauvegarde[12] == 0:
                        tableau_score[12] = tableau_score_actuel[12]
                        tableau_position_score_sauvegarde[12] += 1
                        resultat_sauvegarde = Texte(str(tableau_score[12]), 650, 378, GOLD, 35, screen)
                        groupe_resultat_texte.add(resultat_sauvegarde)
                        lancer = 0

    pygame.quit()
    quit()


def menu_yamso(screen):
    pygame.display.set_caption('Restia-Yamso')
    fond_menu_yams = pygame.Surface(screen.get_size())
    fond_menu_yams = fond_menu_yams.convert()
    fond_menu_yams.fill(SKY_BLUE)
    screen.blit(fond_menu_yams, (0, 0))

    # Fond du titre
    top_fondmenu = screen.get_rect().top + 50
    left_fondmenu = screen.get_rect().centerx - 225
    fondmenu = pygame.Rect(left_fondmenu, top_fondmenu, 450, 90)
    degrademenu = pygame.Rect(left_fondmenu + 5, top_fondmenu + 5, 440, 80)
    bandeau = pygame.Rect(0, 75, 760, 38)

    pygame.draw.rect(screen, DARK_BLUE, bandeau, width=10)
    pygame.draw.rect(screen, BLUE, bandeau, width=0)
    pygame.draw.rect(screen, LIGHT_BLUE, fondmenu, width=0, border_top_left_radius=35, border_top_right_radius=20,
                     border_bottom_left_radius=35, border_bottom_right_radius=35)
    pygame.draw.rect(screen, DARK_BLUE, fondmenu, width=10, border_top_left_radius=35, border_top_right_radius=20,
                     border_bottom_left_radius=35, border_bottom_right_radius=35)
    pygame.draw.rect(screen, BLUE, degrademenu, width=10, border_top_left_radius=35, border_top_right_radius=20,
                     border_bottom_left_radius=35, border_bottom_right_radius=35)

    # Fond bouton
    top_fondregle = screen.get_rect().top + 472
    left_fondregle = screen.get_rect().centerx - 265
    fondregle = pygame.Rect(left_fondregle, top_fondregle, 131, 34)
    pygame.draw.rect(screen, LIGHT_BLUE, fondregle, width=0)
    pygame.draw.rect(screen, DARK_BLUE, fondregle, width=3)

    top_fondrecord = screen.get_rect().top + 472
    left_fondrecord = screen.get_rect().centerx + 126
    fondrecord = pygame.Rect(left_fondrecord, top_fondrecord, 148, 34)
    pygame.draw.rect(screen, LIGHT_BLUE, fondrecord, width=0)
    pygame.draw.rect(screen, DARK_BLUE, fondrecord, width=3)

    top_fondjeu = screen.get_rect().top + 329
    left_fondjeu = screen.get_rect().centerx - 50
    fondjeu = pygame.Rect(left_fondjeu, top_fondjeu, 100, 34)
    pygame.draw.rect(screen, LIGHT_BLUE, fondjeu, width=0)
    pygame.draw.rect(screen, DARK_BLUE, fondjeu, width=3)

    top_fondretour = screen.get_rect().top + 10
    left_fondretour = screen.get_rect().left + 10
    fondretour = pygame.Rect(left_fondretour, top_fondretour, 92, 34)
    pygame.draw.rect(screen, SALMON_RED, fondretour, width=0)
    pygame.draw.rect(screen, BLACK, fondretour, width=3)

    # Affichage d'un texte
    font = pygame.font.Font(None, 36)
    titre = font.render("Bienvenue sur Yamso :", True, BLACK)
    titrepos = titre.get_rect()
    titrepos.top = screen.get_rect().top + 70
    titrepos.centerx = screen.get_rect().centerx
    screen.blit(titre, titrepos)

    sous_titre = font.render("Veuillez choisir une direction", True, BLACK)
    textpos = sous_titre.get_rect()
    textpos.top = screen.get_rect().top + 100
    textpos.centerx = screen.get_rect().centerx
    screen.blit(sous_titre, textpos)

    regle = font.render("Les règles", True, BLACK)
    reglepos = regle.get_rect()
    reglepos.bottom = screen.get_rect().top + 502
    reglepos.centerx = screen.get_rect().centerx - 200
    screen.blit(regle, reglepos)

    record = font.render("Les records", True, BLACK)
    recordpos = record.get_rect()
    recordpos.bottom = screen.get_rect().top + 500
    recordpos.centerx = screen.get_rect().centerx + 200
    screen.blit(record, recordpos)

    jeu = font.render("Le jeu", True, BLACK)
    jeupos = jeu.get_rect()
    jeupos.bottom = screen.get_rect().top + 360
    jeupos.centerx = screen.get_rect().centerx
    screen.blit(jeu, jeupos)

    retour_menu = font.render("Retour", True, BORDEAUX)
    retour_menupos = retour_menu.get_rect()
    retour_menupos.top = screen.get_rect().top + 17
    retour_menupos.left = screen.get_rect().left + 17
    screen.blit(retour_menu, retour_menupos)

    # Musique de fond
    pygame.mixer.music.load("musique_yamso.wav")
    pygame.mixer.music.set_volume(0.05)
    pygame.mixer.music.play(-1)

    # fond du bouton mute
    groupe_fond = pygame.sprite.Group()
    fondmute = Carre(710, 10, 40, 40, LIGHT_BLUE, 0, screen, 3)
    groupe_fond.add(fondmute)
    fondmute = Carre(710, 10, 40, 40, BLACK, 3, screen, 3)
    groupe_fond.add(fondmute)

    mute = 0
    image_mute = pygame.image.load("mute.png")
    image_unmute = pygame.image.load("unmute.png")
    screen.blit(image_unmute, (712, 12))

    pygame.display.flip()
    gameover = False
    while not gameover:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameover = True
            elif event.type == MOUSEBUTTONDOWN and event.button == 1:

                if fondjeu.collidepoint(event.pos):
                    jeu_yamso(screen)

                elif fondrecord.collidepoint(event.pos):
                    record_yamso.afficher_record(screen)
                elif fondregle.collidepoint(event.pos):
                    regle_yamso(screen)
                elif fondretour.collidepoint(event.pos):
                    pygame.mixer.music.fadeout(500)
                    main.menu_gen()

                elif fondmute.carre.collidepoint(event.pos):
                    if mute == 0:
                        pygame.mixer.music.set_volume(0)
                        mute += 1
                        fondmute = Carre(710, 10, 40, 40, LIGHT_BLUE, 0, screen, 3)
                        groupe_fond.add(fondmute)
                        fondmute = Carre(710, 10, 40, 40, BLACK, 3, screen, 3)
                        groupe_fond.add(fondmute)
                        screen.blit(image_mute, (712, 12))
                        pygame.display.flip()
                    else:
                        pygame.mixer.music.set_volume(0.05)
                        mute -= 1
                        fondmute = Carre(710, 10, 40, 40, LIGHT_BLUE, 0, screen, 3)
                        groupe_fond.add(fondmute)
                        fondmute = Carre(710, 10, 40, 40, BLACK, 3, screen, 3)
                        groupe_fond.add(fondmute)
                        screen.blit(image_unmute, (712, 12))
                        pygame.display.flip()
                else:
                    print("Click dehors")

    pygame.quit()
    quit()
