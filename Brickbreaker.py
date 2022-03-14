import pygame , main
import math


def jeu_super_breakeur():
    global balle
    pygame.init()

    # classe pour les scores
    class Parti:

        buffer = int(0)
        finalscore = int(0)
        nombredeballe = int(3)

    # création des infos de la partie

    cur_game = Parti()

    clock = pygame.time.Clock()
    screen_width, screen_height = 760, 660

    # création des groupes de sprite
    objet_touchable = pygame.sprite.Group()
    groupeballe = pygame.sprite.Group()
    groupebrick = pygame.sprite.Group()

    # plice d'ecriture du jeu
    police = pygame.font.Font(None, 36)

    # fonction diverse
    def ajouterballe():
        balle = Balle("Balle.png")
        return balle

    def creerbrique(start, hauteur, number):
        # créer une ranger de brique a partir d'un certain point(start) a une certaine hauteur
        for i in range(0, number):
            if i == 0 or i == number - 1:
                groupebrick.add(BriqueAbime(start, hauteur))
            else:
                groupebrick.add(BriqueNeuve(start, hauteur))
            start = start + 60

    def TestBlock(objet):
        if type(objet) is BriqueNeuve:
            brickremplace = BriqueAbime(objet.rect.x, objet.rect.y)
            groupebrick.add(brickremplace)
            objet_touchable.add(brickremplace)
            objet.kill()
            if cur_game.buffer < 500:
                cur_game.buffer += 50
            cur_game.finalscore += cur_game.buffer

        elif type(objet) is BriqueAbime:
            objet.kill()
            if cur_game.buffer < 500:
                cur_game.buffer += 50
            cur_game.finalscore += cur_game.buffer

        elif type(objet) is Lave:
            balle.kill()
            cur_game.nombredeballe -= 1

        elif type(objet) is Plateforme:
            cur_game.buffer = 0
            # ajoue de l'énergie de la platforme à la balle au contacte
            if objet.direction < 0 and balle.cur_velocity_x < 0:
                balle.cur_velocity_x *= 1.5
            if objet.direction < 0 and balle.cur_velocity_x > 0:
                balle.cur_velocity_x *= 0.5
            if objet.direction > 0 and balle.cur_velocity_x < 0:
                balle.cur_velocity_x *= 0.5
            if objet.direction > 0 and balle.cur_velocity_x > 0:
                balle.cur_velocity_x *= 1.5
            # limitation de la vitesse max et min de la balle
            if balle.cur_velocity_x > 10:
                balle.cur_velocity_x = 10
            if balle.cur_velocity_x < -10:
                balle.cur_velocity_x = -10
            if 2 > balle.cur_velocity_x > 0:
                balle.cur_velocity_x = 2
            if -2 < balle.cur_velocity_x < 0:
                balle.cur_velocity_x = -2

    # définition Sprite
    class SideBarre(pygame.sprite.Sprite):

        def __init__(self, picture_path):
            super().__init__()
            self.image = pygame.image.load(picture_path)
            self.rect = self.image.get_rect()

    class Lave(pygame.sprite.Sprite):

        def __init__(self, pos_x, pos_y):
            super().__init__()
            self.image = pygame.image.load("lave.png")
            self.rect = self.image.get_rect()
            self.rect.x = pos_x
            self.rect.y = pos_y

    class Plateforme(pygame.sprite.Sprite):

        def __init__(self, picture_path, rect_x, rect_y):
            super().__init__()

            self.image = pygame.image.load(picture_path)
            self.rect = self.image.get_rect()
            self.rect.x = rect_x
            self.rect.y = rect_y
            self.speed = 6
            self.direction = 0

        def bouger(self):
            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT]:
                if self.rect.x > 202:
                    self.moveleft(self.speed)
                    self.direction = -1
            elif keys[pygame.K_RIGHT]:
                if self.rect.x < 630:
                    self.moveright(self.speed)
                    self.direction = 1
            else:
                self.direction = 0

        def moveright(self, pixels):
            self.rect.x += pixels

        def moveleft(self, pixels):
            self.rect.x -= pixels

    class Balle(pygame.sprite.Sprite):

        def __init__(self, picture_path):
            super().__init__()
            self.image = pygame.image.load(picture_path)
            self.rect = self.image.get_rect()
            self.rect.x = 482
            self.rect.y = 528
            self.cur_velocity_x = 0
            self.cur_velocity_y = 0
            self.tolerance = 10
            self.velocity = 5

        def testcollision(self, objet):
            if self.rect.colliderect(objet):

                if abs(self.rect.top - objet.rect.bottom) <= self.tolerance:
                    self.cur_velocity_y *= -1
                    TestBlock(objet)
                if abs(self.rect.bottom - objet.rect.top) <= self.tolerance:
                    self.cur_velocity_y *= -1
                    TestBlock(objet)
                if abs(self.rect.right - objet.rect.left) <= self.tolerance:
                    balle.cur_velocity_x *= -1
                    TestBlock(objet)
                if abs(self.rect.left - objet.rect.right) <= self.tolerance:
                    self.cur_velocity_x *= -1
                    TestBlock(objet)
                while self.rect.x < 200 and self.cur_velocity_x < 0:
                    self.cur_velocity_x *= -1

    class BriqueNeuve(pygame.sprite.Sprite):
        def __init__(self, pos_x, pos_y):
            super().__init__()
            self.image = pygame.image.load("BlockNeuf.png")
            self.rect = self.image.get_rect()
            self.rect.x = pos_x
            self.rect.y = pos_y

    class BriqueAbime(pygame.sprite.Sprite):
        def __init__(self, pos_x, pos_y):
            super().__init__()
            self.image = pygame.image.load("BlocAbimer.png")
            self.rect = self.image.get_rect()
            self.rect.x = pos_x
            self.rect.y = pos_y


    # Musique du fond
    pygame.mixer.music.load("Zander Noriega - Fight Them Until We Cant.wav")
    pygame.mixer.music.set_volume(0.05)
    pygame.mixer.music.play(-1)

    # création de différent objet
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption('Restia')
    background_image = pygame.image.load("Background.png").convert()
    sidebarre = SideBarre("SideBarre.png")
    movingplate = Plateforme("Plateforme.png", 418, 550)
    lave = Lave(200, 648)

    # ajout des sprites dans les groupes
    objet_touchable.add(sidebarre)
    objet_touchable.add(movingplate)
    objet_touchable.add(lave)
    # groupepause.add(SideBarre)

    # creation des bricks
    creerbrique(360, 111, 4)
    creerbrique(300, 138, 6)
    creerbrique(240, 165, 8)
    creerbrique(240, 192, 8)
    creerbrique(240, 219, 8)
    creerbrique(240, 246, 8)
    creerbrique(240, 273, 8)
    creerbrique(300, 300, 6)
    creerbrique(360, 327, 4)
    for i in groupebrick.sprites():
        objet_touchable.add(i)

    while True:
        for event in pygame.event.get():
            # fermer la page si besoin
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        screen.blit(background_image, [0, 0])
        # ajout de la balle si il n'y en a pas une
        if not groupeballe:
            # on verifie si le joueur a encore des vie restant
            if cur_game.nombredeballe != 0:

                balle = ajouterballe()
                groupeballe.add(balle)
                movingplate.rect.x = 418
                movingplate.rect.y = 550
            # la parti est fini car le joueur a perdu

            else:
                cur_game.nombredeballe -= 1
                while True:
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            pygame.quit()
                        objet_touchable.draw(screen)
                        screen.blit(texte_score, rect_texte_score)
                        screen.blit(Nbr_Balle, rect_Nbr_Balle)
                        game_over = pygame.image.load("Game Over.png").convert()
                        rejouer = pygame.Rect(325, 390, 105, 35)
                        Menu = pygame.Rect(510, 390, 90, 40)
                        screen.blit(game_over, (280, 200))
                        if event.type == pygame.MOUSEBUTTONDOWN:
                            mouse_pos = event.pos
                            if rejouer.collidepoint(mouse_pos):
                                jeu_super_breakeur()
                            if Menu.collidepoint(mouse_pos):
                                main.menu_gen()

                        pygame.display.flip()
        # mouvement des différent objet

        # pour la balle
        if balle.cur_velocity_x == 0 and balle.cur_velocity_y == 0:
            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT]:
                balle.cur_velocity_x = balle.velocity * -1
                balle.cur_velocity_y = balle.velocity * -1
            if keys[pygame.K_RIGHT]:
                balle.cur_velocity_x = balle.velocity
                balle.cur_velocity_y = balle.velocity * -1
        balle.rect.x += balle.cur_velocity_x
        balle.rect.y += balle.cur_velocity_y

        # mouvement du plateau controler par le joueur
        movingplate.bouger()

        # ajout des objets sur la map
        objet_touchable.draw(screen)
        objet_touchable.update(screen)
        groupeballe.update(screen)
        groupeballe.draw(screen)

        # ajout de element de la sideBarre

        texte_score = police.render("score : " + str(cur_game.finalscore), True, (255, 255, 255))
        rect_texte_score = texte_score.get_rect()
        rect_texte_score.x = 30
        rect_texte_score.y = 125

        Nbr_Balle = police.render("Balles : " + str(cur_game.nombredeballe), True, (255, 255, 255))
        rect_Nbr_Balle = Nbr_Balle.get_rect()
        rect_Nbr_Balle.x = 56
        rect_Nbr_Balle.y = 290
        screen.blit(texte_score, rect_texte_score)
        screen.blit(Nbr_Balle, rect_Nbr_Balle)

        pygame.display.flip()

        # collision
        if balle.rect.right >= screen_width or balle.rect.left <= 0:
            balle.cur_velocity_x *= -1
        if balle.rect.bottom >= screen_height or balle.rect.top <= 0:
            balle.cur_velocity_y *= -1

        for i in objet_touchable.sprites():
            balle.testcollision(i)
        # la partie est fini car le joueur a gagné

        if len(groupebrick) == 0:
            while True:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                    objet_touchable.draw(screen)
                    screen.blit(texte_score, rect_texte_score)
                    screen.blit(Nbr_Balle, rect_Nbr_Balle)
                    Success = pygame.image.load("Success.png").convert()
                    rejouer = pygame.Rect(325, 390, 105, 35)
                    Menu = pygame.Rect(510, 390, 90, 40)
                    screen.blit(Success, (280, 200))
                    texte_score_final = police.render(" Votre score : " + str(cur_game.finalscore), True,
                                                      (255, 255, 255))
                    rect_texte_score_final = texte_score.get_rect()
                    rect_texte_score_final.x = 380
                    rect_texte_score_final.y = 334
                    screen.blit(texte_score_final, rect_texte_score_final)
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        mouse_pos = event.pos
                        if rejouer.collidepoint(mouse_pos):
                            jeu_super_breakeur()
                        if Menu.collidepoint(mouse_pos):
                            main.menu_gen()

                    pygame.display.flip()

        clock.tick(60)

