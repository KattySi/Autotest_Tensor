from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement

from pages.base_page import BasePage
from pages.locators import MainPageLocators



class MainPage(BasePage):
    def __init__(self, browser: WebDriver, url: str, timeout: int = 10) -> None:
        super().__init__(browser, url, timeout)


    def should_be_contacts(self) -> WebElement:
        assert (contacts := self.is_element_present(MainPageLocators.CONTACTS)), "нет кнопки Контакты"
        return contacts

    def should_be_contacts_more(self) -> WebElement:
        assert (contacts_more := self.is_element_present(MainPageLocators.CONTACTS_MORE)), "нет кнопки Еще 25 офисов в регионе"
        return contacts_more

    def should_be_download_local_versions(self) -> WebElement:
        assert (download_local_versions := self.is_element_present(MainPageLocators.DOWNLOAD_LOCAL_VERSIONS)), "нет кнопки Скачать локальные версии"
        return download_local_versions




