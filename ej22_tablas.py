import unittest
import time

from selenium import webdriver
from selenium.webdriver.common.keys import  Keys


#Ejecucion de una automatizacion para una tabla

class UsingUnittest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=r"E:\Selenium\chromedriver.exe")
    
    def test_tables(self):
        driver = self.driver
        driver.get('https://www.w3schools.com/html/html_tables.asp')
        tabla = driver.find_element_by_xpath('//*[@id="customers"]/tbody/tr[2]/td[2]').text
        time.sleep(2)
        print(tabla)
        
        rows = len(driver.find_elements_by_xpath('//*[@id="customers"]/tbody/tr'))
        col = len(driver.find_elements_by_xpath('//*[@id="customers"]/tbody/tr[1]/th'))
        print(rows)
        print(col)
        #Recorrido de toda la tabla por filas y columnas
        for n in range(2, rows+1):
            for b in range(1, col+1):
                dato = driver.find_element_by_xpath('//*[@id="customers"]/tbody/tr['+str(n)+']/td['+str(b)+']').text
                print(dato, end="                                    ")
            print()
    def tearDown(self):
        self.driver.close()

if __name__ == '__main__':
    unittest.main()




        
    