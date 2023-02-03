import pygame
import os

# Initialize pygame
pygame.init()

# Load the image file
image = pygame.image.load("Menu.png")

# Create the window with the desired size and remove the frame
infoObject = pygame.display.Info()
window = pygame.display.set_mode((400, 518), pygame.NOFRAME)

# Set the position of the window on the screen
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (1000, 1000)

# Display the image in the window
window.blit(image, (0, 0))

# Update the display
pygame.display.update()

# Run the game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


