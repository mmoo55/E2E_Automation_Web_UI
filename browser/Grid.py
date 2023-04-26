import chromedriver_autoinstaller
from selenium import webdriver

class Grid:

    def __init__(self):
        chromedriver_autoinstaller.install()

    def iniciar_grid(self):
        """
        Abre el navegador Chrome en modo Grid
        :return: webdriver
        """
        return webdriver.Chrome()