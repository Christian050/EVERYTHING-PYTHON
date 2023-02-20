import pygame
import random

WIDTH = 600
HEIGHT = 600
BLOCK_SIZE = 20

class Snake:
    def __init__(self):
        self.x = WIDTH // 2
        self.y = HEIGHT // 2
        self.body = [(self.x, self.y)]
        self.dx = 0
        self.dy = 0

    def move(self):
        self.x += self.dx
        self.y += self.dy
        self.body.insert(0, (self.x, self.y))
        self.body.pop()

    def grow(self):
        self.body.append((self.x, self.y))

    def change_direction(self, dx, dy):
        self.dx = dx
        self.dy = dy

class Food:
    def __init__(self):
        self.x = random.randint(0, WIDTH // BLOCK_SIZE - 1) * BLOCK_SIZE
        self.y = random.randint(0, HEIGHT // BLOCK_SIZE - 1) * BLOCK_SIZE

    def move(self):
        self.x = random.randint(0, WIDTH // BLOCK_SIZE - 1) * BLOCK_SIZE
        self.y = random.randint(0, HEIGHT // BLOCK_SIZE - 1) * BLOCK_SIZE

def check_collision(snake, food):
    if snake.x == food.x and snake.y == food.y:
        snake.grow()
        food.move()

def check_game_over(snake):
    if (snake.x < 0 or snake.x >= WIDTH or
        snake.y < 0 or snake.y >= HEIGHT or
        (snake.x, snake.y) in snake.body[1:]):
        return True
    return False

def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()
    snake = Snake()
    food = Food()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    snake.change_direction(-BLOCK_SIZE, 0)
                elif event.key == pygame.K_RIGHT:
                    snake.change_direction(BLOCK_SIZE, 0)
                elif event.key == pygame.K_UP:
                    snake.change_direction(0, -BLOCK_SIZE)
                elif event.key == pygame.K_DOWN:
                    snake.change_direction(0, BLOCK_SIZE)

        check_collision(snake, food)
        if check_game_over(snake):
            pygame.quit()
            return

        snake.move()

        screen.fill((0, 0, 0))
        for x, y in snake.body:
            pygame