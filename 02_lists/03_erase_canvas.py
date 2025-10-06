import pygame

# Canvas and cell settings
CELL_SIZE = 20
GRID_WIDTH = 20
GRID_HEIGHT = 15
CANVAS_WIDTH = CELL_SIZE * GRID_WIDTH
CANVAS_HEIGHT = CELL_SIZE * GRID_HEIGHT
ERASER_SIZE = 30  # Eraser is a square
FPS = 60

# Colors
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)


def setup():
    """Initialize Pygame and set up the display."""
    global screen, clock
    pygame.init()  # Initialize Pygame here
    screen = pygame.display.set_mode((CANVAS_WIDTH, CANVAS_HEIGHT))
    pygame.display.set_caption("Eraser Canvas")
    clock = pygame.time.Clock()
    screen.fill(WHITE)


def update_loop(grid, eraser_pos, is_dragging):
    """Handle events, update grid, and draw the canvas."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False, grid, eraser_pos, is_dragging
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Left mouse button
                is_dragging = True
        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                is_dragging = False
        elif event.type == pygame.MOUSEMOTION and is_dragging:
            eraser_pos = list(event.pos)

    # Clear screen
    screen.fill(WHITE)

    # Draw grid
    for row in range(GRID_HEIGHT):
        for col in range(GRID_WIDTH):
            color = BLUE if grid[row][col] else WHITE
            pygame.draw.rect(screen, color,
                             (col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE))
            pygame.draw.rect(screen, BLACK,
                             (col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE), 1)

    # Update grid based on eraser position
    if is_dragging:
        eraser_rect = pygame.Rect(eraser_pos[0] - ERASER_SIZE // 2,
                                  eraser_pos[1] - ERASER_SIZE // 2,
                                  ERASER_SIZE, ERASER_SIZE)
        for row in range(GRID_HEIGHT):
            for col in range(GRID_WIDTH):
                cell_rect = pygame.Rect(col * CELL_SIZE, row * CELL_SIZE,
                                        CELL_SIZE, CELL_SIZE)
                if eraser_rect.colliderect(cell_rect):
                    grid[row][col] = False  # Erase to white

    # Draw eraser
    if is_dragging:
        pygame.draw.rect(screen, BLACK,
                         (eraser_pos[0] - ERASER_SIZE // 2,
                          eraser_pos[1] - ERASER_SIZE // 2,
                          ERASER_SIZE, ERASER_SIZE), 2)

    pygame.display.flip()
    clock.tick(FPS)
    return True, grid, eraser_pos, is_dragging


def main():
    """Main function to run the eraser canvas program."""
    # Initialize grid: True for blue, False for white
    grid = [[True for _ in range(GRID_WIDTH)] for _ in range(GRID_HEIGHT)]
    eraser_pos = [0, 0]
    is_dragging = False

    setup()
    running = True
    while running:
        running, grid, eraser_pos, is_dragging = update_loop(
            grid, eraser_pos, is_dragging)

    pygame.quit()


if __name__ == "__main__":
    main()
