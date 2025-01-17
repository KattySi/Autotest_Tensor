from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



class BasePage:
    def __init__(self, browser: WebDriver, url: str, timeout: int = 20) -> None:
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)


    def is_element_present(self, locator) -> WebElement | bool:
        """Находит один элемент и возвращает его"""
        try:
            obj = WebDriverWait(self.browser, 10).until(EC.presence_of_element_located(locator))
        except NoSuchElementException:
            return False
        return obj


    def open(self) -> None:
        self.browser.get(self.url)


    def is_element_clickable(self, locator) -> WebElement | bool:
        """ Ждёт когда элемент станет кликабельным и возвращает его"""
        try:
            obj = WebDriverWait(self.browser, 20).until(EC.element_to_be_clickable(locator))
        except NoSuchElementException:
            return False
        return obj


    def is_element_visibility(self, locator) -> WebElement | bool:
        """ Ждёт когда элемент станет видимым и возвращает его """
        try:
            obj = WebDriverWait(self.browser, 15).until(EC.visibility_of_element_located(locator))
        except NoSuchElementException:
            return False
        return obj