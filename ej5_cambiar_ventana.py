import time
import unittest

from selenium import  webdriver
from selenium.webdriver.common.keys import Keys


class Using_unittest(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=r"E:\Selenium\chromedriver.exe")
        
    def test_cambiar_ventana(self):
        driver = self.driver
        driver.get("https://www.google.com")
        time.sleep(4)
        driver.execute_script("window.open('');")
        time.sleep(3)
        driver.switch_to_window(driver.window_handles[1])
        driver.get("https://facebook.com")
        time.sleep(3)
        user = driver.find_element_by_id("email")
        user.send_keys("direccion")
        user.send_keys(Keys.ENTER)
        time.sleep(3) 
        password = driver.find_element_by_id("pass")
        password.send_keys("*****")
        password.send_keys(Keys.ENTER)
         
        def tearDown(self):
            self.driver.close()
      

        
if __name__ == '__main__':
    unittest.main()