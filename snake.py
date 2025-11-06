import pygame
import sys
import random

# Инициализация Pygame
pygame.init()

# Параметры окна
WIDTH, HEIGHT = 640, 480
CELL_SIZE = 20
GRID_WIDTH = WIDTH // CELL_SIZE
GRID_HEIGHT = HEIGHT // CELL_SIZE

# Цвета
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
WHITE = (255, 255, 255)

# Настройки игры
FPS = 5  # Скорость змейки (можно увеличить для усложнения)

# Создание окна
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Змейка")
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 36)

# Начальное положение змейки (голова в центре)
snake = [(GRID_WIDTH // 2, GRID_HEIGHT // 2)]
direction = (1, 0)  # Начальное движение — вправо
next_direction = direction

# Генерация еды
def generate_food():
    while True:
        food = (random.randint(0, GRID_WIDTH - 1), random.randint(0, GRID_HEIGHT - 1))
        if food not in snake:
            return food

food = generate_food()
score = 0

# Основной игровой цикл
running = True
game_over = False

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN and not game_over:
            if event.key == pygame.K_UP and direction != (0, 1):
                next_direction = (0, -1)
            elif event.key == pygame.K_DOWN and direction != (0, -1):
                next_direction = (0, 1)
            elif event.key == pygame.K_LEFT and direction != (1, 0):
                next_direction = (-1, 0)
            elif event.key == pygame.K_RIGHT and direction != (-1, 0):
                next_direction = (1, 0)

    if not game_over:
        # Обновляем направление
        direction = next_direction

        # Двигаем змейку
        head_x, head_y = snake[0]
        dx, dy = direction
        new_head = (head_x + dx, head_y + dy)

        # Проверка столкновения со стеной
        if (new_head[0] < 0 or new_head[0] >= GRID_WIDTH or
            new_head[1] < 0 or new_head[1] >= GRID_HEIGHT):
            game_over = True

        # Проверка столкновения с собой
        if new_head in snake:
            game_over = True

        if not game_over:
            snake.insert(0, new_head)

            # Проверка поедания еды
            if new_head == food:
                score += 1
                food = generate_food()
            else:
                snake.pop()  # Убираем хвост, если еда не съедена

    # Отрисовка
    screen.fill(BLACK)

    # Еда
    food_rect = pygame.Rect(food[0] * CELL_SIZE, food[1] * CELL_SIZE, CELL_SIZE, CELL_SIZE)
    pygame.draw.rect(screen, RED, food_rect)

    # Змейка
    for segment in snake:
        rect = pygame.Rect(segment[0] * CELL_SIZE, segment[1] * CELL_SIZE, CELL_SIZE, CELL_SIZE)
        pygame.draw.rect(screen, GREEN, rect)

    # Счёт
    score_text = font.render(f"Счёт: {score}", True, WHITE)
    screen.blit(score_text, (10, 10))

    # Сообщение о конце игры
    if game_over:
        game_over_text = font.render("Игра окончена! Нажмите крестик, чтобы выйти.", True, WHITE)
        screen.blit(game_over_text, (WIDTH // 2 - game_over_text.get_width() // 2,
                                     HEIGHT // 2 - game_over_text.get_height() // 2))

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
sys.exit()