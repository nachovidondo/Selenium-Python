import unittest
import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options  import Options

#Buscar por elementos de busqueda en el input de google. Mostrando los 11 primeros




class UsingUnittest(unittest.TestCase):
   
    
    def setUp(self):
        self.chrome_options = Options()
        self.chrome_options.add_argument("--headless")
        self.driver = webdriver.Chrome(executable_path=r"E:\Selenium\chromedriver.exe")
     
    def test_busqueda(self):
        driver = self.driver
        driver.get('https://www.google.com')
        time.sleep(3)
        palabra_busqueda = "sele"
        busqueda = driver.find_element_by_name("q")
        busqueda.send_keys(palabra_busqueda)
        time.sleep(4)
        
        for i  in range(1,11):
            elementos = driver.find_element_by_xpath('/html/body/div[1]/div[3]/form/div[1]/div[1]/div['+str(i)+']/div/div[2]/input').text
            print(palabra_busqueda + elementos)
    
    def tearDown(self):
        self.driver.close()
        
        
if __name__ == '__main__':
    unittest.main()

