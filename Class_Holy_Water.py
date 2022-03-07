"""

This is the module for the holy water sprite

"""

import pygame
from pygame.sprite import Sprite
import random


class Holy_Water(Sprite):

    def __init__(self, screen):
        super(Holy_Water, self).__init__()
        # Load main screen size
        self.screen = screen

        # List to hold image paths
        self.images = []
        for i in range(1, 6):
            self.images.append(pygame.image.load('images/Holy_Water_%d.png' % i).convert_alpha())
        self.frame = 0
        self.boolFrameUp = True
        self.image = self.images[self.frame]
        self.intRandFrameFlag = 1
        self.intFrameCounter = 0
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # Random groups to set hole centers away from player
        self.starting_pos_group = random.randint(1, 4)

        # Position at random starting point on the screen
        if self.starting_pos_group == 1:
            self.rect.centerx = random.randint(125, 675)
            self.rect.centery = random.randint(125, 200)
        elif self.starting_pos_group == 2:
            self.rect.centerx = random.randint(100, 675)
            self.rect.centery = random.randint(400, 475)
        elif self.starting_pos_group == 3:
            self.rect.centerx = random.randint(125, 200)
            self.rect.centery = random.randint(125, 475)
        elif self.starting_pos_group == 4:
            self.rect.centerx = random.randint(600, 675)
            self.rect.centery = random.randint(125, 475)

    def blitself(self):
        # Place on the main screen
        self.screen.blit(self.image, self.rect)
        # Every 20 loops the remainder of modulus division will be 0
        self.intRandFrameFlag = self.intFrameCounter % 20

        if self.intRandFrameFlag == 0:
            if self.frame < 4 and self.boolFrameUp:
                self.frame += 1
            elif self.boolFrameUp:
                self.boolFrameUp = False
            elif self.frame > 0 and not self.boolFrameUp:
                self.frame -= 1
            elif not self.boolFrameUp:
                self.boolFrameUp = True
            self.image = self.images[self.frame]

        if self.intFrameCounter < 100:
            self.intFrameCounter += 1
        elif self.intFrameCounter == 100:
            self.intFrameCounter = 0


