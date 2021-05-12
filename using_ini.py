import unittest
import time
import configparser

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class UsingUnittes(unittest.TestCase):
    def setUp(self):
       configuration = configparser.ConfigParser()
       configuration.read('configuration.ini')
       configuration.sections()
       get_explorer = configuration['General']['chrome']
       self.page = configuration['Paginas']['page']
       self.driver = webdriver.Chrome(executable_path=get_explorer)
    
    def test_using_implicitly_wait(self):
        driver = self.driver
        driver.implicitly_wait(5)
        driver.get(self.page)
        my_dinamic_element = driver.find_element_by_name("q")
        driver.close()
        
              
              

if __name__ == '__main__':
    unittest.main()


