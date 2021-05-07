import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys



class Usingunittest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=r"E:\Selenium\chromedriver.exe")
    
    def test_pagin_siguiente_anterior(self):
        driver = self.driver
        driver.get("http://www.gmail.com")
        time.sleep(4)
        driver.get("http://www.google.com")
        time.sleep(4)
        driver.get("http://www.youtube.com")
        time.sleep(4)
        driver.back()
        time.sleep(2)
        driver.back()
        time.sleep(2)
        driver.foward()
        time.sleep(3)
        

        
if __name__ == '__main__':
    unittest.main()
        
