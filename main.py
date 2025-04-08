import pygame
from constants import *

def main():
    # Initialize pygame
    pygame.init()

    # Set up the game window
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # Game loop
    while True:
        # Handle events (like closing the window)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return  # Exit the loop and end the program

        # Fill the screen with black
        screen.fill((0, 0, 0))  # RGB for black

        # Update the display
        pygame.display.flip()

if __name__ == "__main__":
    main()
