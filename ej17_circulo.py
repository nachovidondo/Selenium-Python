import unittest
import time

from selenium import webdriver
from selenium.webdriver import ActionChains



class UsingUnittest(unittest.TestCase):
    def setUp(self):
       self.driver = webdriver.Chrome(executable_path=r"E:\Selenium\chromedriver.exe")
       
    def test_circulo(self):
        driver = self.driver
        driver.get("http://www.circuloin.com")
        time.sleep(3)
        alquileres = driver.find_element_by_link_text("Alquileres")
        time.sleep(2)
        hover = ActionChains(driver).move_to_element(alquileres)
        hover.perform()
        alquileres.click()
        time.sleep(2)
        departamentos = driver.find_element_by_link_text("Departamentos")
        time.sleep(2)
        hover = ActionChains(driver).move_to_element(departamentos)
        hover.perform()
        departamentos.click()
        time.sleep(2)
        
        dormitorio = driver.find_element_by_link_text("1 Dormitorio")
        time.sleep(2)
        hover = ActionChains(driver).move_to_element(dormitorio)
        hover.perform()
        dormitorio.click()
        time.sleep(2)
    def tearDown(self):
        self.driver.close()

    
if __name__ == '__main__':
    unittest.main()
    
        
        
#En este ejercicio unimos el hover con el click para ingresar a  una pagina y seleccionar distintos links 
