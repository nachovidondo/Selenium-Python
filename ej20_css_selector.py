import unittest
import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

#Cargar un elemento a traves de un selector de css

class UsingUnitest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=r"E:\Selenium\chromedriver.exe")
    
    def test_css_selector(self):
        driver = self.driver
        driver.get("http://www.circuloin.com/")
        time.sleep(2)
        css = driver.find_element_by_css_selector(".fh5co-property figure .tag")
        css.click()
        time.sleep(4)
        
    def tearDown(self):
        self.driver.close()
    
        
if __name__ == '__main__':
    unittest.main()


