import pyautogui
import time
import random

# Координаты кнопки "Купить" (замени их на реальные координаты)
button_buy_x = 1590
button_buy_y = 701

# Координаты кнопки "+" (замени их на реальные координаты)
button_plus_x = 1641
button_plus_y = 737

# Функция для автоклика
def auto_clicker():
    while True:
        # Нажимаем на кнопку "+" 5 раз
        for _ in range(30):
            pyautogui.click(button_plus_x, button_plus_y)
            time.sleep(0.1)  # Небольшая задержка между кликами

        # Нажимаем на кнопку "Купить"
        pyautogui.click(button_buy_x, button_buy_y)
        
        # Ждем от 10 до 11 секунд
        time.sleep(50 + random.random() * 1)

# Запускаем автокликер
try:
    print("Автокликер запущен. Нажми Ctrl+C, чтобы остановить.")
    auto_clicker()
except KeyboardInterrupt:
    print("Автокликер остановлен.")