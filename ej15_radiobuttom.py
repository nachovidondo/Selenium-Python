import unittest
import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class UsingUnittest(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=r"E:\Selenium\chromedriver.exe")
        
    def test_radiobuttom(self):
        driver = self.driver
        driver.get("https://www.w3schools.com/howto/howto_css_custom_checkbox.asp")
        radiobutom_two = driver.find_element_by_xpath('//*[@id="main"]/div[3]/div[1]/input[4]')
        time.sleep(2)
        radiobutom_two.click()
        time.sleep(2)
        radiobutom_one = driver.find_element_by_xpath('//*[@id="main"]/div[3]/div[1]/input[3]')
        time.sleep(2)
        radiobutom_one.click()
        time.sleep(2)
    
    def tearDown(self):
        self.driver.close()
    
if __name__ == '__main__':
    unittest.main()