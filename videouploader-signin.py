

import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class GoogleSearchTestCase(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome()
        self.addCleanup(self.browser.quit)

    def test_login(self):
        self.browser.get('https://video-uploader-frontend.netlify.app/')
        print(self.browser.title)

        username = self.browser.find_element(By.CSS_SELECTOR,'#username')
        password = self.browser.find_element(By.CSS_SELECTOR, '#password')

        button = self.browser.find_element(By.CSS_SELECTOR, '.css-41aesz')

        username.send_keys('onunez')
        password.send_keys('omarcito123' + Keys.RETURN)

        time.sleep(3)
        button.click()

        alert_text = WebDriverWait(self.browser, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.chakra-alert'))).text
        print(alert_text)
        time.sleep(3)

        self.assertIn('No active account found with the given credentials', alert_text)


if __name__ == '__main__':
    unittest.main(verbosity=2)
