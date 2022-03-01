"""

This is the module for the main level loop of the game

"""

import sys
import pygame
import time
from Class_Background import Background
from Class_Vacuum import Vacuum
from Class_Debris import Debris
from Class_Basic_Ghost import Basic_Ghost
from Class_Adv_Ghost import Adv_Ghost
from Class_Expert_Ghost import Exp_Ghost
from Class_Nightmare_Ghost import NM_Ghost
from pygame.sprite import Group


def run_levels(screen):
    # Level counter
    intLevel = 1
    # Clock Object for controlling game speed
    obj_Clock = pygame.time.Clock()
    # Set flag for game to exit
    boolGameOver = False
    # Set initial speed
    intGameSpeed = 110
    # Make score variable
    intTotalScore = 0
    # Set yellow to be used for text
    colorValYellow = [255, 255, 0]
    # Load custom font
    fontMain25 = pygame.font.Font('fighting-spirit-turbo.bold-italic.ttf', 25)
    fontMain100 = pygame.font.Font('fighting-spirit-turbo.bold-italic.ttf', 100)
    # Levels
    while not boolGameOver:
        # Start the level and draw the initial screen
        # Make instances and add to a list
        # Need a blank list here and then append it with objects
        objGameBackground = Background(screen)

        ''' player group'''
        objPlayerVac = Vacuum(screen)
        groupPlayerGroup = Group()
        groupPlayerGroup.add(objPlayerVac)

        ''' ghost group'''
        if intLevel < 4:
            intNumOfBasicGhosts = 7 - intLevel
            intNumOfAdvGhosts = intLevel - 1
            intNumOfExpGhosts = intLevel - 2
            intNumOfNMGhosts = 1
        elif intLevel == 4:
            intNumOfBasicGhosts = 2
            intNumOfAdvGhosts = 2
            intNumOfExpGhosts = 2
        elif intLevel == 5:
            intNumOfBasicGhosts = 1
            intNumOfAdvGhosts = 3
            intNumOfExpGhosts = 2
        elif intLevel == 6:
            intNumOfBasicGhosts = 0
            intNumOfAdvGhosts = 3
            intNumOfExpGhosts = 3
        elif intLevel > 6:
            intNumOfBasicGhosts = 0
            intNumOfAdvGhosts = 9 - intLevel
            intNumOfExpGhosts = intLevel - 3

        groupGhosts = Group()

        intGhostCounter = intNumOfBasicGhosts
        while intGhostCounter > 0:
            objNewGhost = Basic_Ghost(screen)
            groupGhosts.add(objNewGhost)
            intGhostCounter -= 1
        intGhostCounter = intNumOfAdvGhosts
        while intGhostCounter > 0:
            objNewGhost = Adv_Ghost(screen)
            groupGhosts.add(objNewGhost)
            intGhostCounter -= 1
        intGhostCounter = intNumOfExpGhosts
        while intGhostCounter > 0:
            objNewGhost = Exp_Ghost(screen)
            groupGhosts.add(objNewGhost)
            intGhostCounter -= 1
        intGhostCounter = intNumOfNMGhosts
        while intGhostCounter > 0:
            objNewGhost = NM_Ghost(screen)
            groupGhosts.add(objNewGhost)
            intGhostCounter -= 1

        ''' Debris group'''
        intNumOfDebris = 40
        groupAllDebris = Group()
        while intNumOfDebris > 0:
            objNewDebris = Debris(screen)
            groupAllDebris.add(objNewDebris)
            intNumOfDebris -= 1

        intCountIn = 3
        while intCountIn > 0:
            objGameBackground.blitself()
            textRendCount = fontMain100.render(str(intCountIn), False, colorValYellow)
            screen.blit(textRendCount, [350, 225])
            pygame.display.flip()
            time.sleep(0.5)
            intCountIn -= 1
        objGameBackground.blitself()
        textRendCount = fontMain100.render('GO!', False, colorValYellow)
        screen.blit(textRendCount, [300, 225])
        pygame.display.flip()
        time.sleep(0.5)
        # Load Title Screen Music
        pygame.mixer.music.load('sounds/Level_Funk.ogg')
        pygame.mixer.music.play(loops=-1, start=0.0, fade_ms=1000)
        # Make Title Text
        textRendTitle = fontMain25.render("Spirit Cleaners, Inc.", False, colorValYellow)
        # Make Level Text
        textRendLevel = fontMain25.render('Level: ' + str(intLevel), False, colorValYellow)
        # Make Score Text
        textRendScore = fontMain25.render('Score: ' + str(intTotalScore), False, colorValYellow)
        # Set battery level (100%)
        intBatteryLevel = 10000

        # Main Level Loop
        boolLevelRunning = True
        boolAcceptingInput = True
        stateMoveDirection = '0'

        while boolLevelRunning and not boolGameOver:

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
            for currentSprite in groupGhosts.sprites():
                currentSprite.move_and_blitself()
            for currentSprite in groupPlayerGroup.sprites():
                currentSprite.move_and_blitself()

            # Put the image of the title text on the screen at 10x10
            screen.blit(textRendTitle, [10, 10])
            screen.blit(textRendLevel, [325, 560])
            # Check for collisions update battery or score accordingly
            # First check if player and ghosts collide
            if pygame.sprite.spritecollide(objPlayerVac, groupGhosts, True, pygame.sprite.collide_circle_ratio(0.50)):
                # Remove ghosts player hit
                pygame.sprite.groupcollide(groupPlayerGroup, groupGhosts, False, True)
                # Lose 25% of the full battery charge
                intBatteryLevel -= 2500

            # Second check if player and debris collide
            elif pygame.sprite.spritecollide(objPlayerVac, groupAllDebris, True,
                                             pygame.sprite.collide_circle_ratio(0.50)):
                # Remove debris player hit
                dictDebrisCollide = pygame.sprite.groupcollide(groupPlayerGroup, groupAllDebris, False, True)
                # Gain 100 Points per debris piece
                intNumDebrisCollected = len(dictDebrisCollide) + 1
                intTotalScore += (100 * intNumDebrisCollected)
                # Render the score text
                textRendScore = fontMain25.render('Score: ' + str(intTotalScore), False, colorValYellow)

            # Render the battery text
            textRendBattery = fontMain25.render(('Battery: ' + str(int(intBatteryLevel / 100)) + '%'), True,
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
            elif not groupAllDebris:
                boolLevelRunning = False
                pygame.mixer.music.fadeout(1000)
            # Check if battery still has charge and decrease the battery level
            elif intBatteryLevel > 0:
                intBatteryLevel -= 1
            # Tick speed to control loop speed
            obj_Clock.tick(intGameSpeed)
        # increase game speed by 5 each time a level progresses
        intGameSpeed += 5
        intLevel += 1

    pygame.mixer.music.fadeout(1000)
    return intTotalScore + 100
