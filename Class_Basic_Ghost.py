"""

This is the module for the basic ghost enemy sprite

"""

import pygame
from pygame.sprite import Sprite
import random


class Basic_Ghost(Sprite):

    def __init__(self, screen, xcoord, ycoord):
        super(Basic_Ghost, self).__init__()
        # Load main screen size
        self.screen = screen

        # Load initial ghost image and get rectangle collision hull
        self.images = [pygame.image.load('images/Basic_Ghost_R.png').convert_alpha(),
                       pygame.image.load('images/Basic_Ghost_L.png').convert_alpha(),
                       pygame.image.load('images/Basic_Ghost_U.png').convert_alpha(),
                       pygame.image.load('images/Basic_Ghost_D.png').convert_alpha()]
        self.image = self.images[3]
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        # Set randomly if the ghost will move along the x axis (1) or y axis (2)
        self.axis = random.randint(1, 4)
        if self.axis == 1:
            self.moving_left = True
            self.moving_down = False
        elif self.axis == 2:
            self.moving_left = False
            self.moving_down = False
        elif self.axis == 3:
            self.moving_left = False
            self.moving_down = True
        elif self.axis == 4:
            self.moving_left = False
            self.moving_down = False

        # Position at starting point on the screen

        self.rect.centerx = xcoord
        self.rect.centery = ycoord

    def move_and_blitself(self):
        if self.axis <= 2:
            if self.rect.centerx <= 100 and self.moving_left:
                self.moving_left = False
            elif self.rect.centerx >= 700 and not self.moving_left:
                self.moving_left = True

            if self.moving_left:
                self.rect.centerx -= 1
                self.image = self.images[1]
            elif not self.moving_left:
                self.rect.centerx += 1
                self.image = self.images[0]

            # Place on the main screen coordinates
            self.screen.blit(self.image, self.rect)

        elif self.axis > 2:
            if self.rect.centery <= 100 and not self.moving_down:
                self.moving_down = True
            elif self.rect.centery >= 500 and self.moving_down:
                self.moving_down = False

            if self.moving_down:
                self.rect.centery += 1
                self.image = self.images[3]
            elif not self.moving_down:
                self.rect.centery -= 1
                self.image = self.images[2]

            # Place on the main screen coordinates
            self.screen.blit(self.image, self.rect)
