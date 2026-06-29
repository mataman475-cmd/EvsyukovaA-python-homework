from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Открываем браузер
driver = webdriver.Chrome()

try:
    # Переходим на сайт
    driver.get('http://uitestingplayground.com/ajax')

    # Нажимаем на синюю кнопку
    button = driver.find_element(By.ID, 'ajaxButton')
    button.click()

    # Ждем появления зеленого текста (до 15 секунд)
    wait = WebDriverWait(driver, 20)
    success_label = wait.until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, '.bg-success')))

    # Получаем и выводим текст
    print(success_label.text)
finally:
    driver.quit()
