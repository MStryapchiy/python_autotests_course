from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

link = "https://suninjuly.github.io/math.html"

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try: 
    browser = webdriver.Chrome()
    browser.get(link)
    x_el = browser.find_element(By.CSS_SELECTOR, "#input_value")
    x = x_el.text
    x = calc(x)
    input1= browser.find_element(By.ID, "answer" )
    input1.send_keys(x)
    chbox = browser.find_element(By.ID,"robotCheckbox")
    chbox.click()
    rdb = browser.find_element(By.ID, "robotsRule")
    rdb.click()
    btn = browser.find_element(By.CSS_SELECTOR,"button[type='submit']")
    btn.click()

finally:
    time.sleep(10)
    browser.quit()