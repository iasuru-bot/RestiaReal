import pygame
from dino import Dino
from cactus import Cactus, Cactus2, Cactus3
pygame.init()


class Jeu:

    def __init__(self):
        self.debutJeu = False
        self.genererJoueur = pygame.sprite.Group()
        self.joueur = Dino(self)
        self.genererJoueur.add(self.joueur)
        self.cactus = pygame.sprite.Group()
        self.presse = {}
        self.nbreCactus = 3
        self.score = 0
        self.bestScore = 0

    def start(self):
        self.debutJeu = True
        self.apparitionsCactus()

    def lancement(self, ecran):
        ecran.blit(self.joueur.image, self.joueur.rect)
        font = pygame.font.SysFont("assets/Fredoka_One.zip", 32)
        affichageScore = font.render(f"Score : {self.score}", True, (255, 255, 255))
        affichageBestScore = font.render(f"Record : {self.bestScore}", True, (255, 255, 255))
        ecran.blit(affichageScore, (560, 20))
        ecran.blit(affichageBestScore, (560, 40))
        self.score += 1
        for obstacle in self.cactus:
            obstacle.mouvement()
        self.cactus.draw(ecran)
        if self.presse.get(pygame.K_UP) and self.joueur.rect.y <= 500:
            self.joueur.saute()
        elif self.joueur.rect.y != 500:
            self.joueur.saute()

    def gameOver(self):
        self.cactus = pygame.sprite.Group()
        self.debutJeu = False
        if self.score > self.bestScore:
            self.bestScore = self.score
        self.score = 0

    def collisions(self, sprite, group):
        return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask)

    def apparitionsCactus(self):
        obstacle = Cactus(self)
        self.cactus.add(obstacle)
        obstacle2 = Cactus2(self)
        self.cactus.add(obstacle2)
        obstacle3 = Cactus3(self)
        self.cactus.add(obstacle3)
