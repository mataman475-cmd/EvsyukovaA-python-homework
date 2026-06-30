from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

try:
    driver.get('https://bonigarcia.dev/selenium-webdriver-java/loading-images.html')

    # Ждем, пока загрузится хотя бы 4 картинки
    WebDriverWait(driver, 10).until(
        lambda d: len(d.find_elements(By.TAG_NAME, 'img')) >= 4
    )

    # Находим все картинки
    all_images = driver.find_elements(By.TAG_NAME, 'img')

    # Берем третью (счет с 0)
    third_image = all_images[3]

    # Ждем, пока она загрузится
    WebDriverWait(driver, 10).until(
        lambda d: third_image.size[
            'width'] > 0 or third_image.size['height'] > 0
    )

    # Выводим результат
    print(third_image.get_attribute('src'))

finally:
    driver.quit()
