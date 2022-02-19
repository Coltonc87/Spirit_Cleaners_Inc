"""

This is the module for the player controlled vacuum sprite

"""

import pygame
from pygame.sprite import Sprite


class Vacuum(Sprite):

    def __init__(self, screen):
        super(Vacuum, self).__init__()
        # Load main screen size
        self.screen = screen

        # Load initial vacuum image and get rectangle collision hull
        self.images = [pygame.image.load('images/Vacuum_R.png').convert_alpha(),
                       pygame.image.load('images/Vacuum_L.png').convert_alpha(),
                       pygame.image.load('images/Vacuum_U.png').convert_alpha(),
                       pygame.image.load('images/Vacuum_D.png').convert_alpha()]
        self.image = self.images[3]
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # Movement status, 0 is not moving L(eft) R(ight) D(own) U(p)
        self.moveDirection = '0'

        # Position vacuum centered on screen
        self.rect.centerx = self.screen_rect.centerx
        self.rect.centery = self.screen_rect.centery

    def move_and_blitself(self):
        if self.moveDirection == 'R' and self.rect.centerx < 700:
            self.rect.centerx += 2
            self.image = self.images[0]
        elif self.moveDirection == 'L' and self.rect.centerx > 100:
            self.rect.centerx -= 2
            self.image = self.images[1]
        elif self.moveDirection == 'U' and self.rect.centery > 100:
            self.rect.centery -= 2
            self.image = self.images[2]
        elif self.moveDirection == 'D' and self.rect.centery < 500:
            self.rect.centery += 2
            self.image = self.images[3]

        # Place on the main screen coordinates
        self.screen.blit(self.image, self.rect)

    def set_move_direction(self, direction):
        self.moveDirection = direction
