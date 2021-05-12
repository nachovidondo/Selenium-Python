import configparser

configuration = configparser.ConfigParser()

configuration['General'] = {'chrome':"E:\Selenium\chromedriver.exe"}
configuration['Paginas'] = {'page' : 'https://www.google.com'}

with open('configuration.ini', 'w') as archivoconfig:
    configuration.write(archivoconfig)