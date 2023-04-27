from selenium.webdriver.common.by import By

from control.button import Button
from control.label import Label


class CartSection:

    def __init__(self):
        self.place_order_button = Button(By.XPATH, "//button[text() = 'Place Order']")

    def get_product(self, product):
        product_label = Label(By.XPATH, f"//td[text() = '{product}']")
        return product_label
