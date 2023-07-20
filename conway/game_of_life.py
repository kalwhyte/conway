#!/usr/bin/python3
import pygame
import random
import time
import os

# Initialize Pygame
pygame.init()

# Set the dimensions of the game window
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 600

# Set the dimensions of the game grid
CELLS_X = 50
CELLS_Y = 50
CELL_WIDTH = WINDOW_WIDTH // CELLS_X
CELL_HEIGHT = WINDOW_HEIGHT // CELLS_Y

# Set the colors for the game
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREY = (128, 128, 128)

# Set the font for the button text
FONT = pygame.font.Font(None, 30)

# Set the game window caption
pygame.display.set_caption("Conway's Game of Life")

# Create the game window
game_window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

# Set the clock for the game
clock = pygame.time.Clock()

# Set the initial state of the game
running = False

# Create the game grid
grid = [[0 for x in range(CELLS_X)] for y in range(CELLS_Y)]

# Define the function to draw the game grid
def draw_grid(grid):
    """Draw the game grid on the screen."""
    for x in range(CELLS_X):
        for y in range(CELLS_Y):
            color = WHITE if grid[y][x] else BLACK
            rect = pygame.Rect(x * CELL_WIDTH, y * CELL_HEIGHT, CELL_WIDTH, CELL_HEIGHT)
            pygame.draw.rect(game_window, color, rect)

# Define the function to update the game grid
def update_grid(grid):
    """Update the game grid."""
    new_grid = [[0 for x in range(CELLS_X)] for y in range(CELLS_Y)]
    for x in range(CELLS_X):
        for y in range(CELLS_Y):
            live_neighbours = 0
            for dx in [-1, 0, 1]:
                for dy in [-1, 0, 1]:
                    if dx == 0 and dy == 0:
                        continue
                    elif x + dx < 0 or x + dx >= CELLS_X:
                        continue
                    elif y + dy < 0 or y + dy >= CELLS_Y:
                        continue
                    elif grid[y + dy][x + dx] == 1:
                        live_neighbours += 1
            if grid[y][x] == 1 and live_neighbours in [2, 3]:
                new_grid[y][x] = 1
            elif grid[y][x] == 1 and live_neighbours not in [2, 3]:
                new_grid[y][x] = 0
            elif grid[y][x] == 0 and live_neighbours == 3:
                new_grid[y][x] = 1
    grid[:] = new_grid[:]
    return new_grid

# Define the function to randomize the game grid
def randomize_grid():
    """Randomize the game grid."""
    for x in range(CELLS_X):
        for y in range(CELLS_Y):
            grid[y][x] = random.randint(0, 1)

# Define the function to reset the game grid
def reset_grid():
    """Reset the game grid."""
    global grid
    grid = [[0 for x in range(CELLS_X)] for y in range(CELLS_Y)]

# Randomize the initial grid
grid = [[0 for x in range(CELLS_X)] for y in range(CELLS_Y)]
randomize_grid()

# Set the initial draw state

