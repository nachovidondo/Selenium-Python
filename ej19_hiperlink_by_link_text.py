import unittest
import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class UsingUnittes(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=r"E:\Selenium\chromedriver.exe")
    
    def test_hiperlink(self):
        driver = self.driver
        driver.get("https://www.w3schools.com/")
        time.sleep(2)
        find_link = driver.find_element_by_link_text("Learn HTML")
        find_link.click()
        time.sleep(2)
        
    def tearDown(self):
        self.driver.close()
        
        
if __name__ == '__main__':
    unittest.main()

