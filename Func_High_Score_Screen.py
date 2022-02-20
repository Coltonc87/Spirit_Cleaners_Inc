"""

This is the module for displaying the high score screen

"""

import sys
import pygame
import random
from Class_Background import Background
from Class_Vacuum import Vacuum
from Class_Debris import Debris
from Class_Basic_Ghost import Basic_Ghost
from pygame.sprite import Group


def display_screen(screen, listHighScores):
    pygame.mixer.music.play(loops=-1, start=0.0, fade_ms=1000)
    # Clock Object for controlling game speed
    obj_Clock = pygame.time.Clock()
    # Start and draw the initial screen
    # Make instances and add to a list
    # Need a blank list here and then append it with objects
    objGameBackground = Background(screen)
    # Vacuum for animation
    objVac = Vacuum(screen)

    ''' ghost group'''
    intNumOfGhosts = 25
    groupGhosts = Group()
    while intNumOfGhosts > 0:
        objNewGhost = Basic_Ghost(screen)
        groupGhosts.add(objNewGhost)
        intNumOfGhosts -= 1

    ''' Debris group'''
    intNumOfDebris = 100
    groupAllDebris = Group()
    while intNumOfDebris > 0:
        objNewDebris = Debris(screen)
        groupAllDebris.add(objNewDebris)
        intNumOfDebris -= 1

    # Set yellow to be used for text
    colorValCurrent = [255, 255, 0]
    # Load custom font
    fontScore50 = pygame.font.Font('fighting-spirit-turbo.bold-italic.ttf', 50)
    fontScore25 = pygame.font.Font('fighting-spirit-turbo.bold-italic.ttf', 25)
    # Make Scoreboard Title Text
    strAllScores = ''
    for row in listHighScores:
        for item in row:
            strAllScores = strAllScores + str(item) + '  '

    # Animation timer
    intAnimationTimer = len(strAllScores) * 35
    # Banner starting x value
    intXValue = 800
    # Bool to set initial color change state for glow effect
    boolColorDown = True
    # Main Loop
    while intAnimationTimer > 0:

        # Monitor to user input
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    sys.exit()
                elif event.key == pygame.K_SPACE:
                    intAnimationTimer = 0

        # Place Objects in new location
        objGameBackground.blitself()
        listMoveChoice = ['U', 'D', 'L', 'R']
        if intAnimationTimer % 77 == 0:
            objVac.set_move_direction(listMoveChoice[random.randint(0, 3)])
        for currentSprite in groupAllDebris.sprites():
            currentSprite.blitself()
        objVac.move_and_blitself()
        for currentSprite in groupGhosts.sprites():
            currentSprite.move_and_blitself()

        # Put the image of the title text on the screen at 10x10
        textRendTitle = fontScore50.render("High Scores", False, colorValCurrent)
        screen.blit(textRendTitle, [250, 150])
        textRendScores = fontScore50.render(strAllScores, False, colorValCurrent)
        screen.blit(textRendScores, [intXValue, 250])
        textRendSpace = fontScore25.render("Press Space Bar to Continue", False, colorValCurrent)
        screen.blit(textRendSpace, [225, 550])

        # Erase old and redraw the screen items in new locations
        pygame.display.flip()

        intAnimationTimer -= 1
        intXValue -= 1

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
        # Tick speed to control loop speed
        obj_Clock.tick(120)

    pygame.mixer.music.fadeout(1000)
