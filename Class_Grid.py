"""

This is the module for the game background

"""

import pygame


class Grid:

    def __init__(self, screen):
        # Load main screen size
        self.screen = screen

        # Load background image and get rectangle collision hull
        self.image = pygame.image.load('images/Grid.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # Draw screen centered on window
        self.rect.centerx = self.screen_rect.centerx
        self.rect.centery = self.screen_rect.centery

        # List to hold the status of each map tile for object creation
        # 1 is occupied 0 is unoccupied
        self.stateTileStatus = [
            1, 1, 1, 1, 1, 1, 1, 1,
            1, 0, 0, 0, 0, 0, 0, 1,
            1, 0, 0, 0, 0, 0, 0, 1,
            1, 0, 0, 0, 0, 0, 0, 1,
            1, 0, 0, 0, 0, 0, 0, 1,
            1, 1, 1, 1, 1, 1, 1, 1
        ]

    def blitself(self):
        # Draw on the main screen
        self.screen.blit(self.image, self.rect)
