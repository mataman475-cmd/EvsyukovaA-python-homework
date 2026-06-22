from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def test_navigation():
    driver = webdriver.Chrome()

    # 1. Открываем главную
    driver.get('https://httpbin.org/')
    time.sleep(2)  # загрузка страници
    print('✅ Главная страница:', driver.title)

    # 2. Переходим по ссылке
    link = driver.find_element(By.LINK_TEXT, 'HTML form')
    link.click()
    print('✅ Форма открыта.')

    # 3. Проверка URL
    assert driver.current_url.endswith('/forms/post')
    print('✅ URL формы подтвержден.', driver.current_url)

    # 4. Возвращаемся назад
    driver.back()
    print('✅ Вернулись назад.')

    # 5. Проверка возврата
    assert driver.current_url == "https://httpbin.org/"
    print('✅ Тест пройден!')

    driver.quit()

# Запускаем тест
if __name__ == '__main__':
    test_navigation()