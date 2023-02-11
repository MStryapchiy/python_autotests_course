from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

try:
    browser = webdriver.Chrome()
    link = "http://SunInJuly.github.io/execute_script.html"
    browser.get(link)

    x_ln = browser.find_element(By.ID, "input_value")
    x = x_ln.text
    x = str(math.log(abs(12*math.sin(int(x)))))
    inp_ln = browser.find_element(By.ID, "answer").send_keys(x)
    chbx = browser.find_element(By.ID, "robotCheckbox").click()
    rdbtn = browser.find_element(By.ID, "robotsRule")
    button = browser.find_element(By.CSS_SELECTOR, "button[type ='submit']")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    rdbtn.click()
    button.click()

finally:
    time.sleep(5)
    browser.quit()