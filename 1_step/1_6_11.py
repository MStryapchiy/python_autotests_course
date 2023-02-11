from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try: 
    link = "http://suninjuly.github.io/registration2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element(By.CSS_SELECTOR, ".first_block>.first_class>.first")
    input1.send_keys("Foma")
    input1 = browser.find_element(By.CSS_SELECTOR, ".first_block>.second_class>.second")
    input1.send_keys("Kinev")
    input2 = browser.find_element(By.CSS_SELECTOR, ".first_block>.third_class>.third")
    input2.send_keys("IHSP@gmail.com")
    
    # input1 = browser.find_element(By.CSS_SELECTOR, "input[placeholder='Input your name']")
    # input1.send_keys("Foma")
    # input2 = browser.find_element(By.CSS_SELECTOR, "input[placeholder='Input your email']")
    # input2.send_keys("IHSP@gmail.com")
    # time.sleep(5)


    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    time.sleep(1)

    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    time.sleep(10)
    browser.quit()