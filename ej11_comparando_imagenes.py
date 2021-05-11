import unittest
import cv2
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait



class UsingUnittest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=r"E:\Selenium\chromedriver.exe")
    
    def test_using_opencv(self):
        driver = self.driver
        driver.get("http://www.google.com")
        driver.save_screenshot("img.png")
        time.sleep(3)
    
    def comparing_images(self):
        img1 = cv2.imread("img3.png")
        img2 = cv2.imread('img.png')
        
        
        difference = cv2.absdiff(img1,img2)
        image_gray  = cv2.cvtColor(difference,cv2.COLORS_BGR2GRAY)
        contours,_ = cv2.findContours(image_gray, cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
        
        for c in contours:
            if cv2.contourArea(c)>=20:
                position_x, position_y, width, height = cv2.boundingRect(c)
                cv2.rectangle(img1,(position_x,position_y),(position_x+width,position_y+height),(0,0,255),2)
        
        while(1):
            cv2.imshow('Imagen1',img1)
            cv2.imshow('Imagen2',img2)
            cv2.imshow('Diferencias detectadas', difference)
            teclado = cv2.waitKey(5) & 0xFF
            if teclado == 27:
                break
            cv2.destroyAllWindows()
            
    
if __name__ == '__main__':
    unittest.main()
        