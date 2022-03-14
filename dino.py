import pygame
pygame.init()


class Dino(pygame.sprite.Sprite):

    def __init__(self, jeu):
        super().__init__()
        self.jeu = jeu
        self.image = pygame.image.load('assets/tyrannosaurus.png')
        self.image = pygame.transform.scale(self.image, (128, 128))
        self.vitesse = 10
        self.taille = 64
        self.rect = self.image.get_rect()
        self.rect.x = 80
        self.rect.y = 500

    def saute(self):
        self.rect.y -= self.vitesse
        self.vitesse -= 0.26
        if self.rect.y > 500:
            self.rect.y = 500
        if self.rect.y == 500:
            self.vitesse = 10
