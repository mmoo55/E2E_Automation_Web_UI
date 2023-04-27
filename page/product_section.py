from selenium.webdriver.common.by import By

from control.button import Button
from control.label import Label


class ProductSection:

    def __init__(self):
        self.add_to_cart_button = Button(By.XPATH, "//a[text() = 'Add to cart']")

    def get_product(self, product):
        product_label = Label(By.XPATH, f"//h2[text() = '{product}']")
        return product_label
