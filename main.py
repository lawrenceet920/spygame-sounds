# Ethan Lawrence 
# Feb 12 2025
# Pygame template ver 2

import pygame
import sys
import random
# Window dimentions
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600

# Window Caption
TITLE = 'Sounds'
MT_FONT = 'DejaVuSans.ttf'
FAVICON = 'favicon-starter-cropped.png'


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
    pygame.init()
    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption(TITLE)
    return screen
def handle_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                return False
    return True
def main():
    screen = init_game()
    pygame.mixer.init()
    clock = pygame.time.Clock()
    running = True
    # On Startup
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
    while running:
        running = handle_events()
        screen.fill(WHITE)
        # While Running


        # Limit clock to FPS & Update Screen
        pygame.display.flip()
        clock.tick(FPS)
    pygame.quit()
    sys.exit()

# Other Functions

# Startup
if __name__ == '__main__':
    main()