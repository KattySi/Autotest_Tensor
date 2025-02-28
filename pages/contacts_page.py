from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement

from pages.base_page import BasePage
from pages.locators import ContactsLocators


class ContactsPage(BasePage):
    def __init__(self, browser: WebDriver, url: str, timeout: int = 10) -> None:
        super().__init__(browser, url, timeout)

    def should_be_banner(self) -> WebElement:
        assert (banner := self.is_element_present(ContactsLocators.BANNER)), "нет баннера"
        return banner

    def should_be_region(self) -> WebElement:
        assert (region := self.is_element_present(ContactsLocators.REGION)), "не определяется местоположение"
        return region

    def should_be_list_partners(self) -> WebElement:
        assert (list_partners := self.is_element_present(ContactsLocators.LIST_PARTNERS)), "отсутствует список партнеров"
        return list_partners

    def should_be_kamchatka(self) -> WebElement:
        assert (kamchatka := self.is_element_clickable(ContactsLocators.KAMCHATKA)), "Камчатка отсутствует в списке"
        return kamchatka

    def should_be_present_text_new_region(self):
        assert self.is_element_to_be_present_text(
            locator=ContactsLocators.REGION, text="Камчатский край"
        ), "Выбран не Камчатский Край или не найден регион"



