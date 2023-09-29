import pygame
import random

# Инициализация пайгейм
pygame.init()

# Константы для игры
WIDTH, HEIGHT = 400, 400
SNAKE_SIZE = 20
SPEED = 15

# Цвета
WHITE = (255, 255, 255)
GREEN = (9, 255, 0)
RED = (255, 0, 0)

# Создание окна
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Змейка")

# Инициализация змейки
snake = [(100, 50), (90, 50), (80, 50)]
snake_direction = "RIGHT"

# Фрукт

fruit = (
    random.randrange(1, (WIDTH // SNAKE_SIZE)) * SNAKE_SIZE, random.randrange(1, (HEIGHT // SNAKE_SIZE)) * SNAKE_SIZE)


def draw_fruit(fruit):
    pygame.draw.rect(screen, RED, (fruit[0], fruit[1], SNAKE_SIZE, SNAKE_SIZE))


# LOOP MAIN

game_over = False
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT and snake_direction != "RIGHT":
                snake_direction = "LEFT"
            if event.key == pygame.K_RIGHT and snake_direction != "LEFT":
                snake_direction = "RIGHT"
            if event.key == pygame.K_UP and snake_direction != "DOWN":
                snake_direction = "UP"
            if event.key == pygame.K_DOWN and snake_direction != "UP":
                snake_direction = "DOWN"

#Движение
if snake_direction == "UP":
    new_head = (snake[0][0], snake[0][1] - SNAKE_SIZE)
if snake_direction == "DOWN":
    new_head = (snake[0][0], snake[0][1] + SNAKE_SIZE)
if snake_direction == "LEFT":
    new_head = (snake[0][0] - SNAKE_SIZE, snake[0][1])
if snake_direction == "RIGHT":
    new_head = (snake[0][0] + SNAKE_SIZE, snake[0][1])

snake.insert(0, new_head)






























