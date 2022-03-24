"""

This is the module for the expert ghost enemy sprite

"""

import pygame
from pygame.sprite import Sprite
import random


class Exp_Ghost(Sprite):

    def __init__(self, screen):
        super(Exp_Ghost, self).__init__()
        # Load main screen size
        self.screen = screen

        # Load initial ghost image and get rectangle collision hull
        self.images = [pygame.image.load('images/Exp_Ghost_DL.png').convert_alpha(),
                       pygame.image.load('images/Exp_Ghost_DR.png').convert_alpha(),
                       pygame.image.load('images/Exp_Ghost_UL.png').convert_alpha(),
                       pygame.image.load('images/Exp_Ghost_UR.png').convert_alpha()]
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
            self.moving_left = True
            self.moving_down = True
        # Random groups to set ghost centers away from player
        self.starting_pos_group = random.randint(1, 4)

        # Position at random starting point on the screen
        if self.starting_pos_group == 1:
            self.rect.centerx = random.randrange(100, 700, 50)
            self.rect.centery = random.randrange(100, 200, 50)
        elif self.starting_pos_group == 2:
            self.rect.centerx = random.randrange(100, 700, 50)
            self.rect.centery = random.randrange(400, 500, 50)
        elif self.starting_pos_group == 3:
            self.rect.centerx = random.randrange(100, 200, 50)
            self.rect.centery = random.randrange(100, 500, 50)
        elif self.starting_pos_group == 4:
            self.rect.centerx = random.randrange(600, 700, 50)
            self.rect.centery = random.randrange(100, 500, 50)

    def move_and_blitself(self):

        if self.rect.centerx <= 100 and self.moving_left:
            # self.moving_left = False
            self.rect.centerx = 700
        elif self.rect.centerx >= 700 and not self.moving_left:
            # self.moving_left = True
            self.rect.centerx = 100

        if self.rect.centery <= 100 and not self.moving_down:
            # self.moving_down = True
            self.rect.centery = 500
        elif self.rect.centery >= 500 and self.moving_down:
            # self.moving_down = False
            self.rect.centery = 100

        if self.moving_left and self.moving_down:
            self.rect.centerx -= 1
            self.rect.centery += 1
            self.image = self.images[0]
        elif not self.moving_left and self.moving_down:
            self.rect.centerx += 1
            self.rect.centery += 1
            self.image = self.images[1]
        elif self.moving_left and not self.moving_down:
            self.rect.centerx -= 1
            self.rect.centery -= 1
            self.image = self.images[2]
        elif not self.moving_left and not self.moving_down:
            self.rect.centerx += 1
            self.rect.centery -= 1
            self.image = self.images[3]

        # Place on the main screen coordinates
        self.screen.blit(self.image, self.rect)
