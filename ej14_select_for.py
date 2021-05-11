import unittest
import time

from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys


class UsingUnittest(unittest.TestCase):
    def setUp(self):
       self.driver = webdriver.Chrome(executable_path=r"E:\Selenium\chromedriver.exe")
    
    def test_select_for(self):
        driver = self.driver
        driver.get("https://www.w3schools.com/howto/howto_custom_select.asp")
        select = driver.find_element_by_xpath('//*[@id="main"]/div[3]/div[1]/select')
        option = select.find_elements_by_tag_name("option")
        time.sleep(3)
        for op in option:
            print("Valores son: %s" % op.get_attribute("value"))
            op.click()
            time.sleep(1)
        
        seleccionar = Select(driver.find_element_by_xpath('//*[@id="main"]/div[3]/div[1]/select'))
        seleccionar.select_by_value("10")
        time.sleep(3)
        
    
    def tearDown(self):
        self.driver.close()

if __name__ == '__main__':
    unittest.main()
    
    
#Usando select y for para un combobox