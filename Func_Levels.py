"""

This is the module for the main level loop of the game

"""

import sys
import pygame
from Class_Background import Background
from Class_Vacuum import Vacuum
from Class_Debris import Debris
from Class_Basic_Ghost import Basic_Ghost
from pygame.sprite import Group


def run_levels(screen):
    # Set flag for game to exit
    boolGameOver = False
    # Set initial speed
    intGameSpeed = 1
    # Make score variable
    intTotalScore = 0
    # Levels
    while not boolGameOver:
        # Start the level and draw the initial screen
        # Make instances and add to a list
        # Need a blank list here and then append it with objects
        objGameBackground = Background(screen)
        # Player in group to test collisions
        objPlayerVac = Vacuum(screen)
        groupPlayerGroup = Group()
        groupPlayerGroup.add(objPlayerVac)

        ''' ghost group'''
        intNumOfGhosts = 8
        groupGhosts = Group()
        while intNumOfGhosts > 0:
            objNewGhost = Basic_Ghost(screen)
            groupGhosts.add(objNewGhost)
            intNumOfGhosts -= 1

        ''' Debris group'''
        intNumOfDebris = 50
        groupAllDebris = Group()
        while intNumOfDebris > 0:
            objNewDebris = Debris(screen)
            groupAllDebris.add(objNewDebris)
            intNumOfDebris -= 1

        # Set yellow to be used for text
        colorValYellow = [255, 255, 0]
        # Load custom font
        fontMain = pygame.font.Font('fighting-spirit-turbo.bold-italic.ttf', 25)
        # Make Title Text
        textRendTitle = fontMain.render("Spirit Cleaners, Inc.", True, colorValYellow)
        # Make Score Text
        textRendScore = fontMain.render('Score: ' + str(intTotalScore), True, colorValYellow)
        # Set battery level (100%)
        intBatteryLevel = 10000
        # Make Battery Text
        textRendBattery = fontMain.render(('Battery: ' + str(int(intBatteryLevel / 100)) + '%'), True, colorValYellow)

        # Main Level Loop
        boolLevelRunning = True
        boolAcceptingInput = True
        stateMoveDirection = '0'

        while boolLevelRunning and intBatteryLevel > 0:

            # Monitor to user input
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

                elif event.type == pygame.KEYDOWN and boolAcceptingInput:
                    boolAcceptingInput = False
                    if event.key == pygame.K_RIGHT:
                        stateMoveDirection = 'R'
                        objPlayerVac.set_move_direction(stateMoveDirection)
                    elif event.key == pygame.K_LEFT:
                        stateMoveDirection = 'L'
                        objPlayerVac.set_move_direction(stateMoveDirection)
                    elif event.key == pygame.K_UP:
                        stateMoveDirection = 'U'
                        objPlayerVac.set_move_direction(stateMoveDirection)
                    elif event.key == pygame.K_DOWN:
                        stateMoveDirection = 'D'
                        objPlayerVac.set_move_direction(stateMoveDirection)
                    elif event.key == pygame.K_ESCAPE:
                        sys.exit()
                    elif event.key == pygame.K_SPACE:
                        boolLevelRunning = False
                        boolGameOver = True
                    else:
                        boolAcceptingInput = True

                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_RIGHT and stateMoveDirection == 'R':
                        objPlayerVac.set_move_direction('0')
                        boolAcceptingInput = True
                    elif event.key == pygame.K_LEFT and stateMoveDirection == 'L':
                        objPlayerVac.set_move_direction('0')
                        boolAcceptingInput = True
                    elif event.key == pygame.K_UP and stateMoveDirection == 'U':
                        objPlayerVac.set_move_direction('0')
                        boolAcceptingInput = True
                    elif event.key == pygame.K_DOWN and stateMoveDirection == 'D':
                        objPlayerVac.set_move_direction('0')
                        boolAcceptingInput = True

            # Place Objects in new location
            objGameBackground.blitself()
            for currentSprite in groupAllDebris.sprites():
                currentSprite.blitself()
            for currentSprite in groupPlayerGroup.sprites():
                currentSprite.move_and_blitself()
            for currentSprite in groupGhosts.sprites():
                currentSprite.move_and_blitself()

            # Put the image of the title text on the screen at 10x10
            screen.blit(textRendTitle, [10, 10])
            # Check for collisions update battery or score accordingly
            # First check if player and ghosts collide
            if pygame.sprite.spritecollideany(objPlayerVac, groupGhosts):
                # Remove ghosts player hit
                pygame.sprite.groupcollide(groupPlayerGroup, groupGhosts, False, True)
                # Lose 25% of the full battery charge
                intBatteryLevel = (intBatteryLevel - 2500)
                # Render the battery text
                textRendBattery = fontMain.render(('Battery: ' + str(int(intBatteryLevel / 100)) + '%'), True,
                                                  colorValYellow)
            # Second check if player and debris collide
            elif pygame.sprite.spritecollideany(objPlayerVac, groupAllDebris):
                # Remove debris player hit
                pygame.sprite.groupcollide(groupPlayerGroup, groupAllDebris, False, True)
                # Gain 100 Points!
                intTotalScore += 100
                # Render the score text
                textRendScore = fontMain.render('Score: ' + str(intTotalScore), True, colorValYellow)
            # If no collisions then simply lower the battery level
            else:
                # Render the battery text
                textRendBattery = fontMain.render(('Battery: ' + str(int(intBatteryLevel / 100)) + '%'), True,
                                                  colorValYellow)
            # Place the score text on the screen
            screen.blit(textRendScore, [300, 10])
            # Place the battery text on the screen
            screen.blit(textRendBattery, [600, 10])

            # Erase old and redraw the screen items in new locations
            pygame.display.flip()

            # If the battery is dead end the game
            if intBatteryLevel <= 0:
                boolLevelRunning = False
                boolGameOver = True
            # Go to next level if all debris is collected
            elif not groupAllDebris and intBatteryLevel > 0:
                boolLevelRunning = False
            # Check if battery still has charge and decrease the battery level
            elif intBatteryLevel > 0:
                intBatteryLevel -= intGameSpeed

    return intTotalScore + 100
