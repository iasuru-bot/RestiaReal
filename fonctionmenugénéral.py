import pygame 
from pygame.locals import *
from Couleur import *
def menu_gen():
    pygame.init()
    size=width,height=760,660
   
    screen=pygame.display.set_mode((size))
    pygame.display.set_caption('Restia')
    
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((102, 0, 102))

    # Affichage d'un texte  
    font = pygame.font.Font(None, 36)
    text = font.render("Bienvenue sur la plateforme de jeux Restia", 1, (255, 230, 255))
    textpos = text.get_rect()
    textpos.top= background.get_rect().top+70
    textpos.centerx = background.get_rect().centerx
    background.blit(text, textpos)

    #Affichage du fond des boutons
    #Fond du yams
    top_touryams = background.get_rect().bottom-388
    left_touryams = background.get_rect().left+158
    touryams = pygame.Rect(left_touryams,top_touryams,85,30)
    pygame.draw.rect(background, (217, 179, 255), touryams, width=0,border_top_left_radius=3, border_top_right_radius=3, border_bottom_left_radius=3, border_bottom_right_radius=3)
    pygame.draw.rect(background, BLACK, touryams, width=2,border_top_left_radius=3, border_top_right_radius=3, border_bottom_left_radius=3, border_bottom_right_radius=3)

    #Fond du chevaux
    top_tourchevaux = background.get_rect().bottom-188
    left_tourchevaux = background.get_rect().left+142
    tourchevaux = pygame.Rect(left_tourchevaux,top_tourchevaux,118,30)
    pygame.draw.rect(background, (217, 179, 255), tourchevaux, width=0,border_top_left_radius=3, border_top_right_radius=3, border_bottom_left_radius=3, border_bottom_right_radius=3)
    pygame.draw.rect(background, BLACK, tourchevaux, width=2,border_top_left_radius=3, border_top_right_radius=3, border_bottom_left_radius=3, border_bottom_right_radius=3)

    #Fond du dino
    top_tourdino = background.get_rect().bottom-388
    left_tourdino = background.get_rect().left+421
    tourdino = pygame.Rect(left_tourdino,top_tourdino,158,30)
    pygame.draw.rect(background, (217, 179, 255), tourdino, width=0,border_top_left_radius=3, border_top_right_radius=3, border_bottom_left_radius=3, border_bottom_right_radius=3)
    pygame.draw.rect(background, BLACK, tourdino, width=2,border_top_left_radius=3, border_top_right_radius=3, border_bottom_left_radius=3, border_bottom_right_radius=3)

    #Fond du casse-brique
    top_tourbrique = background.get_rect().bottom-188
    left_tourbrique = background.get_rect().left+405
    tourbrique = pygame.Rect(left_tourbrique,top_tourbrique,191,30)
    pygame.draw.rect(background, (217, 179, 255), tourbrique, width=0,border_top_left_radius=3, border_top_right_radius=3, border_bottom_left_radius=3, border_bottom_right_radius=3)
    pygame.draw.rect(background, BLACK, tourbrique, width=2,border_top_left_radius=3, border_top_right_radius=3, border_bottom_left_radius=3, border_bottom_right_radius=3)





    yams = font.render("Yamso", 1, BLACK)
    yamspos = yams.get_rect()
    yamspos.bottom = background.get_rect().bottom-360
    yamspos.centerx = background.get_rect().left+200
    background.blit(yams, yamspos)
    

    chevaux=font.render("Chevalax", 1, BLACK)
    chevauxpos=chevaux.get_rect()
    chevauxpos.bottom=background.get_rect().bottom-160
    chevauxpos.centerx=background.get_rect().left+200
    background.blit(chevaux, chevauxpos)

    dino=font.render("Dino run run", 1, BLACK)
    dinopos=dino.get_rect()
    
    dinopos.bottom=background.get_rect().bottom-360
    dinopos.centerx=background.get_rect().left+500
    background.blit(dino, dinopos)

    casse_brique=font.render("Super Breakeur", 1, BLACK)
    casse_briquepos=casse_brique.get_rect()
    casse_briquepos.bottom=background.get_rect().bottom-160
    casse_briquepos.centerx=background.get_rect().left+500
    background.blit(casse_brique, casse_briquepos)


    # Afficher le tout dans la fenêtre
    screen.blit(background, (0, 0))
    pygame.display.flip()

    

    gameover=False
    while not gameover:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                gameover=True
            #fonctionnement des bouttons
            elif event.type == MOUSEBUTTONDOWN and event.button == 1:

                if touryams.collidepoint(event.pos): menu_yamso(screen)

                elif tourchevaux.collidepoint(event.pos): print("Chevalax")



                elif tourdino.collidepoint(event.pos): print("Dino run run")



                elif tourbrique.collidepoint(event.pos): print("Super breakeur")
                else: print("Click dehors")

    pygame.quit()
    quit()
    
if __name__ == '__main__': menu_gen()