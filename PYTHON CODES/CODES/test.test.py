import pygame
import sys
import random

# Constants
WIDTH, HEIGHT = 800, 600
BLOCK_SIZE = 20
FPS = 60

# Colors
LIGHT_GREEN = (170, 215, 81)
DARK_GREEN = (162, 209, 73)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
WHITE = (255, 255, 255)

UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)

class SnakeGame:
    def __init__(self):
        pygame.init()
        self.display = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption('Snake Game')
        self.clock = pygame.time.Clock()
        self.running = True
        self.reset()

    def reset(self):

        self.direction = RIGHT
        start_x = WIDTH // 2
        start_y = HEIGHT // 2
        self.snake = [
            (start_x, start_y),
            (start_x - BLOCK_SIZE, start_y),
            (start_x - 2 * BLOCK_SIZE, start_y)
        ]
        self.apple = self.get_random_apple()
        self.score = 0
        self.speed = 10

    def get_random_apple(self):
        while True:
            apple = (
                random.randint(0, (WIDTH - BLOCK_SIZE) // BLOCK_SIZE) * BLOCK_SIZE,
                random.randint(0, (HEIGHT - BLOCK_SIZE) // BLOCK_SIZE) * BLOCK_SIZE
            )
            if apple not in self.snake:  
                return apple

    def play(self):
        while self.running:
            self.handle_events()
            self.move_snake()
            self.check_collision()
            self.display_game()
            self.clock.tick(self.speed)

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self.handle_key_press(event.key)

    def handle_key_press(self, key):
        if key == pygame.K_UP and self.direction != DOWN:
            self.direction = UP
        elif key == pygame.K_DOWN and self.direction != UP:
            self.direction = DOWN
        elif key == pygame.K_LEFT and self.direction != RIGHT:
            self.direction = LEFT
        elif key == pygame.K_RIGHT and self.direction != LEFT:
            self.direction = RIGHT

    def move_snake(self):
        head = self.snake[0]
        new_head = (head[0] + self.direction[0] * BLOCK_SIZE,
                    head[1] + self.direction[1] * BLOCK_SIZE)

      
        self.snake.insert(0, new_head)

        if self.snake[0] == self.apple:
            self.score += 1
            self.apple = self.get_random_apple()
        else:
           
            self.snake.pop()

    def check_collision(self):
        head = self.snake[0]

        if (head[0] < 0 or head[0] >= WIDTH or
            head[1] < 0 or head[1] >= HEIGHT or
            head in self.snake[1:]):
            self.game_over()

    def display_game(self):
        self.display.fill(LIGHT_GREEN)
        self.draw_background()
        for pos in self.snake:
            pygame.draw.rect(self.display, RED, pygame.Rect(pos[0], pos[1], BLOCK_SIZE, BLOCK_SIZE))
        pygame.draw.rect(self.display, GREEN, pygame.Rect(self.apple[0], self.apple[1], BLOCK_SIZE, BLOCK_SIZE))
        font = pygame.font.Font(None, 36)
        text = font.render(f'Score: {self.score}', True, WHITE)
        self.display.blit(text, (10, 10))
        pygame.display.flip()

    def draw_background(self):

        for row in range(HEIGHT // BLOCK_SIZE):
            for col in range(WIDTH // BLOCK_SIZE):
                color = LIGHT_GREEN if (row + col) % 2 == 0 else DARK_GREEN
                pygame.draw.rect(self.display, color, pygame.Rect(col * BLOCK_SIZE, row * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))

    def game_over(self):
        self.display.fill(LIGHT_GREEN)
        self.draw_background()
        font = pygame.font.Font(None, 72)
        text = font.render('Game Over', True, WHITE)
        self.display.blit(text, (WIDTH // 2 - 150, HEIGHT // 2 - 36))
        font = pygame.font.Font(None, 36)
        text = font.render(f'Final Score: {self.score}', True, WHITE)
        self.display.blit(text, (WIDTH // 2 - 100, HEIGHT // 2 + 50))
        pygame.display.flip()
        pygame.time.wait(2000)
        self.reset()  

if __name__ == '__main__':
    game = SnakeGame()
    game.play()
