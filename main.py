# Ethan Lawrence 
# Feb 12 2025
# Pygame template ver 2

import pygame
import sys
import random

pygame.init()
pygame.mixer.init()
# Window dimentions
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600

# Window Caption
TITLE = 'Sounds'
MY_FONT = 'DejaVuSans.ttf'
FAVICON = 'favicon-starter-cropped.png'

# Sound
SOUND_EFFECTS = {
    'beep' : 'beep.ogg',
    'laser' : 'laser5.ogg',
    'zap' : 'zap13.ogg'
}
SOUNDS = {
    'beep' : pygame.mixer.Sound(SOUND_EFFECTS['beep']),
    'laser' : pygame.mixer.Sound(SOUND_EFFECTS['laser']),
    'zap' : pygame.mixer.Sound(SOUND_EFFECTS['zap'])
}
# Frame rate
FPS = 60

# Colors
WHITE = (255, 255, 255)
GREY = (100, 100, 100)
BLACK = (0, 0, 0)

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

YELLOW = (255, 255, 0)
PURPLE = (255, 0, 255)
CYAN = (0, 255, 255)

# Generic Functions
def init_game():

    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption(TITLE)
    return screen

def draw_text(screen, text, font, color, y):
    text = font.render(text, True, color)
    screen.blit(text, (90, y))
def main():
    screen = init_game()
    pygame.mixer.init()
    clock = pygame.time.Clock()
    running = True
    # On Startup
    text_font = pygame.font.Font(MY_FONT, 30)
    font_color = GREEN
    instructions = [
        'Press 1 to Play a beep sound.',
        'Press 2 to Play a laser sound.',
        'Press 3 to Play a zap sound.',
        'Press 4 to Change the text color.'
    ]
    base_y = 30
    line_height = 20
    backround_image = pygame.image.load("backroun.png").convert()
    favicon = pygame.image.load('favicon-starter-cropped.png')
    pygame.display.set_icon(favicon)
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            keys = pygame.key.get_pressed()
        screen.blit(backround_image, (0, 0))
        # While Running
        count = 0
        for i in instructions:
            count += 2
            draw_text(screen, i, text_font, font_color, base_y+count*line_height)
        if keys[pygame.K_1]:
            SOUNDS['beep'].play()
        if keys[pygame.K_2]:
            SOUNDS['laser'].play()
        if keys[pygame.K_3]:
            SOUNDS['zap'].play()
        if keys[pygame.K_4]:
            font_color = (random.randint(0,255), random.randint(0,255), random.randint(0,255))
        # Limit clock to FPS & Update Screen
        pygame.display.flip()
        clock.tick(FPS)
    pygame.quit()
    sys.exit()

# Other Functions

# Startup
if __name__ == '__main__':
    main()
