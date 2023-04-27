from selenium.webdriver.common.by import By

from control.label import Label


class HomeSection:

    def get_product(self, product):
        product_label = Label(By.XPATH, f"//a[text() = '{product}']")
        return product_label
