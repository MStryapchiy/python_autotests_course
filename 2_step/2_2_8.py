from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import os
link = "http://suninjuly.github.io/file_input.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    file_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'file.txt')

    browser.find_element(By.NAME, "firstname").send_keys("Foma")
    browser.find_element(By.NAME, "lastname").send_keys("Kinev")
    browser.find_element(By.NAME, "email").send_keys("FK@fk.com")
    browser.find_element(By.ID, "file").send_keys(file_path)
    browser.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()

finally:
    time.sleep(5)
    browser.quit()