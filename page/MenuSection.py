from selenium.webdriver.common.by import By

from control.Label import Label


class MenuSection:

    def __init__(self, driver):

        self.home_label = Label(driver, By.XPATH, "//a[text() = 'Home ']")
        self.cart_label = Label(driver, By.XPATH, "//a[text() = 'Cart']")