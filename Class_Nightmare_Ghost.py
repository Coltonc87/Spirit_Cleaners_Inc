"""

This is the module for the nightmare ghost enemy sprite
This enemy patrols the perimeter of the level in very unpredictable ways.

"""

import pygame
from pygame.sprite import Sprite
import random


class NM_Ghost(Sprite):

    def __init__(self, screen):
        super(NM_Ghost, self).__init__()
        # Load main screen size
        self.screen = screen

        # Load initial ghost image and get rectangle collision hull
        self.images = []
        for i in range(1, 11):
            self.images.append(pygame.image.load('images/NMG_L_%d.png' % i).convert_alpha())

        self.frame = 0
        self.boolFrameUp = True
        self.image = self.images[self.frame]
        self.intRandFrameFlag = 0
        self.intRandFlag = 1
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
        if self.axis <= 2:
            if self.rect.centerx <= 100 and self.moving_left:
                self.intRandFlag = random.randint(1, 2)
                if self.intRandFlag == 1:
                    self.moving_left = False
                    self.axis = random.randint(1, 4)
                elif self.intRandFlag == 2:
                    self.rect.centerx = 700
            elif self.rect.centerx >= 700 and not self.moving_left:
                self.intRandFlag = random.randint(1, 2)
                if self.intRandFlag == 1:
                    self.moving_left = True
                    self.axis = random.randint(1, 4)
                elif self.intRandFlag == 2:
                    self.rect.centerx = 100

            if self.moving_left:
                self.rect.centerx -= 2
                self.image = self.images[self.frame]
            elif not self.moving_left:
                self.rect.centerx += 2
                self.image = pygame.transform.flip(self.images[self.frame], True, False)

            # Place on the main screen coordinates
            self.screen.blit(self.image, self.rect)

        elif self.axis > 2:
            if self.rect.centery <= 100 and not self.moving_down:
                self.intRandFlag = random.randint(1, 2)
                if self.intRandFlag == 1:
                    self.moving_down = True
                    self.axis = random.randint(1, 4)
                elif self.intRandFlag == 2:
                    self.rect.centery = 500

            elif self.rect.centery >= 500 and self.moving_down:
                self.intRandFlag = random.randint(1, 2)
                if self.intRandFlag == 1:
                    self.moving_down = False
                    self.axis = random.randint(1, 4)
                elif self.intRandFlag == 2:
                    self.rect.centery = 100

            if self.moving_down:
                self.rect.centery += 2
                self.image = pygame.transform.rotate(self.images[self.frame], 90)

            elif not self.moving_down:
                self.rect.centery -= 2
                self.image = pygame.transform.rotate(self.images[self.frame], 270)

            # Place on the main screen coordinates
            self.screen.blit(self.image, self.rect)

        '''
        Code to advance the frame at a random speed by using random and modulus division.
        The way it is coded there is a 1/20 chance that the frame will advance each loop.
        This is because the range of random is from 1 to 100 and there is a 1/20 chance
        that a number will be divisible by 5 with no remainder.
        This makes the ghosts animation move at a constantly varying frame rate to make it
        more interesting and keep the number of frame images low at 10 without the loop being
        too fast.        
        '''
        self.intRandFrameFlag = random.randint(1, 100)

        if self.intRandFrameFlag % 5 == 0:
            if self.frame < 9 and self.boolFrameUp:
                self.frame += 1
            elif self.boolFrameUp:
                self.boolFrameUp = False
            elif self.frame > 0 and not self.boolFrameUp:
                self.frame -= 1
            elif not self.boolFrameUp:
                self.boolFrameUp = True
