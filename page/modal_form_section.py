from selenium.webdriver.common.by import By

from control.button import Button
from control.text_box import TextBox


class ModalFormSection:

    def __init__(self):
        self.name_txtbox = TextBox(By.ID, "name")
        self.country_txtbox = TextBox(By.ID, "country")
        self.city_txtbox = TextBox(By.ID, "city")
        self.card_txtbox = TextBox(By.ID, "card")
        self.month_txtbox = TextBox(By.ID, "month")
        self.year_txtbox = TextBox(By.ID, "year")
        self.purchase_button = Button(By.XPATH, "//button[text() = 'Purchase']")
