from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Control:

    def __init__(self, driver, type, locator):
        self.driver = driver
        self.type = type
        self.locator = locator
        self.control: WebElement = None

    def find(self):
        self.control = self.driver.find_element(self.type, self.locator)

    def click(self):
        self.find()
        print("Damos click en el campo -> {} ".format(self.control))
        self.control.click()

    def control_is_visible(self):
        try:
            self.find()
            return self.control.is_displayed()
        except:
            return False

    def get_text(self):
        self.find()
        return self.control.text

    def wait_control_is_not_in_the_page(self):
        explicit_wait = WebDriverWait(self.driver, 10)
        explicit_wait.until(EC.visibility_of_element_located(self.control))