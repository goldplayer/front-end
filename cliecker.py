import keyboard
import time
import logging

# Налаштування логування з використанням кодування UTF-8
logging.basicConfig(
    filename='movement_log.txt',
    level=logging.INFO,
    format='%(asctime)s - %(message)s',
    encoding='utf-8'  # Додаємо кодування UTF-8
)

# Функція для підрахунку пройдених метрів
def hold_w():
    meters = 0
    meter_per_second = 5  # Скільки метрів проходить персонаж за секунду
    start_time = time.time()

    logging.info('Програма запущена')

    while True:
        keyboard.press('w')  # Натискання клавіші 'W'
        time.sleep(0.1)  # Пауза між натисканнями

        # Оновлення пройдених метрів
        meters += meter_per_second * 0.1

        # Перевірка на натискання пробілу для завершення
        if keyboard.is_pressed('space'):
            keyboard.release('w')  # Відпустити 'W'
            break  # Завершити цикл

    # Логування завершення програми і результату
    end_time = time.time()
    elapsed_time = end_time - start_time
    logging.info(f'Програма зупинена. Пройдено {meters:.2f} метрів за {elapsed_time:.2f} секунд')

    print(f'Пройдено метрів: {meters:.2f}')

# Виклик функції
hold_w()
