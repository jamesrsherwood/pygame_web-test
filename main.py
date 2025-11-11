import pygame
import sys
import asyncio
from timer import Timer

# Initialize Pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Colors
WHITE = (255, 255, 255)

# Set up the display
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Image Alternator")

# Load images
image_a = pygame.image.load('assets/a.png').convert_alpha()
image_b = pygame.image.load('assets/b.png').convert_alpha()

# Scale images to fit the screen (optional)
image_a = pygame.transform.scale(image_a, (SCREEN_WIDTH, SCREEN_HEIGHT))
image_b = pygame.transform.scale(image_b, (SCREEN_WIDTH, SCREEN_HEIGHT))

# Set up timer for 2 seconds (2000 milliseconds)
swap_timer = Timer(2000)

# Track which image is currently displayed
current_image_is_a = True

# Game clock
clock = pygame.time.Clock()

# Main game loop
async def main():
    global current_image_is_a

    while True:
        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Check if it's time to swap images
        if swap_timer.is_ready():
            current_image_is_a = not current_image_is_a
            swap_timer.reset()

        # Clear screen
        screen.fill(WHITE)

        # Draw the current image
        if current_image_is_a:
            screen.blit(image_a, (0, 0))
        else:
            screen.blit(image_b, (0, 0))

        # Update the display
        pygame.display.flip()

        # Cap the frame rate at 60 FPS
        clock.tick(60)

        # CRITICAL: Yield control to browser
        await asyncio.sleep(0)

# Run the async main loop
asyncio.run(main())
