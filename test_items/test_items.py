from selenium.webdriver.common.by import By
import time

link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'

class TestItems():
    def test_items(self, browser):
        browser.get(link)
        browser.implicitly_wait(5)
        assert browser.find_element(By.CSS_SELECTOR, ".btn-add-to-basket")
        time.sleep(30)