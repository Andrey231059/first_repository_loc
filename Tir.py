import pygame
import random
import time

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Игра Тир")

# Иконка (опционально — если файла нет, закомментируй)
try:
    icon = pygame.image.load("img/icon.jpg")
    pygame.display.set_icon(icon)
except:
    pass  # Игнорируем ошибку, если иконки нет

# Загрузка и масштабирование цели
try:
    target_img = pygame.image.load("img/target.jpg")
except:
    # Если изображения нет, создаём простую цветную цель
    target_img = pygame.Surface((80, 80))
    pygame.draw.circle(target_img, (255, 0, 0), (40, 40), 40)

target_width = 80
target_height = 80
target_img = pygame.transform.scale(target_img, (target_width, target_height))

# Начальная позиция цели
target_x = random.randint(0, SCREEN_WIDTH - target_width)
target_y = random.randint(0, SCREEN_HEIGHT - target_height)

# Цвет фона
color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

# Игровые переменные
score = 0
start_time = time.time()
GAME_DURATION = 60  # секунд

# Шрифт для текста
font = pygame.font.SysFont(None, 36)

running = True
while running:
    current_time = time.time()
    elapsed = current_time - start_time
    remaining_time = max(0, GAME_DURATION - int(elapsed))

    # Обработка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN and remaining_time > 0:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if target_x < mouse_x < target_x + target_width and target_y < mouse_y < target_y + target_height:
                score += 1
                target_x = random.randint(0, SCREEN_WIDTH - target_width)
                target_y = random.randint(0, SCREEN_HEIGHT - target_height)
                # Можно менять фон при попадании (опционально)
                color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

    # Очистка экрана
    screen.fill(color)

    # Отрисовка цели (только если время ещё есть)
    if remaining_time > 0:
        screen.blit(target_img, (target_x, target_y))

    # Отображение счёта и времени
    score_text = font.render(f"Попаданий: {score}", True, (0, 0, 0))
    time_text = font.render(f"Время: {remaining_time} с", True, (0, 0, 0))
    screen.blit(score_text, (10, 10))
    screen.blit(time_text, (10, 50))

    # Если время вышло — финальное сообщение
    if remaining_time == 0:
        final_text = font.render(f"Игра окончена! Всего попаданий: {score}", True, (255, 255, 255))
        text_rect = final_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
        screen.blit(final_text, text_rect)
        pygame.display.update()
        pygame.time.wait(3000)  # Показать результат на 3 секунды
        running = False

    pygame.display.update()

# Вывод результата в консоль (на всякий случай)
print(f"Игра завершена. Всего попаданий за минуту: {score}")

pygame.quit()