from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement

from pages.base_page import BasePage
from pages.locators import AboutLocators


class AboutPage(BasePage):
    def __init__(self, browser: WebDriver, url: str, timeout: int = 10) -> None:
        super().__init__(browser, url, timeout)

    def should_be_img_1(self) -> WebElement:
        assert (img_1 := self.is_element_present(AboutLocators.IMG_1)), "отсутствует картинка 'Разрабатываем систему'"
        return img_1

    def should_be_img_2(self) -> WebElement:
        assert (img_2 := self.is_element_present(AboutLocators.IMG_2)), "отсутствует картинка 'Продвигаем сервисы'"
        return img_2

    def should_be_img_3(self) -> WebElement:
        assert (img_3 := self.is_element_present(AboutLocators.IMG_3)), "отсутствует картинка 'Создаем инфраструктуру'"
        return img_3

    def should_be_img_4(self) -> WebElement:
        assert (img_4 := self.is_element_present(AboutLocators.IMG_4)), "отсутствует картинка 'Сопровождаем клиентов'"
        return img_4
