from random import randint
import pygame, time

class De(pygame.sprite.Sprite):
    def __init__(self, picture_path, pos_x, pos_y):
        super().__init__()
        self.image = pygame.image.load(picture_path)
        self.rect = self.image.get_rect()
        self.rect.center = [pos_x, pos_y]


def lancer_yamso(les_des, position_des_sauvegardes):
    for i in range(0, 5):
        if position_des_sauvegardes[i] == 0:
            les_des[i] = randint(1, 6)
    return les_des


def lancer_chevalax():
    de = randint(1, 6)
    return de

def animation_lancage_des_chevalax(screen):
    groupe_de = pygame.sprite.Group()
    son_de = pygame.mixer.Sound('son_de.wav')
    son_de.play()
    for k in range(5):
        le_de = randint(1,6)
        posi_x = 65
        posi_y = 200
        if le_de == 1:
            de1 = De("des_1.png", posi_x, posi_y)
            groupe_de.add(de1)
            groupe_de.draw(screen)
        elif le_de == 2:
            de2 = De("des_2.png", posi_x, posi_y)
            groupe_de.add(de2)
            groupe_de.draw(screen)
        elif le_de == 3:
            de3 = De("des_3.png", posi_x, posi_y)
            groupe_de.add(de3)
            groupe_de.draw(screen)
        elif le_de == 4:
            de4 = De("des_4.png", posi_x, posi_y)
            groupe_de.add(de4)
            groupe_de.draw(screen)
        elif le_de == 5:
            de5 = De("des_5.png", posi_x, posi_y)
            groupe_de.add(de5)
            groupe_de.draw(screen)
        elif le_de == 6:
            de6 = De("des_6.png", posi_x, posi_y)
            groupe_de.add(de6)
            groupe_de.draw(screen)
        pygame.display.flip()
        time.sleep(0.1)

def animation_lancage_des(les_des,position_des_sauvegardes,screen):
    groupe_de = pygame.sprite.Group()
    son_de = pygame.mixer.Sound('son_de.wav')
    son_de.play()
    for k in range(5):

        for i in range(0, 5):
            if position_des_sauvegardes[i] == 0:
                les_des[i] = randint(1, 6)
                posi_x = 100
                posi_y = 580
                for j in les_des:
                    if j == 1:
                        de1 = De("des_1.png", posi_x, posi_y)
                        groupe_de.add(de1)
                        groupe_de.draw(screen)
                    elif j == 2:
                        de2 = De("des_2.png", posi_x, posi_y)
                        groupe_de.add(de2)
                        groupe_de.draw(screen)
                    elif j == 3:
                        de3 = De("des_3.png", posi_x, posi_y)
                        groupe_de.add(de3)
                        groupe_de.draw(screen)
                    elif j == 4:
                        de4 = De("des_4.png", posi_x, posi_y)
                        groupe_de.add(de4)
                        groupe_de.draw(screen)
                    elif j == 5:
                        de5 = De("des_5.png", posi_x, posi_y)
                        groupe_de.add(de5)
                        groupe_de.draw(screen)
                    elif j == 6:
                        de6 = De("des_6.png", posi_x, posi_y)
                        groupe_de.add(de6)
                        groupe_de.draw(screen)
                    posi_x += 100
        pygame.display.flip()
        time.sleep(0.1)
