from control.Control import Control
from selenium.webdriver.common.keys import Keys

class TextBox(Control):

    def __init__(self, driver, type, locator):
        super(TextBox, self).__init__(driver, type, locator)

    def set_text(self, texto: str):
        self.find()
        print("Escribiendo en el campo {} el texto -> {} ".format(self.control, texto))
        self.control.send_keys(texto)

    def set_text_clear(self, texto: str):
        self.find()
        print("Escribiendo en el campo {} el texto -> {} ".format(self.control, texto))
        self.control.clear()
        self.control.send_keys(texto)