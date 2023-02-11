from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

link = "https://suninjuly.github.io/selects1.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    x1_sel = browser.find_element(By.ID, "num1")
    x2_sel = browser.find_element(By.ID, "num2")
    x = int(x1_sel.text) + int(x2_sel.text)
    print(x)
    browser.find_element(By.ID, "dropdown").click()

    select = Select(browser.find_element(By.CSS_SELECTOR, "select"))
    select.select_by_value(str(x))

    browser.find_element(By.CSS_SELECTOR, "button[type='Submit']").click()

finally:
    time.sleep(10)
    browser.quit()
