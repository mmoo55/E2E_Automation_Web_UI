from selenium.webdriver.common.by import By

from control.label import Label


class MenuSection:

    def __init__(self):

        self.home_label = Label(By.XPATH, "//a[text() = 'Home ']")
        self.cart_label = Label(By.XPATH, "//a[text() = 'Cart']")
