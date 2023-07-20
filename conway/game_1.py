import pygame
import random
import sys

# Set the dimensions of the grid cell
CELL_SIZE = 10

# Set the dimensions of the grid
CELLS_X = 60
CELLS_Y = 40

# Set the dimensions of the button
BUTTON_WIDTH = 80
BUTTON_HEIGHT = 30
BUTTON_X = 20
BUTTON_Y = 20

# Set the colors for the grid
ALIVE_COLOR = (255, 255, 255)
DEAD_COLOR = (50, 50, 50)

# Initialize the pygame library
pygame.init()

# Set the dimensions of the screen
SCREEN_WIDTH = CELL_SIZE * CELLS_X
SCREEN_HEIGHT = CELL_SIZE * CELLS_Y + BUTTON_HEIGHT + BUTTON_Y * 2
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Set the font for the button text
font = pygame.font.SysFont(None, 24)

# Set the caption of the window
pygame.display.set_caption("Conway's Game of Life")

# Create a clock object to control the game's frame rate
clock = pygame.time.Clock()

# Initialize the game grid
grid = [[0 for x in range(CELLS_X)] for y in range(CELLS_Y)]

# Create a boolean to track whether the game is running or not
running = False


def draw_grid(grid):
    """Draw the game grid on the screen."""
    screen.fill(DEAD_COLOR)
    for x in range(CELLS_X):
        for y in range(CELLS_Y):
            if grid[y][x] == 1:
                pygame.draw.rect(screen, ALIVE_COLOR, (x*CELL_SIZE, y*CELL_SIZE, CELL_SIZE, CELL_SIZE))
    if not running:
        pygame.draw.rect(screen, ALIVE_COLOR, (BUTTON_X, BUTTON_Y, BUTTON_WIDTH, BUTTON_HEIGHT), 2)
        text = font.render("Start", True, ALIVE_COLOR)
        screen.blit(text, (BUTTON_X + 10, BUTTON_Y + 5))
    else:
        text = font.render("Running...", True, ALIVE_COLOR)
        screen.blit(text, (BUTTON_X + 10, BUTTON_Y + 5))


def update_grid(grid):
    """Update the game grid."""
    new_grid = [[0 for x in range(CELLS_X)] for y in range(CELLS_Y)]
    for x in range(CELLS_X):
        for y in range(CELLS_Y):
            live_neighbours = count_live_neighbours(grid, x, y)
            if grid[y][x] == 1 and (live_neighbours == 2 or live_neighbours == 3):
                new_grid[y][x] = 1
            elif grid[y][x] == 1 and live_neighbours < 2:
                new_grid[y][x] = 0
            elif grid[y][x] == 1 and live_neighbours > 3:
                new_grid[y][x] = 0
            elif grid[y][x] == 0 and live_neighbours == 3:
                new_grid[y][x] = 1
    grid[:] = new_grid[:]
    return new_grid


def randomize_grid():
    """Randomize the game grid."""
    for x in range(CELLS_X):
        for y in range(CELLS_Y):
            grid[y][x] = random.randint(0, 1)


def reset_grid():
    """Reset the game grid."""
    global grid
    grid = [[0 for x in range(CELLS_X)] for y in range(CELLS_Y)]
    draw_grid(grid)


# Run the game loop
while True:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if not running:
                mouse_pos = pygame.mouse.get_pos()
                if BUTTON_X < mouse_pos[0] < BUTTON_X + BUTTON_WIDTH and BUTTON_Y < mouse_pos[1] < BUTTON_Y + BUTTON_HEIGHT:
                    running = True
                    randomize_grid()
            else:
                running = False
                reset_grid()
                draw_grid(grid)

    # Update the game grid
    if running:
        grid = update_grid(grid)
        draw_grid(grid)

    # Update the display
    pygame.display.update()
    clock.tick(10)
