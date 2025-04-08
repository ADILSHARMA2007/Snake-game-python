import pygame
import sys

# Constants
WIDTH, HEIGHT = 300, 300
LINE_WIDTH = 10
BOARD_ROWS, BOARD_COLS = 3, 3
SQUARE_SIZE = WIDTH // BOARD_COLS
CIRCLE_RADIUS = SQUARE_SIZE // 3
CIRCLE_WIDTH = 15
CROSS_WIDTH = 25
SPACE = SQUARE_SIZE // 4

# Colors
BACKGROUND_COLOR = (28, 170, 156)
LINE_COLOR = (23, 145, 135)
CIRCLE_COLOR = (239, 231, 200)
CROSS_COLOR = (66, 66, 66)

# Initialize Pygame
pygame.init()

# Create the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tic Tac Toe")
screen.fill(BACKGROUND_COLOR)

# Game Variables
board = [[None]*BOARD_COLS for _ in range(BOARD_ROWS)]
player = "X"

def draw_lines():
    # Horizontal lines
    pygame.draw.line(screen, LINE_COLOR, (0, SQUARE_SIZE), (WIDTH, SQUARE_SIZE), LINE_WIDTH)
    pygame.draw.line(screen, LINE_COLOR, (0, SQUARE_SIZE * 2), (WIDTH, SQUARE_SIZE * 2), LINE_WIDTH)
    # Vertical lines
    pygame.draw.line(screen, LINE_COLOR, (SQUARE_SIZE, 0), (SQUARE_SIZE, HEIGHT), LINE_WIDTH)
    pygame.draw.line(screen, LINE_COLOR, (SQUARE_SIZE * 2, 0), (SQUARE_SIZE * 2, HEIGHT), LINE_WIDTH)

def draw_figures():
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            if board[row][col] == "X":
                pygame.draw.line(screen, CROSS_COLOR, (col * SQUARE_SIZE + SPACE, row * SQUARE_SIZE + SQUARE_SIZE - SPACE),
                                 (col * SQUARE_SIZE + SQUARE_SIZE - SPACE, row * SQUARE_SIZE + SPACE), CROSS_WIDTH)
                pygame.draw.line(screen, CROSS_COLOR, (col * SQUARE_SIZE + SPACE, row * SQUARE_SIZE + SPACE),
                                 (col * SQUARE_SIZE + SQUARE_SIZE - SPACE, row * SQUARE_SIZE + SQUARE_SIZE - SPACE), CROSS_WIDTH)
            elif board[row][col] == "O":
                pygame.draw.circle(screen, CIRCLE_COLOR, (col * SQUARE_SIZE + SQUARE_SIZE // 2, row * SQUARE_SIZE + SQUARE_SIZE // 2), CIRCLE_RADIUS, CIRCLE_WIDTH)

def mark_square(row, col):
    global player
    board[row][col] = player
    player = "O" if player == "X" else "X"

def check_win():
    # Check horizontal, vertical and diagonal wins
    for row in range(BOARD_ROWS):
        if board[row][0] == board[row][1] == board[row][2] != None:
            return board[row][0]
    
    for col in range(BOARD_COLS):
        if board[0][col] == board[1][col] == board[2][col] != None:
            return board[0][col]
    
    if board[0][0] == board[1][1] == board[2][2] != None:
        return board[0][0]
    
    if board[0][2] == board[1][1] == board[2][0] != None:
        return board[0][2]

    return None

def reset_game():
    global board, player
    board = [[None]*BOARD_COLS for _ in range(BOARD_ROWS)]
    player = "X"
    screen.fill(BACKGROUND_COLOR)
    draw_lines()

# Main game loop
draw_lines()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            mouseX = event.pos[0]
            mouseY = event.pos[1]

            clicked_row = mouseY // SQUARE_SIZE
            clicked_col = mouseX // SQUARE_SIZE

            if board[clicked_row][clicked_col] is None:
                mark_square(clicked_row, clicked_col)
                draw_figures()

                winner = check_win()
                if winner:
                    print(f"Player {winner} wins!")
                    reset_game()

    pygame.display.update()
