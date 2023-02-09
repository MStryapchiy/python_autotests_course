from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
link = "http://suninjuly.github.io/redirect_accept.html"

def calc(val):
    return math.log(abs(12*math.sin(int(val))))

try:
    browser = webdriver.Chrome()
    browser.get(link)
    browser.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)
    x = calc(int(browser.find_element(By.ID,'input_value').text))
    browser.find_element(By.ID,'answer').send_keys(x)
    browser.find_element(By.CSS_SELECTOR,'button[type="submit"]').click()

finally:
    time.sleep(5)
    browser.quit() 