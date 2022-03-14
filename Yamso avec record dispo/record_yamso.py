from easygui import *
import pygame, main, lancerdes, resultat_yamso, time, yamso
from pygame.locals import *
from Couleur import *


def enregistrer_record(score_partie):
    # Récupération du nom du joueur
    reponse = 0
    nom_joueur = ""
    while reponse == 0:
        nom_joueur = enterbox(msg="Quel est votre nom", title="Restia-Yamso-Record", default="Serge")
        if nom_joueur != "":
            reponse += 1
    nouv_record_nom = nom_joueur
    nouv_record_score = int(score_partie)

    # Reconstruction des tableaux de records
    f = open("record_yamso.txt", "a")
    f.close()
    file = open('record_yamso.txt', "r")
    i = 0
    tableau_record = []
    tableau_nom = []
    for line in file:
        i += 1
        if i % 2 == 0:
            score = int(line)
            tableau_nom.append(nom)
            tableau_record.append(score)

        else:
            nom = line.replace("\n", "")
    file.close()

    # Ajout du nouveau score
    for i in range(0, len(tableau_record)):
        if nouv_record_score >= tableau_record[i]:
            tableau_record.insert(i, nouv_record_score)
            tableau_nom.insert(i, nouv_record_nom)
            break
    if len(tableau_record) == 0:
        tableau_record.append(nouv_record_score)
        tableau_nom.append(nouv_record_nom)

    print(tableau_record)
    file = open('record_yamso.txt', "w")
    j = 0

    # Sauvegarde du nouveau tableau de score
    for i in range(0, 2 * len(tableau_record)):

        if i % 2 == 0:
            str1 = str(tableau_nom[j]) + "\n"
            file.write(str1)

        else:
            str1 = str(tableau_record[j]) + "\n"
            file.write(str1)
            j += 1
        if j == 8:
            break
    file.close
    return nom_joueur


def afficher_record(screen):
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
    titre = font.render("Les Records:", True, BLACK)
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

    # Fond record
    groupe_fond = pygame.sprite.Group()
    groupe_fond.add(
        yamso.Carre(screen.get_rect().left + 50, screen.get_rect().top + 170, 660, 418, LIGHT_BLUE, 0, screen, 15),
        yamso.Carre(screen.get_rect().left + 50, screen.get_rect().top + 170, 660, 418, DARK_BLUE, 10, screen, 15), )

    # Ligne des tableaux
    hauteur = 175 + 50
    for i in range(0, 7):
        pygame.draw.line(screen, DARK_BLUE, (50, hauteur), (708, hauteur), width=5)
        hauteur += 50
    pygame.draw.line(screen, DARK_BLUE, (195, 175), (195, 586), width=5)

    # Reconstruction des tableaux de records
    f = open("record_yamso.txt", "a")
    f.close()
    file = open('record_yamso.txt', "r")
    i = 0
    tableau_record = []
    tableau_nom = []
    for line in file:
        i += 1
        if i % 2 == 0:
            score = int(line)
            tableau_nom.append(nom)
            tableau_record.append(score)

        else:
            nom = line.replace("\n", "")
    file.close()
    posx = 140
    posy = 184
    for i in range(0, len(tableau_record)):
        str1 = str(i + 1) + "."
        texte = yamso.Texte(str1, posx, posy, DARK_BLUE, 46, screen)
        texte = yamso.Texte(str(tableau_nom[i]), posx+100, posy+3, DARK_BLUE, 36, screen)
        texte = yamso.Texte(str(tableau_record[i]), posx+300, posy+3, DARK_BLUE, 36, screen)
        posy += 50
        pygame.display.flip()

    pygame.display.flip()
    gameover = False
    while not gameover:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameover = True
            elif event.type == MOUSEBUTTONDOWN and event.button == 1:

                if retour_menupos.collidepoint(event.pos):
                    yamso.menu_yamso(screen)
