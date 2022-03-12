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

            0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0

        ]

        # List to hold the center X coordinate value of each map tile for object creation
        self.coordTileCenterX = [

            150, 250, 350, 450, 550, 650,
            150, 250, 350, 450, 550, 650,
            150, 250, 350, 450, 550, 650,
            150, 250, 350, 450, 550, 650

        ]

        # List to hold the center Y coordinate value of each map tile for object creation
        self.coordTileCenterY = [

            150, 150, 150, 150, 150, 150,
            250, 250, 250, 250, 250, 250,
            350, 350, 350, 350, 350, 350,
            450, 450, 450, 450, 450, 450

        ]

    def blitself(self):
        # Draw on the main screen
        self.screen.blit(self.image, self.rect)

    def checkTileState(self, index):
        return self.stateTileStatus[index]

    def setTileState(self, index):
        self.stateTileStatus[index] = 1

    def returnTileX(self, index):
        return self.coordTileCenterX[index]

    def returnTileY(self, index):
        return self.coordTileCenterY[index]
