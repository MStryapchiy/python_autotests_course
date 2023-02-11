from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import time
import math
from selenium.webdriver.support import expected_conditions as EC

url = "http://suninjuly.github.io/explicit_wait2.html"

def calc(val):
    return math.log(abs(12*math.sin(int(val))))

try:
    browser = webdriver.Chrome()
    browser.get(url)
    browser.implicitly_wait(12)

    if WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, "price"), "$100")):
        browser.find_element(By.ID,'book').click()

    x = calc(int(browser.find_element(By.ID,'input_value').text))
    browser.find_element(By.ID,'answer').send_keys(x)
    browser.find_element(By.CSS_SELECTOR,'button[type="submit"]').click()

finally:
    time.sleep(5)
    browser.quit() 