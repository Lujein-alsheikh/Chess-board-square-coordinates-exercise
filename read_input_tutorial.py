import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up screen
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Enter a String")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
GRAY = (200, 200, 200)

font = pygame.font.Font(None, 36)

button_rect = pygame.Rect(100, 100, 250, 50)
button_color = BLUE
button_text = font.render("Click to Enter Text", True, WHITE)

# Variables for text input
input_active = False
input_text = ""
input_box_rect = pygame.Rect(100, 200, 600, 50)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if button_rect.collidepoint(event.pos):
                input_active = not input_active
        elif event.type == pygame.KEYDOWN and input_active:
            if event.key == pygame.K_RETURN:
                # Here you can add functionality to process the input, 
                # like printing it to the console or storing it.
                print(input_text)  # Example: print the input text to the console
                input_text = ""  # Clear the input text
            elif event.key == pygame.K_BACKSPACE:
                input_text = input_text[:-1]
            else:
                input_text += event.unicode

    screen.fill(WHITE)
    pygame.draw.rect(screen, button_color, button_rect)
    screen.blit(button_text, (button_rect.x + 10, button_rect.y + 10))
    
    if input_active:
        pygame.draw.rect(screen, GRAY, input_box_rect)
        text_surface = font.render(input_text, True, BLACK)
        screen.blit(text_surface, (input_box_rect.x + 5, input_box_rect.y + 5))
    
    pygame.display.flip()
