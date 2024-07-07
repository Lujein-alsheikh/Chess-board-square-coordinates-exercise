import pygame
import sys

pygame.init()

width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Countdown Timer')
font = pygame.font.SysFont(None, 100)

# Set up the clock
clock = pygame.time.Clock()

start_time = 1.0 
time_left = start_time
frame_count = 0

running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    # time passed since the last frame. It is equal to 1/60 = 0.016
    time_passed = clock.get_time() / 1000  # convert milliseconds to seconds
    time_left -= time_passed

    frame_count += 1
    print(f'Frame: {frame_count}, Time passed: {time_passed:.3f} seconds, Time left: {time_left}, Time left rounded: {time_left:.1f} seconds')

    # Ensure the timer does not go below 0
    if time_left < 0:
        time_left = 0
        running = False

    screen.fill((0, 0, 0))  
    timer_text = font.render(f'{time_left:.1f}', True, (255, 255, 255))
    screen.blit(timer_text, (width//2 - timer_text.get_width()//2, height//2 - timer_text.get_height()//2))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
