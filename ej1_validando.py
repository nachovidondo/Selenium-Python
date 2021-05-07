from selenium import webdriver


driver = webdriver.Chrome(executable_path=r"E:\Selenium\chromedriver.exe")

driver.get("http://google.com")

driver.close()