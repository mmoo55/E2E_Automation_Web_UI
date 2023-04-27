from os import getenv

from dotenv import load_dotenv
from pathlib import Path

from config import basedir

class GetEnv:
    _get_env = None

    # DATOS BASE
    _url = None
    _browser = None

    # DATOS PARA LA PRUEBA
    _product_one = None
    _product_two = None
    _name = None
    _country = None
    _city = None
    _card = None
    _month = None
    _year = None

    def __init__(self):
        # global url, browser
        dotenv_path = Path(f"{basedir}/resources/base_data/.env")
        load_dotenv(dotenv_path=dotenv_path)

        # DATOS BASE
        self._url = getenv("URL")
        self._browser = getenv("BROWSER")

        # DATOS PARA LA PRUEBA
        self._product_one = getenv("PRODUCT_ONE")
        self._product_two = getenv("PRODUCT_TWO")
        self._name = getenv("NAME")
        self._country = getenv("COUNTRY")
        self._city = getenv("CITY")
        self._card = getenv("CARD")
        self._month = getenv("MONTH")
        self._year = getenv("YEAR")

    @classmethod
    def get_instance(cls):
        if cls._get_env is None:
            cls._get_env = GetEnv()
        return cls._get_env

    def get_url(self):
        return self._url

    def get_browser(self):
        return self._browser

    def get_product_one(self):
        return self._product_one

    def get_product_two(self):
        return self._product_two

    def get_name(self):
        return self._name

    def get_country(self):
        return self._country

    def get_city(self):
        return self._city

    def get_card(self):
        return self._card

    def get_month(self):
        return self._month

    def get_year(self):
        return self._year

load_env = GetEnv.get_instance()
