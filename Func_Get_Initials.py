"""

This is the module for input of initials for a new high score

"""

import sys
import pygame
from Class_Background import Background


def display_screen(screen, score):
    # Load high score Screen Music
    pygame.mixer.music.load('sounds/High_Scores.ogg')
    pygame.mixer.music.play(loops=0, start=0.0, fade_ms=1000)
    # Clock Object for controlling game speed
    obj_Clock = pygame.time.Clock()
    # Start and draw the initial screen
    # Make instance of background
    objGameBackground = Background(screen)
    # Set color to be used for text
    colorValCurrent = [255, 255, 0]
    # Load custom font in 3 sizes
    fontInputScreen50 = pygame.font.Font('fighting-spirit-turbo.bold-italic.ttf', 50)
    fontTitleScreen25 = pygame.font.Font('fighting-spirit-turbo.bold-italic.ttf', 25)
    fontInputScreen100 = pygame.font.Font('fighting-spirit-turbo.bold-italic.ttf', 100)

    # Tuple of characters
    tupCharacterChoices = ('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
                           'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
                           'U', 'V', 'W', 'X', 'Y', 'Z', '_', '!')

    # Initialize a "blank" list
    listInitials = ['_', ' ', '_', ' ', '_']

    boolInputScreen = True
    boolColorDown = True
    intCursorIndex = 0
    intCharChoiceIndex = 0
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
                elif event.key == pygame.K_RIGHT and intCursorIndex < 4:
                    intCursorIndex += 2
                    intCharChoiceIndex = 0
                elif event.key == pygame.K_LEFT and intCursorIndex > 0:
                    intCursorIndex -= 2
                    intCharChoiceIndex = 0
                elif event.key == pygame.K_UP and intCharChoiceIndex < 27:
                    intCharChoiceIndex += 1
                elif event.key == pygame.K_DOWN and intCharChoiceIndex > 0:
                    intCharChoiceIndex -= 1

        listInitials[intCursorIndex] = tupCharacterChoices[intCharChoiceIndex]

        # Make Title Text
        textRendPrompt = fontInputScreen50.render("Enter Your Initials:", False, colorValCurrent)
        strInitials = ''
        for character in listInitials:
            strInitials = strInitials + character
        textRendInitials = fontInputScreen100.render(strInitials, False, colorValCurrent)
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

        # Tick speed to control loop speed
        obj_Clock.tick(120)

    strInitialsOutput = ''
    for character in listInitials:
        if character != ' ':
            strInitialsOutput = strInitialsOutput + character

    pygame.mixer.music.fadeout(1000)
    return strInitialsOutput
