import pygame, yamso
from pygame.locals import *
from Couleur import *


def enregistrer_record(score_partie, screen):
    # Récupération du nom du joueur
    reponse = 0
    font = pygame.font.Font(None, 32)
    clock = pygame.time.Clock()

    input_box = pygame.Rect(200, 300, 140, 32)
    valide_box = pygame.Rect(550, 300, 40, 34)
    tour_box = pygame.Rect(150, 200, 490, 184)
    color_inactive = BLACK
    color_active = pygame.Color('dodgerblue2')
    color = color_inactive
    active = False
    nom_joueur = ''
    done = False

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                # If the user clicked on the input_box rect.
                if input_box.collidepoint(event.pos):
                    # Toggle the active variable.
                    active = not active

                elif valide_box.collidepoint(event.pos) and nom_joueur != "":
                    done = True
                else:
                    active = False
                # Change the current color of the input box.
                color = color_active if active else color_inactive
            if event.type == pygame.KEYDOWN:
                if active:
                    if (event.key == pygame.K_RETURN or event.key == pygame.K_KP_ENTER) and nom_joueur != "":
                        done = True
                    elif event.key == pygame.K_BACKSPACE:
                        nom_joueur = nom_joueur[:-1]
                    else:
                        nom_joueur += event.unicode

        screen.fill(SKY_BLUE)
        # Render the current text.
        txt_surface = font.render(nom_joueur, True, color)
        # Resize the box if the text is too long.
        width = max(200, txt_surface.get_width() + 10)
        input_box.w = width
        # Blit the input_box rect.
        pygame.draw.rect(screen, LIGHT_BLUE, tour_box, 0, 4)
        pygame.draw.rect(screen, color, input_box, 2)
        pygame.draw.rect(screen, GREEN, valide_box, 0, 2)
        pygame.draw.rect(screen, DARK_GREEN, valide_box, 3, 2)
        pygame.draw.rect(screen, DARK_BLUE, tour_box, 5, 4)
        texte = yamso.Texte("Entrez votre nom :", 290, 250, BLACK, 32, screen)
        ok = yamso.Texte("OK", 553, 307, DARK_GREEN, 34, screen)
        # Blit the text.
        screen.blit(txt_surface, (input_box.x + 5, input_box.y + 5))

        pygame.display.flip()
        clock.tick(30)
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
        texte = yamso.Texte(str(tableau_nom[i]), posx + 100, posy + 3, DARK_BLUE, 36, screen)
        texte = yamso.Texte(str(tableau_record[i]), posx + 300, posy + 3, DARK_BLUE, 36, screen)
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
