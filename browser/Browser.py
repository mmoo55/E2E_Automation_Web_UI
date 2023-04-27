from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

from browser.Chrome import Chrome
from browser.Edge import Edge
from browser.Firefox import Firefox
from browser.Headless import Headless
from browser.Grid import Grid


class Browser:

    def __init__(self):
        self.driver = None

    def open_browser(self, navigator: str = "Chrome"):
        try:
            if navigator == "Chrome":
                self.driver = Chrome().iniciar_chrome()
            elif navigator == "Firefox":
                self.driver = Firefox().iniciar_firefox()
            elif navigator == "Edge":
                self.driver = Edge().iniciar_edge()
            elif navigator == "Safari":
                self.driver = webdriver.Safari()
            elif navigator == "Headless":
                self.driver = Headless().iniciar_headless()
            elif navigator == "Grid":
                self.driver = Grid().iniciar_grid()
            self.vars = {}
            return self.driver
        except Exception as e:
            print(e)

    def navigate(self, url: str, secs: int = 0):
        try:
            self.driver.get(url)
            self.driver.maximize_window()
            time.sleep(secs)
            print("Pagina abierta: " + url)
        except Exception as e:
            print(e)

    def close_browser(self):
        self.driver.close()

    def get_driver(self):
        return self.driver

    def accept_alert(self):
        self.driver.switch_to.alert.accept()

    def get_text_alert(self):
        return self.driver.switch_to.alert.text

    def wait_alert_is_not_in_the_page(self):
        explicit_wait = WebDriverWait(self.driver, 10)
        explicit_wait.until(EC.alert_is_present())