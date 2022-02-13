import sys
import pygame
import random
from background import Background
from Vacuum import Vacuum
from Debris import Debris
from Basic_Ghost import Basic_Ghost
from pygame.sprite import Group


def high_score_screen(screen, listHighScores):
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
    colorValBlue = [176, 224, 230]
    # Load custom font
    fontScore = pygame.font.Font('fighting-spirit-turbo.bold-italic.ttf', 50)
    # Make Scoreboard Title Text
    strAllScores = ''
    for row in listHighScores:
        for item in row:
            strAllScores = strAllScores + item + '  '
    textRendScoreboard = fontScore.render("High Scores:  " + strAllScores, True, colorValBlue)

    # Animation timer
    intAnimationTimer = len(strAllScores) * 60
    # Banner starting x value
    intXValue = 800
    # Main Loop
    while intAnimationTimer > 0:

        # Monitor to user input
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    sys.exit()

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
        screen.blit(textRendScoreboard, [intXValue, 250])

        # Erase old and redraw the screen items in new locations
        pygame.display.flip()

        intAnimationTimer -= 1
        intXValue -= 1
