from selenium.webdriver.common.by import By

from control.Button import Button
from control.TextBox import TextBox


class ModalFormSection:

    def __init__(self, driver):
        self.name_txtbox = TextBox(driver, By.ID, "name")
        self.country_txtbox = TextBox(driver, By.ID, "country")
        self.city_txtbox = TextBox(driver, By.ID, "city")
        self.card_txtbox = TextBox(driver, By.ID, "card")
        self.month_txtbox = TextBox(driver, By.ID, "month")
        self.year_txtbox = TextBox(driver, By.ID, "year")
        self.purchase_button = Button(driver, By.XPATH, "//button[text() = 'Purchase']")