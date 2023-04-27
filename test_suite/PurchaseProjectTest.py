from time import sleep

# from browser.Browser import Browser
from test_suite.TestBase import TestBase


class PurchaseProjectTest(TestBase):

    def test_purchase_test(self):
        product_one = "Samsung galaxy s6"
        product_two = "Nokia lumia 1520"
        name = "Pedro"
        country = "Bolivia"
        city = "La Paz"
        card = "123456789"
        month = "July"
        year = "2023"

        # FIRST PRODUCT
        self.home_section.get_product(product_one).click()
        self.assertEqual(self.product_section.get_product(product_one).get_text(), product_one, "ERROR! the product is different")
        self.product_section.add_to_cart_button.click()
        self.browser.wait_alert_is_not_in_the_page()
        self.assertEqual(self.browser.get_text_alert(), "Product added", "ERROR! the product was not added")
        self.browser.accept_alert()

        # BACK TO HOME
        self.menu_section.home_label.click()

        # SECOND PRODUCT
        self.home_section.get_product(product_two).click()
        self.assertEqual(self.product_section.get_product(product_two).get_text(), product_two, "ERROR! the product is different")
        self.product_section.add_to_cart_button.click()
        self.browser.wait_alert_is_not_in_the_page()
        self.assertEqual(self.browser.get_text_alert(), "Product added", "ERROR! the product was not added")
        self.browser.accept_alert()

        # GO TO CART SECTION
        self.menu_section.cart_label.click()

        # CART SECTION
        self.assertEqual(self.cart_section.get_product(product_one).get_text(), product_one, "ERROR! the product is not in the cart")
        self.assertEqual(self.cart_section.get_product(product_two).get_text(), product_two, "ERROR! the product is not in the cart")
        self.cart_section.place_order_button.click()

        # MODAL FORM SECTION
        self.modal_form_section.name_txtbox.set_text(name)
        self.modal_form_section.country_txtbox.set_text(country)
        self.modal_form_section.city_txtbox.set_text(city)
        self.modal_form_section.card_txtbox.set_text(card)
        self.modal_form_section.month_txtbox.set_text(month)
        self.modal_form_section.year_txtbox.set_text(year)
        self.modal_form_section.purchase_button.click()

        # MODAL CONFIRM SECTION
        self.assertEqual(self.modal_confirm_section.confirm_message_label.get_text(), "Thank you for your purchase!", "ERROR! the purchase failed")
        self.modal_confirm_section.ok_button.click()
