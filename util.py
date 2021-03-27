﻿import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

class PythonOrgSearch(unittest.TestCase):

    def setUp(self):
        #self.driver = webdriver.Firefox(executable_path="C:\tools\webdriver\gecko\geckodriver.exe")
        self.driver = webdriver.Firefox(GeckoDriverManager().install())

    def test_search_in_python_org(self):
        driver = self.driver
        driver.get("http://www.python.org")
        self.assertIn("Python", driver.title)
        elem = driver.find_element_by_name("q")
        elem.send_keys("pycon")
        elem.send_keys(Keys.RETURN)
        assert "No results found." not in driver.page_source


    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()