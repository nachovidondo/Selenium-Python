import unittest
import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

#Display elements sirve para ver si un elemento esta cargado continue sino lo espera

class UsingUnittest(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=r"E:\Selenium\chromedriver.exe")
        
    def test_display_elements(self):
        driver = self.driver
        driver.get("http://www.google.com")
        time.sleep(2)
        display_elements = driver.find_element_by_xpath('/html/body/div[1]/div[3]/form/div[1]/div[1]/div[3]/center/input[2]')
        time.sleep(2)
        print(display_elements.is_displayed()) #Regresa True o false si etsa cargado el elemento o no
        print(display_elements.is_enabled()) #Regresa un True o false si el elemento etsa disponible
        #La diferencia es que displayed es q lo muestra en pantalla , y enable es que este disponible para darle click.
        
    def tearDown(self):
        self.driver.close()
        

if __name__ == '__main__':
    unittest.main()











