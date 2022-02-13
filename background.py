import pygame


class Background:

    def __init__(self, screen):
        # Load main screen size
        self.screen = screen

        # Load background image and get rectangle collision hull
        self.image = pygame.image.load('images/Level_1.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # Draw screen centered on window
        self.rect.centerx = self.screen_rect.centerx
        self.rect.centery = self.screen_rect.centery

    def blitself(self):
        # Draw on the main screen
        self.screen.blit(self.image, self.rect)
