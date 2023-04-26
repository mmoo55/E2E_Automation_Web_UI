import geckodriver_autoinstaller
from selenium import webdriver

class Firefox:

    def __init__(self):
        geckodriver_autoinstaller.install()

    def iniciar_firefox(self):
        """
        Abre el navegador Firefox
        :return: webdriver
        """
        return webdriver.Firefox()