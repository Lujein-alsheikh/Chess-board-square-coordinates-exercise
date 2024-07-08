import config
import pygame
import random

class Board:
        def __init__(self, top_left_x = config.board_left_top_x, top_left_y = config.board_left_top_y, length = config.board_length, side = 'white', random_side=False):
              self.top_left_x = top_left_x
              self.top_left_y = top_left_y
              self.length = length 
              self.side = side
              self.random_side = random_side
              self.original_board_image = pygame.image.load('Pieces_images/maple.jpg')
              self.board_image = pygame.transform.scale(self.original_board_image, (self.length,self.length))

        def draw(self, screen):
            screen.blit(self.board_image, (self.top_left_x, self.top_left_y))

        def click_within_board(self, click_x, click_y)  -> bool:
            if self.top_left_x <= click_x <= self.top_left_x + self.length and self.top_left_y <= click_y <= self.top_left_y + self.length:
                print("Click within board")
                return True
            else:
                print("click outside of board")
                return False 
            
        def get_board_side(self) -> str:
            return self.side   
        
        def set_board_side(self, new_side):
               self.side = new_side 
               print(f"Board side is set to {new_side}")

        def get_random_side(self) -> bool:
              return self.random_side

        def set_random_side(self, bool_value):
              self.random_side = bool_value 
              if bool_value == True:
                    self.set_board_side(random.choice(["white", "black"]))            


class Button:
    def __init__(self, text, is_clicked, top_left_x, top_left_y, width, height, color="dimgrey", border_color='seashell',  text_color='black', font=config.font): 
        self.text = text
        self.color = color 
        self.is_clicked = is_clicked
        self.rect = pygame.Rect(top_left_x, top_left_y, width, height)
        self.border_color = border_color
        self.text_color = text_color
        self.font = font 

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)
        border_rect = self.rect.inflate(2, 2)  # Expand the rectangle by 1 pixel on each side (addition of 2 pixels in total on each side.)
        pygame.draw.rect(screen, self.border_color, border_rect, width= 1)
        # note that the width is of the border color which doesn't affect the coordinates of border_rect
        text_surface = self.font.render(self.text, True, self.text_color)
        text_rect = text_surface.get_rect(center=(self.rect[0] + self.rect[2] // 2, self.rect[1] + self.rect[3] // 2))
        screen.blit(text_surface, text_rect)

    def button_clicked_fun(self, click_pos):
        # click_pos is supposed to be a tuple because event.pos which is the input argument is a tuple.
        if self.rect.collidepoint(click_pos): 
            return True
        else:
            return False
        
    def set_clicked(self): 
       self.is_clicked = True  
       self.color = 'firebrick'  
       print(f"Button {self.text} set to clicked.")

    def unclick(self):
          self.is_clicked=False 
          self.color = "dimgrey"  
          print(f"Button {self.text} set to unclicked.")

    def get_clicked(self):
          #print(f"Checking if Button {self.text} is clicked or not. clicked state is: {self.is_clicked}")
          return self.is_clicked      


class Pieces:
        def __init__(self, img_size=config.image_size):
              self.img_size = img_size
              self.white_images_dict={}
              self.black_images_dict={}
              self.load_white_images() 
              self.load_black_images()

        def load_white_images(self):
                w_queen = pygame.image.load('Pieces_images/wQ.svg')
                w_queen = pygame.transform.scale(w_queen, self.img_size)

                w_king = pygame.image.load('Pieces_images/wK.svg')
                w_king = pygame.transform.scale(w_king, self.img_size)

                w_rook = pygame.image.load('Pieces_images/wR.svg')
                w_rook = pygame.transform.scale(w_rook, self.img_size)

                w_bishop = pygame.image.load('Pieces_images/wB.svg')
                w_bishop = pygame.transform.scale(w_bishop, self.img_size)

                w_knight = pygame.image.load('Pieces_images/wN.svg')
                w_knight = pygame.transform.scale(w_knight, self.img_size)

                w_pawn = pygame.image.load('Pieces_images/wP.svg')
                w_pawn = pygame.transform.scale(w_pawn, (self.img_size[0], self.img_size[1]))

                self.white_images_dict = {'w_queen': w_queen, 'w_king': w_king, 'w_rook': w_rook, 'w_bishop': w_bishop, 'w_knight': w_knight,
                       'w_pawn': w_pawn}
                
        def load_black_images(self):
            b_queen = pygame.image.load('Pieces_images/bQ.svg')
            b_queen = pygame.transform.scale(b_queen, self.img_size)

            b_king = pygame.image.load('Pieces_images/bK.svg')
            b_king = pygame.transform.scale(b_king, self.img_size)

            b_rook = pygame.image.load('Pieces_images/bR.svg')
            b_rook = pygame.transform.scale(b_rook, self.img_size)

            b_bishop = pygame.image.load('Pieces_images/bB.svg')
            b_bishop = pygame.transform.scale(b_bishop, self.img_size)

            b_knight = pygame.image.load('Pieces_images/bN.svg')
            b_knight = pygame.transform.scale(b_knight, self.img_size)

            b_pawn = pygame.image.load('Pieces_images/bP.svg')
            b_pawn = pygame.transform.scale(b_pawn, (self.img_size[0],self.img_size[1]))

            self.black_images_dict = {'b_queen': b_queen, 'b_king': b_king, 'b_rook': b_rook, 'b_bishop': b_bishop, 'b_knight': b_knight,
                        'b_pawn': b_pawn}   

        def pieces_offsets_fun(self, side):
            if side == 'white':
                return {'rook':[0,7], 'knight':[1,6], 'bishop':[2,5], 'queen':[3], 'king':[4]}
            elif side == 'black':
                return {'rook':[0,7], 'knight':[1,6], 'bishop':[2,5], 'queen':[4], 'king':[3]}

        def draw(self, screen, side, board_left_top_x= config.board_left_top_x, board_left_top_y=config.board_left_top_y, square_length = config.square_length):
            if side == 'random':
                board_side = random.choice(['white', 'black'])
            else:
                  board_side = side    
            pieces_except_pawn = ['rook', 'knight', 'bishop', 'queen', 'king']
            for piece in pieces_except_pawn:
                    white_piece = self.white_images_dict['w_'+piece]
                    black_piece = self.black_images_dict['b_'+piece]
                    piece_offsets = self.pieces_offsets_fun(board_side)[piece]
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
                second_row_pawns = self.white_images_dict['w_pawn']
                seventh_row_pawns = self.black_images_dict['b_pawn']
            elif board_side == 'black':
                second_row_pawns = self.black_images_dict['b_pawn']
                seventh_row_pawns = self.white_images_dict['w_pawn']

            for i in range(8):
                    screen.blit(second_row_pawns, (board_left_top_x + square_length * i + 2, board_left_top_y + square_length* 6 -3))    
                    screen.blit(seventh_row_pawns, (board_left_top_x + square_length * i + 2, board_left_top_y + square_length))       


class RandomSquare:
    def __init__(self, board_side):
            self.board_side = board_side
            self.square=''
            self.square_top_left_x = 0
            self.square_top_left_y = 0
            self.init_random_square()
            self.init_top_left_coord()

    def  init_random_square(self):
        columns = ['a','b','c','d','e','f','g','h']
        rows = ['1','2','3','4','5','6','7','8']
        random_col = random.choice(columns)
        random_row = random.choice(rows)
        square = random_col+random_row
        self.square = square

    def init_top_left_coord(self):
            self.square_top_left_x, self.square_top_left_y = squares_coord(self.board_side)[self.square]

    def get_square(self):
            return self.square
    
    def get_square_coord(self):
            return (self.square_top_left_x, self.square_top_left_y)
    
    def click_within_square(self,click_x, click_y,square_length = config.square_length):
            if self.square_top_left_x <= click_x <= self.square_top_left_x  + square_length and  self.square_top_left_y <= click_y <= self.square_top_left_y + square_length:
                print("click within square: True")
                return True
            else:
                print("click within square: False")
                return False
            
    def draw_coord(self, screen, board_left_top_x = config.board_left_top_x, board_left_top_y= config.board_left_top_y, board_length= config.board_length):
                text_surface = config.big_font.render(self.square, True, 'lavenderblush')
                text_rect = text_surface.get_rect(center=(board_left_top_x + 0.5 * board_length, board_left_top_y + 0.5 * board_length))
                screen.blit(text_surface, text_rect) 

    def draw_frame_around_square(self, screen, square_length=config.square_length, color='navy', border_thickness=4):
                frame_rect = pygame.Rect(self.square_top_left_x, self.square_top_left_y , square_length , square_length)          
                pygame.draw.rect(screen, color, frame_rect, border_thickness)

# top left coordinates of each square
def squares_coord(board_side, board_left_top_x = config.board_left_top_x, board_left_top_y = config.board_left_top_y, square_length = config.square_length):
        
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


class FindSquareResponse:
    def __init__(self, was_correct_square_guessed, click_x, click_y):
          self.correct_square_answered = was_correct_square_guessed
          self.click_x = click_x
          self.click_y= click_y

    def draw_frame_around_square(self, screen, board_side, square_length = config.square_length, board_left_top_x =config.board_left_top_x,
board_left_top_y = config.board_left_top_y, border_thickness=4):
                square_name,square_coord = finding_square(board_side, self.click_x, self.click_y)
                if self.correct_square_answered is False:                        
                    color = 'darkred'
                    print("Wrong! You clicked on ",square_name)
                else:
                     color="green"     
                frame_rect = pygame.Rect(square_coord[0] , square_coord[1] , square_length , square_length)          
                pygame.draw.rect(screen, color, frame_rect, border_thickness) 

    def get_correct_square_answered(self):
                  return self.correct_square_answered

    
# this function is used when player clicks on a wrong square    
def finding_square(board_side, click_x, click_y, square_length = config.square_length):            
            for key,value in squares_coord(board_side).items():
                    if value[0]<= click_x < value[0] + square_length and value[1] <= click_y < value[1] + square_length:
                            return (key,value)

         
# Other classes who use the draw method, namely the score and input box classes, will inherit from this class.
class Drawable:
    def draw(self, screen, value_to_draw, background_color, frame_thickness, top_left_x, top_left_y,width, 
             height, text_color, border_thickness, border_color):
                # First overwrite what was written previously by filling the area with the background color
                inner_rect = pygame.Rect(top_left_x , top_left_y, width, height)
                screen.fill(background_color, inner_rect)
                frame_rect = pygame.Rect(top_left_x - frame_thickness, top_left_y - frame_thickness, width + 2*frame_thickness, height + 2* frame_thickness)          
                pygame.draw.rect(screen, border_color, frame_rect, border_thickness)
                score_text =  config.font.render(value_to_draw, True, text_color)
                text_rect = score_text.get_rect(center=(top_left_x + width / 2, top_left_y + height / 2))
                screen.blit(score_text, text_rect)  

# Note: all buttons/score/timer/response have a frame of thickness of 1 pixel around them.

class Score(Drawable):
        def __init__(self, which_game):
            self.score =0
            self.which_game= which_game
            self.frame_thickness = 1
            self.top_left_x = 30
            self.init_drawing_details()

        def init_drawing_details(self):
            if self.which_game == "find_square":
                self.background_color='darkgreen'
                self.top_left_y= config.find_square_score_top_left_y
                self.width= 340
                self.height= 120
                self.text_color = 'black'
                self.border_thickness= 1
                self.border_color = "yellow"  # "darkolivegreen"  

            elif self.which_game == "name_square":
                self.background_color = 'navy'
                self.top_left_y= config.name_square_response_top_left_y+ 120+16
                self.width= 340/2.0
                self.height= 120
                self.text_color = 'black'     
                self.border_thickness= 2
                self.border_color = "purple"

        def get_score(self):
              return self.score
        
        def update_score(self):
              self.score += 1

        def draw(self, screen):
            value_to_draw = f"Score: {self.score}"
            super().draw(screen, value_to_draw, self.background_color, self.frame_thickness, self.top_left_x,
                         self.top_left_y, self.width, self.height, self.text_color, self.border_thickness, self.border_color)

      

class GameState:
        def __init__(self):
            self.find_or_name_square = True # Find square
            self.board_side_chosen = True # white
            self.click_find_square = False # this click is expected from the player after random coordinates are shown. 
            self.something_typed = False # this is to check if the player wrote an answer or not
            self.allowed_to_read_input=False # this is to allow reading a KEYDOWN input
            self.find_square_time_running = False
            self.name_square_time_running=False
            self.after_game_msg = False
        '''
            self.find_square_button_clicked = True
            self.name_square_button_clicked = False
            self.white_side_button_clicked=True
            self.random_side_button_clicked = False
            self.black_side_button_clicked= False

        def get_find_square_button_clicked(self):
              return self.find_square_button_clicked
        def set_find_square_button_clicked(self, new_value):
              self.find_square_button_clicked = new_value

        def get_name_square_button_clicked(self):
              return self.name_square_button_clicked
        def set_name_square_button_clicked(self, new_val):
              self.name_square_button_clicked= new_val

        def get_white_side_button_clicked(self):
              return self.white_side_button_clicked
        def set_white_side_button_clicked(self, new_value):
              self.white_side_button_clicked= new_value

'''

        def get_find_square_time_running(self):
              return self.find_square_time_running
        
        def start_timer_find_square(self):
              self.find_square_time_running = True    

        def stop_timer_find_square(self):
              self.find_square_time_running = False       

        def get_name_square_time_running(self):
              return self.name_square_time_running
        
        def start_timer_name_square(self):
              self.name_square_time_running=True

        def stop_timer_name_square(self):
              self.name_square_time_running = False     

              
        def set_click_find_square(self, new_value):
              self.click_find_square = new_value

        def get_click_find_square(self) -> bool:
              return self.click_find_square            
        
        def set_allowed_to_read_input(self, new_value):
              self.allowed_to_read_input= new_value

        def get_allowed_to_read_input(self):
              return self.allowed_to_read_input    

        def get_something_typed(self):
              return self.something_typed

        def set_something_typed(self, bool_value):
              self.something_typed = bool_value   

        def set_after_game_msg(self, bool_value):
              self.after_game_msg = bool_value      

class NameSquareResponse(Drawable):
        def __init__(self, correct_square="", input_answer=""):
            self.correct_square = correct_square
            self.input_answer = input_answer 
            self.is_correct_answer_given = False
            self.init_drawing_details()

        def fun_is_correct_answer_given(self):
               self.is_correct_answer_given = self.correct_square == self.input_answer

        def init_drawing_details(self):
                self.background_color='navy'
                self.frame_thickness = 1
                self.top_left_x = 30
                self.top_left_y= config.name_square_response_top_left_y
                self.width= 340
                self.height= 120
                self.text_color = 'black'
                self.border_thickness = 2
                self.border_color= "purple"

        def set_input(self, some_value):
              self.input_answer = some_value

        def get_input(self) -> str:
              return self.input_answer

        def get_is_correct_answer_given(self) -> bool:
              return self.is_correct_answer_given
        
        def set_correct_square(self, new_square):
              self.correct_square = new_square

        def reset_input_internal(self): # by internal I mean that this method is used only by other methods within the class only. It is never called in the main code.
              self.input_answer = ""

        def reset_input(self):
              if len(self.input_answer)==2:
                    self.reset_input_internal()

        def draw_response_box(self, screen):
            super().draw(screen, self.input_answer, self.background_color, self.frame_thickness, self.top_left_x,
                         self.top_left_y, self.width, self.height, self.text_color,self.border_thickness,
                        self.border_color)

        def force_answer_correct_format_and_evaluate(self):
                columns =  ["a","b","c","d","e","f", "g", "h"]
                rows = ["1","2","3","4","5","6","7","8"]
                #print(f"before evaluating input is {self.input_answer}")
                if len(self.input_answer) == 1:
                    if self.input_answer[0] not in columns:
                          self.reset_input_internal()
                elif len(self.input_answer) == 2:
                      if self.input_answer[1].isalpha() or self.input_answer[1] not in rows:
                            self.input_answer = self.input_answer[0]
                      elif self.input_answer[1] in rows: # if answer is in correct form check if it correct
                                self.fun_is_correct_answer_given()
                #print(f"after evaluating input is {self.input_answer}")

        def reset_correct_answer_given(self, new_value):
              self.is_correct_answer_given = new_value


class Timer(Drawable):
      def __init__(self, which_game):
            self.which_game = which_game
            self.frame_thickness = 1
            self.init_drawing_details()

      def init_drawing_details(self):
            if self.which_game == "find_square":
                self.background_color=  "darkgreen" #"olive"
                self.top_left_x = 30
                self.top_left_y = config.find_square_score_top_left_y + 120+16
                self.width= 340
                self.height= 120
                self.text_color = 'black'
                self.border_thickness= 1
                self.border_color = "yellow" #"darkolivegreen"

            elif self.which_game == "name_square":
                self.background_color= 'navy'
                self.top_left_x = 30 + 340/2.0
                self.top_left_y= config.name_square_response_top_left_y + 120+16
                self.width= 340/2.0
                self.height= 120
                self.text_color = 'black'   
                self.border_thickness= 2
                self.border_color = "purple"

      def draw_time(self, screen):
            to_draw = f"{self.time:.1f}"
            super().draw(screen, to_draw, self.background_color, self.frame_thickness, self.top_left_x,
                         self.top_left_y, self.width, self.height, self.text_color, self.border_thickness, self.border_color)
      def set_time(self, time):
            self.time = time            

class AfterGameMsg(Drawable):
        def __init__(self, score):
            self.score = score            
            self.init_drawing_details()

        def init_drawing_details(self): 
                self.background_color=  "wheat"
                self.top_left_x = 30
                self.top_left_y= config.highest_button_top_left_y + 3*(60+16)
                self.width= 340
                self.height= 120
                self.frame_thickness = 1
                self.text_color = 'black'
                self.border_thickness= 1
                self.border_color = "wheat"

        def draw_msg(self,screen):
                to_draw=f"Time is up! Your score is {self.score}"
                super().draw(screen, to_draw, self.background_color, self.frame_thickness, self.top_left_x,
                         self.top_left_y, self.width, self.height, self.text_color, self.border_thickness, self.border_color)
                

class TimeBar:
        def __init__(self, which_game, time_left):
            self.bar_top_left_x = config.board_left_top_x
            self.bar_top_left_y =  config.board_left_top_y + config.board_length + 16
            self.original_bar_width = config.board_length
            self.bar_height = 16  
            self.which_game = which_game
            self.time_left = time_left
            self.init_bar_color()

        def init_bar_color(self):
              if self.which_game == "find_square":
                    self.color = "darkgreen"
                    self.border_color = "yellow"
              elif self.which_game == "name_square":
                    self.color = "navy"
                    self.border_color = "purple"      

        def draw(self, screen, time_left):
            time_left = max(0, time_left)
            self.dynamic_bar_width = int(((config.time_limit-time_left) / config.time_limit) * self.original_bar_width)
            pygame.draw.rect(screen, self.color, (self.bar_top_left_x, self.bar_top_left_y, self.dynamic_bar_width , self.bar_height))
            pygame.draw.rect(screen, self.border_color, (self.bar_top_left_x, self.bar_top_left_y, self.original_bar_width, self.bar_height), 2)


