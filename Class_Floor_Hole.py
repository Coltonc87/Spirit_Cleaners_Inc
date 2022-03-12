"""

This is the module for the floor hole sprite

"""

import pygame
from pygame.sprite import Sprite
import random


class Floor_Hole(Sprite):

    def __init__(self, screen, xcoord, ycoord):
        super(Floor_Hole, self).__init__()
        # Load main screen size
        self.screen = screen

        # List to hold image paths
        self.images = []
        for i in range(1, 6):
            self.images.append(pygame.image.load('images/Hole_%d.png' % i).convert_alpha())
        self.intRandImageIndex = random.randint(0, 4)
        self.image = self.images[self.intRandImageIndex]
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # Position at starting point on the screen

        self.rect.centerx = xcoord
        self.rect.centery = ycoord

    def blitself(self):
        # Place on the main screen
        self.screen.blit(self.image, self.rect)
        # Change to another image 1/50 of the time randomly with each loop
        if random.randint(1, 50) == 1:
            self.intRandImageIndex = random.randint(0, 4)
            self.image = self.images[self.intRandImageIndex]
