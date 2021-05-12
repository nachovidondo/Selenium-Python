import unittest
import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# Este ejercicio es para poder elegir entre  2 opciones en las notificaciones de Chrome..

options = Options()
options.add_experimental_option("prefs",{
    "profile.default_content_setting_values.notifications":2
})

class UsingUnittest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(chrome_options= options, executable_path=r"E:\Selenium\chromedriver.exe")
    
    def test_notificacion(self):
        driver = self.driver
        driver.get('https://developer.mozilla.org/es/docs/Web/API/notification')
        time.sleep(3)
        
        
    def tearDown(self):
        self.driver.close()
        
        
        
if __name__ == '__main__':
    unittest.main()