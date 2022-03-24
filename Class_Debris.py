"""

This is the module for the debris collectible sprite

"""

import pygame
from pygame.sprite import Sprite
import random


class Debris(Sprite):

    def __init__(self, screen):
        super(Debris, self).__init__()
        # Load main screen size
        self.screen = screen

        # List to hold image paths
        self.listImageChoice = ['images/Debris_1.png',
                                'images/Debris_2.png',
                                'images/Debris_3.png',
                                'images/Debris_4.png']
        self.intRandImageIndex = random.randint(0, 3)
        self.imageInitial = pygame.image.load(self.listImageChoice[self.intRandImageIndex]).convert_alpha()
        self.rect = self.imageInitial.get_rect()
        self.screen_rect = screen.get_rect()

        # Position at random starting point on the screen
        self.rect.centerx = random.randrange(100, 700, 2)
        self.rect.centery = random.randrange(100, 500, 2)

    def blitself(self):
        # Place on the main screen
        self.screen.blit(self.imageInitial, self.rect)
