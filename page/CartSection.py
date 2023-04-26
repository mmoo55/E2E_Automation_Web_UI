from selenium.webdriver.common.by import By

from control.Button import Button
from control.Label import Label


class CartSection:

    def __init__(self, driver):
        self.driver = driver
        self.place_order_button = Button(driver, By.XPATH, "//button[text() = 'Place Order']")

    def get_product(self, product):
        product_label = Label(self.driver, By.XPATH, f"//td[text() = '{product}']")
        return product_label