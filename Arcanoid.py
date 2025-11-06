import pygame
import sys

# Инициализация Pygame
pygame.init()

# Параметры окна
screen_width, screen_height = 600, 400
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Арканоид")

# Параметры кирпичей
brick_rows = 5
brick_cols = 10
brick_width = screen_width // brick_cols
brick_height = 20
brick_gap = 5  # Промежуток между кирпичами

# Список кирпичей
bricks = [(col * (brick_width + brick_gap), row * (brick_height + brick_gap))
          for row in range(brick_rows) for col in range(brick_cols)]

# Цвета
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)

# ФПС
clock = pygame.time.Clock()
fps = 60

# Параметры платформы
paddle_width, paddle_height = 100, 10
paddle_x = (screen_width - paddle_width) // 2
paddle_y = screen_height - paddle_height - 20
paddle_speed = 6

# Параметры мяча
ball_radius = 8
ball_x = screen_width // 2
ball_y = paddle_y - ball_radius
ball_speed_x = 4
ball_speed_y = -4

# Жизни
lives = 3
font = pygame.font.SysFont(None, 48)
game_over = False
game_won = False

# Основной цикл игры
running = True
while running:
    # Обработка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if not game_over and not game_won:
        # Управление платформой
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and paddle_x > 0:
            paddle_x -= paddle_speed
        if keys[pygame.K_RIGHT] and paddle_x < screen_width - paddle_width:
            paddle_x += paddle_speed

        # Движение мяча
        ball_x += ball_speed_x
        ball_y += ball_speed_y

        # Столкновение с боковыми стенками
        if ball_x <= ball_radius or ball_x >= screen_width - ball_radius:
            ball_speed_x = -ball_speed_x

        # Столкновение с верхней стенкой
        if ball_y <= ball_radius:
            ball_speed_y = -ball_speed_y

        # Пропуск мяча — потеря жизни
        if ball_y >= screen_height:
            lives -= 1
            if lives <= 0:
                game_over = True
            else:
                # Сброс мяча
                ball_x = screen_width // 2
                ball_y = paddle_y - ball_radius
                ball_speed_y = -4  # вверх
                # Можно также сбросить скорость по X, но оставим как есть

        # Столкновение с кирпичами
        brick_rects = [pygame.Rect(brick[0], brick[1], brick_width, brick_height) for brick in bricks]
        for i, brick_rect in enumerate(brick_rects):
            if brick_rect.collidepoint(ball_x, ball_y):
                bricks.pop(i)
                ball_speed_y = -ball_speed_y
                break  # удаляем только один кирпич за кадр

        # Проверка победы
        if len(bricks) == 0:
            game_won = True

        # Столкновение с платформой
        if (paddle_x <= ball_x <= paddle_x + paddle_width and
            paddle_y <= ball_y + ball_radius <= paddle_y + paddle_height and
            ball_speed_y > 0):  # только при движении вниз
            ball_speed_y = -ball_speed_y
            # Дополнительно: можно менять направление по X в зависимости от места удара

    # Отрисовка
    screen.fill(BLACK)

    # Кирпичи
    for brick in bricks:
        pygame.draw.rect(screen, WHITE, pygame.Rect(brick[0], brick[1], brick_width, brick_height))

    # Платформа и мяч
    pygame.draw.rect(screen, WHITE, (paddle_x, paddle_y, paddle_width, paddle_height))
    pygame.draw.circle(screen, BLUE, (int(ball_x), int(ball_y)), ball_radius)

    # Жизни
    lives_text = font.render(f"Жизни: {lives}", True, WHITE)
    screen.blit(lives_text, (10, 10))

    # Сообщения об окончании
    if game_over:
        text = font.render("Вы проиграли", True, RED)
        screen.blit(text, (screen_width // 2 - text.get_width() // 2, screen_height // 2 - text.get_height() // 2))
    elif game_won:
        text = font.render("Вы выиграли!", True, WHITE)
        screen.blit(text, (screen_width // 2 - text.get_width() // 2, screen_height // 2 - text.get_height() // 2))

    pygame.display.flip()
    clock.tick(fps)

pygame.quit()
sys.exit()