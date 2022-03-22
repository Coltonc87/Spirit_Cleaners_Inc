"""

This is the module for displaying the title screen

"""

import sys
import pygame
from Class_Background import Background


def display_screen(screen):
    # explosion_sound = pygame.mixer.Sound("assets/sounds/explosion_1.wav")
    # pygame.mixer.Sound.play(explosion_sound)
    # Load Title Screen Music
    pygame.mixer.music.load('sounds/Title_Theme.ogg')
    # Play music
    pygame.mixer.music.play(loops=-1, start=0.0, fade_ms=1000)
    # Clock Object for controlling game speed
    obj_Clock = pygame.time.Clock()
    # Create the background object instance
    objGameBackground = Background(screen)
    # Set initial RGB color to be used for text
    colorValCurrent = [255, 255, 0]
    # Load custom font in 2 sizes, 100 and 25 point
    fontTitleScreen100 = pygame.font.Font('fighting-spirit-turbo.bold-italic.ttf', 100)
    fontTitleScreen25 = pygame.font.Font('fighting-spirit-turbo.bold-italic.ttf', 25)
    # Boolean for run state
    boolTitleScreen = True
    # Initial state for text color glow effect
    boolColorDown = True
    while boolTitleScreen:
        # Monitor to user input
        for event in pygame.event.get():
            # Make the red x work...
            if event.type == pygame.QUIT:
                sys.exit()

            elif event.type == pygame.KEYDOWN:
                # Press escape key to exit
                if event.key == pygame.K_ESCAPE:
                    sys.exit()
                # Press space to move to next screen
                elif event.key == pygame.K_SPACE:
                    boolTitleScreen = False

        # Make Title Text pieces
        textRendSpirit = fontTitleScreen100.render("Spirit", False, colorValCurrent)
        textRendCleaners = fontTitleScreen100.render("Cleaners", False, colorValCurrent)
        textRendInc = fontTitleScreen100.render("Inc.", False, colorValCurrent)
        # Make text for space bar prompt
        textRendSpace = fontTitleScreen25.render("Press Space Bar to Continue", False, colorValCurrent)
        # Draw the background object
        objGameBackground.blitself()
        # Put the image of the text on the screen
        screen.blit(textRendSpirit, [100, 100])
        screen.blit(textRendCleaners, [200, 200])
        screen.blit(textRendInc, [300, 300])
        screen.blit(textRendSpace, [225, 550])
        # Erase old and redraw the screen items in new locations
        pygame.display.flip()

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
