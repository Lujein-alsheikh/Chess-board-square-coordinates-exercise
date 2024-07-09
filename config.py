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

# we have to initialize the font first. Otherwise, I will get an error
pygame.font.init()
font = pygame.font.Font("freesansbold.ttf", 20)
big_font = pygame.font.Font("freesansbold.ttf", 150)

# drawing the pieces
image_size = (60, 60)

# The find square/name square buttons, the white/random/black buttons, and the start button all have height 60.
# Margin between any two consecutive buttons is 16.
highest_button_top_left_y = 166  # this corresponds to the find/name square buttons
find_square_score_top_left_y = 220
name_square_response_top_left_y = 220

time_limit = 30.0  # in seconds
FPS = 60
