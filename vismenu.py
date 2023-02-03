import pygame
import sys
import os

# Initialize pygame
pygame.init()

# Load the menu file
image = pygame.image.load("menu2.png")

# Create the window
infoObject = pygame.display.Info()
window = pygame.display.set_mode((400, 518), pygame.NOFRAME)

# Display the image in the window
window.blit(image, (0, 0))

# Update the display
pygame.display.update()

# Keep track of mouse position for window dragging
mouse_x, mouse_y = 0, 0
dragging = False

def handle_events():
    global mouse_x, mouse_y, dragging
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                mouse_x, mouse_y = event.pos
                dragging = True
        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                dragging = False
        elif event.type == pygame.MOUSEMOTION:
            if dragging:
                new_x, new_y = event.pos
                os.environ['SDL_VIDEO_WINDOW_POS'] = f"{new_x - mouse_x},{new_y - mouse_y}"
                pygame.display.set_mode(window.get_size(), pygame.NOFRAME)
                mouse_x, mouse_y = new_x, new_y

# Run the loop
running = True
while running:
    handle_events()
