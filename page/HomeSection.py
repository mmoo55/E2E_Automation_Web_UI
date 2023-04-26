from selenium.webdriver.common.by import By

from control.Label import Label


class HomeSection:

    def __init__(self, driver):
        self.driver = driver

    def get_product(self, product):
        product_label = Label(self.driver, By.XPATH, f"//a[text() = '{product}']")
        return product_label