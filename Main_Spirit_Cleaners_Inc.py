"""

This is the main script for the game run it to test all features

"""

import os
import sqlite3
import pygame
import Func_Levels as Levels
import Func_High_Score_Screen as Score_Screen
import Func_Title_Screen as Title_Screen
import Func_Get_Initials as Initials_Screen

"""Setting up and checking the SQL Database for high scores"""
# set directory to the current files path for the game
directory_name = os.path.dirname(__file__)
# set database path to the current directory
database_path = os.path.join(directory_name, "Top_10_Scores.db")

# try and except to handle any error when connecting to database and exit if an error occurs
try:
    sqlConnection = sqlite3.connect(database_path)
except sqlConnection.DatabaseError:
    print("Cannot open database.")
    exit(0)

# Create cursor for commands to SQL
sqlCursor = sqlConnection.cursor()

# try to create a table if one doesn't exist
try:
    # Create table
    sqlCursor.execute('''CREATE TABLE storage(playerInitials CHAR(3), playerScore INT(255))''')
# except if table exists
except sqlConnection.DatabaseError:
    print("Table Exists.")

# Initial data for testing
# current_string = 'INSERT INTO storage (playerInitials, playerScore) VALUES ("RRC", 2000);'
# sqlCursor.execute(current_string)
# sqlConn.commit()

# Read the scores in as a list of tuples from database, sorting with the query
sqlCursor.execute("SELECT * FROM storage ORDER BY playerScore DESC")
list_All_Scores = sqlCursor.fetchall()
# Main Game, Start PyGame
pygame.init()
# Define the main screen size
game_screen = pygame.display.set_mode((800, 600))
# Set window caption
pygame.display.set_caption("Spirit Cleaners, Inc.")
# Show title screen
Title_Screen.display_screen(game_screen)
# Show high scores
Score_Screen.display_screen(game_screen, list_All_Scores)
# Run the main levels loop until Game Over and return the score
intScoreReturn = Levels.run_levels(game_screen)

# Check if the current score is in the top 10 scores
bool_Score_Check = False
for row in list_All_Scores:
    for item in row:
        # Check if item is an integer to prove if it's a score or not
        if isinstance(item, int):
            # If current score is higher than any previous score return True
            if item < intScoreReturn:
                bool_Score_Check = True
# If it's a new ranking score run the initials input screen
if bool_Score_Check:
    charNewScoreInit = Initials_Screen.display_screen(game_screen, intScoreReturn)
    current_string = 'INSERT INTO storage (playerInitials, playerScore) ' \
                     'VALUES ("' + charNewScoreInit + '", ' + str(intScoreReturn) + ');'
    sqlCursor.execute(current_string)
    sqlConnection.commit()
    sqlCursor.execute("SELECT * FROM storage ORDER BY playerScore DESC")
    list_All_Scores = sqlCursor.fetchall()


# Display high score screen
Score_Screen.display_screen(game_screen, list_All_Scores)
# Show title screen
Title_Screen.display_screen(game_screen)
# Close database
sqlConnection.close()
