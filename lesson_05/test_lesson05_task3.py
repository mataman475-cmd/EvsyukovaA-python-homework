from selenium import webdriver
from selenium.webdriver.common.by import By


def test_multiple_elements():
    driver = webdriver.Chrome()
    driver.get("https://httpbin.org/links/10")

    # 1. Находим все ссылки на странице (тег <a>)
    links = driver.find_elements(By.TAG_NAME, "a")

    # 2. Проверяем количество ссылок и выводим результат
    expected_count = 9
    actual_count = len(links)

    if actual_count == expected_count:
        print(f"Ожидалось {expected_count} ссылки, найдено {actual_count} ссылок. ТЕСТ ПРОЙДЕН.")
    else:
        print(f"Ожидалось {expected_count} ссылки, но найдено {actual_count} ссылок. ТЕСТ СОРВАН!")
        driver.quit()
        return

    # 3. Проверяем, что все ссылки отображаются на странице
    for link in links:
        assert link.is_displayed()

    # 4. Проверяем, что текст первой ссылки содержит "1"
    first_link_text = links[0].text
    assert "1" in first_link_text, f"Текст первой ссылки ('{first_link_text}') не содержит '1'"

    driver.quit()


# Запускаем тест
if __name__ == "__main__":
    test_multiple_elements()
