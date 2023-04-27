import unittest

from page.cart_section import CartSection
from page.home_section import HomeSection
from page.menu_section import MenuSection
from page.modal_confirm_section import ModalConfirmSection
from page.modal_form_section import ModalFormSection
from page.product_section import ProductSection
from session.session import session
from util.get_env import load_env


class TestBase(unittest.TestCase):

    cart_section = CartSection()
    home_section = HomeSection()
    menu_section = MenuSection()
    modal_confirm_section = ModalConfirmSection()
    modal_form_section = ModalFormSection()
    product_section = ProductSection()

    PRODUCT_ONE = load_env.get_product_one()
    PRODUCT_TWO = load_env.get_product_two()
    NAME = load_env.get_name()
    COUNTRY = load_env.get_country()
    CITY = load_env.get_city()
    CARD = load_env.get_card()
    MONTH = load_env.get_month()
    YEAR = load_env.get_year()

    def setUp(self):
        session.get_browser().get(load_env.get_url())

    def tearDown(self):
        session.get_instance().close_session()
