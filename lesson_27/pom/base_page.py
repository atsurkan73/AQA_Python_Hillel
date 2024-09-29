import time

from selenium.common import TimeoutException, NoSuchElementException
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait



class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.base_url = 'https://tracking.novaposhta.ua/#/uk'
        self.driver.set_window_size(1550, 838)

    def find_element(self, locator: tuple[str, str]):
        """Функція для очікування наявності елемента на сторінці"""
        try:
            element = WebDriverWait(self.driver, timeout=5).until(
                EC.presence_of_element_located(locator)
            )
            return element

        except TimeoutException:
            raise NoSuchElementException("За даний час елемент не зявився на сторінці")


    def open(self, url):
        url = self.base_url + url
        self.driver.get(url)
