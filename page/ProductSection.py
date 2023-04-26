from selenium.webdriver.common.by import By

from control.Button import Button
from control.Label import Label


class ProductSection:

    def __init__(self, driver):
        self.driver = driver
        self.add_to_cart_button = Button(driver, By.XPATH, "//a[text() = 'Add to cart']")

    def get_product(self, product):
        product_label = Label(self.driver, By.XPATH, f"//h2[text() = '{product}']")
        return product_label