import unittest
import time

from selenium import webdriver


class UsingUnittes(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=r"E:\Selenium\chromedriver.exe")
    
    def test_aler(self):
        driver = self.driver
        driver.get('file:///E:/Selenium/alert_simple.html')
        time.sleep(3)
        alert = driver.find_element_by_name('alert')
        alert.click()
        time.sleep(3)
        alert = driver.switch_to_alert()
        alert.dismiss() #Dismiss es un boton que viene por default en un alert
        time.sleep(3)
        
        
        
    
    def tearDown(self):
        self.driver.close()
    
    
    
if __name__ == '__main__':
    unittest.main()