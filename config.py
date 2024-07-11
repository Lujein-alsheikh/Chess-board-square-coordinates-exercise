import pygame

# suitable height and width for my screen
WIDTH = 1000
HEIGHT = 680
background_color = (0, 0, 0)

# board size and coordinates. A bit bigger than the board of lichess.
board_left_top_x = 404
board_left_top_y = 92
board_length = 496
square_length = 62

# we have to initialize the font first. Otherwise, we will get an error
pygame.font.init()
font = pygame.font.Font("freesansbold.ttf", 20)
big_font = pygame.font.Font("freesansbold.ttf", 150)

# We need to resize the images later
image_size = (60, 60)

# corresponds to the find/name square rectangles
highest_button_top_left_y = 166 
# corresponds to the score rectangle shown in case of find square 
find_square_score_top_left_y = 220 
# corresponds to the reponse rectangle in case of name square
name_square_response_top_left_y = 220 

# in seconds
time_limit = 30.0  
# Frames Per Second. Used to update the screen.
FPS = 60
