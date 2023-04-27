from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from session.session import session


class Control:

    def __init__(self, type, locator):
        """
        Constructor de inicio de la clase Control.
        :param driver: La instancia creada que nos permite interactuar con el navegador.
        :param type: Tipo de selector que se ingresará, puede ser de tipo:
                    id, name, link text, css selector, partial link text, class name, xpath.
        :param locator: elemento a referenciar de la página web.
        :return:
        """
        self.type = type
        self.locator = locator
        self.control: WebElement = None
        self.driver = session.get_browser()

    def find(self):
        """
        Encuentra y obtiene el elemento
        :return:
        """
        self.control = self.driver.find_element(self.type, self.locator)

    def click(self):
        """
        Permite realizar una acción de 'click' en un elemento de la página web.
        :return:
        """
        self.find()
        print("Damos click en el campo -> {} ".format(self.locator))
        self.control.click()

    def control_es_visible(self):
        """
        Permite verificar si un elemento de la pagina web esta visible.
        :return: Boolean, True si es visible o de lo contrario False
        """
        try:
            self.find()
            return self.control.is_displayed()
        except:
            return False

    def get_text(self):
        """
        Obtiene el texto de un elemento.
        :return: str
        """
        self.find()
        return self.control.text

    def wait_control_is_not_in_the_page(self):
        """
        Permite realizar una espera durante un tiempo determinado.
        :return:
        """
        explicit_wait = WebDriverWait(self.driver, 10)
        explicit_wait.until(EC.visibility_of_element_located(self.control))
