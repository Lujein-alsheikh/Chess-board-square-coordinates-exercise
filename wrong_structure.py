import pygame
import random

pygame.init()

# suitable height and width for my screen
WIDTH = 1000
HEIGHT = 680 
background_color = (0,0,0)
# board size and coordinates. A bit bigger than the board of lichess.
board_left_top_x = 404
board_left_top_y = 92
board_length = 496
square_length=62

screen = pygame.display.set_mode([WIDTH,HEIGHT])
pygame.display.set_caption('Square Coordinates Exercise')
font=pygame.font.Font('freesansbold.ttf', 20)
big_font = pygame.font.Font('freesansbold.ttf', 150)

# loading the images
image_size= (60,60)
def load_black_images(img_size = image_size):
        b_queen = pygame.image.load('Pieces_images/bQ.svg')
        b_queen = pygame.transform.scale(b_queen, img_size)

        b_king = pygame.image.load('Pieces_images/bK.svg')
        b_king = pygame.transform.scale(b_king, img_size)

        b_rook = pygame.image.load('Pieces_images/bR.svg')
        b_rook = pygame.transform.scale(b_rook, img_size)

        b_bishop = pygame.image.load('Pieces_images/bB.svg')
        b_bishop = pygame.transform.scale(b_bishop, img_size)

        b_knight = pygame.image.load('Pieces_images/bN.svg')
        b_knight = pygame.transform.scale(b_knight, img_size)

        b_pawn = pygame.image.load('Pieces_images/bP.svg')
        b_pawn = pygame.transform.scale(b_pawn, (img_size[0],img_size[1]))

        images_dict = {'b_queen': b_queen, 'b_king': b_king, 'b_rook': b_rook, 'b_bishop': b_bishop, 'b_knight': b_knight,
                       'b_pawn': b_pawn}
        
        return images_dict

def load_white_images(img_size = image_size):
        w_queen = pygame.image.load('Pieces_images/wQ.svg')
        w_queen = pygame.transform.scale(w_queen, img_size)

        w_king = pygame.image.load('Pieces_images/wK.svg')
        w_king = pygame.transform.scale(w_king, img_size)

        w_rook = pygame.image.load('Pieces_images/wR.svg')
        w_rook = pygame.transform.scale(w_rook, img_size)

        w_bishop = pygame.image.load('Pieces_images/wB.svg')
        w_bishop = pygame.transform.scale(w_bishop, img_size)

        w_knight = pygame.image.load('Pieces_images/wN.svg')
        w_knight = pygame.transform.scale(w_knight, img_size)

        w_pawn = pygame.image.load('Pieces_images/wP.svg')
        w_pawn = pygame.transform.scale(w_pawn, (img_size[0], img_size[1]))

        images_dict = {'w_queen': w_queen, 'w_king': w_king, 'w_rook': w_rook, 'w_bishop': w_bishop, 'w_knight': w_knight,
                       'w_pawn': w_pawn}
        return images_dict

# drawing board and pieces
def draw_board(screen= screen, board_left_top_x= board_left_top_x, board_left_top_y= board_left_top_y, board_length=board_length):
            board_image= pygame.image.load('Pieces_images/maple.jpg')
            board_image = pygame.transform.scale(board_image, (board_length,board_length))
            screen.blit( board_image, (board_left_top_x, board_left_top_y))

def pieces_offsets_fun(side):
        if side == 'white':
            return {'rook':[0,7], 'knight':[1,6], 'bishop':[2,5], 'queen':[3], 'king':[4]}
        elif side == 'black':
              return {'rook':[0,7], 'knight':[1,6], 'bishop':[2,5], 'queen':[4], 'king':[3]}

def draw_pieces(board_side, board_left_top_x= board_left_top_x, board_left_top_y=board_left_top_y, square_length =square_length):
    pieces_except_pawn = ['rook', 'knight', 'bishop', 'queen', 'king']
    
    for piece in pieces_except_pawn:
            white_piece = load_white_images()['w_'+piece]
            black_piece = load_black_images()['b_'+piece]
            piece_offsets = pieces_offsets_fun(side=board_side)[piece]
            if board_side == 'white':               
                first_row_piece = white_piece
                eight_row_piece = black_piece
            elif board_side == 'black':
                first_row_piece = black_piece
                eight_row_piece = white_piece     
            for i in range(len(piece_offsets)):
                offset = piece_offsets[i]
                screen.blit(eight_row_piece,(board_left_top_x + square_length * offset,board_left_top_y)) 
                screen.blit(first_row_piece,(board_left_top_x + square_length * offset,board_left_top_y + square_length*7))

    # The +2 and -3 are added to centralize the pawns.
    if board_side == 'white':
        second_row_pawns = load_white_images()['w_pawn']
        seventh_row_pawns = load_black_images()['b_pawn']
    elif board_side == 'black':
         second_row_pawns = load_black_images()['b_pawn']
         seventh_row_pawns = load_white_images()['w_pawn']

    for i in range(8):
            screen.blit(second_row_pawns, (board_left_top_x + square_length * i + 2, board_left_top_y + square_length* 6 -3))    
            screen.blit(seventh_row_pawns, (board_left_top_x + square_length * i + 2, board_left_top_y + square_length))       

# generating random coordinates
def create_random_coord():
    columns = ['a','b','c','d','e','f','g','h']
    rows = ['1','2','3','4','5','6','7','8']
    random_col = random.choice(columns)
    random_row = random.choice(rows)
    square = random_col+random_row
    return square

def draw_button(color, rect, text, screen= screen):
    pygame.draw.rect(screen, color, rect)
    border_rect = rect.inflate(2, 2)  # Expand the rectangle by 2 pixels on all sides
    pygame.draw.rect(screen, 'lightcoral', border_rect, width=1)
    text_surface = font.render(text, True, 'white')
    text_rect = text_surface.get_rect(center=(rect[0] + rect[2] // 2, rect[1] + rect[3] // 2))
    screen.blit(text_surface, text_rect)

def button_rect(top_left_x, top_left_y, width, height):
       return pygame.Rect(top_left_x, top_left_y, width, height)
       
# buttons rectangles       
button_rect_find_square = button_rect(top_left_x = 30, top_left_y = 184, width = 170, height = 60)   
button_rect_find_coord = button_rect(top_left_x = 200, top_left_y = 184, width = 170, height = 60 )
button_rect_white_sided_board = button_rect(top_left_x = 30, top_left_y = 260, width = 113.33, height = 60)
button_rect_randomly_sided_board = button_rect(top_left_x = 143.33, top_left_y = 260, width = 113.33, height = 60)
button_rect_black_sided_board = button_rect(top_left_x = 256.66, top_left_y = 260, width = 113.33, height = 60)

def draw_all_buttons(square_button_color, coord_button_color, white_sided_board_color, randomly_sided_board_color, black_sided_board_color):

    draw_button(square_button_color, button_rect_find_square, "find square")
    draw_button(coord_button_color, button_rect_find_coord, "find coordinates")
    draw_button(white_sided_board_color, button_rect_white_sided_board, "white")
    draw_button(randomly_sided_board_color, button_rect_randomly_sided_board, "random")
    draw_button(black_sided_board_color, button_rect_black_sided_board, "black")

# top left coordinates of each square
def squares_coord(board_side, board_left_top_x = board_left_top_x, board_left_top_y =board_left_top_y, square_length =square_length):
        
        columns_white = ['a','b','c','d','e','f','g','h']
        rows_white = ['1','2','3','4','5','6','7','8']

        columns_black = ['h','g','f','e','d','c','b','a']
        rows_black = ['8','7','6','5','4','3','2','1']

        cols_offsets = [0,1,2,3,4,5,6,7]
        rows_offsets = [7,6,5,4,3,2,1,0]

        if board_side == 'white':
               columns = columns_white
               rows = rows_white
        elif board_side == 'black':
               columns = columns_black   
               rows = rows_black  

        squares_coord = {}
        for (col, col_offset) in zip(columns, cols_offsets):
            top_left_x = board_left_top_x + col_offset * square_length
            for (row, row_offset) in zip(rows, rows_offsets):          
                top_left_y = board_left_top_y + row_offset * square_length
                squares_coord[col+row] = (top_left_x, top_left_y)
        return squares_coord
          
def click_within_square(click_x, click_y, square_top_left_x, square_top_left_y, square_length = square_length):
        if square_top_left_x <= click_x <= square_top_left_x  + square_length and  square_top_left_y <= click_y <= square_top_left_y + square_length:
                return True
        else:
              return False

def click_within_board(click_x, click_y, board_left_top_x = board_left_top_x, board_left_top_y= board_left_top_y, board_length= board_length):
      if board_left_top_x <= click_x <= board_left_top_x + board_length and board_left_top_y <= click_y <= board_left_top_y + board_length:
            return True
      else:
            return False        

def draw_coord(coord, screen= screen, font = big_font, board_left_top_x = board_left_top_x, board_left_top_y=board_left_top_y, board_length=board_length):
                text_surface = big_font.render(coord, True, 'lavenderblush')
                text_rect = text_surface.get_rect(center=(board_left_top_x + 0.5 * board_length, board_left_top_y + 0.5 * board_length))
                screen.blit(text_surface, text_rect)



# this function is used later to draw a red frame around a wrongly clicked on square.
def finding_wrong_square(board_side, click_x, click_y):
            
            for key,value in squares_coord(board_side).items():
                    if value[0]<= click_x < value[0] + square_length and value[1] <= click_y < value[1] + square_length:
                            return (key,value)
                
def frame_around_square(board_side, click_x, click_y, square_length = square_length, frame_thickness = 2, color='darkred', board_left_top_x =board_left_top_x,
board_left_top_y = board_left_top_y):

        square_name,square_coord = finding_wrong_square(board_side, click_x, click_y)
        print("Wrong! You clicked on ",square_name)       
        frame_rect = pygame.Rect(square_coord[0] - frame_thickness, square_coord[1] - frame_thickness, square_length + frame_thickness, square_length + frame_thickness)          
        # return frame_rect
        pygame.draw.rect(screen, 'darkred', frame_rect, 2)


def button_clicked(button_rect, click_pos):
       # click_pos is supposed to be a tuple because event.pos which is the input argument is a tuple.
       if button_rect.collidepoint(click_pos): 
            return True
       else:
            return False

def square_or_coord_button_clicked(click_pos):
       if button_clicked(button_rect_find_square, click_pos) or button_clicked(button_rect_find_coord, click_pos):
              return True
       else:
              return False

def board_side_button_clicked(click_pos):
        if button_clicked(button_rect_white_sided_board, click_pos) or button_clicked(button_rect_black_sided_board, click_pos) or \
        button_clicked(button_rect_randomly_sided_board, click_pos):
               return True
        else:
               return False

def draw_score(some_score, color= 'firebrick', frame_thickness = 2, frame_top_left_x = 30, frame_top_left_y= 336, width= 340, height= 120):
        # First overwrite the previous score by filling the score area with the background black
        inner_rect = pygame.Rect(frame_top_left_x , frame_top_left_y, width, height)
        screen.fill(color, inner_rect)
        frame_rect = pygame.Rect(frame_top_left_x - frame_thickness, frame_top_left_y - frame_thickness, width + frame_thickness, height + frame_thickness)          
        pygame.draw.rect(screen, 'grey', frame_rect, 2)
        score_text =  font.render(f'Score: {some_score}', True, 'black')
        text_rect = score_text.get_rect(center=(frame_top_left_x + width / 2, frame_top_left_y + height / 2))
        screen.blit(score_text, text_rect)
        
def draw_timer(starting_time, color= 'olive', frame_thickness=2,frame_top_left_x = 30, frame_top_left_y= 472, width= 340, height= 120):

                    elapsed_time = pygame.time.get_ticks() - starting_time
                    remaining_time_s = (time_limit - elapsed_time) // 1000
                    inner_rect = pygame.Rect(frame_top_left_x , frame_top_left_y, width, height)
                    screen.fill(color, inner_rect)

                    frame_rect = pygame.Rect(frame_top_left_x - frame_thickness, frame_top_left_y - frame_thickness, width + frame_thickness, height + frame_thickness)          
                    pygame.draw.rect(screen, 'grey', frame_rect, 2)

                    timer_text = font.render(f'Time left: {remaining_time_s}s', True, 'black')
                    text_rect = timer_text.get_rect(center=(frame_top_left_x + width / 2, frame_top_left_y + height / 2))
                    screen.blit(timer_text, text_rect)

def draw_timer_clock(some_time, color= 'olive', frame_thickness=2,frame_top_left_x = 30, frame_top_left_y= 472, width= 340, height= 120):
                    inner_rect = pygame.Rect(frame_top_left_x , frame_top_left_y, width, height)
                    screen.fill(color, inner_rect)

                    frame_rect = pygame.Rect(frame_top_left_x - frame_thickness, frame_top_left_y - frame_thickness, width + frame_thickness, height + frame_thickness)          
                    pygame.draw.rect(screen, 'grey', frame_rect, 2)

                    timer_text = font.render(f'Time left: {some_time:.1f}', True, 'black')
                    text_rect = timer_text.get_rect(center=(frame_top_left_x + width / 2, frame_top_left_y + height / 2))
                    screen.blit(timer_text, text_rect)

# default settings
find_square_button_clicked=False
find_coord_button_clicked = False
white_board_button_clicked = False
random_board_button_clicked= False
black_board_button_clicked = False

square_button_color = 'firebrick'
coord_button_color = 'grey'
white_sided_board_color = 'firebrick'
randomly_sided_board_color = 'grey'
black_sided_board_color='grey'

time_limit = 10.0  # time in seconds
board_side = 'white'
board_side_random = False
board_side_chosen = False

find_square_score = 0

run=True
while run:

    for event in pygame.event.get(): 

        if event.type == pygame.QUIT:  
            run = False
        
        elif event.type == pygame.MOUSEBUTTONDOWN:
            click_x, click_y = pygame.mouse.get_pos()

            if square_or_coord_button_clicked(event.pos):
                    if button_clicked(button_rect_find_square, event.pos):
                        square_button_color = 'firebrick'
                        coord_button_color = 'grey'
                        find_square_button_clicked = True
                        find_coord_button_clicked = False
                        print("find_square_button_clicked = True", "find_coord_button_clicked = False")

                    else:
                            square_button_color = 'grey'
                            coord_button_color = 'firebrick'
                            find_square_button_clicked = False
                            find_coord_button_clicked = True
                            print("find_square_button_clicked = False", "find_coord_button_clicked = True")
                    find_square_score = 0        
            elif board_side_button_clicked(event.pos):
                    board_side_chosen = True
                    if button_clicked(button_rect_white_sided_board, event.pos):
                        white_board_button_clicked = True
                        random_board_button_clicked= False
                        black_board_button_clicked = False
                        white_sided_board_color = 'firebrick'
                        randomly_sided_board_color = 'grey'
                        black_sided_board_color='grey'
                        board_side = 'white'
                    elif button_clicked(button_rect_randomly_sided_board, event.pos):
                        white_board_button_clicked = False
                        random_board_button_clicked= True
                        black_board_button_clicked = False
                        white_sided_board_color = 'grey' 
                        randomly_sided_board_color = 'firebrick'
                        black_sided_board_color='grey'
                        board_side_random = True 
                    else:
                        white_board_button_clicked = False
                        random_board_button_clicked= False
                        black_board_button_clicked = True
                        white_sided_board_color = 'grey' 
                        randomly_sided_board_color = 'grey' 
                        black_sided_board_color='firebrick'
                        board_side = 'black'  
                    find_square_score = 0        

    screen.fill(background_color) 
    draw_board()
    draw_pieces(board_side)
    draw_all_buttons(square_button_color, coord_button_color, white_sided_board_color, randomly_sided_board_color, black_sided_board_color)
    
    if find_square_score != 0:
        draw_score(some_score = find_square_score)
    

    if find_square_button_clicked == True and board_side_chosen == True: 
            find_square_score = 0
            clock = pygame.time.Clock()
            time_left = time_limit
            draw_score(some_score = find_square_score)
            correct_square = True
            while time_left > 0:
                    time_passed = clock.get_time()/1000 # in seconds
                    time_left -= time_passed
                    draw_timer_clock(time_left)
                    if correct_square: 
                                if board_side_random == True:
                                      board_side = random.choice(['white', 'black'])
                                draw_board()
                                draw_pieces(board_side)                               
                                print("correct_square= ", correct_square)
                                random_coord = create_random_coord()
                                print("Random coordinates:", random_coord)   
                                correct_square_top_left_x = squares_coord(board_side)[random_coord][0]
                                correct_square_top_left_y = squares_coord(board_side)[random_coord][1]
                                draw_coord(random_coord)     
                                pygame.display.update()

                    else:
  
                        frame_around_square(board_side, click_x, click_y)
                        pygame.display.update()

                    waiting_for_click = True
                    while waiting_for_click and time_left > 0:
                        draw_score(some_score = find_square_score)
                        for event in pygame.event.get():
                            if event.type == pygame.MOUSEBUTTONDOWN:
                                click_x, click_y = pygame.mouse.get_pos()
                                if click_within_board(click_x, click_y) == True:

                                    if click_within_square(click_x =click_x, click_y = click_y, square_top_left_x =correct_square_top_left_x , square_top_left_y = correct_square_top_left_y, square_length = square_length):
                                        correct_square = True
                                        find_square_score = find_square_score + 1    
                                        draw_score(some_score = find_square_score)                                           
                                    else:
                                        correct_square = False
                                    waiting_for_click = False

                    pygame.display.flip()
                    clock.tick(60)
                      
            print("Time is up!")        
            print(f"score is {find_square_score} ") 
            board_side = 'white'  # to reset the board to white side                
            find_square_button_clicked = False    
            board_side_chosen = False       
            
    pygame.display.flip()

pygame.quit()            


'''
if find_square_button_clicked == True and board_side_chosen == True: 
            find_square_score = 0
            start_time = pygame.time.get_ticks()
            draw_score(some_score = find_square_score)
            draw_timer(starting_time = start_time)
            correct_square = True
            while pygame.time.get_ticks() - start_time <= time_limit:
                    draw_timer(starting_time = start_time)
                    if correct_square: 
                                if board_side_random == True:
                                      board_side = random.choice(['white', 'black'])
                                draw_board()
                                draw_pieces(board_side)                               
                                print("correct_square= ", correct_square)
                                random_coord = create_random_coord()
                                print("Random coordinates:", random_coord)   
                                correct_square_top_left_x = squares_coord(board_side)[random_coord][0]
                                correct_square_top_left_y = squares_coord(board_side)[random_coord][1]
                                draw_coord(random_coord)     
                                pygame.display.update()

                    else:
  
                        frame_around_square(board_side, click_x, click_y)
                        pygame.display.update()

                    waiting_for_click = True
                    while waiting_for_click and pygame.time.get_ticks() - start_time <= time_limit:
                        print("waiting for click")
                        draw_score(some_score = find_square_score)
                        draw_timer(starting_time = start_time)
                        for event in pygame.event.get():
                            if event.type == pygame.MOUSEBUTTONDOWN:
                                click_x, click_y = pygame.mouse.get_pos()
                                if click_within_board(click_x, click_y) == True:

                                    if click_within_square(click_x =click_x, click_y = click_y, square_top_left_x =correct_square_top_left_x , square_top_left_y = correct_square_top_left_y, square_length = square_length):
                                        correct_square = True
                                        find_square_score = find_square_score + 1    
                                        draw_score(some_score = find_square_score)                                           
                                    else:
                                        correct_square = False
                                    waiting_for_click = False

                          
            print("Time is up!")        
            print(f"score is {find_square_score} ") 
            board_side = 'white'  # to reset the board to white side                
            find_square_button_clicked = False    
            board_side_chosen = False       

'''