"""

This is the module for the floor hole sprite

"""

import pygame
from pygame.sprite import Sprite
import random


class Floor_Hole(Sprite):

    def __init__(self, screen):
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
        # Change to another image 1/10 of the time randomly with each loop
        if random.randint(1, 30) == 1:
            self.intRandImageIndex = random.randint(0, 4)
            self.image = self.images[self.intRandImageIndex]

