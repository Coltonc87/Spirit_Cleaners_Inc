"""

This is the module for the main level loop of the game

"""

import sys
import pygame
import time
import random
from Class_Background import Background
from Class_Grid import Grid
from Class_Vacuum import Vacuum
from Class_Holy_Water import Holy_Water
from Class_Debris import Debris
from Class_Basic_Ghost import Basic_Ghost
from Class_Adv_Ghost import Adv_Ghost
from Class_Expert_Ghost import Exp_Ghost
from Class_Nightmare_Ghost import NM_Ghost
from Class_Floor_Hole import Floor_Hole
from pygame.sprite import Group


def run_levels(screen):
    Ghost_Collide_Sound = pygame.mixer.Sound("sounds/Ghost_Collide.ogg")
    Holy_Water_Sound = pygame.mixer.Sound("sounds/Holy_Water.ogg")
    Count_Beep_Sound = pygame.mixer.Sound("sounds/Count_Beep.ogg")
    Count_Chord_Sound = pygame.mixer.Sound("sounds/Count_Chord.ogg")
    Game_Over_Sound = pygame.mixer.Sound("sounds/Game_Over.ogg")
    # Level counter
    intLevel = 1
    # Clock Object for controlling game speed
    obj_Clock = pygame.time.Clock()
    # Set flag for game to exit
    boolGameOver = False
    # Set initial speed
    intGameSpeed = 110
    # State of the vacuum "inspired" or not
    boolStateCheck = False
    # State of the vacuum "possession"
    boolPossessedCheck = False
    # Grid indices
    intMasterIndices = [0, 1, 2, 3, 4, 5, 6, 7, 10, 11, 12, 13, 16, 17, 18, 19, 20, 21, 22, 23]
    # Pick up text state, display counter, and coordinate values
    boolShowPickUp = False
    intPickUpCountDown = 0
    intPickUpx = 0
    intPickUpy = 0
    # Make score variable
    intTotalScore = 0
    # Set yellow to be used for text
    colorValYellow = [255, 255, 0]
    # Set blue to be used for text
    colorValBlue = [173, 216, 230]
    # Load custom font in 2 sizes, 25 and 100 point
    fontMain25 = pygame.font.Font('fighting-spirit-turbo.bold-italic.ttf', 25)
    fontMain100 = pygame.font.Font('fighting-spirit-turbo.bold-italic.ttf', 100)
    # Levels run
    while not boolGameOver:
        # Start the level and create the background object
        objGameBackground = Background(screen)
        # Make a grid object to hold tile states and return starting coordinates of objects
        # This is being simplified or replaced with the list below.
        objGrid = Grid(screen)

        ''' player group'''
        objPlayerVac = Vacuum(screen)
        groupPlayer = Group()
        groupPlayer.add(objPlayerVac)

        intAvailableIndices = intMasterIndices.copy()

        ''' ghost group'''
        if intLevel < 4:
            intNumOfBasicGhosts = 6 - intLevel
            intNumOfAdvGhosts = intLevel - 1
            intNumOfExpGhosts = intLevel - 2
            intNumOfNMGhosts = random.randint(0, 1)
        elif intLevel == 4:
            intNumOfBasicGhosts = 1
            intNumOfAdvGhosts = 2
            intNumOfExpGhosts = 2
            intNumOfNMGhosts = random.randint(0, 1)
        elif intLevel == 5:
            intNumOfBasicGhosts = 0
            intNumOfAdvGhosts = 3
            intNumOfExpGhosts = 2
            intNumOfNMGhosts = random.randint(1, 2)
        elif intLevel == 6:
            intNumOfBasicGhosts = 0
            intNumOfAdvGhosts = 2
            intNumOfExpGhosts = 3
            intNumOfNMGhosts = 2
        elif intLevel > 6:
            intNumOfBasicGhosts = 0
            intNumOfAdvGhosts = 3
            intNumOfExpGhosts = 6
            intNumOfNMGhosts = 2

        groupGhosts = Group()

        intGhostCounter = intNumOfBasicGhosts
        while intGhostCounter > 0:
            intRandGridIndex = random.choice(intAvailableIndices)
            objNewGhost = Basic_Ghost(screen, objGrid.returnTileX(intRandGridIndex),
                                      objGrid.returnTileY(intRandGridIndex))
            objGrid.setTileState(intRandGridIndex)
            intAvailableIndices.remove(intRandGridIndex)
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
        intNumOfDebris = 60
        groupAllDebris = Group()
        while intNumOfDebris > 0:
            objNewDebris = Debris(screen)
            groupAllDebris.add(objNewDebris)
            intNumOfDebris -= 1

        intAvailableIndices = intMasterIndices.copy()

        '''Floor holes group'''
        intNumOfHoles = 2
        groupAllHoles = Group()
        # List to hold available tiles instead of grid object

        while intNumOfHoles > 0:
            intRandGridIndex = random.choice(intAvailableIndices)
            objNewHole = Floor_Hole(screen, objGrid.returnTileX(intRandGridIndex),
                                    objGrid.returnTileY(intRandGridIndex))
            objGrid.setTileState(intRandGridIndex)
            intAvailableIndices.remove(intRandGridIndex)
            groupAllHoles.add(objNewHole)
            intNumOfHoles -= 1

        # Check for collisions between any debris and holes and remove debris so nothing is floating
        pygame.sprite.groupcollide(groupAllDebris, groupAllHoles, True, False)

        ''' holy water group'''
        groupHolyWater = Group()
        intRandGridIndex = random.choice(intAvailableIndices)
        objHolyWater = Holy_Water(screen, objGrid.returnTileX(intRandGridIndex),
                                  objGrid.returnTileY(intRandGridIndex))
        objGrid.setTileState(intRandGridIndex)
        intAvailableIndices.remove(intRandGridIndex)
        groupHolyWater.add(objHolyWater)

        # Countdown
        intCountIn = 3
        while intCountIn > 0:
            objGameBackground.blitself()
            textRendCount = fontMain100.render(str(intCountIn), False, colorValYellow)
            screen.blit(textRendCount, [350, 225])
            pygame.mixer.Sound.play(Count_Beep_Sound)
            pygame.display.flip()
            time.sleep(0.5)
            intCountIn -= 1
        objGameBackground.blitself()
        textRendCount = fontMain100.render('GO!', False, colorValYellow)
        screen.blit(textRendCount, [300, 225])
        pygame.mixer.Sound.play(Count_Chord_Sound)
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
            # objGrid.blitself()
            for currentSprite in groupAllHoles.sprites():
                currentSprite.blitself()
            for currentSprite in groupAllDebris.sprites():
                currentSprite.blitself()
            for currentSprite in groupHolyWater.sprites():
                currentSprite.blitself()
            for currentSprite in groupPlayer.sprites():
                currentSprite.move_and_blitself()
            for currentSprite in groupGhosts.sprites():
                currentSprite.move_and_blitself()

            # Put the image of the title text on the screen at 10x10
            screen.blit(textRendTitle, [10, 10])
            screen.blit(textRendLevel, [325, 560])
            # Check for collisions update battery or score accordingly
            if pygame.sprite.spritecollide(objPlayerVac, groupHolyWater, True,
                                           pygame.sprite.collide_circle_ratio(0.5)):
                # Remove holy water player hit
                pygame.sprite.groupcollide(groupPlayer, groupHolyWater, True, False)
                pygame.mixer.Sound.play(Holy_Water_Sound)
                # Vacuum becomes "inspired"
                objPlayerVac.inspire()
                boolStateCheck = objPlayerVac.inspire_state()
                # Set inspire counter for time limit in loops to stay inspired
                intInspireCounter = 600
                if boolPossessedCheck:
                    objPlayerVac.exorcise()
                    boolPossessedCheck = objPlayerVac.possessed_state()

            if pygame.sprite.spritecollide(objPlayerVac, groupAllHoles, True, pygame.sprite.collide_circle_ratio(0.15)):
                # Remove ghosts player hit
                pygame.sprite.groupcollide(groupPlayer, groupAllHoles, True, False)
                boolLevelRunning = False
                boolGameOver = True
                pygame.mixer.Sound.play(Game_Over_Sound)

            # Check if player and ghosts collide
            if not boolStateCheck:
                # Check if vacuum is not currently inspired, which would result in being able to pass ghosts
                if pygame.sprite.spritecollide(objPlayerVac, groupGhosts, True,
                                               pygame.sprite.collide_circle_ratio(0.50)):
                    # Remove ghosts player hit
                    pygame.sprite.groupcollide(groupPlayer, groupGhosts, False, True)
                    # Lose 25% of the full battery charge
                    intBatteryLevel -= 2500
                    pygame.mixer.Sound.play(Ghost_Collide_Sound)
                    # Vacuum becomes "possessed"
                    objPlayerVac.possess()
                    boolPossessedCheck = objPlayerVac.possessed_state()
                    # Set inspire counter for time limit in loops to stay inspired
                    intPossessionCounter = 400

            # Check if player and debris collide
            if pygame.sprite.spritecollide(objPlayerVac, groupAllDebris, True,
                                           pygame.sprite.collide_circle_ratio(0.50)):
                # Remove debris player hit
                dictDebrisCollide = pygame.sprite.groupcollide(groupPlayer, groupAllDebris, False, True)
                # Gain 100 Points per debris piece
                intNumDebrisCollected = len(dictDebrisCollide) + 1
                pygame.mixer.Sound.play(Count_Beep_Sound)
                intTotalScore += (100 * intNumDebrisCollected)
                # Render the score text
                textRendScore = fontMain25.render('Score: ' + str(intTotalScore), False, colorValYellow)
                # Render a pick up score
                textPickUp = fontMain25.render(str(100 * intNumDebrisCollected), False, colorValYellow)
                boolShowPickUp = True
                intPickUpCountDown = 50
                intPickUpx = random.randint(-50, 25)
                intPickUpy = random.randint(-50, 25)

            # Render the battery text
            textRendBattery = fontMain25.render(('Battery: ' + str(int(intBatteryLevel / 100)) + '%'), True,
                                                colorValYellow)
            # Place the score text on the screen
            screen.blit(textRendScore, [300, 10])
            # Place the battery text on the screen
            screen.blit(textRendBattery, [600, 10])

            if boolShowPickUp and intPickUpCountDown > 0:
                intPickUpCountDown -= 1
                screen.blit(textPickUp,
                            [objPlayerVac.rect.centerx + intPickUpx, objPlayerVac.rect.centery + intPickUpy])
            else:
                boolShowPickUp = False

            if boolStateCheck and intInspireCounter > 1:
                intInspireCounter -= 1
                textInspCountDown = fontMain25.render(str(int(intInspireCounter / 100)), False, colorValYellow)
                screen.blit(textInspCountDown, [objPlayerVac.rect.centerx - 10, objPlayerVac.rect.centery - 60])
                textInspired = fontMain25.render('INSPIRED!', False, colorValYellow)
                screen.blit(textInspired, [objPlayerVac.rect.centerx - 75, objPlayerVac.rect.centery + 20])
            else:
                objPlayerVac.uninspire()
                boolStateCheck = objPlayerVac.inspire_state()

            if boolPossessedCheck and intPossessionCounter > 1:
                intPossessionCounter -= 1
                textPossessCountDown = fontMain25.render(str(int(intPossessionCounter / 100)), False, colorValBlue)
                screen.blit(textPossessCountDown, [objPlayerVac.rect.centerx - 10, objPlayerVac.rect.centery - 60])
                textInspired = fontMain25.render('POSSESSED!', False, colorValBlue)
                screen.blit(textInspired, [objPlayerVac.rect.centerx - 100, objPlayerVac.rect.centery + 20])
            else:
                objPlayerVac.exorcise()
                boolPossessedCheck = objPlayerVac.possessed_state()

            # Erase old and redraw the screen items in new locations
            pygame.display.flip()

            # If the battery is dead end the game
            if intBatteryLevel <= 0:
                boolLevelRunning = False
                boolGameOver = True
                pygame.mixer.Sound.play(Game_Over_Sound)
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
    return intTotalScore
