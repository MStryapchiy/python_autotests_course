def test_substring(full_string, substring):
    if substring not in full_string:
        print (f"expected '{substring}' to be substring of '{full_string}'")

from selenium import webdriver

# инициализируем драйвер браузера. После этой команды вы должны увидеть новое открытое окно браузера
driver = webdriver.Firefox()

driver.get("https://stepik.org/lesson/25969/step/8")