"""

This is the module for displaying the high score screen

"""

import sys
import pygame
import random
from Class_Background import Background
from Class_Grid import Grid
from Class_Vacuum import Vacuum
from Class_Debris import Debris
from Class_Basic_Ghost import Basic_Ghost
from Class_Adv_Ghost import Adv_Ghost
from Class_Expert_Ghost import Exp_Ghost
from Class_Nightmare_Ghost import NM_Ghost
from pygame.sprite import Group


def display_screen(screen, listHighScores):
    # Grid indices
    intMasterIndices = [0, 1, 2, 3, 4, 5, 6, 7, 10, 11, 12, 13, 16, 17, 18, 19, 20, 21, 22, 23]
    # Load high score Screen Music
    pygame.mixer.music.load('sounds/High_Scores.ogg')
    # Play music
    pygame.mixer.music.play(loops=0, start=0.0, fade_ms=1000)
    # Clock Object for controlling game speed
    obj_Clock = pygame.time.Clock()
    # Create background object
    objGameBackground = Background(screen)
    # Make a grid object to hold tile states and return starting coordinates of objects
    # This is being simplified or replaced with the list below.
    objGrid = Grid(screen)
    # Create vacuum for animation
    objVac = Vacuum(screen)

    intAvailableIndices = intMasterIndices.copy()

    ''' ghost group'''
    # Set number of each type of ghosts to animate
    intNumOfBasicGhosts = 3
    intNumOfAdvGhosts = 3
    intNumOfExpGhosts = 3
    intNumOfNMGhosts = 3
    # Create an empty group to hold ghosts
    groupGhosts = Group()
    # Loop to create Basic Ghosts and add to group
    intGhostCounter = intNumOfBasicGhosts
    while intGhostCounter > 0:
        intRandGridIndex = random.choice(intAvailableIndices)
        objNewGhost = Basic_Ghost(screen, objGrid.returnTileX(intRandGridIndex),
                                  objGrid.returnTileY(intRandGridIndex))
        objGrid.setTileState(intRandGridIndex)
        intAvailableIndices.remove(intRandGridIndex)
        groupGhosts.add(objNewGhost)
        intGhostCounter -= 1
    # Loop to create Advanced Ghosts and add to group
    intGhostCounter = intNumOfAdvGhosts
    while intGhostCounter > 0:
        objNewGhost = Adv_Ghost(screen)
        groupGhosts.add(objNewGhost)
        intGhostCounter -= 1
    # Loop to create Expert Ghosts and add to group
    intGhostCounter = intNumOfExpGhosts
    while intGhostCounter > 0:
        objNewGhost = Exp_Ghost(screen)
        groupGhosts.add(objNewGhost)
        intGhostCounter -= 1
    # Loop to create Nightmare Ghosts and add to group
    intGhostCounter = intNumOfNMGhosts
    while intGhostCounter > 0:
        objNewGhost = NM_Ghost(screen)
        groupGhosts.add(objNewGhost)
        intGhostCounter -= 1

    ''' Debris group'''
    intNumOfDebris = 50
    groupAllDebris = Group()
    # Loop to create each debris piece and add to group
    while intNumOfDebris > 0:
        objNewDebris = Debris(screen)
        groupAllDebris.add(objNewDebris)
        intNumOfDebris -= 1

    # Set initial color to be used for text
    colorValCurrent = [255, 255, 0]
    # Load custom font in 2 sizes, 50 and 25 point
    fontScore50 = pygame.font.Font('fighting-spirit-turbo.bold-italic.ttf', 50)
    fontScore25 = pygame.font.Font('fighting-spirit-turbo.bold-italic.ttf', 25)
    # Make Scoreboard Title Text that will scroll
    strAllScores = ''
    for row in listHighScores:
        for item in row:
            strAllScores = strAllScores + str(item) + '  '

    # Animation timer based on the number of high scores
    intAnimationTimer = len(strAllScores) * 35
    # Banner starting x value for animation scrolling
    intXValue = 800
    # Bool to set initial color change state for glow effect
    boolColorDown = True
    # Main Loop
    while intAnimationTimer > 0:

        # Monitor to user input, red x, escape key, or space bar are valid inputs
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    sys.exit()
                elif event.key == pygame.K_SPACE:
                    intAnimationTimer = 0

        # Draw background
        objGameBackground.blitself()
        # List to hold characters that are used as movement flags for input into vacuum object methods
        listMoveChoice = ['U', 'D', 'L', 'R']
        # Randomly select a new movement direction flag for vacuum every 77 loops for animation
        if intAnimationTimer % 77 == 0:
            objVac.set_move_direction(listMoveChoice[random.randint(0, 3)])
        # Draw each debris piece
        for currentSprite in groupAllDebris.sprites():
            currentSprite.blitself()
        # Move and draw the vacuum
        objVac.move_and_blitself()
        # Move and draw each ghost in the ghost group
        for currentSprite in groupGhosts.sprites():
            currentSprite.move_and_blitself()

        # Put the image of the title text on the screen
        textRendTitle = fontScore50.render("High Scores", False, colorValCurrent)
        screen.blit(textRendTitle, [250, 150])
        # Draw the scrolling high scores banner
        textRendScores = fontScore50.render(strAllScores, False, colorValCurrent)
        # Notice the location x value is set to intXValue which is constantly increasing to scroll
        screen.blit(textRendScores, [intXValue, 250])
        # Text for space bar prompt
        textRendSpace = fontScore25.render("Press Space Bar to Continue", False, colorValCurrent)
        screen.blit(textRendSpace, [225, 550])

        # Erase old and redraw the screen items in new locations
        pygame.display.flip()
        # Decrease the timer and the x value
        intAnimationTimer -= 1
        intXValue -= 1

        # Change color for glow effect
        # This is done by changing the R and B values of the RGB tuples
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
    # Fade music out during pause between screens
    pygame.mixer.music.fadeout(1000)
