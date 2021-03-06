"""

This is the module for the player controlled vacuum sprite

"""

import pygame
from pygame.sprite import Sprite
import random


class Vacuum(Sprite):

    def __init__(self, screen):
        super(Vacuum, self).__init__()
        # Load main screen size
        self.screen = screen

        # Load initial vacuum image and get rectangle collision hull
        self.images_normal = [pygame.image.load('images/Vacuum_R.png').convert_alpha(),
                              pygame.image.load('images/Vacuum_L.png').convert_alpha(),
                              pygame.image.load('images/Vacuum_U.png').convert_alpha(),
                              pygame.image.load('images/Vacuum_D.png').convert_alpha()]
        self.images_inspired = [pygame.image.load('images/Vacuum_I_R.png').convert_alpha(),
                                pygame.image.load('images/Vacuum_I_L.png').convert_alpha(),
                                pygame.image.load('images/Vacuum_I_U.png').convert_alpha(),
                                pygame.image.load('images/Vacuum_I_D.png').convert_alpha()]
        self.image_set = self.images_normal
        self.image = self.images_normal[0]
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # Movement status, 0 is not moving L(eft) R(ight) D(own) U(p)
        self.moveDirection = '0'

        # Position vacuum centered on screen
        self.rect.centerx = self.screen_rect.centerx
        self.rect.centery = self.screen_rect.centery

        # Set "inspired" flag for Holy Water interaction
        self.boolInspired = False
        # Set "possessed" flag for ghost interaction
        self.boolPossessed = False
        self.intPossessionType = 0

    def move_and_blitself(self):
        if self.boolInspired:
            self.image_set = self.images_inspired
        else:
            self.image_set = self.images_normal

        if not self.possessed_state():
            if self.moveDirection == 'R' and self.rect.centerx < 700:
                self.rect.centerx += 2
                self.image = self.image_set[0]
            elif self.moveDirection == 'L' and self.rect.centerx > 100:
                self.rect.centerx -= 2
                self.image = self.image_set[1]
            elif self.moveDirection == 'U' and self.rect.centery > 100:
                self.rect.centery -= 2
                self.image = self.image_set[2]
            elif self.moveDirection == 'D' and self.rect.centery < 500:
                self.rect.centery += 2
                self.image = self.image_set[3]

        elif self.possessed_state() and self.intPossessionType == 1:
            if self.moveDirection == 'R' and self.rect.centerx > 100:
                self.rect.centerx -= 2
                self.image = self.image_set[0]
            elif self.moveDirection == 'L' and self.rect.centerx < 700:
                self.rect.centerx += 2
                self.image = self.image_set[1]
            elif self.moveDirection == 'U' and self.rect.centery < 500:
                self.rect.centery += 2
                self.image = self.image_set[2]
            elif self.moveDirection == 'D' and self.rect.centery > 100:
                self.rect.centery -= 2
                self.image = self.image_set[3]

        elif self.possessed_state() and self.intPossessionType == 2:
            if self.moveDirection == 'R' and self.rect.centerx < 700:
                self.rect.centerx += 1
                self.image = self.image_set[0]
            elif self.moveDirection == 'L' and self.rect.centerx > 100:
                self.rect.centerx -= 1
                self.image = self.image_set[1]
            elif self.moveDirection == 'U' and self.rect.centery > 100:
                self.rect.centery -= 1
                self.image = self.image_set[2]
            elif self.moveDirection == 'D' and self.rect.centery < 500:
                self.rect.centery += 1
                self.image = self.image_set[3]

        elif self.possessed_state() and self.intPossessionType == 3:
            if self.moveDirection == 'R' and self.rect.centerx < 700:
                self.rect.centerx += 5
                self.image = self.image_set[0]
            elif self.moveDirection == 'L' and self.rect.centerx > 100:
                self.rect.centerx -= 5
                self.image = self.image_set[1]
            elif self.moveDirection == 'U' and self.rect.centery > 100:
                self.rect.centery -= 5
                self.image = self.image_set[2]
            elif self.moveDirection == 'D' and self.rect.centery < 500:
                self.rect.centery += 5
                self.image = self.image_set[3]

        # Place on the main screen coordinates
        self.screen.blit(self.image, self.rect)

    def set_move_direction(self, direction):
        self.moveDirection = direction

    def inspire(self):
        self.boolInspired = True

    def uninspire(self):
        self.boolInspired = False

    def inspire_state(self):
        return self.boolInspired

    def possess(self):
        self.boolPossessed = True
        self.intPossessionType = random.randint(1, 3)

    def exorcise(self):
        self.boolPossessed = False

    def possessed_state(self):
        return self.boolPossessed
