import time
import unittest

from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class Using_unittest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=r"E:\Selenium\chromedriver.exe")
    
    def test_buscar_por_xpath(self):
        driver = self.driver
        driver.get("https://www.google.com")
        time.sleep(4)
        buscar_por_xpath = driver.find_element_by_xpath("/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input")
        time.sleep(3)
        buscar_por_xpath.send_keys("selenium", Keys.ARROW_DOWN)
        time.sleep(4)
    
    def tearDown(self):
        self.driver.close()
        
        

        
        
if __name__ == '__main__':
    unittest.main()
# Xpath es una estructura de objetos.
#Existen 2 tipos : Xpath relativo y el Xpath absoluto.
# Relativo : Tiene una ventaja parte de un nodo especifico , es el mas usado.
