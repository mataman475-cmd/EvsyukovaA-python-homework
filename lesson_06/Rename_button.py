from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

try:
    driver.get('http://uitestingplayground.com/textinput')

    # Вводим текст
    input_field = driver.find_element(By.ID, 'newButtonName')
    input_field.clear()
    input_field.send_keys('SkyPro')

    # Кликаем по кнопке
    button = driver.find_element(By.ID, 'updatingButton')
    button.click()

    # Ждем, пока текст изменится
    WebDriverWait(driver, 10).until(
        EC.text_to_be_present_in_element((By.ID, 'updatingButton'), 'SkyPro'))

    # Получаем текст
    final_text = driver.find_element(By.ID, 'updatingButton').text
    print(final_text)

finally:
    driver.quit()
