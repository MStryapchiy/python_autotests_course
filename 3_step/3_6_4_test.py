import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

class TestAuth():
    @pytest.mark.parametrize('link', ["https://stepik.org/lesson/236895/step/1","https://stepik.org/lesson/236896/step/1","https://stepik.org/lesson/236897/step/1","https://stepik.org/lesson/236898/step/1","https://stepik.org/lesson/236899/step/1","https://stepik.org/lesson/236903/step/1","https://stepik.org/lesson/236904/step/1","https://stepik.org/lesson/236905/step/1"])
    def test_login(self, browser, link):
        browser.get(link)
        time.sleep(3)
        browser.find_element(By.CSS_SELECTOR, '#ember33').click()
        browser.find_element(By.CSS_SELECTOR, 'input[name="login"]').send_keys('***Your login***')
        browser.find_element(By.CSS_SELECTOR, 'input[name="password"]').send_keys('***Your Password***')
        browser.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
        time.sleep(3)
        answer = math.log(int(time.time()))
        browser.find_element(By.CSS_SELECTOR,".ember-text-area.ember-view.textarea.string-quiz__textarea").send_keys(answer)
        time.sleep(1)
        browser.find_element(By.CSS_SELECTOR, ".submit-submission").click()
        browser.implicitly_wait(8)
        time.sleep(1)
        res = browser.find_element(By.CSS_SELECTOR, ".smart-hints__hint").text
        assert res == "Correct!"




