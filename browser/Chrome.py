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
        return webdriver.Chrome()