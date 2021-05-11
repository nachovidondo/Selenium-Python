import unittest

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



class UsingUnittest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=r"E:\Selenium\chromedriver.exe")
    
    def test_implicit_wait(self):
        driver = self.driver
        driver.implicitly_wait(5) #Esperando 5 segundos si no lo encuentra , si lo encuentra cierra la pagina.
        driver.get("http://www.google.com")
        
        myDinamicElement  = driver.find_element_by_name("q")
        
    
if __name__ == '__main__':
    unittest.main()
        