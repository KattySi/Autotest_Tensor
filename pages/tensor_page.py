from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement

from pages.base_page import BasePage
from pages.locators import TensorLocators



class TensorPage(BasePage):
    def __init__(self, browser: WebDriver, url: str, timeout: int = 10) -> None:
        super().__init__(browser, url, timeout)


    def should_be_strength_in_people(self) -> WebElement:
        assert (strength_in_people := self.is_element_present(TensorLocators.STRENGTH_IN_PEOPLE)), "отсутствует блок 'Сила в людях'"
        return strength_in_people

    def should_be_more_details(self) -> WebElement:
        assert (more_details := self.is_element_present(TensorLocators.MORE_DETAILS)), "отсутствует блок 'Сила в людях'"
        return more_details
