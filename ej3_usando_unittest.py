import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys



class Using_Unittest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=r"E:\Selenium\chromedriver.exe")
    
    def test_buscar(self):
        driver = self.driver
        driver.get("https://www.google.com")
        self.assertIn("Google", driver.title)
        element = driver.find_element_by_name("q")
        element.send_keys("selenium")
        element.send_keys(Keys.RETURN)
        time.sleep(5)
        assert "No se encontro el elemento .'google'" not in driver.page_source
    
    def tearDown(self):
        self.driver.close()
        
if __name__ == '__main__':
    unittest.main()