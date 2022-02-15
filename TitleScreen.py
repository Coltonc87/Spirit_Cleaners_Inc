import sys
import pygame
import random
from background import Background
from Vacuum import Vacuum
from Debris import Debris
from Basic_Ghost import Basic_Ghost
from pygame.sprite import Group


def title_screen(screen):
    # Start and draw the initial screen
    # Make instances and add to a list
    # Need a blank list here and then append it with objects
    objGameBackground = Background(screen)
    # Set color to be used for text
    colorValCurrent = [255, 255, 0]
    # Load custom font
    fontTitleScreen100 = pygame.font.Font('fighting-spirit-turbo.bold-italic.ttf', 100)
    fontTitleScreen25 = pygame.font.Font('fighting-spirit-turbo.bold-italic.ttf', 25)

    boolTitleScreen = True
    boolColorDown = True
    while boolTitleScreen:
        # Monitor to user input
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    sys.exit()
                elif event.key == pygame.K_SPACE:
                    boolTitleScreen = False

        # Make Title Text
        textRendSpirit = fontTitleScreen100.render("Spirit", False, colorValCurrent)
        textRendCleaners = fontTitleScreen100.render("Cleaners", False, colorValCurrent)
        textRendInc = fontTitleScreen100.render("Inc.", False, colorValCurrent)
        textRendSpace = fontTitleScreen25.render("Press Space Bar to Continue", False, colorValCurrent)
        objGameBackground.blitself()
        # Put the image of the title text on the screen
        screen.blit(textRendSpirit, [100, 100])
        screen.blit(textRendCleaners, [200, 200])
        screen.blit(textRendInc, [300, 300])
        screen.blit(textRendSpace, [225, 550])
        # Erase old and redraw the screen items in new locations
        pygame.display.flip()

        # Change color for glow effect
        if colorValCurrent[0] > 0 and boolColorDown:
            colorValCurrent[0] -= 1
            # colorValCurrent[1] -= 1
            colorValCurrent[2] += 1
        elif boolColorDown:
            boolColorDown = False
        elif not boolColorDown and colorValCurrent[0] < 255:
            colorValCurrent[0] += 1
            # colorValCurrent[1] += 1
            colorValCurrent[2] -= 1
        else:
            boolColorDown = True
