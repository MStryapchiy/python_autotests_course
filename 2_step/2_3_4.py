from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
link = "http://suninjuly.github.io/alert_accept.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    browser.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
    browser.switch_to.alert.accept()

    x_ln = browser.find_element(By.ID, "input_value")
    x = int(x_ln.text)
    x = str(math.log(abs(12*math.sin(int(x)))))
    browser.find_element(By.ID, "answer").send_keys(x)
    browser.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()

finally:
    time.sleep(5)
    browser.quit() 