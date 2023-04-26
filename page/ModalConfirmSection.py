from selenium.webdriver.common.by import By

from control.Button import Button
from control.Label import Label


class ModalConfirmSection:

    def __init__(self, driver):
        self.confirm_message_label = Label(driver, By.XPATH, "//h2[text() = 'Thank you for your purchase!']")
        self.ok_button = Button(driver, By.XPATH, "//button[text() = 'OK']")