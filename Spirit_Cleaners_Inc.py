import os
import sqlite3
import pygame
import Levels as Levels
import HighScoreScreen as HighScoreScreen

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
cur = sqlConn.cursor()

# try to create a table if one doesn't exist
try:
    # Create table
    cur.execute('''CREATE TABLE storage(playerInitials TEXT, playerScore TEXT)''')
# except if table exists
except sqlConn.DatabaseError:
    print("Table Exists.")

# Initial data for testing
# current_string = 'INSERT INTO storage (playerInitials, playerScore) VALUES ("EKC", "1000000");'
# cur.execute(current_string)
# sqlConn.commit()

highScores = cur.execute("SELECT * FROM storage")

listAllScores = cur.fetchall()

# Main Game, Start PyGame
pygame.init()
# Define the main screen
game_screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Spirit Cleaners, Inc.")
HighScoreScreen.high_score_screen(game_screen, listAllScores)
Levels.run_levels(game_screen)

# Close database
sqlConn.close()
