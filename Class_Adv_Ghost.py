"""

This is the module for the advanced ghost enemy sprite

"""

import pygame
from pygame.sprite import Sprite
import random


class Adv_Ghost(Sprite):

    def __init__(self, screen):
        super(Adv_Ghost, self).__init__()
        # Load main screen size
        self.screen = screen

        # Load initial ghost image and get rectangle collision hull
        self.images = [pygame.image.load('images/Adv_Ghost_DL.png').convert_alpha(),
                       pygame.image.load('images/Adv_Ghost_DR.png').convert_alpha(),
                       pygame.image.load('images/Adv_Ghost_UL.png').convert_alpha(),
                       pygame.image.load('images/Adv_Ghost_UR.png').convert_alpha()]
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
            self.rect.centerx = random.randint(100, 700)
            self.rect.centery = random.randint(100, 200)
        elif self.starting_pos_group == 2:
            self.rect.centerx = random.randint(100, 700)
            self.rect.centery = random.randint(400, 500)
        elif self.starting_pos_group == 3:
            self.rect.centerx = random.randint(100, 200)
            self.rect.centery = random.randint(100, 500)
        elif self.starting_pos_group == 4:
            self.rect.centerx = random.randint(600, 700)
            self.rect.centery = random.randint(100, 500)

    def move_and_blitself(self):

        if self.rect.centerx <= 100 and self.moving_left:
            self.moving_left = False
        elif self.rect.centerx >= 700 and not self.moving_left:
            self.moving_left = True
        if self.rect.centery <= 100 and not self.moving_down:
            self.moving_down = True
        elif self.rect.centery >= 500 and self.moving_down:
            self.moving_down = False

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
