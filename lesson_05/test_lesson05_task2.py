from selenium import webdriver
from selenium.webdriver.common.by import By
import time  # Для sleep
from selenium.webdriver.support.ui import WebDriverWait  # Для будущих ожиданий


def test_form_submission():
    driver = webdriver.Chrome()

    # 1. Открыть страницу
    driver.get("https://httpbin.org/forms/post")
    time.sleep(2)  # Пауза для наглядности

    # 2. Найти поле и вводим имя
    field_custname = driver.find_element(By.NAME, "custname")
    field_custname.send_keys("Ann")

    # 3. Найти кнопку и нажать
    submit_button = driver.find_element(By.XPATH, '//button[.="Submit order"]')
    submit_button.click()

    # 4. Проверка, что URL изменился
    assert driver.current_url == "https://httpbin.org/post"
    "Ошибка: URL не изменился"
    print("✅ Тест пройден!")

    # 5. Закрываем браузер
    driver.quit()


# Запуск теста
if __name__ == "__main__":
    test_form_submission()
