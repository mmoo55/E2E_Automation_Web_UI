import unittest

from browser.Browser import Browser
#from os import getenv
#from dotenv import load_dotenv

from page.HomeSection import HomeSection
from page.CartSection import CartSection
from page.MenuSection import MenuSection
from page.ModalConfirmSection import ModalConfirmSection
from page.ModalFormSection import ModalFormSection
from page.ProductSection import ProductSection


class TestBase(unittest.TestCase):

    def setUp(self):
        self.browser = Browser()
        self.browser.open_browser("Chrome")
        self.browser.navigate("https://www.demoblaze.com/")

        self.driver = self.browser.get_driver()
        self.driver.implicitly_wait(15)

        self.cart_section = CartSection(self.driver)
        self.home_section = HomeSection(self.driver)
        self.menu_section = MenuSection(self.driver)
        self.modal_confirm_section = ModalConfirmSection(self.driver)
        self.modal_form_section = ModalFormSection(self.driver)
        self.product_section = ProductSection(self.driver)


        """
        def setUp(self):
               load_dotenv(dotenv_path="../resources/.env")
               self.navigator = getenv("NAVIGATOR")
               self.url = getenv("URL")
               self.browser = Browser()
               self.browser.seleccionar_navegador(self.navigator)
               self.browser.navegar_web(self.url, 2)
               self.driver = self.browser.get_driver()

           def tearDown(self):
               self.driver.close()

           """


    def tearDown(self):
        self.browser.close_browser()