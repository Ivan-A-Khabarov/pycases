import pygame
import sys
import random

# Инициализация Pygame
pygame.init()

# Определение констант
SCREEN_WIDTH = 1600
SCREEN_HEIGHT = 900
GRID_SIZE = 20
SNAKE_SIZE = 20

# Определение цветов
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Определение направлений
UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)

# Класс для представления змеи
class Snake:
    def __init__(self):
        self.body = [(100, 100), (90, 100), (80, 100)]
        self.direction = RIGHT

    def move(self):
        head = self.body[0]
        new_head = (head[0] + self.direction[0] * SNAKE_SIZE, head[1] + self.direction[1] * SNAKE_SIZE)
        self.body.insert(0, new_head)
        self.body.pop()

    def change_direction(self, new_direction):
        if (new_direction[0] * -1, new_direction[1] * -1) != self.direction:
            self.direction = new_direction

    def grow(self):
        tail = self.body[-1]
        new_tail = (tail[0] - self.direction[0] * SNAKE_SIZE, tail[1] - self.direction[1] * SNAKE_SIZE)
        self.body.append(new_tail)

    def check_collision(self):
        head = self.body[0]
        return head in self.body[1:]

    def draw(self, surface):
        for segment in self.body:
            pygame.draw.rect(surface, WHITE, (segment[0], segment[1], SNAKE_SIZE, SNAKE_SIZE))

# Класс для представления еды
class Food:
    def __init__(self):
        self.position = (random.randint(0, (SCREEN_WIDTH - GRID_SIZE) // GRID_SIZE) * GRID_SIZE,
                         random.randint(0, (SCREEN_HEIGHT - GRID_SIZE) // GRID_SIZE) * GRID_SIZE)

    def draw(self, surface):
        pygame.draw.rect(surface, RED, (self.position[0], self.position[1], GRID_SIZE, GRID_SIZE))

# Инициализация окна
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Змейка")

# Инициализация змеи и еды
snake = Snake()
food = Food()

# Основной цикл игры
clock = pygame.time.Clock()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                snake.change_direction(UP)
            elif event.key == pygame.K_DOWN:
                snake.change_direction(DOWN)
            elif event.key == pygame.K_LEFT:
                snake.change_direction(LEFT)
            elif event.key == pygame.K_RIGHT:
                snake.change_direction(RIGHT)

    snake.move()

    # Проверка столкновения с границами экрана
    if not (0 <= snake.body[0][0] < SCREEN_WIDTH and 0 <= snake.body[0][1] < SCREEN_HEIGHT):
        pygame.quit()
        sys.exit()

    # Проверка столкновения с едой
    if snake.body[0] == food.position:
        snake.grow()
        food = Food()

    # Проверка столкновения с самой собой
    if snake.check_collision():
        pygame.quit()
        sys.exit()

    # Отрисовка фона
    screen.fill(BLACK)

    # Отрисовка змеи и еды
    snake.draw(screen)
    food.draw(screen)

    pygame.display.flip()
    clock.tick(10)  # Установка скорости обновления экрана (10 кадров в секунду)
