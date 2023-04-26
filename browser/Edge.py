import edgedriver_autoinstaller
from selenium import webdriver

class Edge:

    def __init__(self):
        edgedriver_autoinstaller.install()

    def iniciar_edge(self):
        """
        Abre el navegador Edge
        :return: webdriver
        """
        return webdriver.Edge()