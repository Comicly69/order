import os
import pygame

# Initialize pygame
pygame.init()

# Set screen size and title
screen = pygame.display.set_mode((400, 300))
pygame.display.set_caption("Menu")

# Load the icon
icon = pygame.image.load(os.path.join("icons", "icon.png"))

# Set the window icon
pygame.display.set_icon(icon)

# Set font and font size
font = pygame.font.Font(None, 30)

# Define menu items and their prices
menu_items = {"burger": 7.99, "drink": 2.99, "fries": 3.99}

# Loop to keep menu open until user closes it
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Render menu items
    screen.fill((255, 255, 255))
    x, y = 50, 50
    for item in menu_items:
        text = font.render(item + " - $" + str(menu_items[item]), True, (0, 0, 0))
        screen.blit(text, (x, y))
        y += 50
        
    # Update screen
    pygame.display.update()

# Quit pygame
pygame.quit()
