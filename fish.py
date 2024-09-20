# import pyautogui
# import time

# time.sleep(3)  # Дает вам 5 секунд на наведение курсора на нужную область

# print(pyautogui.position())  # Выводит координаты текущей позиции курсора


import pyautogui
from PIL import ImageGrab
import time
import keyboard  # Библиотека для отслеживания нажатия клавиш

# Координаты кнопок на экране
left_button_coords = (72, 796, 269, 1002)  # Замените на координаты области, где находится левая кнопка
right_button_coords = (1640, 796, 1844, 1003)  # Замените на координаты области, где находится правая кнопка

# Порог для определения изменения яркости (разница в яркости)
brightness_threshold = 50

def calculate_brightness(coords):
    screenshot = ImageGrab.grab(bbox=coords)
    pixels = screenshot.load()
    
    total_brightness = 0
    for x in range(screenshot.size[0]):
        for y in range(screenshot.size[1]):
            r, g, b = pixels[x, y]
            total_brightness += (r + g + b) / 3
    
    avg_brightness = total_brightness / (screenshot.size[0] * screenshot.size[1])
    return avg_brightness

# Измеряем начальную яркость (когда кнопки не активны)
initial_left_brightness = calculate_brightness(left_button_coords)
initial_right_brightness = calculate_brightness(right_button_coords)

while True:
    # Проверяем, была ли нажата клавиша пробела для завершения программы
    if keyboard.is_pressed('space'):
        print("Программа завершена по нажатию пробела.")
        break
    
    # Проверяем текущую яркость областей кнопок
    current_left_brightness = calculate_brightness(left_button_coords)
    current_right_brightness = calculate_brightness(right_button_coords)
    
    # Если яркость изменяется на заданное количество единиц, кликаем по соответствующей кнопке
    if current_left_brightness - initial_left_brightness > brightness_threshold:
        pyautogui.click(button='left')
    elif current_right_brightness - initial_right_brightness > brightness_threshold:
        pyautogui.click(button='right')
    
    time.sleep(0.5)  # Задержка между проверками