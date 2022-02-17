"""

This is the module for input of initials for a new high score

"""

import sys
import pygame
from Class_Background import Background


def display_screen(screen, score):
    # Start and draw the initial screen
    # Make instance of background
    objGameBackground = Background(screen)
    # Set color to be used for text
    colorValCurrent = [255, 255, 0]
    # Load custom font in 3 sizes
    fontInputScreen50 = pygame.font.Font('fighting-spirit-turbo.bold-italic.ttf', 50)
    fontTitleScreen25 = pygame.font.Font('fighting-spirit-turbo.bold-italic.ttf', 25)
    fontInputScreen100 = pygame.font.Font('fighting-spirit-turbo.bold-italic.ttf', 100)

    # Initialize a "blank" list
    listInitials = ['_', '_', '_']

    boolInputScreen = True
    boolColorDown = True
    while boolInputScreen:
        # Monitor to user input
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    sys.exit()
                elif event.key == pygame.K_SPACE:
                    boolInputScreen = False

        # Make Title Text
        textRendPrompt = fontInputScreen50.render("Enter Your Initials:", False, colorValCurrent)
        textRendInitials = fontInputScreen100.render("_ _ _", False, colorValCurrent)
        textRendSpace = fontTitleScreen25.render("Press Space Bar to Continue", False, colorValCurrent)

        objGameBackground.blitself()
        # Put the image of the title text on the screen
        screen.blit(textRendPrompt, [150, 100])
        screen.blit(textRendInitials, [250, 200])
        screen.blit(textRendSpace, [225, 550])
        # Erase old and redraw the screen items in new locations
        pygame.display.flip()

        # Change color for glow effect
        if colorValCurrent[0] > 0 and boolColorDown:
            colorValCurrent[0] -= 1
            colorValCurrent[2] += 1
        elif boolColorDown:
            boolColorDown = False
        elif not boolColorDown and colorValCurrent[0] < 255:
            colorValCurrent[0] += 1
            colorValCurrent[2] -= 1
        else:
            boolColorDown = True
