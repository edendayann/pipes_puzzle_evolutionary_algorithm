import pygame
import random

# Initialize Pygame
pygame.init()

# Constants
TILE_SIZE = 100
board_sizes = {
    4: (4, 4),
    5: (5, 5),
    7: (7, 7),
    10: (10, 10),
}
board_size = 4  # Default board size
ROWS, COLS = board_sizes[board_size]

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Initialize the screen
WIDTH = COLS * TILE_SIZE
HEIGHT = ROWS * TILE_SIZE
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Puzzle Pipes")


# Load and scale images
def load_and_scale_image(image_path, size):
    image = pygame.image.load(image_path)
    return pygame.transform.scale(image, size)


pipe_images = {
    "i": load_and_scale_image("assets/i_pipe_icon.png", (TILE_SIZE*0.8, TILE_SIZE*0.8)),
    "l": load_and_scale_image("assets/lower_l_pipe_icon.png", (TILE_SIZE, TILE_SIZE*0.9)),
    "T": load_and_scale_image("assets/T_pipe_icon.png", (TILE_SIZE*0.8, TILE_SIZE)),
    "L": load_and_scale_image("assets/upper_L_pipe_icon.png", (TILE_SIZE*0.85, TILE_SIZE*0.85)),
}

base_offsets = {
    "i": (0, 0),
    "l": (0, 0),
    "T": (25, 0),
    "L": (0, 0)
}


def get_rotated_offset(base_offset, angle):
    x, y = base_offset
    if angle == 90:
        return -y, x
    elif angle == 180:
        return -x, -y
    elif angle == 270:
        return y, -x
    return x, y


# Function to rotate images
def rotate_image(image, angle):
    return pygame.transform.rotate(image, angle)


# Create a board with random pipes and rotation angles
def create_board():
    return [[(random.choice(list(pipe_images.keys())), random.randint(0, 3) * 90) for _ in range(COLS)] for _ in
            range(ROWS)]


# board = create_board()
# print(board)
#board = [[('T', 0), ('L', 270), ('T', 270), ('T', 180)], [('l', 0), ('l', 0), ('l', 0), ('L', 0)],
         #[('i', 270), ('i', 270), ('L', 180), ('l', 0)], [('l', 0), ('l', 0), ('l', 0), ('L', 0)]]
board = [[('T', 0), ('L', 0), ('T', 0), ('T', 0)], [('l', 0), ('l', 0), ('l', 0), ('L', 0)],
         [('i', 0), ('i', 0), ('L', 0), ('l', 0)], [('l', 0), ('l', 0), ('l', 0), ('L', 0)]]


# Function to update board size
def update_board_size(size):
    global TILE_SIZE, ROWS, COLS, WIDTH, HEIGHT, board
    if 4 <= size <= 5:
        TILE_SIZE = 100
    else:
        TILE_SIZE = 50
    ROWS, COLS = board_sizes[size]
    WIDTH = COLS * TILE_SIZE
    HEIGHT = ROWS * TILE_SIZE
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    board = create_board()


# Function to draw grid lines on the board
def draw_grid():
    for x in range(0, WIDTH, TILE_SIZE):
        pygame.draw.line(screen, BLACK, (x, 0), (x, HEIGHT))
    for y in range(0, HEIGHT, TILE_SIZE):
        pygame.draw.line(screen, BLACK, (0, y), (WIDTH, y))


# Main loop
running = True
while running:
    screen.fill(WHITE)
    draw_grid()
    # Draw the board
    for row in range(ROWS):
        for col in range(COLS):
            pipe_type, rotation_angle = board[row][col]
            pipe_image = pipe_images[pipe_type]
            rotated_image = rotate_image(pipe_image, rotation_angle)

            # Calculate the new offset based on rotation
            base_offset = base_offsets[pipe_type]
            rotated_offset = get_rotated_offset(base_offset, rotation_angle)

            # Apply the offset to position the pipe
            offset_x, offset_y = rotated_offset
            position = (col * TILE_SIZE + offset_x, row * TILE_SIZE + offset_y)

            screen.blit(rotated_image, position)

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                board = create_board()  # Reset the board when spacebar is pressed
            elif event.key == pygame.K_4:
                update_board_size(4)  # Change board size to 4x4
            elif event.key == pygame.K_5:
                update_board_size(5)  # Change board size to 5x5
            elif event.key == pygame.K_7:
                update_board_size(7)  # Change board size to 7x7
            elif event.key == pygame.K_1:
                update_board_size(10)  # Change board size to 10x10

    pygame.display.flip()

pygame.quit()
