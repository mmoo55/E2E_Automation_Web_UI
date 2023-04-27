import chromedriver_autoinstaller
from selenium import webdriver

class Chrome:

    def __init__(self):
        chromedriver_autoinstaller.install()

    def iniciar_chrome(self):
        """
        Abre el navegador Chrome
        :return: webdriver
        """
        driver = webdriver.Chrome()
        driver.implicitly_wait(15)
        driver.set_page_load_timeout(15)
        return driver
