import unittest
import time

from selenium import webdriver
from selenium.webdriver import ActionChains



class UsingUnittest(unittest.TestCase):
    def setUp(self):
       self.driver = webdriver.Chrome(executable_path=r"E:\Selenium\chromedriver.exe")
    
    def test_Action(self):
        driver = self.driver
        driver.get("http://www.circuloin.com")
        obj = driver.find_element_by_link_text("Contactanos")
        time.sleep(3)
        #Encontrar elemento por texto , y el hover lo mueve 
        hover = ActionChains(driver).move_to_element(obj)
        hover.perform()
        
    def tearDown(self):
        self.driver.close()
    
if __name__ == '__main__':
    unittest.main()

        
#Esto sirve para validar que los links tengan el mismo nombre en la pagina y los carguen