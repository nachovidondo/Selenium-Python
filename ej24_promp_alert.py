import unittest
import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class UsingUnittes(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=r"E:\Selenium\chromedriver.exe")
    
    def test_promp_alert(self):
        driver = self.driver
        driver.get('file:///E:/Selenium/promp_alert.html')
        time.sleep(3)
        alert = driver.find_element_by_name("prompt-alert")
        alert.click()
        time.sleep(3)
        alert = driver.switch_to_alert()
        alert.dismiss()
        time.sleep(2)
    
    def tearDown(self):
        self.driver.close()
        
        
        
if __name__ == '__main__':
    unittest.main()