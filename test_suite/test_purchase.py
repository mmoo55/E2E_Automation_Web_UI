from session.session import session
from test_suite.test_base import TestBase


class PurchaseProjectTest(TestBase):

    def test_purchase_test(self):
        # FIRST PRODUCT
        self.home_section.get_product(self.PRODUCT_ONE).click()
        self.assertEqual(self.product_section.get_product(self.PRODUCT_ONE).get_text(), self.PRODUCT_ONE, "ERROR! the product is different")
        self.product_section.add_to_cart_button.click()
        session.wait_alert_is_not_in_the_page()
        self.assertEqual(session.get_text_alert(), "Product added", "ERROR! the product was not added")
        session.accept_alert()

        # BACK TO HOME
        self.menu_section.home_label.click()

        # SECOND PRODUCT
        self.home_section.get_product(self.PRODUCT_TWO).click()
        self.assertEqual(self.product_section.get_product(self.PRODUCT_TWO).get_text(), self.PRODUCT_TWO, "ERROR! the product is different")
        self.product_section.add_to_cart_button.click()
        session.wait_alert_is_not_in_the_page()
        self.assertEqual(session.get_text_alert(), "Product added", "ERROR! the product was not added")
        session.accept_alert()

        # GO TO CART SECTION
        self.menu_section.cart_label.click()

        # CART SECTION
        self.assertEqual(self.cart_section.get_product(self.PRODUCT_ONE).get_text(), self.PRODUCT_ONE, "ERROR! the product is not in the cart")
        self.assertEqual(self.cart_section.get_product(self.PRODUCT_TWO).get_text(), self.PRODUCT_TWO, "ERROR! the product is not in the cart")
        self.cart_section.place_order_button.click()

        # MODAL FORM SECTION
        self.modal_form_section.name_txtbox.set_text(self.NAME)
        self.modal_form_section.country_txtbox.set_text(self.COUNTRY)
        self.modal_form_section.city_txtbox.set_text(self.CITY)
        self.modal_form_section.card_txtbox.set_text(self.CARD)
        self.modal_form_section.month_txtbox.set_text(self.MONTH)
        self.modal_form_section.year_txtbox.set_text(self.YEAR)
        self.modal_form_section.purchase_button.click()

        # MODAL CONFIRM SECTION
        self.assertEqual(self.modal_confirm_section.confirm_message_label.get_text(), "Thank you for your purchase!", "ERROR! the purchase failed")
        self.modal_confirm_section.ok_button.click()
