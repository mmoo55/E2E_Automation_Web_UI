from selenium.webdriver.common.by import By

from control.button import Button
from control.label import Label


class ModalConfirmSection:

    def __init__(self):
        self.confirm_message_label = Label(By.XPATH, "//h2[text() = 'Thank you for your purchase!']")
        self.ok_button = Button(By.XPATH, "//button[text() = 'OK']")
