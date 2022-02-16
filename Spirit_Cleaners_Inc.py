import os
import sqlite3
import pygame
import Levels as Levels
import HighScoreScreen as HighScoreScreen
import TitleScreen as Titlescreen
import GetInitials as GetInitials

"""Setting up and checking the SQL Database for high scores"""
# set directory to the current files path
directory_name = os.path.dirname(__file__)
# set database path to the current directory
database_path = os.path.join(directory_name, "Top_10_Scores.db")

# print the path to check it
print(database_path)

# try and except to handle any error when connecting to database and exit if an error occurs
try:
    sqlConn = sqlite3.connect(database_path)
except sqlConn.DatabaseError:
    print("Cannot open database.")
    exit(0)

# Create cursor for commands to SQL
sqlCursor = sqlConn.cursor()

# try to create a table if one doesn't exist
try:
    # Create table
    sqlCursor.execute('''CREATE TABLE storage(playerInitials CHAR(3), playerScore INT(255))''')
# except if table exists
except sqlConn.DatabaseError:
    print("Table Exists.")

# Initial data for testing
# current_string = 'INSERT INTO storage (playerInitials, playerScore) VALUES ("RRC", 2000);'
# sqlCursor.execute(current_string)
# sqlConn.commit()

highScores = sqlCursor.execute("SELECT * FROM storage ORDER BY playerScore DESC")

listAllScores = sqlCursor.fetchall()

# Main Game, Start PyGame
pygame.init()
# Define the main screen
game_screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Spirit Cleaners, Inc.")
Titlescreen.title_screen(game_screen)
HighScoreScreen.high_score_screen(game_screen, listAllScores)
intScoreReturn = Levels.run_levels(game_screen)

boolHighScoreCheck = False
for row in listAllScores:
    for item in row:
        if isinstance(item, int):
            if item < intScoreReturn:
                boolHighScoreCheck = True

if boolHighScoreCheck:
    GetInitials.get_initials(game_screen, intScoreReturn)

# Close database
sqlConn.close()
