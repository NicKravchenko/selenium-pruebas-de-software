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

    def test_PageTitle(self):
        self.browser.get('https://www.google.com/')
        self.assertIn('Google', self.browser.title)

    def test_GoogleSearch(self):
        self.browser.get('https://www.google.com/')
        search_box = WebDriverWait(self.browser, 10).until(EC.presence_of_element_located((By.NAME, 'q')))
        search_box.send_keys('Pruebas de software' + Keys.RETURN)

        WebDriverWait(self.browser, 10).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, 'div#search'), 'Pruebas de software'))

    def test_GoogleAbout(self):
        self.browser.get('https://www.google.com/intl/en/about/')

        WebDriverWait(self.browser, 10).until(EC.title_contains('About Google'))

        body_text = WebDriverWait(self.browser, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'body'))).text
        self.assertIn('Our mission is to organize the world’s information and make it universally accessible and useful.', body_text)



if __name__ == '__main__':
    unittest.main(verbosity=2)
