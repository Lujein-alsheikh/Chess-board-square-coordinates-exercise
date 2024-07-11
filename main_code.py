import pygame
import config
import random
from classes import (
    Board,
    Button,
    Pieces,
    RandomSquare,
    FindSquareResponse,
    Score,
    GameState,
    NameSquareResponse,
)
from classes import Timer, AfterGameMsg, TimeBar

pygame.init()
screen = pygame.display.set_mode([config.WIDTH, config.HEIGHT])
pygame.display.set_caption("Square Coordinates Exercise")


# some functions that use the buttons objects defined later
def draw_all_buttons(screen):
    find_square_button.draw(screen)
    name_square_button.draw(screen)
    white_board_button.draw(screen)
    random_board_button.draw(screen)
    black_board_button.draw(screen)
    start_button.draw(screen)

def click_on_find_or_name_square_buttons(click_pos):
    if find_square_button.button_clicked_fun(
        click_pos
    ) or name_square_button.button_clicked_fun(click_pos):
        return True
    else:
        return False

def click_on_one_of_the_board_side_buttons(click_pos):
    if (
        white_board_button.button_clicked_fun(click_pos)
        or black_board_button.button_clicked_fun(click_pos)
        or random_board_button.button_clicked_fun(click_pos)
    ):
        return True
    else:
        return False


# basic objects
board = Board()
pieces = Pieces()
find_square_button = Button(
    text="Find Square",
    color="firebrick",
    is_clicked=True,
    top_left_x=30,
    top_left_y=config.highest_button_top_left_y,
    width=170,
    height=60,
)
name_square_button = Button(
    text="Name Square",
    is_clicked=False,
    top_left_x=200,
    top_left_y=config.highest_button_top_left_y,
    width=170,
    height=60,
)
white_board_button = Button(
    text="white",
    color="firebrick",
    is_clicked=True,
    top_left_x=30,
    top_left_y=config.highest_button_top_left_y + 60 + 16,
    width =113.33,
    height=60,
)
random_board_button = Button(
    "random",
    is_clicked=False,
    top_left_x=143.33,
    top_left_y=config.highest_button_top_left_y + 60 + 16,
    width=113.33,
    height=60,
)
black_board_button = Button(
    "black",
    is_clicked=False,
    top_left_x=256.66,
    top_left_y=config.highest_button_top_left_y + 60 + 16,
    width=113.33,
    height=60,
)
start_button = Button(
    "START",
    color="firebrick",
    is_clicked=False,
    top_left_x=30,
    top_left_y=config.highest_button_top_left_y + 2 * (60 + 16),
    width=340,
    height=60,
)
clock = pygame.time.Clock()
game_state = GameState()

# game loop
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            click_x, click_y = pygame.mouse.get_pos()

            if start_button.button_clicked_fun(event.pos):
                '''if a game is already in play; don't allow for a new game to start. This is actually
                   not needed since once a game is in play, we don't even show the start button.   
                '''
                if (
                    start_button.get_clicked()
                ):  
                    pass
                else:
                    '''
                    In brief, when the start button is clicked on, we initialize the score, timer, time_bar, game_state,
                    and random_square. We also choose a random side for the board if needed.
                    '''
                    start_button.set_clicked()

                    time_left = config.time_limit
                    print("---------------------------------------------")
                    if board.get_random_side() == True:
                        board.set_board_side(random.choice(["white", "black"]))
                    random_square = RandomSquare(board.get_board_side())
                    print(f"Initial square: {random_square.get_square()}")

                    if find_square_button.get_clicked():
                        score = Score("find_square")
                        timer = Timer("find_square")
                        time_bar = TimeBar("find_square", config.time_limit)
                        game_state.start_timer_find_square()

                    elif name_square_button.get_clicked():
                        score = Score("name_square")
                        timer = Timer("name_square")
                        time_bar = TimeBar("name_square", config.time_limit)
                        game_state.start_timer_name_square()
                        name_square_response = NameSquareResponse(
                            correct_square=random_square.get_square()
                        )
                        game_state.set_allowed_to_read_input(True)
                    '''This line is needed in the case where a game is over and the final score message is shown. If the
                        player clicks on one of the start buttons, we want the old score message to disappear'''
                    game_state.set_after_game_msg(False)

            else:
                # if the start button has not been already clicked on
                if (
                    start_button.get_clicked() == False
                ): 
                    if click_on_find_or_name_square_buttons(event.pos):

                        if find_square_button.button_clicked_fun(event.pos):

                            find_square_button.set_clicked()
                            name_square_button.unclick()

                        else:
                            name_square_button.set_clicked()
                            find_square_button.unclick()
                        print(f"Board side: {board.get_board_side()}")
                        '''This line is needed in the case where a game is over and the final score message is shown. If the
                        player clicks on one of the find/name square buttons, we want the old score message to disappear'''
                        game_state.set_after_game_msg(False)

                    elif click_on_one_of_the_board_side_buttons(event.pos):
                        if white_board_button.button_clicked_fun(event.pos):
                            white_board_button.set_clicked()
                            black_board_button.unclick()
                            random_board_button.unclick()
                            board.set_board_side("white")
                            board.set_random_side(False)

                        elif random_board_button.button_clicked_fun(event.pos):
                            white_board_button.unclick()
                            random_board_button.set_clicked()
                            black_board_button.unclick()
                            # an initial random side is chosen here.
                            board.set_random_side(
                                True
                            )  

                        else:
                            white_board_button.unclick()
                            random_board_button.unclick()
                            black_board_button.set_clicked()
                            board.set_board_side("black")
                            board.set_random_side(False)

                        print(
                            f"find square clicked: {find_square_button.get_clicked()}, name square clicked {name_square_button.get_clicked()}"
                        )
                        '''This line is needed in the case where a game is over and the final score message is shown. If the
                        player clicks on one of the board side buttons, we want the old score message to disappear'''
                        game_state.set_after_game_msg(False)

                else:
                    if find_square_button.get_clicked():
                        if board.click_within_board(click_x, click_y):
                            if random_square.click_within_square(click_x, click_y):

                                find_square_response = FindSquareResponse(
                                    True, click_x, click_y
                                )
                                score.update_score()
                                print(f"score is {score.get_score()}")
                            else:
                                find_square_response = FindSquareResponse(
                                    False, click_x, click_y
                                )

                            game_state.set_click_find_square(True)

        elif event.type == pygame.KEYDOWN:
            if (
                name_square_button.get_clicked()
                and start_button.get_clicked()
                and game_state.get_allowed_to_read_input()
            ):
                # if input is the enter key
                if event.key == pygame.K_RETURN:
                    name_square_response.set_input("")
                elif event.key == pygame.K_BACKSPACE:
                    name_square_response.set_input(
                        name_square_response.get_input()[:-1]
                    )

                else:
                    # limit the input to 2 characters
                    if (
                        len(name_square_response.get_input()) < 2
                    ):  
                        name_square_response.set_input(
                            name_square_response.get_input() + event.unicode
                        )

                print(
                    f"input is {name_square_response.get_input()} of length {len(name_square_response.input_answer)}"
                )
                game_state.set_something_typed(True)

    screen.fill(config.background_color)
    board.draw(screen)
    if start_button.get_clicked() == True:
        pass
    else:
        draw_all_buttons(screen)
    pieces.draw(screen, board.get_board_side())
    # xor
    if (
        game_state.get_find_square_time_running()
        != game_state.get_name_square_time_running()
    ):  
        # this is the time passed since the last frame. It is 1/60 = 0.016 sec
        time_passed = (
            clock.get_time() / 1000
        )  
        # time_left is how much time is left for the player
        time_left -= time_passed
        score.draw(screen)
        timer.set_time(time_left)
        timer.draw_time(screen)
        time_bar.draw(screen, time_left)

        if game_state.get_find_square_time_running():
            # this is to keep drawing the coordinates on the screen until a click is made
            if game_state.get_click_find_square() is False:
                random_square.draw_coord(screen)
                pygame.display.update()
            # if a click is made    
            else:
                # if correct_square was guessed
                if (
                    find_square_response.get_correct_square_answered()  
                ):
                    # The following three instructions are to draw a green frame around a correctly guessed square
                    find_square_response.draw_frame_around_square(
                        screen, board.get_board_side()
                    )
                    pygame.display.flip()
                    # wait for 50 ms showing the green frame
                    pygame.time.wait(50)  

                    board.draw(screen)
                    if board.get_random_side():
                        board.set_board_side(random.choice(["white", "black"]))

                    pieces.draw(screen, board.get_board_side())
                    random_square = RandomSquare(board.get_board_side())
                    print(f"Random coord {random_square.get_square()}")
                    random_square.draw_coord(screen)
                    pygame.display.update()
                    game_state.set_click_find_square(False)

                # if player didn't click on the correct_square
                else:
                    find_square_response.draw_frame_around_square(
                        screen, board.get_board_side()
                    )
                    random_square.draw_coord(screen)
                    pygame.display.update()
        else:
            name_square_response.draw_response_box(screen)
            # this line forces the input to be a valid square
            name_square_response.force_answer_correct_format_and_evaluate()
            # this is to keep showing the blue frame until a valid input is entered
            if game_state.get_something_typed() is False:
                random_square.draw_frame_around_square(screen)
                pygame.display.update()
                
            else:
                if name_square_response.get_is_correct_answer_given():
                    score.update_score()
                    print(f"score is {score.get_score()}")
                    # prepare for a new square
                    name_square_response.reset_input()
                    name_square_response.reset_correct_answer_given(False)
                    board.draw(screen)

                    if board.get_random_side():
                        board.set_board_side(random.choice(["white", "black"]))

                    pieces.draw(screen, board.get_board_side())
                    random_square = RandomSquare(board.get_board_side())
                    print(f"Random square {random_square.get_square()}")
                    name_square_response.set_correct_square(random_square.get_square())
                    random_square.draw_frame_around_square(screen)
                    pygame.display.update()
                    game_state.set_something_typed(False)

                # We end up in this else statement if (1) the input is in a valid format, but wrong or (2) in case only
                # one valid character is typed because the correct_answer_given is still set to False (its default value)              
                else:
                    random_square.draw_frame_around_square(screen)
                    name_square_response.reset_input()
                    pygame.display.update()

        if time_left <= 0:
            game_state.stop_timer_find_square()
            game_state.stop_timer_name_square()
            start_button.unclick()
            game_state.set_click_find_square(False)
            game_state.set_something_typed(False)
            game_state.set_allowed_to_read_input(False)
            # prepare to keep the score shown using the after_game_msg
            after_game_msg = AfterGameMsg(score.get_score())
            game_state.set_after_game_msg(True)

    # if no timer is running and there is an after_game_msg (the score) to be shown, show it.
    # Note that this score will be shown until a new click is made on either find/name square or board colors buttons.
    else:
        if game_state.after_game_msg:
            after_game_msg.draw_msg(screen)

    pygame.display.flip()
    # the clock is used to update the screen each frame. FPS: frame per second.
    clock.tick(config.FPS)

pygame.quit()
