import chromedriver_autoinstaller
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

class Headless:

    def __init__(self):
        chromedriver_autoinstaller.install()

    def iniciar_headless(self):
        """
        Abre el navegador Chrome en modo Headless
        :return: webdriver
        """
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        return webdriver.Chrome(chrome_options=chrome_options)