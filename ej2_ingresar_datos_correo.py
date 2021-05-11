import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path=r"E:\Selenium\chromedriver.exe")
driver.get("https://facebook.com")

user = driver.find_element_by_id("email")
user.send_keys("direccion")
user.send_keys(Keys.ENTER)
time.sleep(3)

password = driver.find_element_by_id("pass")
password.send_keys("password")
password.send_keys(Keys.ENTER)
