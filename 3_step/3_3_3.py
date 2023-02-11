from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest
import time

class test_for_lesson_3_2_13(unittest.TestCase):
    def test_reg1(self):
        link = "http://suninjuly.github.io/registration1.html"
        browser = webdriver.Chrome()
        browser.get(link)
        input1 = browser.find_element(By.CSS_SELECTOR, ".first_block>.first_class>.first")
        input1.send_keys("Foma")
        input1 = browser.find_element(By.CSS_SELECTOR, ".first_block>.second_class>.second")
        input1.send_keys("Kinev")
        input2 = browser.find_element(By.CSS_SELECTOR, ".first_block>.third_class>.third")
        input2.send_keys("IHSP@gmail.com")
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()
        time.sleep(1)
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        welcome_text = welcome_text_elt.text
        self.assertEqual(welcome_text,"Congratulations! You have successfully registered!" , "Reg1 test not passed")

    def test_reg2(self): 
        link = "http://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome()
        browser.get(link)
        input1 = browser.find_element(By.CSS_SELECTOR, ".first_block>.first_class>.first")
        input1.send_keys("Foma")
        input1 = browser.find_element(By.CSS_SELECTOR, ".first_block>.second_class>.second")
        input1.send_keys("Kinev")
        input2 = browser.find_element(By.CSS_SELECTOR, ".first_block>.third_class>.third")
        input2.send_keys("IHSP@gmail.com")
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()
        time.sleep(1)
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        welcome_text = welcome_text_elt.text
        self.assertEqual(welcome_text,"Congratulations! You have successfully registered!" , "Reg1 test not passed")   

if __name__ == "__main__":
    unittest.main()
