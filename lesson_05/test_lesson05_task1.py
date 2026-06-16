from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


def test_navigation():
    driver = webdriver.Chrome()

    # 1. Открыть сайт
    driver.get("https://httpbin.org/")
    print("✅ Загружена главная страница:", driver.title)

    # 2. Ожидание появления ссылки и кликнуть
    wait = WebDriverWait(driver, timeout=10)
    link = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "HTML form")))
    link.click()

    # 3. Проверка перехода
    assert "/forms/post" in driver.current_url, "Ошибка: не перешли на форму."
    print("✅ Открыта форма:", driver.current_url)

    # 4. Возвращаемся назад
    driver.back()
    time.sleep(2)  # Чтобы увидеть результат

    # 5. Проверка возврата
    assert driver.current_url == "https://httpbin.org/"
    "Ошибка: не вернулись на главную."
    print("✅ Тест пройден!")

    driver.quit()


# Запуск теста
if __name__ == "__main__":
    test_navigation()
