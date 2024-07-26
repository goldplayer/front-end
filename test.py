from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

# Путь к вашему веб-драйверу
driver_path = 'C:\\Users\\kosty\\Downloads\\chrome-win64\\chrome-win64.exe'

service = Service(executable_path=driver_path)

driver = webdriver.Chrome(service=service)

try:
    # Открыть сайт
    driver.get('http://127.0.0.1:5500/index.html')

    # Дать время сайту загрузиться
    time.sleep(2)

    # Найти секцию на сайте
    section = driver.find_element(By.TAG_NAME, 'section')

    # Проверить, что секция существует
    assert section is not None
    print("Тест пройден: секция найдена")

except Exception as e:
    print(f"Тест не пройден: {e}")

finally:
    # Закрыть браузер
    driver.quit()
