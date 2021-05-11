import time
import unittest

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC



class UsingUnittest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=r"E:\Selenium\chromedriver.exe")
        
    def test_using_explicit_wait(self):
        driver = self.driver
        driver.get("http://www.google.com")
        try:
            element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME,"q")))
        finally:
            driver.quit()
            
        
if __name__ == '__main__':
    unittest.main()
        
        
        
"""
Explicit wait:

Las esperas explícitas están disponibles para los clientes de lenguajes imperativos y
procedimentales de Selenium. Permiten que tu código detenga la ejecución del programa,
o congelar el hilo, hasta que la condición que le pases se resuelva.""" 