import pygame
import random
pygame.init()


class Cactus(pygame.sprite.Sprite):

    def __init__(self, jeu):
        super().__init__()
        self.jeu = jeu
        self.image = pygame.image.load('assets/cactus.png')
        self.image = pygame.transform.scale(self.image, (128, 128))
        self.rect = self.image.get_rect()
        self.rect.x = 2000
        self.rect.y = 500
        self.vitesse = 9

    def mouvement(self):
        if self.jeu.collisions(self, self.jeu.genererJoueur):
            self.jeu.gameOver()
        self.rect.x -= self.vitesse
        if self.rect.x <= -200:
            self.jeu.nbreCactus = random.randint(1, 3)
            self.rect.x = 760
        if self.jeu.score == 5000:
            self.vitesse += 0.15
        if self.jeu.score == 10000:
            self.vitesse += 0.15
        if self.jeu.score == 20000:
            self.vitesse += 0.15
        if self.jeu.score == 40000:
            self.vitesse += 0.15
        if self.jeu.score == 60000:
            self.vitesse += 0.15
        if self.jeu.score == 100000:
            self.vitesse += 0.15


class Cactus2(pygame.sprite.Sprite):

    def __init__(self, jeu):
        super().__init__()
        self.jeu = jeu
        self.image = pygame.image.load('assets/cactus.png')
        self.image = pygame.transform.scale(self.image, (128, 128))
        self.rect = self.image.get_rect()
        self.rect.x = 2100
        self.rect.y = 500
        self.vitesse = 9

    def mouvement(self):
        if self.jeu.collisions(self, self.jeu.genererJoueur):
            self.jeu.gameOver()
        self.rect.x -= self.vitesse
        if self.rect.x <= -200:
            self.rect.x = 760
            if self.jeu.nbreCactus == 1:
                self.image = pygame.image.load('assets/Cache.png')
                self.image = pygame.transform.scale(self.image, (128, 128))
            else:
                self.image = pygame.image.load('assets/cactus.png')
                self.image = pygame.transform.scale(self.image, (128, 128))
        if self.jeu.score == 5000:
            self.vitesse += 0.15
        if self.jeu.score == 10000:
            self.vitesse += 0.15
        if self.jeu.score == 20000:
            self.vitesse += 0.15
        if self.jeu.score == 40000:
            self.vitesse += 0.15
        if self.jeu.score == 60000:
            self.vitesse += 0.15
        if self.jeu.score == 100000:
            self.vitesse += 0.15


class Cactus3(pygame.sprite.Sprite):

    def __init__(self, jeu):
        super().__init__()
        self.jeu = jeu
        self.image = pygame.image.load('assets/cactus.png')
        self.image = pygame.transform.scale(self.image, (128, 128))
        self.rect = self.image.get_rect()
        self.rect.x = 2200
        self.rect.y = 500
        self.vitesse = 9

    def mouvement(self):
        if self.jeu.collisions(self, self.jeu.genererJoueur):
            self.jeu.gameOver()
        self.rect.x -= self.vitesse
        if self.rect.x <= -200:
            self.rect.x = 760
            if self.jeu.nbreCactus < 3:
                self.image = pygame.image.load('assets/Cache.png')
                self.image = pygame.transform.scale(self.image, (128, 128))
            else:
                self.image = pygame.image.load('assets/cactus.png')
                self.image = pygame.transform.scale(self.image, (128, 128))
        if self.jeu.score == 5000:
            self.vitesse += 0.15
        if self.jeu.score == 10000:
            self.vitesse += 0.15
        if self.jeu.score == 20000:
            self.vitesse += 0.15
        if self.jeu.score == 40000:
            self.vitesse += 0.15
        if self.jeu.score == 60000:
            self.vitesse += 0.15
        if self.jeu.score == 100000:
            self.vitesse += 0.15
