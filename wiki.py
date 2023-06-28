import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class WikipediaTestCase(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome()
        self.addCleanup(self.browser.quit)

    def test_HomePageTitle(self):
        self.browser.get('https://www.wikipedia.org/')
        self.assertIn('Wikipedia', self.browser.title)

    def test_WikipediaSearch(self):
        self.browser.get('https://www.wikipedia.org/')
        search_box = WebDriverWait(self.browser, 10).until(EC.presence_of_element_located((By.NAME, 'search')))
        search_box.send_keys('Python (programming language)' + Keys.RETURN)

        result_titles = WebDriverWait(self.browser, 10).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'span.mw-page-title-main')))
        self.assertNotEqual([], [title.text for title in result_titles])



if __name__ == '__main__':
    unittest.main(verbosity=2)
